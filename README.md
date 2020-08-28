# wordpress_pic_zip
使用Python3 将 wordpress 文件夹的wp-content 下 uploads 文件夹下所有 jpg,png 图片进行压缩

## 使用方法
- 备份 根目录下 wp-content/uploads 文件夹
- 将 zippic.py 文件放在wordpress 根目录下  
- 通过ssh 运行 > python zippic.py 
- 完成 日志文件储存在根目录下 log.json 文件中

## Tips
- ssh 操作时最好使用root账户登录
- 某些主机可能需要运行 python3 zippic.py
- 有问题可以Email 我 wicos@wicos.cn 或者 在我的博客留言 [歪克士](https://www.wicos.me)
