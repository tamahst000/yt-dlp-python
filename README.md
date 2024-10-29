# yt-dlp 動画保存ツール windows

## セットアップ

### パッケージのインストール

`py/pip_install.bat`をダブルクリック

### cokkies.txt の保存

※任意、Youtube Premium に加入している場合は推奨

まず、Cookie をテキストファイルとして取り出すために、ブラウザの拡張機能をインストールする

Chrome の場合：[Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid)

Firefox の場合：[cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

インストールが済んだらログインした Youtube ページを開き、拡張機能を実行(アイコンをクリック)、cookie.txt がダウンロードできる

**`py`フォルダーの中に保存する**

既に同じ名前のファイルが存在する場合は上書きする

## 使い方

### 動画保存

大体の動画サイトはこれで保存できる(はず)

1. 保存したい動画の URL をコピー
2. `動画mp4保存.bat` をダブルクリック
3. 保存したい動画の URL を貼り付けてエンター
   - 何も入力しなければ `url.txt`※ から反映
4. `yt-dlp`フォルダーに動画が保存される

※`url.txt` に保存したい動画の URL を一行ずつコピーしておく、複数 URL 保存したい場合に便利

主な対応サイト

- Youtube
  - 再生リストの URL にも対応
- Tver
- X(Twitter)
- ABEMA
- niconico
- TikTok
- bilibili
- Dailymotion

### youtube music 保存

youtube music の音楽をアルバムアートワーク付きで保存できる

1. 保存したい音楽の URL をコピー
   - 保存したい音楽を開く -> 共有 -> コピー
   - プレイリストの URL にも対応
2. `YoutubeMusicをmp3保存.bat` をダブルクリック
3. コピーした URL を貼り付けてエンター
   - 何も入力しなければ `url.txt` から反映
4. `yt-dlp`フォルダーに音楽が保存される

### プロセカ MV を mp3 保存

サムネイルをアルバムアートワークに設定して保存できる

プロセカの MV 動画を mp3 変換したい際に便利

他の youtube 動画でも同様に mp3 保存できる

1. 保存したい動画の URL をコピー
2. `プロセカMVをmp3保存.bat` をダブルクリック
3. 保存したい動画の URL を貼り付けてエンター
   - 何も入力しなければ `url.txt` から反映
4. `yt-dlp`フォルダーに音楽が保存される

## ※上手く動画保存できない場合

yt-dlp のアップデート行うと大体うまくいく

`py/update.bat`をダブルクリック
