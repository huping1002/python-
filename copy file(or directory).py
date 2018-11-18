import os
import shutil


def copy_file(scr_dir, dst_dir):
    # 递归实现文件拷贝(如果有子目录)
    for file_name in os.listdir(scr_dir):
        print(file_name)
        scr_file = scr_dir + '/' + file_name
        dst_file = dst_dir + '/' + file_name
        if os.path.isdir(scr_file):  # 判断文件是文件还是文件夹, 如果是文件夹， 就创建这个文件夹
            os.mkdir(dst_file)
            copy_file(scr_file, dst_file)   # 调用新的目录路径
        else:
            with open(scr_file, 'rb') as f:
                with open(dst_file, 'wb') as d:
                    while True:
                        file_data = f.read(1024)
                        if file_data:
                            d.write(file_data)
                        else:
                            break

if __name__ == '__main__':
    scr_dir = '/home/python/Desktop/text'  # 选择你要复制的文件或目录
    dst_dir = '/home/python/Desktop/haha'  # 复制后的存储位置
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)   # 如果新目录存在就删除目录
    os.mkdir(dst_dir)
    copy_file(scr_dir, dst_dir)   # 调用copy_file函数
