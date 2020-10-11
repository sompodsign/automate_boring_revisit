import shutil, os, re

# Create a regex that matches the files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before date
            ((0|1)?\d)-            # one or two digits for the month
            ((0|1|2|3)?\d)-         # One or two digits for the day
            ((19|20)\d\d)           # four digits for the year
            (.*?)$                  # all text after the date
            """, re.VERBOSE)

for amerFileName in os.listdir('.'):
    mo = datePattern.search(amerFileName)

    if mo == None:
        continue
    # Get the different part of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterpart = mo.group(8)

    # Form the Eu-style filename.
    euroFileName = beforePart+dayPart + '-' + monthPart + '-' + yearPart + afterpart
    # Get the full, abs file paths.
    absWorkingDir = os.path.abspath('.')
    amerFileName = os.path.join(absWorkingDir, amerFileName)
    euroFileName = os.path.join(absWorkingDir, euroFileName)

    # Rename the files
    print(f"Renaming '{amerFileName}' to {euroFileName}...")
    shutil.move(amerFileName, euroFileName)