import os
import random
from urllib.request import quote, unquote
import json

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
             filename = tmp[1]
             hair = mapping[tmp[2]]
             mask = mapping[tmp[3]]
             tattoo = mapping[tmp[4]]
             glasses = mapping[tmp[5]]
             clothes = mapping[tmp[6]]
             token_dict[token_id] = dict()

             token_dict[token_id]["hair"] = hair
             token_dict[token_id]["mask"] = mask
             token_dict[token_id]['tattoo'] = tattoo
             token_dict[token_id]['glass'] = glasses
             token_dict[token_id]['cloth'] = clothes
             token_dict[token_id]['filename'] = filename
         return token_dict

token_dict = atrribute_info("files/pokerClub.csv")

for i in range(len(token_dict)):
    with open("files/metadata.json") as tmp_file:
        filename = token_dict[str(i)]['filename']
        encode_filename = quote(filename, encoding="utf-8")

        content = json.load(tmp_file)
        content['image'] = "https://github.com/Hello2021Year/mystery_boxes_nft/blob/main/image/{}%EF%B8%8F.jpg".format(encode_filename)
        content['trait_type'][0]['hair'] = token_dict[str(i)]['hair']
        content['trait_type'][1]['mask'] = token_dict[str(i)]['mask']
        content['trait_type'][2]['tattoo'] = token_dict[str(i)]['tattoo']
        content['trait_type'][3]['glass'] = token_dict[str(i)]['glass']
        content['trait_type'][4]['cloth'] = token_dict[str(i)]['cloth']

        cur_path = os.getcwd() + "/token_uri/"  + "{}.json".format(i)
        with open(cur_path, "w") as f:
            json.dump(content, f)



