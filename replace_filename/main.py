import os

# 获取当前文件夹下的所有文件和文件夹列表
file_list = os.listdir()
for file in file_list:
    if 'test' in file:
        # 用test_替换test
        new_file = 'test_'.join(file.split('test'))
        # 文件名替换
        os.rename(file, new_file)
    # if os.path.isfile(file):
    #     print(file + '是文件')
    # if file.endswith('.txt'):
    #     print(file)
