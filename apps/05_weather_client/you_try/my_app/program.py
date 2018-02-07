import requests
import bs4
import collections

WeatherReport = collections.namedtuple("WeatherReport", "condition, temp, scale, location")

def main():
    print_header()
    zip_code = input("For what zip code would you like the weather? [12345] ")
    html = get_html_from_web(zip_code)
    report= get_weather_from_html(html)

    print("The temperature in {} is {} {}, and  {}.".format(
        report.location,
        report.temp,
        report.scale,
        report.condition
    ))

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

def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    report = WeatherReport(temp=temp, condition=condition, scale=scale, location=loc)

    return report

def cleanup_text(text :str):
    if not text:
        return text
    text = text.strip()

    return text

def find_city_and_state(loc: str):
    parts = loc.split("\n")
    return parts[0].strip()

if __name__ == '__main__':
    main()


