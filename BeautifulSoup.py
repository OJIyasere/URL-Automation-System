import requests
from bs4 import BeautifulSoup

# userInput = str(input("Enter the page you want to count url Links: "))

# countLinksOnPage(userInput)
def countLinksOnPage(url): 
    try: 
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        print(len(links))
        return len(links)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return -1 
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
    


class LinkChecker:
    def __init__(self, statusCode='undefined'): 
        self.statusCode = statusCode 
        self.linkList = []
        self.brokenLinks = []
        self.workingLinks = []

    def allLinks(self):
        # Prints all links in list 
        print("Links\n---------------------------------")
        for link in self.linkList:
            print(link)

    def allBrokenList(self): 
        # Print broken Links found
        print("Broken Links\n-----------------------------") 
        for link in self.brokenLinks:
            print(link)

    def allWorkingLinks(self):
        print("All working Links\n-----------------------------")
        for link in self.workingLinks:
            print(link)

    def addLink(self, url):
        # Adds link to list 
        self.linkList.append(url)
        return True 

    def removeLink(self, url):
        # Removes desired link from list 
        for link in self.linkList:
            if link == url:
                self.linkList.remove(link)
                print("Link was removed")
                return True 
            
        print("The URL you were looking for was not found") 

    def linkStatus(self, url):
        # Returns status of link 
        response = requests.get(url) 
        self.statusCode = response.status_code
        # print(f"Website Status: {self.statusCode}")
        return self.statusCode 
    
    '''
    def brokenListAdder(self):
        brokenLinks = 0

        # Adds broken links into seperate list 
        for link in self.linkList:
            self.linkStatus(link)
            if self.statusCode != 200: # Check for other working status codes  
                self.brokenLinks.append(link)
                brokenLinks += 1

        print(f"{brokenLinks} (s) were found.") # Prints how many broken links were found

    def workingListAdder(self):
        # Adds working links into list 
        for link in self.linkList:
            self.linkStatus(link)
            if self.statusCode == 200:
                self.workingLinks.append(link) '''

    def listSortion(self):
        brokenLinks = 0 
        for link in self.linkList:
            self.linkStatus(link) 
            if self.statusCode == 200:
                self.workingLinks.append(link)

            else:
                self.brokenLinks.append(link) 
                brokenLinks += 1

        print(f"{brokenLinks} broken link(s) was found")

    def sortedList(self):
        print("\nWorking links\n------------------")
        for link in self.workingLinks:
            print(link)

        print("\nBroken Links\n-----------------")
        for link in self.brokenLinks:
            print(link)



LC = LinkChecker() 
LC.addLink('https://www.youtube.com/5746443534')
LC.addLink('https://www.youtube.com/5')
LC.listSortion()
LC.sortedList()



            
        
    
        