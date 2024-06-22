# CLI-todo-appのマニュアル

※僕の環境じゃ動いてます
## インストールと使用方法の確認

1. 以下のコマンドをインストールしたいディレクトリに移動してからターミナルに打ち込んでください。

```sh
git clone -- depth 1 https://github.com/riku-yanagihashi/CLI-todo-app.git ~/CLI-todo-app && cd ~/CLI-todo-app && pip install .
```

###  コマンドの説明
```bash
git clone https://github.com/riku-yanagihashi/CLI-todo-app.git
```
↑リポジトリをローカル上にクローンするコマンド

```sh
cd CLI-todo-app
```
↑本ツールのディレクトリに移動するコマンド

```sh
pip install .
```
↑必要なパッケージなどをインストールするコマンド

3. 'todo'コマンドで起動
```
todo
```

## 言語変更の仕方
インストールされている状態でターミナルに
```
todo lang {使用したい言語}
```
{使用したい言語}のなかに'en','ja'のどれかを入力すると変更される
### 例:
```
todo lang ja
```
上記のコマンドで日本語に変更可能

## 本ツールのアンインストール方法
```sh
pip uninstall cli_todo_app
```
なんか聞かれたら'yes'と入力してください
