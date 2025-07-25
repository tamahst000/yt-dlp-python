set /p inURL="URL:"

yt-dlp %inURL% --hls-use-mpegts --merge-output-format mp4 -o "yt-dlp\%%(upload_date)s %%(title)s.mp4"

pause
