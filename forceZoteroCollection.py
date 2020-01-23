''' I have messy zotero collections that are missing years and journal names and the like, this very zloppy script will take them and try to find the data on DOI and then fix the reference

Get your user ID and keys here
https://www.zotero.org/settings/keys

FYI your library ID is not your username.

You'll need to go to your library in the browser to get the collecction ID it will be the last part of the URL

For example, if you are in your collecetion and the URL is
https://www.zotero.org/USERNAME/collections/CUUG5M26

'CUUG5M26' is the collection ID

'''

import fileinput
import string
import os
import sys
import requests
from pyzotero import zotero
import crossref_commons.retrieval
from habanero import Crossref
cr = Crossref()
import click
import argparse

library_id = sys.argv[1]
api_key = sys.argv[3]
collectionID = sys.argv[2]
force = sys.argv[4]
zot = zotero.Zotero(library_id, 'user', api_key) # this will always be user because I wrote this to fix my own mess, change it if you're fixing someone else's mess
collectionItems = zot.everything(zot.collection_items(collectionID))


for item in collectionItems:
    #print(collectionItems)
    #print("*" *10 )
    #print(item["data"]["title"])
    #print(item["data"]["itemType"])\
    try:
        if item["data"]["itemType"] == "journalArticle":
            #print(item["data"]["title"])
            print(item["data"]["title"])
            print(item["data"]["creators"][0]["lastName"])
            # we have no journal, let's see if we can pull the DOI from somewhere.
            theDOI =item["data"]["DOI"]
            if item["data"]["DOI"].strip() == "":
                print("no DOOI!!!!")
                print(item["data"]["title"])
                #try the title????
                #crSearch = cr.works(query = item["data"]["title"], sort = "score")
                #for p in iterate_publications_as_json(max_results=20, filter = filter, queries=queries, sort =sort ):
                    #print(p.keys())
                #    print(p["title"])
                    #print(p["author"])
            else:
                print(theDOI) # we have a DOI that's cool
                r = crossref_commons.retrieval.get_publication_as_json(theDOI)
                #print(r.keys()) # this is good to see what's happening
                #print("*" * 10)
                #print(item["data"].keys())
                #print("*" * 10)
                #print(item["data"]["title"])
                #print(r["title"])
                #print(r["original-title"])
                #print(r["container-title"])
                #print(r["journal-issue"])
                print("*" * 100)
                print(r["created"]['date-parts'][0][0])
                item["data"]["date"] = r["created"]['date-parts'][0][0]
                #now we do some updates =
                item["data"]["publicationTitle"] = r["container-title"][0] # this is a list
                #item["data"]["publicationTitle"] = r["container-title"][0] # this is a list
                #item["data"]["date"] = r["container-title"][0] # this is a list
                #print(item)
                #input("Press Enter to actually update...")
                zot.update_item(item)
    except:
        print("Something broke")
        # we ndded to fix the dates too
