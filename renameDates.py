#! python3
# renameDates.py - Renames filenames with American MM-DD-YYY date format
# to Military Format DD MM Year

import shutil, os, re

# create a regex that matches files with the american date format
datePattern = re.compile(r"""^(.*?)
        ((0|1)?\d)-
        ((0|1|2|3)?\d)-
        ((19|20)\d\d)
        (.*?)$
        """, re.VERBOSE)

# TODO loop over the files in working dir
for amerDateFile in os.listdir('.'):
    mo = datePattern.search(amerDateFile)

    # skip files without a date
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    print(f'Before Part: {beforePart}')



# Form the European-style filename.
# Actually Mil Format
    euroDateFile = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerDateFile = os.path.join(absWorkingDir, amerDateFile)
    euroDateFile = os.path.join(absWorkingDir, euroDateFile)

# Rename the files.
    print(f'renaming {amerDateFile} to {euroDateFile}')
    shutil.move(amerDateFile, euroDateFile)
