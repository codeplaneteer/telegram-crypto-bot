import requests
from bs4 import BeautifulSoup

url = ""
http_proxy = "http://118.107.44.181:8000"
proxies = {"http": http_proxy}


def get_AllCount(i = 0):
    r = requests.get("https://www.worldcoinindex.com/", proxies=proxies)
    soup = BeautifulSoup(r.text, "lxml")
    MoneyCounts = soup.find("div", class_="tradetable tradetable-mob").find_all("tr", class_="coinzoeken")
    file = open("CoinData.txt", "w+")
    for item in MoneyCounts:
        i += 1
        if i >= 21:
            continue
        MoneyCost = item.find("td", class_="number pricekoers lastprice").text
        MoneyName = item.find("td", class_="bitcoinName").find("span").text
        MoneyDifference = item.find("td", class_="percentage").text
        with open("CoinData.txt", "a") as file:
            file.write(f"<b>{MoneyName}</b>: <u>{MoneyCost}</u>  {MoneyDifference}\n")


def main():
    get_AllCount(0)


if __name__ == "__main__":
    main()
