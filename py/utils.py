import os
import re
from PIL import Image
from mutagen.id3 import ID3, APIC
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
import subprocess
import ffmpeg


def _extract_url_list_from_playlist(playlist_url):
    ydl_opts = {
        "extract_flat": True,
        "force_generic_extractor": True,
    }
    url_list = []
    with YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)
        for entry in playlist_info["entries"]:
            video_id = entry["id"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            url_list.append(video_url)
    return url_list


def _convert_from_txt_to_url_list():
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
    return url_list


def convert_from_inURL_to_url_list():
    inURL = input("URL:")

    if not inURL:
        print("url.txt を読み込みます...")
        return _convert_from_txt_to_url_list()

    if "music" in inURL:
        inURL = inURL.replace("music.", "")
        inURL = inURL.split("&si=")[0]

    if "playlist" in inURL:
        url_list = _extract_url_list_from_playlist(inURL)
    else:
        url_list = [inURL]
    return url_list


def download_from_youtubedl(ydl_opts, url):
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        filename_base = os.path.splitext(os.path.basename(filename))[0]
        print(f"----- Converting {filename_base}...")
        return filename_base
    except DownloadError as e:
        return None


def crop_thumbnail(webp_path, crop_path):
    if not os.path.exists(webp_path):
        print("----- ERROR : 画像ファイルが見つかりません。")
        return

    with Image.open(webp_path) as img:
        img_width, img_height = img.size
        target_width, target_height = img_height, img_height

        left = (img_width - target_width) // 2
        upper = (img_height - target_height) // 2
        right = left + target_width
        lower = upper + target_height

        cropped_img = img.crop((left, upper, right, lower))
        cropped_img.save(crop_path)
    os.remove(webp_path)
    print("----- Thumbnail crop completed!")


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


def embed_image_in_mp4(video_path, img_path, tmp_video_path):
    video = ffmpeg.input(video_path)
    cover = ffmpeg.input(img_path)
    (
        ffmpeg.output(
            video,
            cover,
            tmp_video_path,
            c="copy",
            **{"c:v:1": "mjpeg"},
            **{"disposition:v:1": "attached_pic"},
        )
        .global_args("-map", "0")
        .global_args("-map", "1")
        .global_args("-loglevel", "error")
        .run(overwrite_output=True)
    )
    os.remove(img_path)
    os.remove(video_path)
    os.rename(tmp_video_path, video_path)
    print("----- Thumbnail embedding completed!")


def sanitize_filename(filename_base, output_dir, audio_path):
    invalid_chars = r'[<>:"/\\|?*⧸♥♡]'
    replacement_char = " "
    sanitized_filename = re.sub(invalid_chars, replacement_char, filename_base)
    if sanitized_filename != filename_base:
        new_audio_path = os.path.join(output_dir, f"{sanitized_filename}.mp3")
        os.rename(audio_path, new_audio_path)
        print("-----Update filename!")
    return sanitized_filename


def run_subprocess(cmd):
    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False
