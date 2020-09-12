mkdir "twitch_chat" > /dev/null 2>&1

function get_twitch_chat {
    VID=$(<VID.txt)
    echo "I'm starting at video "$VID
    MAX_T=2500
    EVID=$(($VID - 2500))
    while [ $VID -ge $EVID ]; do
        ((i=i%MAX_T)); ((i++==0)) && wait
        tcd --settings-file "custom_settings.json" -v $VID -f json -o "twitch_chat" &
        sleep 0.025
        VID=$(($VID - 1))
    done
    echo $VID > VID.txt
}

while [ true ]; do
    get_twitch_chat
    sleep 1
done