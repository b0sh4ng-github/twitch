youtube-dl -U
mkdir tw_videos > /dev/null 2>&1
cd tw_videos && youtube-dl --force-ipv4 --geo-bypass --download-archive ydl-archive.txt -R 50 -c --write-thumbnail https://twitch.tv/videos/$1