import movie_svc
import requests.exceptions


def main():
    print_header()
    event_search_loop()


def print_header():
    print("---------------------------------------------------")
    print("                  Movie Search App")
    print("---------------------------------------------------")


def event_search_loop():
    search = 'start'

    while search.lower() != 'x':
        try:
            search = input("What movie would you like to search for? (Press 'x' to Exit) ")

            if search.strip().lower() != 'x':
                movies = movie_svc.find_movies(search)

                print("Found {} movies".format(len(movies)))
                for m in movies:
                    print("{}--{}".format(m.title, m.year))

        except requests.exceptions.ConnectionError as ce:
            print("Sorry, that didn't work because {}".format(ce))

        except ValueError as val_err:
            print(val_err)


    print("Exiting..........")

if __name__ == '__main__':
    main()