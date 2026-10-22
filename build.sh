#!/usr/bin/env bash
# Encerra o script se algum comando falhar
set -o errexit

# Instala as dependências do Python
pip install -r requirements.txt

# Coleta os arquivos estáticos (CSS, JS, imagens) para o WhiteNoise
python manage.py collectstatic --noinput

# Aplica as migrações do banco de dados
python manage.py migrate
