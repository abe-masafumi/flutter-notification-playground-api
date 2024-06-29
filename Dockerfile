# ベースイメージとしてPythonを使用
FROM python:3.12-slim

# 作業ディレクトリを作成
WORKDIR /app

# Poetryをインストール
RUN pip install poetry

# Poetryの仮想環境を無効にする設定
RUN poetry config virtualenvs.create false

# 必要なファイルをコピー
COPY pyproject.toml poetry.lock* /app/

# 依存関係をインストール
RUN poetry install --no-root

# プロジェクトの全てのファイルをコピー
COPY . /app/

# エントリポイントとしてDjangoのサーバーを起動
CMD ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
