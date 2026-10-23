#!/usr/bin/env bash
# Encerra o script se algum comando falhar
set -o errexit

# Instala as dependências do Python
pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS, JS, imagens) para o WhiteNoise
python manage.py collectstatic --noinput

# Aplica as migrações do banco de dados
python manage.py migrate

# Cria o superusuário inicial (admin/coordenador) caso não exista (ideal para o plano Free do Render)
python manage.py shell -c "
import os
from apps.usuarios.models import Usuario
email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@ahd.com')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
if not Usuario.objects.filter(email=email).exists():
    Usuario.objects.create_superuser(
        username=email,
        email=email,
        password=password,
        tipo='admin',
        first_name='Tatiana',
        last_name='Sorrentino'
    )
    print(f'Superusuario {email} criado com sucesso!')
else:
    print(f'Superusuario {email} ja existe.')
"

