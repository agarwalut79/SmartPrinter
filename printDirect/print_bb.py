import os
import time

Folder_path = r"/home/pi/Desktop/print"

while True:
    files = os.listdir(Folder_path)

    pdf_files = list()
    name=''
    '''for file in files:
        ext = file.split('.')[1]
        name = file.split('.')[0]
        if ext == 'pdf':
            if name.lower() =='quit':
                break
            else:'''
    for file in files:
        name = file.split('.')[0]
        #print(name)
        ext = file.split('.')[1]
        #print(ext)
        if ext=='pdf':
        #for file in pdf_files:
            fd = os.open(file, os.O_RDWR)
            print (name)
            name=name.strip()
            kk='lp '+ name+'.pdf'
            print(kk)
            os.system(kk)
            print("Printing File : " , file)
            time.sleep(20)
            print("File Printed")
            os.close(fd)
            os.remove(file)
            print("File Deleted")
