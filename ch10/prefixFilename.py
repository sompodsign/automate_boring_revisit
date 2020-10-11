import shutil, os, re

for filename in os.listdir('.'):
    absworkingdir = os.path.abspath('.')

    originalFileName = os.path.join(absworkingdir, filename)
    toFileName = 'spam_'+filename

    print(f"Renaming '{filename}...")
    shutil.move(originalFileName, toFileName)