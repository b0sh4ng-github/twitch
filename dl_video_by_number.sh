# USAGE: sh dl_video_by_number.sh video_number_eg_740247417 video_number_2 724651520 etc

IFS=$'\n' # split on newline only
set -f    # disable globbing
list=($(printf "%s" "$input"))

mkdir tw_videos > /dev/null 2>&1

youtube-dl -U

for VIDEO_NUM in $list; do 
    cd tw_videos && youtube-dl --force-ipv4 --geo-bypass --download-archive ydl-archive.txt -R 50 -c --write-thumbnail https://twitch.tv/videos/$VIDEO_NUM &
done
