import subprocess
from PIL import Image
import os
import re

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
    #Youtube MusicからのURLの場合
    if "music" in inURL:
        inURL=inURL.replace("music.","")
        #inURL=inURL.replace("&feature=share","")
        #231001変更
        inURL=inURL.split("&si=")[0]

    try:
        #ファイル名取得
        cmd1 =f"yt-dlp {inURL} --cookies cookies.txt --get-filename"
        filename=subprocess.run(cmd1, shell=True, stdout = subprocess.PIPE,encoding='shift-jis')
        filename=str(filename.stdout)
        filename=filename.replace(".webm\n","")

        #音声とサムネイルをDL
        cmd2 =f"yt-dlp {inURL} --cookies cookies.txt -x --audio-format mp3 -P ./yt-dlp --write-thumbnail --convert-thumbnails jpg"
        subprocess.run(cmd2, shell=True, stdout = subprocess.PIPE)

        #画像を正方形に切り取り
        os.rename(f"yt-dlp/{filename}.jpg", "yt-dlp/inb.jpg")
        cmd3 =f"magick yt-dlp\\inb.jpg -crop 720x720+280+0 yt-dlp\\in.jpg"
        subprocess.run(cmd3, shell=True, stdout = subprocess.PIPE)
        os.remove("yt-dlp/inb.jpg")

        #mp3にカバーアートを追加
        os.rename(f"yt-dlp/{filename}.mp3", "yt-dlp/in.mp3")
        cmd4 =f'ffmpeg -i yt-dlp\\in.mp3 -i yt-dlp\\in.jpg -map 0:a -map 1:v -c copy -disposition:1 attached_pic -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" yt-dlp\\out.mp3'
        subprocess.run(cmd4, shell=True, stdout = subprocess.PIPE)

        name=re.sub("(?<=\[).*(?=\])","",filename)
        name=name.replace("[","")
        name=name.replace("]","")
        print(type(name))
        os.rename(f"yt-dlp/out.mp3", f"yt-dlp/{name}.mp3")
        os.remove("yt-dlp/in.mp3")
        os.remove("yt-dlp/in.jpg")

    except:#ファイル名が特殊でエラーが起きる場合
        error=input("エラー:mp3とjpgのファイル名を「in」に変更してください(変更したらエンター)")

        cmd3 =f"magick yt-dlp\\in.jpg -crop 720x720+280+0 yt-dlp\\in.jpg"
        subprocess.run(cmd3, shell=True, stdout = subprocess.PIPE)

        cmd4 =f'ffmpeg -i yt-dlp\\in.mp3 -i yt-dlp\\in.jpg -map 0:a -map 1:v -c copy -disposition:1 attached_pic -id3v2_version 3 -metadata:s:v title="Album cover" -metadata:s:v comment="Cover (front)" yt-dlp\\out.mp3'
        subprocess.run(cmd4, shell=True, stdout = subprocess.PIPE)

        os.remove("yt-dlp/in.mp3")
        os.remove("yt-dlp/in.jpg")
