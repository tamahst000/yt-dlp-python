set /p inURL="URL:"

yt-dlp %inURL% --cookies cookies.txt --embed-thumbnail -f bestvideo+bestaudio --merge-output-format mp4 -o "yt-dlp\%%(upload_date)s %%(title)s"

pause
