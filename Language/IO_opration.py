# 当前工作目录在Python文件夹
f = open('./Language/test_IO.txt', 'r')
str = f.read()
print(str)
# 文件打开会会占用资源必须关闭
f.close()
# 使用with语句
with open('./Language/test_IO.txt', 'r') as f:
    print(f.read())
# 还可以使用read(size)和readline()防止文件太大导致内存爆炸
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可
# f = open('/Users/michael/test.jpg', 'rb')
# 读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
# 如果遇到编码错误后如何处理。最简单的方式是直接忽略
# f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件，文件不存在时自动创建文件
with open('./Language/test_IO.txt', 'w') as f:# 覆盖模式
    f.write("yes!")
with open('./Language/test_IO.txt', 'a') as f:# 追加模式
    f.write('\nappend mode')

# 操作文件和目录
import os
print(os.name)# 查看操作系统类型
print(os.path.abspath('.'))# 返回当前所在工作目录路径
os.mkdir('./Language/testdir')# 创建文件夹
os.rmdir('./Language/testdir')# 删除文件夹