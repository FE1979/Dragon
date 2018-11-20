import json
from urllib.request import urlopen, Request
from html.parser import HTMLParser



def Get_Info_Table(html_data):
    start = html_data.find('<table>')
    end = html_data.find('</table>', start)
    table_data = html_data[start:end]
    INFO_TABLE = []
    parsed_data = []

    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'tr':
                parsed_data.append('New_row')

        def handle_endtag(self, tag):
            if tag == 'tr':
                parsed_data.append('End_row')

        def handle_data(self, data):
            parsed_data.append(data)

    parser = MyHTMLParser()
    parser.feed(table_data)

    entry_switch = 0
    for i in parsed_data:
        if i == "New_row":
            INFO_TABLE.append([])
        if i != "New_row" and i != "End_row":
            INFO_TABLE[-1].append(i)
            entry_switch += 1
        if i == "End_row":
            INFO_TABLE[-1].append('')
            entry_switch = 0

    return INFO_TABLE

URL_VIEW = "http://example.webscraping.com"
URL_GET = ""
HEAD = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/201'}
start, end = 0, 0

search_request = input('Type country name to find\n>')

URL_SEARCH = f"http://example.webscraping.com/places/ajax/search.json?&search_term={search_request}&page_size=10&page=0"
REQ = Request(URL_SEARCH, headers = HEAD)
Response = urlopen(REQ).read()
Response = Response.decode('utf-8')
SEARCH_RES = json.loads(Response)

if SEARCH_RES['records'] == []:
    print('No matches found')
else:
    start = SEARCH_RES['records'][0]['pretty_link'].find("\"")
    end = SEARCH_RES['records'][0]['pretty_link'].find("\"", start + 1)
    URL_GET = URL_VIEW + SEARCH_RES['records'][0]['pretty_link'][start+1:end]
    REQ = Request(URL_GET, headers = HEAD)
    Response = urlopen(REQ).read()
    Response = Response.decode('utf-8')
    Country_Data = Get_Info_Table(Response)
    for i in Country_Data:
        print(i[0], i[1])
