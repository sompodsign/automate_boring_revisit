import os, shutil

newFolder = r'../nasrin'
if not os.path.exists(newFolder):
    os.makedirs(newFolder)

for foldername, subfolders, filenames in os.walk('sompod'):
    for filename in filenames:
        if filename.endswith('.txt'):
            absFilePath = os.path.join(os.path.abspath(foldername), filename)
            shutil.copy(absFilePath, newFolder)

