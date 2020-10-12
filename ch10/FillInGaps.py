
import os, re, shutil

folder = '/home/shampad/Desktop/automate_boring_revisit/ch10/sompod'
prefix = 'spam'

orderedRegex = re.compile(r'(%s)(\d*)(.*)(.txt)' %(prefix))

found = [] # keep track of numbering of files with chosen prefix

for folders, subfolders, filenames in os.walk(folder):
    for filename in filenames:
        if orderedRegex.search(filename) != None:

            # Determine length of numbering digits (for later naming)
            numLength = int(len(orderedRegex.search(filename).group(2))) #prints 3,4,2 like this.

            # Find file extension of files (for later naming)
            extension = orderedRegex.search(filename).group(4) # .txt

            # Number of files with chosen prefix
            found.append(orderedRegex.search(filename).group(2))
            # print(orderedRegex.search(filename).group(2))

ordered = sorted([int(x) for x in found])
print(found)
print(ordered)

for number in range(1, len(found)+1):
    # Calculate amount of 0's to prepend to reconstruct original format
    zeroes = '0' * (numLength - len(str(number)))
    # Recreate path of what should be the next file
    current_file = '{}/{}{}{}{}'.format(folder, prefix, zeroes, number, extension)

    # Check if the file exists
    if not os.path.exists(current_file):
        # Find numbering of actual next file and format path
        next_num = ordered[number - 1]
        next_zeroes = '0' * (numLength - len(str(next_num)))
        next_file = (folder + '/' + prefix + str(next_zeroes)+ str(next_num) + extension)

        # Rename actual to desired through shutil move
        shutil.move(next_file, current_file)

print('File numbering has been fixed.')