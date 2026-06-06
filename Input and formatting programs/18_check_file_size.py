import os

filename="Demo.txt"


if os.path.exists(filename):
    
    file_info=os.stat(filename)
    
    if file_info.st_size == 0:
        print(f"Status : {filename} is empty!")

    else:
        print(f"Status : {filename} Size is {file_info.st_size}")
        
else:
    print("File Does not exist")       
           