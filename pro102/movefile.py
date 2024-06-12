import os
import shutil

intoC102Folder = 'C:/Users/marcu/OneDrive/Desktop/Projects/pro102'
intoC102ImageFile = 'C:/Users/marcu/OneDrive/Desktop/Projects/pro102/files'

LofFiles = os.listdir(intoC102Folder)
print(LofFiles)

for filename in LofFiles :
    name, extention = os.path.splitext(filename)
    
    if extention == ''
        continue
    if extention in ['.txt','.doc','.docx', '.pdf']
        path1 = intoC102Folder + '/' + filename
        path2 = intoC102ImageFile + '/' + 'files'
        path3 = intoC102Folder + '/' + 'files' + filename

        if os.path.exists(path2):
            print("Moving File.")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("Moving your file.")
            shutil.move(path1,path3)
