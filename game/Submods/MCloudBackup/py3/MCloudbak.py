###############################
# 这里是exe文件的源码，修改这里的文件无效
# 
#
###############################

import argparse, os
from email.mime import base
from charset_normalizer import from_path
from webdav4.client import Client

url = "https://pan.monika.love/dav"
a="test"
p="test"
no=0

wclient = None

dataDir = os.getenv("APPDATA") + "\RenPy\Monika After Story"

def main():
    parser = argparse.ArgumentParser(description='Monika Pan - MAS persistent backup')
    #parser.add_argument('-u', '--url', help='莫盘webdav url')
    parser.add_argument('-a', '--account', help='账号')
    parser.add_argument('-p', '--pwd', help='密码')
    parser.add_argument('-n','--no', help='编号')
    args = parser.parse_args()
    a = args.account
    p = args.pwd
    no = args.no
    loadwebdav()
    upload_file()


def loadwebdav():
    global wclient
    wclient = Client(base_url=url, auth=(a, p))

def namer():
    return "persistent_{}".format(no)

def upload_file():
    wclient.upload_file(from_path=dataDir+"/persistent", to_path='/MAS_backup/'+namer(), overwrite=True)

def delete_old():
    try:
        wclient.remove('/MAS_backup/persistent_{}'.format(int(no)-10))
    except:
        pass


main()