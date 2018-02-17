import os

def main():
    print_header()
    #ask user what directory to search
    folder = get_folder_from_user()
    while not folder:
        print("Sorry, we can't do anything with this")
        folder = get_folder_from_user()

    #ask user what text to search for
    text = get_text_from_user()
    #search
    found = search_folder(folder, text)
    #return output
    print(found)


def get_folder_from_user():
    folder = input("What folder would you like to search? ")
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)

def get_text_from_user():
    text = input("What text would you like to search for? ")
    return text.lower()

def search_folder(folder, text):
    '''
    :param folder: The folder being searched
    :param text: The text you are searching for
    :return:
    '''

    all_matches = []

    items = os.listdir(folder)
    for item in items:
        full_item = os.path.join(folder, item)
        if os.path.isdir(full_item):
            continue
        else:
            matches = search_file(full_item, text)
            all_matches.extend(matches)

    return all_matches


def search_file(filename, text):

    matches = []

    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            if line.lower().find(text) >= 0:
                matches.append(line)

    return matches



def print_header():
    print('---------------------------------------------------')
    print('                     FILE SEARCHER APP')
    print('---------------------------------------------------')


if __name__ == '__main__':
    main()