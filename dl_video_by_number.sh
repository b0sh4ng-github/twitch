# USAGE: sh dl_video_by_number.sh video_number_eg_740247417
# Notes: bash 3 doesn't allow for reading stdin as array without using another file, so I'll refactor this with a higher level language that does allow it
# eg https://docs.python.org/3/library/subprocess.html
# eg https://stackoverflow.com/questions/3736210/how-to-execute-a-shell-script-from-c-in-linux

mkdir tw_videos > /dev/null 2>&1

youtube-dl -U

cd tw_videos && youtube-dl --force-ipv4 --geo-bypass --download-archive ydl-archive.txt -R 50 -c --write-thumbnail https://twitch.tv/videos/$VIDEO_NUM &

