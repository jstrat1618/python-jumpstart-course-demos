def main():
    print_header()
    zip_code = input("For what zip code would you like the weather? [12345] ")
    get_html_from_web(zip_code)
    #get html from web
    #parse html
    #display forecast


def print_header():
    print("-----------------------------------------------")
    print("                 WEATHER CLIENT                ")
    print("-----------------------------------------------")
    print()

def get_html_from_web(zipcode):
    main_string = 'https://www.wunderground.com/weather/{}'.format(zipcode)
    print(main_string)




if __name__ == '__main__':
    main()


