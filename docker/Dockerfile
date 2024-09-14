FROM python:3.12

# 作業ディレクトリを/appに設定
WORKDIR /app

# appを作業ディレクトリにコピー
COPY ../app ./

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install -r /app/requirements.txt