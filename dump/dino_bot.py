import requests
import bs4

company_name = "airbnb"
def get_company(company_name):
    r = requests.get("https://play.google.com/store/search?q="+company_name)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    subtitles = soup.findAll("a", {'class':"subtitle"})
    dev_urls = []
    for title in subtitles:
        try:
            text = title.attrs["title"].lower()
        #Sometimes there is a subtitle without any text on GPlay
        #Catchs the error
        except KeyError:
            continue
        if company_name in text:
            url = "https://play.google.com" + title.attrs["href"]
            dev_urls.append(url)
    return dev_urls

def get_company_apps_url(dev_url):
    r = requests.get(dev_url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    titles = soup.findAll("a", {"class":"title"})
    return ["https://play.google.com"+title.attrs["href"] for title in titles]

def get_app_category(app_url):
    r = requests.get(app_url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    developer_name = soup.find("span", {"itemprop":"name"}).text
    app_name = soup.find("div", {"class":"id-app-title"}).text
    category = soup.find("span", {"itemprop":"genre"}).text
    return (developer_name, app_name, category)

dev_urls = get_company("airbnb")
apps_urls = get_company_apps_url(dev_urls[0])
get_app_category(apps_urls[0])

>>> get_company("airbnb")
['https://play.google.com/store/apps/developer?id=Airbnb,+Inc']
>>> get_company_apps_url("https://play.google.com/store/apps/developer?id=Airbnb,+Inc")
['https://play.google.com/store/apps/details?id=com.airbnb.android']
>>> get_app_category("https://play.google.com/store/apps/details?id=com.airbnb.android")
('Airbnb, Inc', 'Airbnb', 'Travel & Local')