import os
import sys
import random
import shutil
import re

class NBay(object):
    # devide half data to test folder and half to trainging folder
    def __init__(self):
        self.source_path = sys.argv[1]
        self.class_name = sys.argv[2]
        self.training_name = sys.argv[3]
        self.test_name = sys.argv[4]
        # 创建目标文件夹
        self.class_path = os.path.join(self.source_path, self.class_name)
        self.test_path = os.path.join(self.source_path, self.test_name)
        self.training_path = os.path.join(self.source_path, self.training_name)
        # get all classes
        self.data_classes = os.listdir(self.class_path)
        self.training_data = []
    def split(self, training_percent):
        if os.path.exists(self.test_path):
            shutil.rmtree(self.test_path)
        if os.path.exists(self.training_path):
            shutil.rmtree(self.training_path)
        os.makedirs(self.test_path)
        os.makedirs(self.training_path)
        
        for data_folder in self.data_classes:
            # print(data_folder)
            data_folder_path = os.path.join(self.class_path, data_folder)
            data_folder_test_path = os.path.join(self.test_path, data_folder)
            data_folder_training_path = os.path.join(self.training_path, data_folder)
            data_names = os.listdir(data_folder_path)
            # print (data_folder_path, data_folder_self.test_path, data_folder_self.training_path)
            os.makedirs(data_folder_test_path)
            os.makedirs(data_folder_training_path)
            # 随机选择一些文件并将其复制到training 和 test 文件夹
            training_num = int(len(data_names) * float(training_percent))
            training_names = random.sample(data_names, training_num)
            # print(training_names)
            for i in data_names:
                if i in training_names:
                    shutil.copy(os.path.join(data_folder_path, i), data_folder_training_path)
                else:
                    shutil.copy(os.path.join(data_folder_path, i), data_folder_test_path)
    #open and read the files in given path
    def read_file(self):
        print(self.data_classes)
        for data_folder in self.data_classes:
            # combine each traning data folder path
            data_folder_path = os.path.join(self.training_path, data_folder)
            # got all file name under this group
            files = os.listdir(data_folder_path)
            files_len = len(files)
            # print(data_folder, files_len)
            class_word_list = []
            for i in range(2):
                #combine the file path with folder path and file name
                file = os.path.join(data_folder_path, files[i])
                #open file
                f = open(file, encoding='utf-8', errors='ignore')
                # read everyline in file to the 'lines'
                lines = f.readlines()
                temp_list = []
                for line in lines:
                    # remove all other symbols except words
                    line = re.sub(r"[\W]", " ", line)
                    # split the str line into list, and add them into 'temp_list'
                    temp_list += line.split()
                f.close()
                # add all text under 1 group into 1 list "class_word_list"
                class_word_list += temp_list
            self.training_data.append(class_word_list)
        print(len(self.training_data))
        print(self.training_data[19])


temp = NBay()
temp.source_path = sys.argv[1]
temp.class_name = sys.argv[2]
temp.training_name = sys.argv[3]
temp.test_name = sys.argv[4]
temp.split(sys.argv[5])
temp.read_file()