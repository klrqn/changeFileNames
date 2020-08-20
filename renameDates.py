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

# TODO skip files without a date

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.
