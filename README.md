# flutter-notification-playground-api
Django

### 環境

- python：3.12.4(pyenvで管理)
- Poetry：(version 1.8.3)

### 実行環境を準備
-  pyenvをインストールし、使用したいpythonのバージョンをインストール(新しいもの)、グローバルに設定
-  poetryをインストール

### プロジェクトの作成

- Djangoの開発環境をDockerfile、docker-compose.ymlファイルで定義

- pyproject.tomlファイルを作成

```
poetry init --name django_project --dependency django --dependency psycopg2-binary --dependency djangorestframework

- poetry install

```

- Djangoプロジェクトを作成

```
poetry run django-admin startproject myproject .
```

- DB設定

`myproject/settings.py`を修正

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

- dockerコンテナの起動

```
docker-compose up -d
```

- VS CodeでDockerコンテナに接続
プロジェクトに必要なツールはコンテナ内に存在するため、VSCodeでコンテナに接続する(任意)

ショートカットキー(Cmd+Shift+P)を使用し、Python: Select Interpreterを選択し、対象の環境を選択