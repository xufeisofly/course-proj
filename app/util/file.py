# coding: utf-8
import os
import shutil
import tarfile


def rotate_delete_node_of_dir(dir):
    """滚动删除 dir 中最早的 node（文件或文件夹）
    """
    l = os.listdir(dir)
    l.sort()
    for name in l:
        path = os.path.join(dir, name)
        if not all(item not in path for item in ['.tar', '.zip']):
            if os.path.exists(path):
                os.remove(path)


def get_node_num_of_dir(dir):
    """获取目录中 node 个数
    :param dir: 目录 path
    """
    return len(os.listdir(dir))

def make_targz(source_dir, with_delete=False):
    """压缩打包文件夹
    :param source_dir: 目标文件夹
    :param with_delete: 是否删除目标文件夹
    """
    output_filename = source_dir + '.tar'
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    if with_delete:
        shutil.rmtree(source_dir)
