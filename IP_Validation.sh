#!/bin/bash

#Practice_08 IP_Validation
#------------------------------------
VALID=0
#------------------------------------
SUCCESS()
{
	echo -e "\e[32m[SUCCESS]\e[0m"
}
#------------------------------------

ERROR()
{
	echo -e "\e[31m[ERROR]\e[0m"
}
#------------------------------------

INFO()
{
	echo -e "\e[35m[[INFO]\e[0m"
}
#------------------------------------
####################-CONFIG-####################
while [ -z $IP ]										# All Empty
do
	read -p "Enter Your IP Address:" IP
done

#------------------------------------
IP=`echo $IP | tr -d [:blank:] | tr -d [:alpha:]`						# Delete the spaces and chars     

#------------------------------------
NUMBER_OCTETS=`echo $IP | cut -d '.' -f 1- | tr '.' '\n' | wc -l`				# Octets

#------------------------------------

if [ $NUMBER_OCTETS -ne 4 ]									# 4 Octet Validation
then

	echo "$(ERROR) Invalid Octets"

else	

	for i in {1..4}										# Single Octet Validation
	do 
		OCTET=`echo $IP | cut -d "." -f $i`

		if [ -z $OCTET ] 								# Empty Octet Validation
		then 

			echo "$(ERROR) Empty Octet"

			let VALID=VALID-1

		fi

		if [ $OCTET -gt 255 ] > /dev/null 2>&1|| [ $OCTET -lt 0 ] > /dev/null 2>&1	# Every Octet between 0-255
		then 

			let VALID=VALID-1

		else

			let VALID=VALID+1

		fi

	done

	if [ $VALID -eq 4 ]									# Pinging the IP
	then

		if  ping -c 1 "$IP" > /dev/null 2>&1						# Pingable IP
		then

			printf "Pinging"

			for i in {1..20}							# Progress Bar
			do
			        printf '\e[95m%.0s.\e[0m' $i

				sleep 0.2

			done
			#------------------------------------
			echo -e "\n$(SUCCESS)Average Ping $IP: \e[32m$(ping -c 2 "$IP" | tail -1 | cut -d '=' -f 2 | cut -d "/" -f 2)\e[0m ms" | tee -a Practice_08_output.txt 
			echo "-----------------------------------" >> Practice_08_output.txt

		else										
												# Not Pingable IP
			printf "Pinging"
                        for i in {1..20}
                        do									# Progress Bar

                                printf '\e[95m%.0s.\e[0m' $i

                                sleep 0.2

                        done

			echo -e "\n$(ERROR) Average Ping $IP: \e[31m-1\e[0m ms" | tee -a Practice_08_output.txt
			
			echo "-----------------------------------" >> Practice_08_output.txt
		fi
	fi
fi
