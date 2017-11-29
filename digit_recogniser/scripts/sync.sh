#!/bin/bash
# sanity check, then sync files for a given UUN

# must run from data directory

if test `basename $(pwd)` != "data"
	then
	echo "Can only run from a directory called 'data'"
	exit 1
fi


SOURCE=../data_upload
TARGET=.
INFO=info.txt
UUN=$1



FLIST=""
# check all files exist
# training data
for TYPE in lab mfcc wav
do
	FLIST+=${SOURCE}/${TYPE}/train/${UUN}_train.${TYPE}" "
done

# testing data
FLIST+=${SOURCE}/lab/test/${UUN}_test.mlf" "

for TYPE in wav mfcc
do
	for N in $(seq -f "%02g" 1 30)
	do
		FLIST+=${SOURCE}/${TYPE}/test/${UUN}_test${N}.${TYPE}" "
	done
done


for F in ${FLIST}
do
	echo -n Checking ${F}":"
	if test -f $F
		then
		echo OK
	else
		echo 
		echo Missing $F
		exit 1
	fi
done

if grep -q $UUN ${SOURCE}/info.txt
	then
	echo -n "Found info line OK : "
        grep $UUN ${SOURCE}/info.txt
else
	echo Missing info line
	exit -1
fi

# check train label file format - xlabel format will contain the string "font"
if grep -q font ${SOURCE}/lab/train/${UUN}_train.lab
	then
	echo "Training labels in WAVES format - OK"
else
	echo "Your training labels ("${UUN}_train.lab") have been saved in the wrong format."
	echo "You need to load this file back into Wavesurfer, change the format to WAVES, then save it again."
	echo "You will probably need to use 'save transcription as' to force Wavesurfer to save it."
	echo "See 'Label your training data' Step 3 here:"
	echo "http://www.speech.zone/exercises/digit-recogniser/speaker-dependent-system/collect-and-label-the-data/"
	echo "After doing this, run the make_mfccs script again."
	exit -1
fi

echo "All good - copying files"
for F in ${FLIST}
do
	# dirty - hardwired dir names
	O=`echo ${F} | sed 's/data_upload/data/'`

	cp -X -v $F $O
	chmod u=rw,go=r $O
done


echo "Copying info line"
grep --text -v $UUN ${TARGET}/info.txt > /tmp/1.txt
grep --text    $UUN  ${SOURCE}/info.txt | tail -1 > /tmp/2.txt
cat /tmp/1.txt /tmp/2.txt > /tmp/info.txt
rm /tmp/1.txt /tmp/2.txt
cp /tmp/info.txt ${TARGET}/info.txt
echo "Done - here is the end of the info.txt file"
tail  info.txt

