done=0
if [ $1 ]; then
	while true ; do
		leaks $1;
		if [ "$done" -ne 0 ]; then
			break
		fi
		if [[ $2 == "" ]]; then
			sleep 2;
		else
			sleep $2;
		fi
	done
fi
