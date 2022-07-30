#MAS-MCloudBackup  
用莫盘备份你的MAS存档

----------------  

> 其实原理都是和discord同步状态是一样的  
> 因为MAS本身不支持py3，所以用pyinstaller提前将代码打包成程序，需要的时候直接给程序参数让他自己执行就好了

----------------

## 使用教程
1. 登录莫盘，进入webdav界面，点击 **创建新账号**
2. 备注名随便写，相对目录看你自己的需求，默认会在 **根目录/MAS_backup/** 下进行备份
3. 用记事本打开 **game/Submods/MCloudBackup/MCloudBackup.rpy**，修改账号密码即可
4. 每次启动游戏都会进行备份
