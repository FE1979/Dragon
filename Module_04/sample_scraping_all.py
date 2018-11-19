"""
Just scraping
NOTE:
There is sleep for 1 second in a script to avoid 429 HTTP Error
"""

from urllib.request import urlopen, Request
import time

def Read_Page(URL, HEAD):
    REQ = Request(URL, headers = HEAD)
    Response = urlopen(REQ).read()
    Response = Response.decode('utf-8')
    return Response

def Add_Countries(Response):
    """Takes Response and return list of countries on the page"""

    """ Find a table with countries"""
    Table_start = Response.find('<table>')
    Table_end = Response.find('</table', Table_start)
    Content = Response[Table_start : Table_end]

    Current_position = 0
    Countries = []

    """ Let take a country and delete it from Content"""
    while Content:
        Current_position = Content.find('/> ', Current_position) + 3 #Plus lenght of '/> ' - starting point
        Country_name_end = Content.find('</a>', Current_position) #end point of Country's name
        if Country_name_end == -1: #If no ending tag found - exit
            break
        Countries.append(Content[ Current_position : Country_name_end ]) #add it to the list
        Content = Content[Country_name_end:] #remove all before other countries
        Current_position = 0 #Let start from the beginning
        pass

    return Countries


URL = "http://example.webscraping.com/"
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/201'}
NEXT_tag = "\">Next &gt"
NEXT_pos = 0
NEXT_URL_tag = """<a href="/places/default/index/"""
NEXT_URL_pos = 0
LIST_OF_COUNTRIES = []
TEMP_LIST = []
NEXT_URL = URL

while True:
    RESP = Read_Page(NEXT_URL, HEAD)
    TEMP_LIST = Add_Countries(RESP)
    LIST_OF_COUNTRIES += TEMP_LIST
    NEXT_pos = RESP.find(NEXT_tag)
    print(NEXT_pos)
    if NEXT_pos == -1:
        break
    else:
        """save the next url moving left"""
        i = 1
        symbol = RESP[NEXT_pos - i]
        NEXT_URL = ''
        while symbol != '\"':
            NEXT_URL = symbol + NEXT_URL
            i += 1
            symbol = RESP[NEXT_pos - i]
            pass
        NEXT_URL = URL + NEXT_URL[1:] #remove \ on the start
        print('Next url ', NEXT_URL)

    time.sleep(1)

print(LIST_OF_COUNTRIES)
