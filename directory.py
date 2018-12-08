import os
import glob

def image_list(directory):
    filelist = []
    for (path, dir, files) in os.walk(directory):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg':
                filelist.append(filename)
    return filelist

def remove_all_files(directory):       
    for (path, dir, files) in os.walk(directory):
        for filename in files:
            os.remove(str(path)+'/'+str(filename))
            