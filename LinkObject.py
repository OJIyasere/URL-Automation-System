import requests 
# Link Object Class
# 
# Author: Addy B.
# First written: 10/13/2025
# 
# defines class LinkObject
# is imported by all other files in project
# defines attributes "target link" which is the link being sorted
# and "source link" which is the link to the page the target link is from

class LinkObject():    
    def __init__(self, url, srcUrl, status='undefined'):
        # target link is the link that gets sorted
        self.target_link = url
        # source link is the link to the page the target link comes from
        self.source_link = srcUrl
        # Status code of the webpage 
        self.statusCode = status
        # Creates Satus Code immediately for Link
        try:
            if self.statusCode == 'undefined':
                self.webStatus()
        except Exception:
            # don't raise on init; leave status as provided
            pass

    def webStatus(self):
        try:
            response = requests.get(self.target_link)
            self.statusCode = response.status_code
            return self.statusCode
        except requests.exceptions.RequestException:
            # 0 indicates network/request failure (distinct from HTTP codes)
            self.statusCode = 404
            return self.statusCode
