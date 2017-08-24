import os

def directory_list(target_path):
    for i in os.listdir(target_path):
        print(i)
if __name__ == '__main__':
    directory_list('Homework')
