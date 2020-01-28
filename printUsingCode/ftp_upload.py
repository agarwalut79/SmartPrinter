import ftplib
ftp = ftplib.FTP('ftpupload.net','epiz_25099387', '98p1cjl7WnkJ')
files = ftp.dir('/htdocs/Prints/')
ftp.cwd("/htdocs/Uploads")
filematch = '*.pdf'
target_dir = '/home/pi/Desktop/uploads'
import os
import shutil
while True:
    for filename in ftp.nlst(filematch):
        print(type(ftp.nlst(filematch)))
        target_file_name = os.path.join(target_dir,os.path.basename(filename))
        with open(target_file_name,'wb') as fhandle:
            ftp.retrbinary('RETR %s' % filename, fhandle.write)
            if os.path.isdir(filename)== True:
                shutil.rmtree(filename)
            else:
                ftp.delete(filename)