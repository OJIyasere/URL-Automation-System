'''
Link Extractor
Worked on By: Talon and Jonathan

Last Updated: 10/31/2025 @ 11:30 AM (Jonathan Converted funciton into a class)

Defines a Script that parses the .docx files 
and pulls links from them, creating a list of LinkObject items

Link Extractor Function:
    1) Passed the input file as a parameter 
    2) Runs a function to loop through file until all links are pulled from them
    3) Returns a list of LinkObjects 
'''

from LinkObject import LinkObject
import requests
from bs4 import BeautifulSoup
from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

class LinkExtractor:
    def __init__(self, filename):
        self.filename = filename 
        self.links = []

    # Function to Extract Links from word document 
    def extract_links(self):
        doc = Document(self.filename)
        rels = doc.part.rels

        for r in rels:
            # Extracts embedded links using relationships
            if rels[r].reltype.endswith("/hyperlink"):
                self.links.append(LinkObject(rels[r]._target, self.filename))

        for para in doc.paragraphs:
            texts = para.text.split()
            for text in texts: # Extracts regular links
                if text.startswith("http"):
                    self.links.append(LinkObject(text, self.filename))

        return self.links

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

