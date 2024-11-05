    # import os
    # import shutil
    # import unittest
    # from datetime import datetime, timedelta

    # from app.controllers import data_controller
    # from app.http.schemas.tdms import TdmsDataSchema


    # class TestDataController(unittest.TestCase):

    #     def setUp(self):
    #         self.data = {
    #             "type": "strain",
    #             "root": {
    #                 "name": "root1.tdms",
    #                 "title": "root1",
    #                 "author": "xufei",
    #                 "description": "description..."
    #             },
    #             "group": {
    #                 "name": "group1",
    #                 "timestamp": 155555555,
    #                 "sensor_num": 2,
    #                 "channels": [
    #                     {
    #                         "channel_name": "time",
    #                         "channel_data": [0,1,2,3,4,5]
    #                     }, {
    #                         "channel_name": "intensity",
    #                         "channel_data": [10,11,12,13,14,15]
    #                     }
    #                 ]
    #             }
    #         }
    #         # 创建目录
    #         self.log_path = os.path.join('/Users/sofly', 'logs')
    #         if not os.path.exists(self.log_path):
    #             os.makedirs(self.log_path)

    #         yesterday = datetime.today() - timedelta(days=1)
    #         yesterday_name = yesterday.strftime("%Y-%m-%d")
    #         self.yesterday_path = os.path.join(self.log_path, yesterday_name)
    #         if not os.path.exists(self.yesterday_path):
    #             os.makedirs(self.yesterday_path)

    #         old_file_path = os.path.join(self.yesterday_path, 'old.log')
    #         with open(old_file_path, 'w') as f:
    #             f.write("abcd")

    #     def tearDown(self):
    #         shutil.rmtree(self.log_path)

    #     def test_save_data_organized_by_date(self):
    #         """按日期生成新文件夹"""
    #         input = TdmsDataSchema().load(self.data)
    #         # import pdb ; pdb.set_trace()
    #         data_controller.save_data_organized_by_date(input.data, self.log_path)

    #         today_dirname = datetime.now().strftime("%Y-%m-%d")
    #         self.assertTrue(os.path.exists(os.path.join(self.log_path, today_dirname)))
    #         self.assertTrue(os.path.exists(os.path.join(self.yesterday_path + '.tar')))
    #         self.assertFalse(os.path.exists(os.path.join(self.yesterday_path)))

    #     def test_save_data_organized_by_date_over_max_num(self):
    #         """当 date folder 个数超过上限时，删除最早的压缩文件"""
    #         input = TdmsDataSchema().load(self.data)
            
    #         data_controller.save_data_organized_by_date(input.data, self.log_path, max_num=1)
    #         data_controller.save_data_organized_by_date(input.data, self.log_path, max_num=1)
    #         today_dirname = datetime.now().strftime("%Y-%m-%d")
    #         self.assertTrue(os.path.exists(os.path.join(self.log_path, today_dirname)))
    #         self.assertFalse(os.path.exists(os.path.join(self.yesterday_path + '.tar')))
    #         self.assertFalse(os.path.exists(os.path.join(self.yesterday_path)))

    #     def test_save_data_organized_by_date_over_file_size(self):
    #         """当 tdms file 大小超过上限时，生成新文件"""
    #         input = TdmsDataSchema().load(self.data)
    #         data_controller.save_data_organized_by_date(input.data, self.log_path, file_rotate_size_kb=0.01)
    #         data_controller.save_data_organized_by_date(input.data, self.log_path, max_num=1, file_rotate_size_kb=0.01)
    #         today_dirname = datetime.now().strftime("%Y-%m-%d")
    #         today_path = os.path.join(self.log_path, today_dirname)
    #         self.assertTrue(os.path.exists(today_path))
    #         self.assertTrue(len(os.listdir(today_path))>1)


    # if __name__ == '__main__':
    #     unittest.main()
