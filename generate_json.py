import os
import random


# dict 保留数字和属性的映射
mapping = {"1":"A","2":"B","3":"C","4":"D","5":"E","6":"F"}
def atrribute_info(filepath):
    with open (filepath,'r') as f:
         # skip the header
         next(f)
         lines = f.readlines();
         token_dict = dict()
         for line in lines:
             tmp = line.split(",")

             token_id = tmp[0]
             filename = tmp[2]
             hair = mapping[tmp[1]]
             mask = mapping[tmp[2]]
             tattoo = mapping[tmp[3]]
             glasses = mapping[tmp[4]]
             clothes = mapping[tmp[5]]
             token_dict[token_id] = dict()

             token_dict[token_id]["hair"] = hair
             token_dict[token_id]["mask"] = mask
             token_dict[token_id]['tattoo'] = tattoo
             token_dict[token_id]['glasses'] = glasses
             token_dict[token_id]['clothes'] = clothes
         return token_dict



def shuffle(filepath):
    file_list = []
    files = os.listdir(filepath)
    for filename in files:
        tmp_file = filepath + "/" + filename
        sub_files = os.listdir(tmp_file)
        file_list = file_list + sub_files

    return file_list

# 获取所有的文件名，并进行shuffle
file_list = shuffle('image')
random.shuffle(file_list)
for file in file_list:
    print(file)


token_dict = atrribute_info("files/pokerClub.csv")



#image = "https://github.com/Hello2021Year/mystery_boxes_nft/blob/main/image/{}%EF%B8%8F/{}EF%B8%8F.jpg".format()