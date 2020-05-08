import ftplib
ftp = ftplib.FTP('hostname','username', 'password')
files = ftp.dir('/htdocs/Prints/')
ftp.cwd("/htdocs/Prints")
filematch = '*.pdf'
target_dir = '/home/pi/Desktop/print'
import os
import shutil
while True:
    for filename in ftp.nlst(filematch):
        target_file_name = os.path.join(target_dir,os.path.basename(filename))
        with open(target_file_name,'wb') as fhandle:
            ftp.retrbinary('RETR %s' % filename, fhandle.write)
            if os.path.isdir(filename)== True:
                shutil.rmtree(filename)
            else:
                ftp.delete(filename)
