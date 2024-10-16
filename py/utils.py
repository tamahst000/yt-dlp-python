import os
import re
from PIL import Image
from mutagen.id3 import ID3, APIC


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


def convert_thumbnail(webp_path, convert_path):
    if not os.path.exists(webp_path):
        print("----- ERROR : 画像ファイルが見つかりません。")
        return
    with Image.open(webp_path) as img:
        img.save(convert_path)
    os.remove(webp_path)
    print("----- Thumbnail convert completed!")


def sanitize_filename(filename_base):
    invalid_chars = r'[<>:"/\\|?*⧸♥♡]'
    replacement_char = " "
    sanitized_filename = re.sub(invalid_chars, replacement_char, filename_base)

    change = False
    if sanitized_filename != filename_base:
        change = True
    return sanitized_filename, change


def get_url_list():
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
