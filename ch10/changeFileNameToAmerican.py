
import shutil, os, re

# Create a regex that matches the files with the American date format.
datePattern = re.compile(r"""^(.*?)             
            ((0|1|2|3)?\d)-  
            ((0|1)?\d)-            
            ((19|20)\d\d)          
            (.*?)$         
            """, re.VERBOSE)

for euroFilename in os.listdir('.'):
    mo = datePattern.search(euroFilename)
    print(mo)
    

    if mo == None:
        continue
    # Get the different part of the filename.
    beforePart = mo.group(1)
    dayPart = mo.group(2)
    monthPart = mo.group(4)
    yearPart = mo.group(6)
    afterpart = mo.group(8)

    # Form the Eu-style filename.
    amerFilename = beforePart+monthPart + '-' + dayPart + '-' + yearPart + afterpart
    # Get the full, abs file paths.
    absWorkingDir = os.path.abspath('.')
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    amerFilename = os.path.join(absWorkingDir, amerFilename)

    # Rename the files
    print(f"Renaming '{euroFilename}' to {amerFilename}...")
    shutil.move(euroFilename, amerFilename)