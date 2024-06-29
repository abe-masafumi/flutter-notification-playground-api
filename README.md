# flutter-notification-playground-api
Django

 ローカルでの作業
 
 pyenvをインストールし、使用したいpythonのバージョンをインストール(新しいもの)、グローバルに設定

 poetryをインストール


Djangoの開発環境をDockerfile、docker-compose.ymlファイルで定義


pyproject.tomlファイルを作成
```
poetry init --name django_project --dependency django --dependency psycopg2-binary --dependency djangorestframework

poetry install
```

Djangoプロジェクトを作成
```
poetry run django-admin startproject myproject .
```

DB設定
`myproject/settings.py`

```
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DJANGO_DB_NAME'),
        'USER': os.getenv('DJANGO_DB_USER'),
        'PASSWORD': os.getenv('DJANGO_DB_PASSWORD'),
        'HOST': os.getenv('DJANGO_DB_HOST'),
        'PORT': os.getenv('DJANGO_DB_PORT'),
    }
}
```

dockerコンテナの起動
```
docker-compose up -d
```