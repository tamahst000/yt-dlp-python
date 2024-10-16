set /p inURL="URL:"

yt-dlp %inURL% --cookies cookies.txt -x --audio-format mp3 -P ./yt-dlp --write-thumbnail --convert-thumbnails png

pause