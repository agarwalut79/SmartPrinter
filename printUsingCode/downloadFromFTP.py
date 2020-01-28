import os,sys,subprocess,time
filename = "123"
while True:
    print("Enter Code")
    newfilename = (str(input())).strip()+".pdf"
    #if os.path.isfile(filename):
    
    filename = newfilename
    print(filename)
    if filename == "quit.pdf":
        break
    if os.path.isfile(filename):
        print("Your file is printing...\n")
    #for line in fp:
        kk='lp '+ filename
        os.system(kk)
        time.sleep(5)
        os.remove(newfilename)
    else:
        print("File Not Found. Renter Code")