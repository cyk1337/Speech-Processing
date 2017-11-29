import re
import os, subprocess
# from numpy.random import permutation
from random import shuffle

cat_stat = dict()

cat_stat['NN'] = {  'm':{
                        'big':[],
                        'small':[],
                        'headset':[],
                        'laptop': [],
                        'iMac': []
                        },
                    'f':{
                        'big':[],
                        'small':[],
                        'headset':[],
                        'laptop': [],
                        'iMac': []
                     }
                }
cat_stat['SC'] = {
                    'm':{
                        'big':[],
                        'small':[],
                        'headset':[],
                        'laptop': [],
                        'iMac': []
                        },
                    'f':{
                        'big':[],
                        'small':[],
                        'headset':[],
                        'laptop': [],
                        'iMac': []
                     }
}

cat_stat['UK'] = {
                    'm':{
                        'big':[],
                        'small':[],
                        'headset':[],
                        'laptop': [],
                        'iMac': []
                        },
                    'f':{
                        'big':[],
                        'small':[],
                        'headset':[],
                        'laptop': [],
                        'iMac': []
                     }
}

cat_uk_m = []
cat_uk_f = []

cat_sc_m = []
cat_sc_f = []


cat_nn_m = []
cat_nn_f = []

cat_n_m = []
cat_n_f=[]

# accent
pat_NN = "\s+NN\s+"
pat_SC = "\s+SC\s+"
pat_UK = "\s+UK\s+"
pat_AZ = "\s+AZ\s+"
pat_NA = "\s+NA\s+"

# gender
pat_female = "\s+(Female|f)\s+"
pat_male = "\s+(Male|m)\s+"

# microphone type
pat_big = "\s+big\s+"
pat_small = "\s+small\s+"
pat_headset = "headset"  # three kinds of headset
pat_laptop = "\s+laptop\s+"
pat_iMac = "iMac"  # some iMac  has suffix

pat_name = "(s\d{7})|([a-z]+\s+)"
# path_ = "/Volumes/Network/courses/sp/data/mfcc/train/{}_train.mfcc\n"
path_ = "{}\n"

def parse_category(filename):
    with open(filename) as f:
        for f in f.readlines():
            seg = f.split()
            if len(seg)>0:
                # uk_ = re.findall(pat_UK, f)
                # # print(f)
                # if len(uk_)>0:
                #     # find all ukers
                #     uk_m = re.findall(pat_male, f)
                #     if len(uk_m)>0:
                #         # find all uk male
                #         if(exclude_list(seg[0])):
                #             # exclude all bad users
                #             # print(seg[0])
                #             cat_uk_m.append(seg[0])
                #             # print(seg[0])
                #     else:
                #         if (exclude_list(seg[0])):
                #             # exclude all bad users
                #             # print(seg[0])
                #             cat_uk_f.append(seg[0])
                #             # print(seg[0])
                # sc_ = re.findall(pat_SC, f)
                # if len(sc_) > 0:
                #                 # find all ukers
                #                 sc_m = re.findall(pat_male, f)
                #                 if len(sc_m) > 0:
                #                     # find all uk male
                #                     if (exclude_list(seg[0])):
                #                         # exclude all bad users
                #                         # print(seg[0])
                #                         cat_sc_m.append(seg[0])
                #                         # print(seg[0])
                #                 else:
                #                     if (exclude_list(seg[0])):
                #                         # exclude all bad users
                #                         # print(seg[0])
                #                         cat_sc_f.append(seg[0])
                #                         # print(seg[0])

                # NN

                nn_ = re.findall(pat_NN, f)
                # print(f)
                if len(nn_ ) > 0:
                    # find all ukers
                    nn_m = re.findall(pat_male, f)
                    if len(nn_m) > 0:
                        # find all uk male
                        if (exclude_list(seg[0])):
                            # exclude all bad users
                            # print(seg[0])
                            cat_nn_m.append(seg[0])
                            # print(seg[0])
                    else:
                        if (exclude_list(seg[0])):
                            # exclude all bad users
                            # print(seg[0])
                            cat_nn_f.append(seg[0])
                            # print(seg[0])
                else:
                    n_m = re.findall(pat_male, f)
                    if len(n_m) > 0:
                        # find all uk male
                        if (exclude_list(seg[0])):
                            # exclude all bad users
                            # print(seg[0])
                            cat_n_m.append(seg[0])
                            # print(seg[0])
                    else:
                        if (exclude_list(seg[0])):
                            # exclude all bad users
                            # print(seg[0])
                            cat_n_f.append(seg[0])
                # if exclude_list(0):
                #     print(f.split()[0])
                #     nn_ = re.findall(pat_NN, f)
                #     if len(nn_)>0:
                #         # not native speaker
                #         NN = re.findall("",f)
                #         cat_stat['NN'].append(NN)

                # else:
                #     # native speaker
                #     N = re.findall("s\d{7}", f)
                #     if len(N)> 0 and exclude_list(N[0]):
                #         cat_stat['N'].append(N[0])



def exclude_list(uname):
    # re.findall("s\d{7}", f)
    return uname not in ['calum','jamesc','behzad','s0343804','s0346429','s0451815','s0455730','s0126163','s0676515',
                         "=================================================================", "Year:","Year", "Name",
                         "----","students","Information","behzad","calum","jamesc","panagiot","s0343804","s0346429","s0348176",
                         "s0349492","s0451815","s0455730","s0565246","s0568074","s0674876","s0946728","s1054017","s1210107",
                         "s1210764","s1233656","s1239695","s1305077","s1324313","s1347498","s1408442","s1458392","s1471720",
                         "s1524812","s1531452","s1614280","s1617188","s1623659","s1648755","s1676749","s1685899","s1700949",
                         "s1702456","s1718768","s1720613","s1731574","s1763562","s1775528","s1775678","s1778033","s1785247",
                         "s1789553","s1789699","s1794269"
                         ]

def flag_(pat, s):
    if(len(re.findall(pat, s))) > 0:
        return True
    else:
        return False

def gen_train_file(fname, cat_list):
    if os.path.isfile(fname):
        os.remove(fname)
    with open(fname, 'w') as f:
        for uun in cat_list:
            f.write(path_.format(uun))
    print("{} has generated!".format(fname))

def run_bash(script, param=None):
    if param is None:
        os.system('sh {}'.format(script))
    else:
        os.system('sh {} {}'.format(script,param))


if __name__ == "__main__":
    fname="info.txt"
    parse_category(fname)
    # print(cat_stat)


    #UK
    # print("UK male", '-' * 80)
    # print(cat_uk_m,len(cat_uk_m))# 42
    # print("UK female"+'-'*80)
    # print(cat_uk_f,len(cat_uk_m)) #42
    # gen_train_file(fname='train_uk_m30', cat_list=cat_uk_m[:30])
    # gen_train_file(fname='train_uk_f30', cat_list=cat_uk_f[:30])
    # gen_train_file(fname='val_uk_m10', cat_list=cat_uk_m[30:40])
    # gen_train_file(fname='val_uk_f10', cat_list=cat_uk_f[30:40])
    # gen_train_file(fname='train_uk_m_f_30', cat_list=cat_uk_m[:15]+cat_uk_m[:15])


    # sc
    # print(cat_sc_m, len(cat_sc_m)) # 27
    # print(cat_sc_f, len(cat_sc_f)) # 6
    # gen_train_file(fname='sc_m27', cat_list=cat_uk_m)
    # gen_train_file(fname='test_sc_m10', cat_list=cat_uk_m[:10])
    # gen_train_file(fname='test_sc_f6', cat_list=cat_uk_m[:6])

    # print(cat_nn_m, len(cat_nn_m))  #
    # print(cat_nn_f, len(cat_nn_f))  #
    # gen_train_file(fname='nn_m', cat_list=cat_nn_m)
    # gen_train_file(fname='nn_f', cat_list=cat_nn_f)

    # print(cat_n_m, len(cat_n_m))  #
    # print(cat_n_f, len(cat_n_f))  #
    # gen_train_file(fname='n_m', cat_list=cat_n_m)
    # gen_train_file(fname='n_f', cat_list=cat_n_f)

    print(cat_nn_m, len(cat_nn_m))  #
    print(cat_nn_f, len(cat_nn_f))  #
    gen_train_file(fname='nn_m', cat_list=cat_nn_m)
    gen_train_file(fname='nn_f', cat_list=cat_nn_f)

"""
    # NN 199, Native 160
    shuffle(cat_stat['NN'])
    shuffle(cat_stat['N'])

    # experiment 1.1
    train1 = cat_stat['NN'][:100] + cat_stat['N'][:100]
    # generate 100 not native and 100 native
    gen_train_file(fname='train11_nn_vs_n',cat_list=train1)

    # experiment 1.2
    train2 = cat_stat['NN'][:100]
    gen_train_file(fname='train12_nn', cat_list=train2)

    # experiment 1.3
    train3 = cat_stat['N'][:100]
    gen_train_file(fname='train13_n', cat_list=train3)

    # val 1
    val1 = cat_stat['NN'][100:110] + cat_stat['N'][100:110]
    gen_train_file(fname='val1_nn_vs_n', cat_list=val1)
"""
    # run_bash('script/test.sh',"ssss xxxx")




# check echo have a \n
    # with open('users_mfcc.txt','r') as f:
    #     s= f.readline()
    #     print('\n' in s)
# name, gender, microphone, accent