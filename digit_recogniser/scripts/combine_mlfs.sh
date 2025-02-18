#!/bin/sh

# a script to combine all MLFs into one big MLF

# the shared data folder
HOME=${DATA:-/Users/yekun/Desktop/0SP/digit_recogniser}
DATA=${DATA:-${HOME}/loc_data}
# and where the MLFs are for test data
MLF_DIR=${DATA}/lab/test

# create a temporary place to work
# mktemp -d creates a temporary directory, guaranteed to have a unique name
# we'll provide a meaningful prefix for the unique name using the -t option,
#  so that (if we fail to clean up) we'll know what it is
WORKING_DIRECTORY=`mktemp -d -t combine_mlfs_temp_dir`
echo Temporary working directory is ${WORKING_DIRECTORY}


MLF_LIST_FILE=${WORKING_DIRECTORY}/mlf_list
SCP_FILE=${WORKING_DIRECTORY}/files.scp


# catch signals, such as if the user hits ctrl-C during execution
# and exit cleanly
trap "{ echo; echo Cleaning up and terminating script; rm -rf $WORKING_DIRECTORY; exit 1; }" SIGINT SIGTERM SIGKILL

# find all MLFS
echo "Looking for MLFs in "${MLF_DIR}

# # find everything that matches *.mlf, except files whose name starts with a period (which are special files created by OS X)
# find ${MLF_DIR} -type f  \( -iname "*.mlf" ! -iname ".*" \) > ${MLF_LIST_FILE}
# NUM_MLFS=`cat ${MLF_LIST_FILE} | wc -l`
# echo Found ${NUM_MLFS} MLF files to process
#
# # create a valid, empty MLF file, as a starting point
# echo "#!MLF!#" > ${WORKING_DIRECTORY}/everyone.mlf
#
# # initialise a variable as a counter
# COUNTER=0
#
# # for every MLF that we can find
# for MLF in `cat ${MLF_LIST_FILE}`
# do
#     # increment the counter by 1
#     ((COUNTER++))
#
#     # echo -n prints without a newline
# 	echo -n "Processing "${COUNTER}" of "${NUM_MLFS}": "
#
#     # extract the names of the label files in the current 'everyone.mlf' MLF, and place in a script file
# 	grep '"' ${WORKING_DIRECTORY}/everyone.mlf | tr -d '"' > ${SCP_FILE}
#     # and the same for the current MLF, appending to the same script file
# 	grep '"' $MLF | tr -d '"' >> ${SCP_FILE}
#
#     # attempt to combine 'everyone.mlf' and the current MLF, using HLEd
#     # since HLEd needs an 'instructions' file, but we don't want to make any changes, we give it /dev/null (an empty file)
# 	HLEd -I $MLF -I ${WORKING_DIRECTORY}/everyone.mlf -I $MLF -i ${WORKING_DIRECTORY}/everyone_new.mlf -S ${SCP_FILE} /dev/null
#
#     # did HLEd exit with an error?
# 	if [ $? -ne 0 ]; then
#         echo
#         echo "Error from HLEd - skipping "${MLF}
#         # don't keep the new MLF - we can't add the current user to it
#         rm -f ${WORKING_DIRECTORY}/everyone_new.mlf
#     else
#         # all good, keep the new MLF, to replace the previous one
#         echo "HLEd ran OK - keeping "${MLF}
#         mv ${WORKING_DIRECTORY}/everyone_new.mlf ${WORKING_DIRECTORY}/everyone.mlf
#     fi
#
# done
#
# # move the final MLF to the current directory
# mv ${WORKING_DIRECTORY}/everyone.mlf .
#
# # clean up
# rm -rf ${WORKING_DIRECTORY}
#
# echo "Finished. The final MLF is in the current directory and is called everyone.mlf"
#
#                                                                                                                                                 
