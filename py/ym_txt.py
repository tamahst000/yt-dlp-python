import os

from utils import (
    convert_from_txt_to_url_list,
    download_from_youtubedl,
    crop_thumbnail,
    embed_image_in_mp3,
    sanitize_filename,
)


cookies_file = "py/cookies.txt"
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

url_list = convert_from_txt_to_url_list()

for url in url_list:
    filename_base = download_from_youtubedl(ydl_opts, url)

    thumbnail_webp_path = os.path.join(output_dir, f"{filename_base}.webp")
    audio_path = os.path.join(output_dir, f"{filename_base}.mp3")
    thumbnail_crop_path = os.path.join(output_dir, "thumbnail_convert.jpg")

    crop_thumbnail(thumbnail_webp_path, thumbnail_crop_path)

    try:
        embed_image_in_mp3(audio_path, thumbnail_crop_path)
        sanitize_filename(filename_base, output_dir, audio_path)

    except FileExistsError:
        print("----- ERROR : 同じ名前のファイルが既に存在しています")
        continue
