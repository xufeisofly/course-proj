# # coding: utf-8
# import os
# from datetime import datetime

# from app.util.file import (get_node_num_of_dir, make_targz,
#                            rotate_delete_node_of_dir)
# from nptdms import ChannelObject, GroupObject, RootObject, TdmsFile, TdmsWriter


# def save_data_organized_by_date(data, parent_dir, max_num=100, compress=True, file_rotate_size_kb=100000):
#     """按照日期保存并整理文件夹
#     :param parent_dir: 父目录
#     :param max_num: 子目录个数上限，超过上限滚动删除之前的文件夹
#     :param compress: 是否压缩旧的子文件夹
#     """
#     # 检查父目录中子目录个数是否超过上限，如果超过则删除最早的
#     if not os.path.exists(parent_dir):
#         os.makedirs(parent_dir)
        
#     if get_node_num_of_dir(parent_dir) > max_num:
#         rotate_delete_node_of_dir(parent_dir)

#     today_dirname = datetime.now().strftime("%Y-%m-%d")
#     sub_dir_names = [name for name in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, name))] 
#     # 压缩之前的目录
#     if compress:
#         for sub_dir in sub_dir_names:
#             if str(sub_dir) == today_dirname:
#                 continue
#             sub_path = os.path.join(parent_dir, sub_dir)
#             make_targz(sub_path, with_delete=True)

#     # 创建 date 文件夹，并写入文件
#     today_dir_path = os.path.join(parent_dir, today_dirname)
#     if not os.path.exists(today_dir_path):
#         os.makedirs(today_dir_path)

#     save_data_to_multi_tdms_files(data, today_dir_path, rotate_size_kb=file_rotate_size_kb)



# def save_data_to_multi_tdms_files(data, date_dir, rotate_size_kb=100000):
#     """滚动保存数据
#     :param data: tdmsData dict
#     :param date_dir: 目录
#     :param rotate_size_kb: 单个文件大小上限 kb, 0 则不滚动
#     """
#     # 如果当前文件大小超过上限，则重命名
#     if not os.path.exists(date_dir):
#         os.makedirs(date_dir) 

#     cur_filename = 'cur.tdms'
#     cur_file_path = os.path.join(date_dir, cur_filename)
#     if not os.path.exists(cur_file_path):
#         f = open(cur_file_path, 'w')
#         f.close()

#     file_stats = os.stat(cur_file_path)
#     if file_stats.st_size > rotate_size_kb * 1024:
#         new_filename = 'END-' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.tdms'
#         os.rename(cur_file_path, os.path.join(date_dir, new_filename))

#     # 写入 cur.tdms
#     save_data_to_tdms_file(cur_file_path, data)



# root_key = 'root'
# channels_key = 'channels'

# def save_data_to_tdms_file(file_path, tdmsData):
#     group = tdmsData.get('group').data
#     group_name = group.get('name', '')

#     try:
#         tdms_file = TdmsFile.read(file_path)
#         _ = tdms_file[group_name]
#     except:
#         with TdmsWriter(file_path, mode='a+') as tdms_writer:
#             root = tdmsData.get(root_key)
#             root_object = RootObject(properties=root)
#             # 用当前时间戳作为默认 group name
#             group_data = without_keys(group, [channels_key])
#             group_object = GroupObject(group_name, properties=group_data)

#             channel_objects = []
#             for chn in group.get(channels_key, []):
#                 channel_name = chn['channel_name']
#                 channel_data = chn['channel_data']
#                 channel_object = ChannelObject(group_name, channel_name, channel_data)
#                 channel_objects.append(channel_object)

#             tdms_writer.write_segment([root_object, group_object] + channel_objects)


# def without_keys(d, keys):
#     return {x: d[x] for x in d if x not in keys}
