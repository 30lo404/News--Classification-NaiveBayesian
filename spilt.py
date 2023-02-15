import os
import sys
import random
import shutil

class NBay(object):
    def split(self, source_path, class_name, training_name, test_name, training_percent):
        # 创建目标文件夹
        class_path = os.path.join(source_path, class_name)
        test_path = os.path.join(source_path, test_name)
        training_path = os.path.join(source_path, training_name)
        if os.path.exists(test_path):
            os.system("rm -r %s" % test_path)
        if os.path.exists(training_path):
            os.system("rm -r %s" % training_path)
        os.makedirs(test_path)
        os.makedirs(training_path)
        
        # get all classes
        data_classes = os.listdir(class_path)
        for data_folder in data_classes:
            # print(data_folder)
            data_folder_path = os.path.join(class_path, data_folder)
            data_folder_test_path = os.path.join(test_path, data_folder)
            data_folder_training_path = os.path.join(training_path, data_folder)
            data_names = os.listdir(data_folder_path)
            # print (data_folder_path, data_folder_test_path, data_folder_training_path)
            os.makedirs(data_folder_test_path)
            os.makedirs(data_folder_training_path)
            # 随机选择一些文件并将其复制到training 和 test 文件夹
            training_num = int(len(data_names) * float(training_percent))
            training_names = random.sample(data_names, training_num)
            # print(training_names)
            for i in data_names:
                if i in training_names:
                    os.system("cp %s %s" % (os.path.join(data_folder_path, i), data_folder_training_path))
                else:
                    os.system("cp %s %s" % (os.path.join(data_folder_path, i), data_folder_test_path))

temp = NBay()
temp.split(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])