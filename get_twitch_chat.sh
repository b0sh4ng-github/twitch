mkdir "twitch_chat" > /dev/null 2>&1
VID=$1
echo $VID > VID.txt
MAX_T=3500
while [ $VID -ge 0 ]; do
    ((i=i%MAX_T)); ((i++==0)) && wait
    tcd --settings-file "custom_settings.json" -v $VID -f json -o "twitch_chat" &
    sleep 0.02
    VID=$(($VID - 1))
    # if [ ! $(($VID % 1000)) ]
    #     then
    #     echo $VID > EVID.txt
    # fi
done