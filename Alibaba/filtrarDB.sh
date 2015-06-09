#!/bin/bash

# En el mismo directorio que se encuentra train_format1.csv, ejecutar haciendo ./filtrarDB.sh <tamañoDB>
# Tiene como salida dos archivos: train.csv (con el 70% de la población, para entrenar la red) y test.csv (con el 30% restante, para predecir)

CANTTOTAL=$1

CONT1=0
CONT0=0
MAX_COMP=$((CANTTOTAL / 2))
MAX_NOCOMP=$((CANTTOTAL / 2))
MAX_TRAIN_COMP=$(echo "$MAX_COMP*0.7" | bc)
MAX_TRAIN_NOCOMP=$(echo "$MAX_NOCOMP*0.7" | bc)


rm train.csv 2> /dev/null
rm test.csv 2> /dev/null
tail -n +2 train_format1.csv | while read line && [ $CONT1 -lt $MAX_COMP -o $CONT0 -lt $MAX_NOCOMP ]
do
	VAR="$(echo "$line" | grep "1$")"
	if [ "$VAR" != "" ] && [ $CONT1 -lt $MAX_COMP ]
	then
		if [ $(echo "$CONT1 < $MAX_TRAIN_COMP" | bc) -ne 0 ]
		then
			user_id="^$(echo "$VAR" | cut -d, -f1),"
			VAR="$VAR,$(grep "$user_id" user_info_format1.csv | cut -d, -f2,3)"
			echo "$VAR" >> train.csv
		else
			user_id="^$(echo "$VAR" | cut -d, -f1),"
			VAR="$VAR,$(grep "$user_id" user_info_format1.csv | cut -d, -f2,3)"
			echo "$VAR" >> test.csv
		fi
		CONT1=$((CONT1+1))
	else
		if [ "$VAR" = "" ] && [ $CONT0 -lt $MAX_NOCOMP ]
		then
			if [ $(echo "$CONT0 < $MAX_TRAIN_NOCOMP" | bc) -ne 0 ]
			then
				user_id="^$(echo "$line" | cut -d, -f1),"
				line="$line,$(grep "$user_id" user_info_format1.csv | cut -d, -f2,3)"
				echo "$line" >> train.csv
			else
				user_id="^$(echo "$line" | cut -d, -f1),"
				line="$line,$(grep "$user_id" user_info_format1.csv | cut -d, -f2,3)"
				echo "$line" >> test.csv
			fi
			CONT0=$((CONT0+1))
		fi
	fi
done

