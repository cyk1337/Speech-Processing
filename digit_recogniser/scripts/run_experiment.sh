#!/bin/sh


# TRAIN=$1
# TEST=$2

# TRAIN=resources/train_list
# TEST=resources/test_list

TRAIN1=experiment/uk_m30
TRAIN2=experiment/uk_f30
TRAIN3=experiment/uk_m_f30
TRAIN4=experiment/sc_m27

TEST0=experiment/uk_m10_in
TEST1=experiment/uk_m10
TEST2=experiment/uk_f10
TEST3=experiment/sc_m10
TEST4=experiment/sc_f6

# experiment 3
TRAIN_NN=experiment/nn_f # (80) 82.65
TRAIN_NN50=experiment/nn_f50 # 75.59
TRAIN_M=experiment/nn_n_100 # 75.59

TEST_NN10=experiment/nn_f7 # 27


TRAIN=$TRAIN_NN50
TEST=$TEST_NN10

./scripts/initialise_and_train_models $TRAIN
# at this point, the special shell variable $? contains the exit status of HInit
# for readability, let's put that status into a variable with a nicer name
STATUS=$?

# test whether the return status is 0 (indicates success)
if [ ${STATUS} = 0 ]
then
 echo "HInit ran without error"
else
 echo "Something went wrong in HInit, which exited with code "${STATUS}
 # a good idea is to exit this script with the same error code
 # (or some other non-zero value, if you prefer)
 # so that anything calling this script can also detect the error
 exit ${STATUS}
fi
 ./scripts/recognise_test_data $TEST

 ./scripts/results

# =======================
# Train1 uk_m_30
# test0: 87.65
# test1: m 94.93
# test2: f 79.67
# test3: sc_m 89.97
# test4: sc_f 98.32

# Train1 uk_f_30
# test1: m 72.97
# test2: f 92.33
# test3: sc_m 66.56
# test4: sc_f 78.77

# train4 sc_m_27
# test1: m 96.96
# test3 sc_m 87.63

#NN 100
# test 59.33

# NN 50 67.67
