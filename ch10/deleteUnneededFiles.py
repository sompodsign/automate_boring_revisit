import os

for foldername, subfolder, filenames in os.walk('sompod'):
    for filename in filenames:
        filename = os.path.join(os.path.abspath(foldername), filename)
        # print(os.path.getsize(filename))


        # if os.path.getsize(filename) > 100:
        #     os.unlink(filename)