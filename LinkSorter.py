"""
Link Sorter
Link Sorter Class / Function, Calls LinkExtractor function
to perform sorting algorith on returned array of LinkedObjects
Creates two new arrays, brokenLinks and workingLinkks

Author: Jonathan Iyasere
Date: October 16, 2025
ENGR 340
"""

from LinkObject import LinkObject
class LinkChecker:
    def __init__(self, links=None):
        """Initialize with an optional list of LinkObject instances or URL strings.

        links: iterable of LinkObject or str
        """
        self.linkList = []
        self.workingList = []
        self.brokenList = []

    def addLink(self, item): # Adds Links into Link List
        self.linkList.append(item) 

    def allLinks(self): # Prints all Links and their Source
        for links in self.linkList:
            print(f"{links.target_link}   {links.source_link}")

    def workingLinks(self): # Prints Working Links and their Source 
        for link in self.workingList:
            print(f"{link.target_link}    {link.source_link}")

    def brokenLinks(self): # Prints broken Links and their Source 
        for link in self.brokenList:
            print(f"{link.target_link}    {link.source_link}")

    def linkSortion(self): # Sorts Links putting them into a working List and Broken one 
        brokenList = 0
        for link in self.linkList:

            if (200 <= link.statusCode <= 399) or link.statusCode == 403: 
                self.workingList.append(link)
            else: 
                self.brokenList.append(link)
                brokenList += 1

        # Tells how many broken links were detected 
        print(f"{brokenList} broken links were detected")

    def sortedList(self): # Prints Both Working and Broken List 
        print("Working Links\n---------------------------")
        self.workingLinks()

        print("\n")
        
        print("Broken Links\n-----------------------------")
        self.brokenLinks()
