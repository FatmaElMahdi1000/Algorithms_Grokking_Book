from os.path import join, isdir, isfile
from os import listdir

def printing_names(start_dir):
    for File in listdir(start_dir):
        Full_path = join(start_dir, File)
        if isfile(Full_path):
            print(File)
        else:
            printing_names(Full_path)
            
printing_names(".") #listdir when it takes "." it means we're listing what's in the current directory.