set /p inURL="URL:"

yt-dlp %inURL% -o "yt-dlp\%%(upload_date)s %%(title)s.mp4" 

pause
