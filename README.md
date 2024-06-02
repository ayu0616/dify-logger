# Difyのログ取得

## 環境構築

### requirements.txtで必要なライブラリをインストール

```bash
pip install -r requirements.txt
```

### .envファイルを作成

`.env`（なければ作成）ファイルに以下の内容を記述する  
`=`の後ろには自分のApp IDとAPI Keyを記述する

```bash
DIFY_APP_ID="YOUR DIFY APP ID"
DIFY_API_KEY="YOUR DIFY API KEY"
```

## ログ取得

```bash
python src/get_log.py
```

取得されたログは`log/`ディレクトリに保存。  
個別メッセージのログは`log/message/`ディレクトリに保存される。
