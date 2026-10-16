#!/bin/bash

#Practice_03
####################-FUNC-######################

SUCCESS()
{
	echo -e "\e[32m[SUCCESS]\e[0m"
}
INFO()
{
 	echo -e "\e[33m[INFO]\e[0m"
}
ERROR()
{
	echo -e "\e[31m[ERROR]\e[0m"
}
Progress_bar()
{
	for i in {1..100}
	do
        FILLED=$((i / 5))
        EMPTY=$((20 - FILLED))

        BAR=$(printf '\e[33m%0.s#\e[0m' $(seq 1 $FILLED))
        if [ "$EMPTY" -gt 0 ]; then
                SPACES=$(printf '\e[33m%0.s-\e[0m' $(seq 1 $EMPTY))
        else
            SPACES=""
        fi
        printf "\r[%s%s] %d%%" "$BAR" "$SPACES" "$i"

        sleep 0.05
	done

}
####################-CONFIG-####################

if ping -c 1 "$1" > /dev/null 2>&1
then
	echo "$(SUCCESS)Server is pingable"
	sleep 2
	echo "$(INFO)Copying file."

	sshpass -p "$3" scp $4 "$2@$3:"$5""
	if [ $? -eq 0 ]
	then
		Progress_bar	
		echo "$(SUCCESS)FIle Copied."
	fi
else
	Progress_bar
	echo "$(ERROR)server is not accessible"
fi

#DONE

