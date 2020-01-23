# youthfulIndiscretion
random pieces of code that I use over and over and over

- risFixer.py:
    This flips the author name orders from broken RIS export from things like mendelay and readcube.

    You probably want this when you need to move references around from different pieces of reference manager software.

    It looks for all of the ".RIS" files in a folder and fixes them. It is not even sort of bug tested, it also will fail ungracefully in situations where authors have last names separated by spaces; sorry, Brent Vander Wyk. 
    
    You should still proof your imported references.

    run it like this (for example, if RIS files are in your Downloads folder)

    `python risFixer.py ~/Downloads/`
- ForceZoteroCollection.py
    My zotero library is full of semi broken references from exports and hand entering referecences in the 90's. Fortunately a lot of them actually have a DOI and the internet is full of tools to make this easier. We should never have to enter a reference by hand again. 
    This particularly ugly piece of code will:
    - go find your zotero collection
    - find the journal articles
    - see if they have a DOI
    - if they do, it will update the journal name and the year. 
    
    
    Get your user ID and keys here
    https://www.zotero.org/settings/keys

    FYI your library ID is **not** your username.

    You'll need to go to your library in the browser to get the collecction ID it will be the last part of the URL

    For example, if you are in your collecetion and the URL is
    https://www.zotero.org/USERNAME/collections/CUUG5M26

    'CUUG5M26' is the collection ID
    
    then run it like this 
     python fixZoteroCollection.py <userid> <collectionID>  <secretAPIKey> 1











    
