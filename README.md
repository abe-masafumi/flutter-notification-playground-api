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

poetry install
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

### 以下のエラーでコンテナが起動しない場合
```
web-1  | The virtual environment found in /app/.venv seems to be broken.
web-1  | Recreating virtualenv django-project in /app/.venv
web-1  | Traceback (most recent call last):
web-1  |   File "/app/manage.py", line 11, in main
web-1  |     from django.core.management import execute_from_command_line
web-1  | ModuleNotFoundError: No module named 'django'
web-1  | 
web-1  | The above exception was the direct cause of the following exception:
web-1  | 
web-1  | Traceback (most recent call last):
web-1  |   File "/app/manage.py", line 22, in <module>
web-1  |     main()
web-1  |   File "/app/manage.py", line 13, in main
web-1  |     raise ImportError(
web-1  | ImportError: Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH environment variable? Did you forget to activate a virtual environment?
```

poetryの仮想環境が破損している可能性があります。一度削除してください。
```
poetry env info
rm -rf [プロジェクトのパス].venv
or
.venvディレクトリを削除
```

dockerコンテナのクリア
```
docker-compose down --volumes --remove-orphans
```

依存関係を再インストール
```
poetry install
```

再度コンテナを立ち上げ
```
docker-compose build --no-cache
docker-compose up
```


python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser

developer

sample@example.com

tester123
