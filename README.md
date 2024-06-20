# CLIで動くtodoアプリ

UIとか考えるのめんどいのでこれで

## インストールと使用方法の確認

1. GitHubリポジトリをクローンします。

```sh
git clone https://github.com/riku-yanagihashi/CLI-todo-app.git
cd CLI-todo-app
```

2. パッケージをインストールします
```
pip install .
```

3. 'todo'コマンドで実行
```
todo
```

## 言語変更の仕方
インストールされている状態でターミナルに
```
todo lang {使用したい言語}
```
{使用したい言語}のなかに'en','ja'のどれかを入力すると変更される
### 例
```
todo lang ja
```
上記のコマンドで日本語に変更可能

## 本ツールのアンインストール方法
```sh
pip uninstall cli_todo_app
```
なんか聞かれたら'yes'と入力してください
