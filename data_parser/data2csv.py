'''

@Author : maxl

@Email : 807507917@qq.com

@IDE : PyCharm

@Time : 2018/10/9 11:14 AM

@Desc :

'''
# Lib Import
import json
from config import config_util

def save(filename, contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()
def Data2String(path):

    File = open(path, 'rb')
    # csv title
    data="label,keyword,title,tag,s0,s1,s2,s3,s4,s5,s6,s7,s8,s9,w0,w1,w2,w3,w4,w5,w6,w7,w8,w9"
    JsonIndex = 0
    for line in File:
        # Read Every Lines
        tmp_data = line.decode('utf-8').split("\t")
        tmp_json = tmp_data[1]
        TmpRSpace = tmp_json.replace(' ', '')
        # Error Raise For Empty Data
        if TmpRSpace == "":
            continue
        s = tmp_data[4].replace("\r\n","")+","+tmp_data[0].replace(",","")+","+tmp_data[2].replace(",","")+","+tmp_data[3]
        json_data = json.loads(TmpRSpace)
        list_data = sorted(json_data.items(), key=lambda d: d[1], reverse=True)
        list_len = len(list_data)
        for i in range(10):
            if (i+1)>list_len:
                s=s+","+"none"
            else:
                s=s+","+list_data[i][0].replace(",","")
        for i in range(10):
            if (i+1)>list_len:
                s=s+","+"0"
            else:
                s=s+","+list_data[i][1]
        data = data+"\n"+s
        JsonIndex = JsonIndex + 1
        if JsonIndex%10000==0:
            print(str(JsonIndex))
    # Close Txt
    File.close()
    return data
# Main Func
if __name__ == '__main__':
    # Save File Method
    txtpath = config_util.DATA_TXT_BASE
    data = Data2String(txtpath+'\\oppo_round1_train_20180929.txt')
    save(txtpath+'\\train.csv',data)


    # data = Data2String(txtpath + '/oppo_round1_train_20180929.txt')
    # save(txtpath + '/train.csv', data)



