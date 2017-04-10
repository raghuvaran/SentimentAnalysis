import csv
import codecs
import urllib2
from bs4 import BeautifulSoup


##################################
#       Variable declaration
##################################
dataFileUrl = "https://cecas.clemson.edu/~rchowda/ds/aapl_valuewalk.csv"
requestHeaders = {
# 'Host': 'www.valuewalk.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'Accept-Language': 'en-US,en;q=0.5',
# 'Accept-Encoding': 'gzip, deflate',
# 'Cookie': '__cfduid=d6af358037329b89dc6527d9d60a9449f1491484430; PHPSESSID=6459f0fb8876bf1c86bb85dc97eca111; swpm_session=94c2e99905aeaacee2c76c400b227961',
# 'Connection': 'keep-alive',
# 'Upgrade-Insecure-Requests': 1,
# 'Cache-Control': 'max-age=0'
}

targetDir = './newsArticles/'

csvFile = csv.reader(urllib2.urlopen(dataFileUrl))
headers = csvFile.next()
for row in csvFile:
    reverseDate = row[0].split('/')
    reverseDate.reverse()
    newFile = codecs.open(targetDir+'_'.join(reverseDate)+'#'+'_'.join(row[2].split('/')), 'w', encoding='utf8')
    print row[2]
    # newFile.write(row[2]+'\n')
    request = urllib2.Request(row[2], headers=requestHeaders)
    try:
        response = urllib2.urlopen(request)
    except urllib2.HTTPError as err:
        print 'Error : ' + str(err.code)
        continue

    soup = BeautifulSoup(response.read(), 'html.parser')
    response.close()
    for line in soup.article.find_all('p'):
        newFile.write(line.get_text())







