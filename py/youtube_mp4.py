import os

from utils import (
    convert_from_inURL_to_url_list,
    download_from_youtubedl,
    convert_thumbnail,
    embed_image_in_mp4,
)

cookies_file = "py/cookies.txt"
output_dir = "yt-dlp"
ydl_opts = {
    "cookiefile": "cookies.txt",
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
    "outtmpl": "yt-dlp/%(upload_date)s %(title)s.%(ext)s",
    "writethumbnail": "true",
}
ydl_opts_except = {
    "format": "bestvideo+bestaudio",
    "outtmpl": "yt-dlp/%(upload_date)s %(title)s.%(ext)s",
    "writethumbnail": "true",
}
url_list = convert_from_inURL_to_url_list()

for url in url_list:
    filename_base = download_from_youtubedl(ydl_opts, url)

    if not filename_base:
        filename_base = download_from_youtubedl(ydl_opts_except, url)

    formats = [".webp", ".png", ".jpg"]
    thumbnail_path = next(
        (
            os.path.join(output_dir, f"{filename_base}{ext}")
            for ext in formats
            if os.path.exists(os.path.join(output_dir, f"{filename_base}{ext}"))
        ),
        None,
    )

    if thumbnail_path is None:
        continue

    if thumbnail_path.endswith(".webp"):
        convert_thumbnail(
            thumbnail_path, os.path.join(output_dir, "thumbnail_convert.jpg")
        )
        thumbnail_path = os.path.join(output_dir, "thumbnail_convert.jpg")

    video_path = os.path.join(output_dir, f"{filename_base}.mp4")
    tmp_video_path = os.path.join(output_dir, "tmp.mp4")
    embed_image_in_mp4(video_path, thumbnail_path, tmp_video_path)
