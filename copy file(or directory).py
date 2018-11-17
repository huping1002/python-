import os
import shutil


def copy_file(scr_dir, dst_dir):
    for file_name in os.listdir(scr_dir):
        print(file_name)
        scr_file = scr_dir + '/' + file_name
        dst_file = dst_dir + '/' + file_name
        if os.path.isdir(scr_file):  # 如果是文件夹， 就创建这个文件夹
            os.mkdir(dst_file)
            return copy_file(scr_file, dst_file)
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
    scr_dir = '/home/python/Desktop/text'
    dst_dir = '/home/python/Desktop/haha'
    if os.path.exists(dst_dir):
        shutil.rmtree(dst_dir)   # 如果目录存在就删除目录
    os.mkdir(dst_dir)
    copy_file(scr_dir, dst_dir)


