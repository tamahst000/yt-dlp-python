set /p inURL="URL:"

yt-dlp %inURL% --cookies cookies.txt -P ./yt-dlp --write-thumbnail --convert-thumbnails jpg

pause