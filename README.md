# youthfulIndiscretion
random pieces of code that I use over and over and over

- risFixer.py:
    This flips the author name orders from broken RIS export from things like mendelay and readcube.

    You probably want this when you need to move references around from different pieces of reference manager software.

    It looks for all of the ".RIS" files in a folder and fixes them. It is not even sort of bug tested, it also will fail ungracefully in situations where authors have last names separated by spaces; sorry, Brent Vander Wyk. 
    
    You should still proof your imported references.

    run it like this (for example, if RIS files are in your Downloads folder)

    `python risFixer.py ~/Downloads/`
