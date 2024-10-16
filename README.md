# セットアップ

## パッケージのインストール
```
cd py
pip install -r requirements.txt
```

## cokkies.txtの保存
まず、Cookieをテキストファイルとして取り出すために、ブラウザの拡張機能をインストールする。

Chromeの場合：[Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid)
Firefoxの場合：[cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

インストールが済んだらログインしたYoutubeページを開き、拡張機能を実行(アイコンをクリック)、cookie.txtがダウンロードできる。

-cookiesオプションでCookieを指定することで認証することができる

**url.txtのあるディレクトリと同じディレクトリに保存する**

## 保存ディレクトリの作成
エクスプローラーで新しいフォルダーを作成 or コマンド実行

```
mkdir yt-dlp
```
