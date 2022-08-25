
default persistent._MCloudBackup_time = None
default persistent._MCloudBackup_no = 0
init python:
    import os
    os.environ['REQUESTS_CA_BUNDLE'] = renpy.config.basedir + "/game/python-packages/certifi/cacert.pem"
init -900 python in mcb:
    #################################
    # 在以下区域，将账号密码修改为你自己的
    mcb_client = {
        'webdav_hostname': "https://pan.monika.love/dav",
        'webdav_login':    "1951548620@qq.com",
        'webdav_root':  "/",
        'webdav_password': "hdNXNPzDr11cHBuHuvEJk31734dZHVg0"
    }
    # 旧存档过期时间，单位s
    timeout = 60*60*24*30
    #################################
    import os
    from webdav2.client import Client
    import time
    from store.mas_submod_utils import submod_log
    info = submod_log.info

    dataDir = os.getenv("APPDATA") + "\RenPy\Monika After Story"
    mcb = Client(mcb_client)

    def del_old():
        baklist = mcb.list("MAS_Backup")
        for i in baklist:
            baklist[baklist.index(i)] = i.split("_")
        for bak in baklist:
            try:
                stime = int(bak[1])
                if (time.time() - stime) > timeout:
                    mcb.clean("MAS_Backup/{}_{}".format(bak[0], bak[1]))
                    info("[MCB]删除了旧存档：'{}_{}'".format(bak[0], bak[1]))
            except:
                continue
    def upload():
        try:
            mcb.mkdir("MAS_Backup")
        except:
            pass
        mcb.upload(remote_path="MAS_Backup/persistent_{}".format(time.time()) , local_path=dataDir + "/persistent")
        info("[MCB]上传了存档：'{}_{}'".format("persistent", time.time()))
    def upload_save():
        if mcb.check("MAS_Backup/persistent"):
            mcb.clean("MAS_Backup/persistent")
        upload()


init python:
    import subprocess
    import store
    import datetime
    import store.mcb
    def mc_bak():
        store.mcb.upload_save()
        store.mcb.del_old()
        persistent._MCloudBackup_no = persistent._MCloudBackup_no + 1
        persistent._MCloudBackup_time = datetime.datetime.now()
        

init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="云端备份 莫盘版",
        description=(
            "将你的游戏存档备份至莫盘"
        ),
        version="1.1.1",
        settings_pane="mc_info",
    )
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="云端备份莫盘版",
            user_name="MAS-Submod-MoyuTeam",
            repository_name="MAS-MCloudBackup",
            update_dir="",
            attachment_id=None
        )
screen mc_info():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"
    text "上次备份于：[persistent._MCloudBackup_time]":
                xalign 1.0 yalign 0.0
                xoffset -10
                style "main_menu_version"
    textbutton "> 立刻备份":
        action Function(mc_bak)
