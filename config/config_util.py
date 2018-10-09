'''

@Author : maxl

@Email : 807507917@qq.com

@IDE : PyCharm

@Time : 2018/10/9 11:04 AM

@Desc :

'''
import configparser

config = configparser.ConfigParser()
config.read("../config/config.ini")

DATA_TXT_BASE = config["data"]["txt_path_base"]
DATA_JSON_BASE = config["data"]["json_path_base"]
DATA_MAT_BASE = config["data"]["mat_path_base"]
DATA_CSV_BASE = config["data"]["csv_path_base"]
