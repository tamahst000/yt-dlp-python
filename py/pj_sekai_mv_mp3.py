import os
from yt_dlp import YoutubeDL

from utils import get_url_list, convert_thumbnail, embed_image_in_mp3, sanitize_filename

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

url_list = get_url_list()

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

    sanitized_filename, change = sanitize_filename(filename_base)
    if change:
        new_audio_path = os.path.join(output_dir, f"{sanitized_filename}.mp3")
        os.rename(audio_path, new_audio_path)
        print("-----Update filename!")
