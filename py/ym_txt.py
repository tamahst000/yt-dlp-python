import os
from yt_dlp import YoutubeDL
from PIL import Image
from mutagen.id3 import ID3, APIC


def crop_thumbnail(webp_path, before_path, after_path):
    if not os.path.exists(webp_path):
        print("----- ERROR : 画像ファイルが見つかりません。")
        return

    os.rename(webp_path, before_path)
    with Image.open(before_path) as img:
        img_width, img_height = img.size
        target_width, target_height = img_height, img_height

        left = (img_width - target_width) // 2
        upper = (img_height - target_height) // 2
        right = left + target_width
        lower = upper + target_height

        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(after_path)
    os.remove(before_path)
    print("----- Thumbnail crop completed!")


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
    print("----- Thumbnail embedding completed!")


cookies_file = "cookies.txt"
output_dir = "yt-dlp"
ydl_opts = {
    "cookiefile": cookies_file,
    "format": "best",
    "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
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
    print(f"----- Converting {filename_base}...")

    thumbnail_webp_path = os.path.join(output_dir, f"{filename_base}.webp")
    thumbnail_before_path = os.path.join(output_dir, "thumbnail_before.jpg")
    thumbnail_after_path = os.path.join(output_dir, "thumbnail_after.jpg")
    crop_thumbnail(thumbnail_webp_path, thumbnail_before_path, thumbnail_after_path)

    audio_path = os.path.join(output_dir, f"{filename_base}.mp3")
    embed_image_in_mp3(audio_path, thumbnail_after_path)

    os.remove(os.path.join(output_dir, "thumbnail_after.jpg"))
