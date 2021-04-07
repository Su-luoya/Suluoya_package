import os 
from pprint import pprint
def get_files(path):
    """获取文件夹内所有文件
    
    Args:
        path (str): 文件夹路径
    """        
    for filepath,dirnames,filenames in os.walk(path):
        for filename in filenames:
            pprint(filepath+'\\'+filename)
if __name__ == '__main__':
    get_files(path='../')