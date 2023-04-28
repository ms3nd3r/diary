# 日記アプリケーション

このアプリケーションは、PythonとDjangoを使用して作成された簡単な日記アプリケーションです。アプリケーションでは、日付とテキストの入力フィールドと保存ボタンが提供されます。ユーザーが入力した日記エントリは、ローカルファイルシステムに保存されます。

## インストール方法

1. このリポジトリをクローンします。
2. Pythonとpipをインストールします。
3. 仮想環境を作成し、仮想環境に入ります。
4. 必要なPythonパッケージをインストールします。以下のコマンドを実行します。

```
pip install -r requirements.txt
```

## 使い方

1. 仮想環境に入ります。
2. プロジェクトのルートディレクトリで、以下のコマンドを実行します。

```
python manage.py runserver
```

3. ブラウザを開き、`http://localhost:8000/diary/`にアクセスします。
4. 日付とテキストの入力フィールドに日記エントリを入力し、保存ボタンをクリックします。
5. 入力された日記エントリは、ローカルファイルシステムに保存されます。
6. 過去の日記エントリを確認するには、アプリケーションのトップページに戻り、表示されるエントリのリストをクリックします。