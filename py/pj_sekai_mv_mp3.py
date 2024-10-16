import os
from yt_dlp import YoutubeDL
from PIL import Image
from mutagen.id3 import ID3, APIC


def convert_thumbnail(webp_path, convert_path):
    if not os.path.exists(webp_path):
        print("----- ERROR : 画像ファイルが見つかりません。")
        return
    with Image.open(webp_path) as img:
        img.save(convert_path)
    os.remove(webp_path)
    print("----- Thumbnail convert completed!")


def embed_image_in_mp3(audio_path, img_path):
    if not os.path.exists(audio_path):
        print("----- ERROR : 音楽ファイルが見つかりません。")
        return

    tags = ID3(audio_path)
    with open(img_path, "rb") as img_file:
        tags.add(
            APIC(
                mime="image/jpeg",
                type=3,
                desc="Cover",
                data=img_file.read(),
            )
        )
    tags.save()
    os.remove(img_path)
    print("----- Thumbnail embedding completed!")


cookies_file = "cookies.txt"
output_dir = "yt-dlp"
ydl_opts = {
    "cookiefile": cookies_file,
    "format": "best",
    "outtmpl": f"{output_dir}/%(upload_date)s %(title)s.%(ext)s",
    "writethumbnail": True,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
}

url_list = []
with open(r".\\url.txt", "r", encoding="utf_8") as f:
    while True:
        line = f.read()
        script_line = line.split("\n")
        for t in script_line:
            if "http" in t:
                url_list.append(t)
        else:
            break

for inURL in url_list:
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(inURL, download=True)
        filename = ydl.prepare_filename(info)
    filename_base = os.path.splitext(os.path.basename(filename))[0]

    thumbnail_webp_path = os.path.join(output_dir, f"{filename_base}.webp")
    thumbnail_path = os.path.join(output_dir, "thumbnail_convert.jpg")
    convert_thumbnail(thumbnail_webp_path, thumbnail_path)

    audio_path = os.path.join(output_dir, f"{filename_base}.mp3")
    embed_image_in_mp3(audio_path, thumbnail_path)
