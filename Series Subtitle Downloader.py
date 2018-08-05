#A python script to download subtitles from a certain url which is already assigned in the program,
#all you have to do is get the series's base url corresponding to html portion only and poof, it's done.

from bs4 import BeautifulSoup
import urllib.request

series = input("Enter Series Name: ")
season = input("Enter Season Number: ")
episodes = int(input("Enter total number of episodes: "))

base = "http://www.tvsubtitles.net/"
index = input("Enter .html part of url: ")
url = base+index

data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")

link = soup.find_all('tr')
n = episodes

request_list = []

for k in range(2, n+2):
    get_link = (link[0].find_all('tr'))[k].find_all('td')[3].nobr.find_all('a')[0].get('href')
    request_list.append(get_link)

for redirect in request_list:
    if "subtitle" in redirect:
        lin = redirect
    elif "episode" in redirect:
        url = base + redirect
        data = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(data, 'html.parser')
        a = soup.find_all('div')
        for i in a:
            try:
                get = i.div.get('class')
                if get != None:
                    link = i.div.find_all('a')
                    for j in link:
                        txt = j.get('href')
                        if 'subtitle' in txt:
                            lin = txt[1:]
                            break
            except:
                pass

    else:
        print("Nothing to grab")

    if lin:
        lin = lin.split('-')
        lin[0] = "download"
        lin = "-".join(lin)
        url = base + lin
        print(url)
        print(series+" Season " + season + " Episode " + str(n) + " Downloading.......")
        urllib.request.urlretrieve(url, series + " s" + season + " episode " + str(n) + ".rar")
        print("File Downloaded :)")

    n -= 1
