#サムネイルをアートワークにしてmp3保存(YYYYMMDD title.mp3)

import subprocess
from PIL import Image
import os
import re

#txtからurlを取得
urllist = []
with open(r".\\url.txt", "r", encoding="utf_8") as f:
    while True:
        line=f.read()
        script_line=line.split("\n")
        for t in script_line:
            if "http" in t:
                urllist.append(t)
        else:
            break

for inURL in urllist:
    try:
        #アップロード日 タイトルを取得
        cmd0 =f'yt-dlp {inURL} --print "%(upload_date)s %(title)s"'
        datatitle=subprocess.run(cmd0, shell=True, stdout = subprocess.PIPE,encoding='shift-jis')
        datatitle=str(datatitle.stdout)
        print(datatitle)

        #タイトルを取得
        cmd1 =f'yt-dlp {inURL} --print "%(title)s"'
        fn=subprocess.run(cmd1, shell=True, stdout = subprocess.PIPE,encoding='shift-jis')
        fn=str(fn.stdout)
        fn=fn.replace("\n","")
        #idを取得
        cmd1 =f"yt-dlp {inURL} --cookies cookies.txt --get-id"
        id=subprocess.run(cmd1, shell=True, stdout = subprocess.PIPE,encoding='shift-jis')
        id=str(id.stdout)
        id=id.replace("\n","")
        #スラッシュを変換してファイル名取得
        fn=fn.replace("/","⧸")
        filename=f"{fn} [{id}]"
        print(filename)

        #音声とサムネイルをDL
        cmd2 =f"yt-dlp {inURL} --cookies cookies.txt -x --audio-format mp3 -P ./yt-dlp --write-thumbnail --convert-thumbnails jpg"
        subprocess.run(cmd2, shell=True, stdout = subprocess.PIPE)

        #mp3にサムネを合体
        os.rename(f"yt-dlp/{filename}.jpg", "yt-dlp/in.jpg")
        os.rename(f"yt-dlp/{filename}.mp3", "yt-dlp/in.mp3")
        cmd4 =f'ffmpeg -i yt-dlp\\in.mp3 -i yt-dlp\\in.jpg -map 0:a -map 1:v -c copy -disposition:1 attached_pic -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" yt-dlp\\out.mp3'
        subprocess.run(cmd4, shell=True, stdout = subprocess.PIPE)

        #不要なファイルを消去
        os.remove("yt-dlp/in.mp3")
        os.remove("yt-dlp/in.jpg")

        #ファイル名に使用出来ない文字を変換
        datatitle=re.sub(r'[\\|/|:|?|.|"|<|>|\|]','-',datatitle)
        datatitle=datatitle.replace("\n","")
        print(f"{datatitle}.mp3")
        os.rename(f"yt-dlp/out.mp3", f"yt-dlp/{datatitle}.mp3")


    except:#ファイル名が特殊でエラーが起きる場合
        error=input("エラー:mp3とjpgのファイル名を「in」に変更してください(変更したらエンター)")

        cmd4 =f'ffmpeg -i yt-dlp\\in.mp3 -i yt-dlp\\in.jpg -map 0:a -map 1:v -c copy -disposition:1 attached_pic -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" yt-dlp\\out.mp3'
        subprocess.run(cmd4, shell=True, stdout = subprocess.PIPE)

        os.remove("yt-dlp/in.mp3")
        os.remove("yt-dlp/in.jpg")
