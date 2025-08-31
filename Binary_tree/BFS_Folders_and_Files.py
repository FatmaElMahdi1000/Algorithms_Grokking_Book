from collections import deque 
from os import listdir
from os.path import join, isfile, isdir

def printing_names(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    
    while search_queue:
        current_dir = search_queue.popleft()
        for File in listdir(current_dir):
            full_path = join(current_dir, File)
            if isfile(full_path):
                print(f"File Name: {full_path}")
            elif isdir(full_path):
                search_queue.append(full_path)

print(printing_names(".")) #with listdir giving the method this "." means we're working on the current directory      