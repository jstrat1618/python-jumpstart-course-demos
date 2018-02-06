import requests


def main():
    print_header()
    zip_code = input("For what zip code would you like the weather? [12345] ")
    html = get_html_from_web(zip_code)
    print(html)
    #get html from web
    #parse html
    #display forecast


def print_header():
    print("-----------------------------------------------")
    print("                 WEATHER CLIENT                ")
    print("-----------------------------------------------")
    print()

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather/{}'.format(zipcode)
    response = requests.get(url) #want a response code of 200; code of 404 or 500 not so good
    #print(response.status_code)
    return response.text



if __name__ == '__main__':
    main()


