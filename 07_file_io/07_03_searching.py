'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of
all .jpg files. The list should contain the complete path of each .jpg file.

If you are feeling bold, create a list containing each type of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then switch that
small folder name with a bigger folder. This program should work for any specified folder on your computer.

'''

from os import listdir
#Get the directory
directory = '/Users/michaelstresing/Desktop/Key'
files_dir = listdir(directory)

#create an empty list to place all images
imagelist = []
#take only files ending in jpg
for file in files_dir:
    filetype = ".jpg"
    if file.endswith(filetype):
        #add them to the imagelist
        imagelist.append(f"{file}")
print(f"You have {len(imagelist)} {filetype} files, in {directory}, they are: {imagelist}")

#create empty list to store file types
filetypes = []

for file in files_dir:
    #extensions can vary in length, so printing just the last x chars of each file won't work...
    filesname = file.split(".")
    #preventing issues with filesname[1] not existing (where there is no '.'
    if len(filesname) == 2:
        for splitfile in filesname:
            extention = filesname[1]
            #avoid adding duplicate file types
            if extention not in filetypes:
                filetypes.append(extention)
            else:
                pass
    else:
        pass

print(f"The file types in {directory} are {filetypes}")
