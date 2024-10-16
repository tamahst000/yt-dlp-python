# yt-dlp 動画保存ツール windows

## セットアップ

### パッケージのインストール

`py/pip_install.bat`をダブルクリック

### cokkies.txt の保存

※Youtube Premium に加入している場合は行った方が良い

まず、Cookie をテキストファイルとして取り出すために、ブラウザの拡張機能をインストールする。

Chrome の場合：[Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/bgaddhkoddajcdgocldbbfleckgcbcid)
Firefox の場合：[cookies.txt](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/)

インストールが済んだらログインした Youtube ページを開き、拡張機能を実行(アイコンをクリック)、cookie.txt がダウンロードできる。

**url.txt のあるフォルダーと同じフォルダーに保存する**

既に同じ名前のファイルが存在する場合は上書きする

## ※上手く動画保存できない場合

yt-dlp のアップデート行うと大体うまくいく

`py/update.bat`をダブルクリック

## 使い方

### 動画保存(メイン)

大体の動画サイトはこれで保存できる(はず)

1. 保存したい動画の URL をコピー
2. `youtube動画変換-cookies使用.bat` をダブルクリック
3. 保存したい動画の URL を貼り付けてエンター
4. `yt-dlp`フォルダーに動画が保存される

主な対応サイト

- Youtube
- Tver

### 動画保存(サブ)

動画保存(メイン)で保存ができないサイトに使用する

1. 保存したい動画の URL をコピー
2. `twitter動画変換.bat` をダブルクリック
3. 保存したい動画の URL を貼り付けてエンター
4. `yt-dlp`フォルダーに動画が保存される

主な対応サイト

- Twitter
- Abema
- bilibili

### url.txt から動画保存

複数の動画をまとめて変換できる

1. 保存したい動画の URL を、`url.txt`に一行ずつコピー
2. `url.txtからyoutube動画変換 .bat` or `url.txtからtwitter動画変換 .bat`をダブルクリック
3. `yt-dlp`フォルダーに動画が保存される

### youtube 生配信保存

youtube のライブ配信動画をリアルタイムで保存したい場合に使用する

(アーカイブ動画は 動画変換(メイン) で保存できる)

1. 保存したい動画の URL をコピー
2. `youtube生配信保存.bat` をダブルクリック
3. 保存したい動画の URL を貼り付けてエンター
4. 生配信終了後、`yt-dlp`フォルダーに動画が保存される

### youtube サムネイル保存

youtube のサムネイルのみ保存する

1. 保存したい動画の URL をコピー
2. `youtubeサムネイル保存.bat` をダブルクリック
3. 保存したい動画の URL を貼り付けてエンター
4. `yt-dlp`フォルダーに画像が保存される

### youtube music 保存

1. 保存したい音楽の URL をコピー
   - 保存したい音楽を開く -> 共有 -> コピー
2. `YoutubeMusic保存(ym.py).bat` をダブルクリック
3. コピーした URL を貼り付けてエンター
4. `yt-dlp`フォルダーに音楽が保存される

### url.txt から youtube music 保存

1. 保存したい音楽の URL を、`url.txt`に一行ずつコピー
   - 保存したい音楽を開く -> 共有 -> コピー
2. `YoutubeMusic保存(ym_txt.py).bat` をダブルクリック
3. `yt-dlp`フォルダーに音楽が保存される

### プロセカ MV を mp3 保存

サムネイルをアルバムアートワークに設定して保存できる。

プロセカの MV 動画を mp3 変換したい際に便利。

他の youtube 動画でも同様に mp3 保存できる。

1. 保存したい動画の URL を、`url.txt`に一行ずつコピー
2. `プロセカMVをmp3保存(txt).bat` をダブルクリック
3. `yt-dlp`フォルダーに動画が保存される
