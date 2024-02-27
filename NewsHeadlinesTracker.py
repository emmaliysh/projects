# Write your code here :-)

from bs4 import BeautifulSoup
import requests

# scrap headlines from bbc news
web = requests.get("https://www.bbc.com/news")

if web.status_code == 200:
    soup = BeautifulSoup(web.text, "html.parser")

    bbcheadlines = soup.find_all("h3")

    for i in range(len(bbcheadlines)):
        print(bbcheadlines[i].text)

else:
    print("Failed to fetch the website. Status code: ", web.status_code)

# scrap headlines from cnn news
    
web = requests.get("https://edition.cnn.com/")

if web.status_code == 200:
    soup = BeautifulSoup(web.text, "html.parser")

    cnnheadline = soup.find_all("h2", class_ ="container__title_url-text container_lead-package__title_url-text")

    print(cnnheadline)

    cnnheadlines = soup.find_all("span", class_ ="container__headline-text")

    for i in range(len(cnnheadlines)):
        print(cnnheadlines[i].text)

else:
    print("Failed to fetch the website. Status code: ", web.status_code)



# scrap headlines from newyork times
    
web = requests.get("https://www.nytimes.com/")

if web.status_code == 200:
    soup = BeautifulSoup(web.text, "html.parser")

    nyheadlines = soup.find_all("p", class_="indicate-hover css-vf1hbp")

    for i in range(len(nyheadlines)):
        print(nyheadlines[i].text)

    nynheadlines = soup.find_all("p", class_="indicate-hover css-1j7a2zk")

    for i in range(len(nynheadlines)):
        print(nynheadlines[i].text)

    headlines = soup.find_all("p", class_="indicate-hover css-66vf3i")

    for i in range(len(headlines)):
        print(headlines[i].text)

else:
    print("Failed to fetch the website. Status code: ", web.status_code)
    
