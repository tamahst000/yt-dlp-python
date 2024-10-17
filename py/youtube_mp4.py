from utils import (
    convert_from_inURL_to_url_list,
    run_subprocess,
)

url_list = convert_from_inURL_to_url_list()

for url in url_list:
    cmd1 = f'yt-dlp {url} --cookies cookies.txt --embed-thumbnail -f bestvideo+bestaudio --merge-output-format mp4 -o "yt-dlp\%(upload_date)s %(title)s"'
    subprocess = run_subprocess(cmd1)

    if not subprocess:
        cmd2 = f'yt-dlp {url} -o "yt-dlp\%(upload_date)s %(title)s.mp4"'
        subprocess = run_subprocess(cmd2)

    print("----- Video conversion completed successfully!")
