#!/usr/bin/env bash
# Encerra o script se algum comando falhar
set -o errexit

# Instala as dependências do Python
pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS, JS, imagens) para o WhiteNoise
python manage.py collectstatic --noinput

# Aplica as migrações do banco de dados
python manage.py migrate

# Cria o superusuário inicial (coordenação) apenas se a senha for definida nas
# variáveis de ambiente. NUNCA deixe uma senha padrão no código.
python manage.py shell -c "
import os
from apps.usuarios.models import Usuario
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
if not email or not password:
    print('DJANGO_SUPERUSER_EMAIL/PASSWORD nao definidos: superusuario nao criado.')
elif Usuario.objects.filter(email=email).exists():
    print(f'Superusuario {email} ja existe.')
else:
    Usuario.objects.create_superuser(
        username=email, email=email, password=password,
        tipo='admin', first_name='Coordenação', last_name='AHD',
    )
    print(f'Superusuario {email} criado com sucesso!')
"
