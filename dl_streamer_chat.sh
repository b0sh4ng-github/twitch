mkdir $1"_chat" > /dev/null 2>&1
tcd --settings-file "custom_settings.json" -c $1 -f json --first=$2 -o $1"_chat" &