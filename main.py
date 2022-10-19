import urllib.parse
import requests
from bs4 import BeautifulSoup
 
 
# Making a GET request
r = requests.get('https://web.archive.org/web/20150517055039/http://www.greatfreedom.org/audiomore.html')
 
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)


rightColumn = soup.find('div', id="rightcolumn")

firstTable = rightColumn.find('table')

tbody = firstTable.find('tbody')

tr = tbody.find('tr')

td = tr.find('td')

innerTables = td.find_all('table')


allLinks = [ [link.get('href') for link in table.find_all('a')] for table in innerTables]



ls = [link for links in allLinks for link in links if 'amazon' in link]
#print(ls)
print(len(ls))

links = { l.replace('https://web.archive.org/web/20150517055039/', '') for l in ls }

for l in links:
  print(l)

  encodedTitle = l[l.rfind('/')+1:]
  title = urllib.parse.unquote(encodedTitle)
  print(title)

  response = requests.get(l)
  filename = "/Users/watsco/Desktop/CandiceDownloads/" + title
  print(filename)
  with open(filename, "wb") as f:
    f.write(response.content)
