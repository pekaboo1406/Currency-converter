import lxml
import bs4
import requests


def scrape(from_curr, to_curr, amount):
    scrape_link = 'https://xe.com/currencyconverter/convert/?Amount=' + str(
        amount) + '&From=' + from_curr + '&To=' + to_curr
    re = requests.get(scrape_link)

    soup = bs4.BeautifulSoup(re.text, 'lxml')
    site_data = soup.select('p')
    print(site_data[1].getText() + " " + site_data[2].getText(), '\n')
    print(site_data[3].getText() + '\n' + site_data[4].getText())


def get_input():
    from_curr=input("From : ")
    print()
    to_curr=input("To : ")

    print()
    amount = int(input("Amount = "))

    print('\n\n')

    scrape(from_curr=from_curr, to_curr=to_curr, amount=amount)


def main():
    get_input()


if __name__ == '__main__':
    main()
