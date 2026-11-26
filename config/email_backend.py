"""Backend de e-mail via API HTTPS do Brevo (porta 443).

Necessário no plano gratuito do Render, que bloqueia portas SMTP (25, 465, 587).
"""

import json
import logging
import urllib.error
import urllib.request
from email.utils import parseaddr

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend

logger = logging.getLogger(__name__)

BREVO_API_URL = "https://api.brevo.com/v3/smtp/email"


class BrevoEmailBackend(BaseEmailBackend):
    """Envia e-mails transacionais do Django pela API REST v3 do Brevo."""

    def send_messages(self, email_messages):
        if not email_messages:
            return 0

        api_key = getattr(settings, "BREVO_API_KEY", "").strip()
        if not api_key:
            if not self.fail_silently:
                raise RuntimeError("BREVO_API_KEY não configurada.")
            return 0

        enviados = 0
        for message in email_messages:
            if not message.to:
                continue
            if self._enviar_um(message, api_key):
                enviados += 1
        return enviados

    def _enviar_um(self, message, api_key):
        sender_name, sender_email = parseaddr(
            message.from_email or settings.DEFAULT_FROM_EMAIL
        )
        sender = {"email": sender_email}
        if sender_name:
            sender["name"] = sender_name

        payload = {
            "sender": sender,
            "to": [{"email": parseaddr(addr)[1] or addr} for addr in message.to],
            "subject": str(message.subject),
        }
        if message.body:
            payload["textContent"] = message.body

        for content, mimetype in getattr(message, "alternatives", ()) or ():
            if mimetype == "text/html":
                payload["htmlContent"] = content
                break

        if message.cc:
            payload["cc"] = [{"email": parseaddr(addr)[1] or addr} for addr in message.cc]
        if message.bcc:
            payload["bcc"] = [{"email": parseaddr(addr)[1] or addr} for addr in message.bcc]

        req = urllib.request.Request(
            BREVO_API_URL,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "api-key": api_key,
                "Content-Type": "application/json",
                "Accept": "application/json",
                "User-Agent": "projeto-ahd-django/1.0",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                if 200 <= resp.status < 300:
                    return True
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")
            logger.error("Erro HTTP %s ao enviar e-mail via Brevo: %s", exc.code, body)
            if not self.fail_silently:
                raise
        except Exception:
            logger.error("Falha ao enviar e-mail via Brevo.", exc_info=True)
            if not self.fail_silently:
                raise
        return False
