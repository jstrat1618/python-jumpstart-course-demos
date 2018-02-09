import os
import cat_service
import subprocess
import platform

def main():
    # print header
    print_header()
    # get or create output folder
    folder = get_output_folder()
    # get cats from internet
    download_cats(folder)
    # display cats
    show_cats(folder)


def print_header():
    print('----------------------------------------------')
    print('                 LOL CAT Factory              ')
    print('----------------------------------------------')


def get_output_folder():
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating New Directory at {}.'.format(full_path))
        os.mkdir(full_path)

    full_path = os.path.abspath(folder)
    return full_path

def download_cats(folder):
    print('Contacting server to download cats.....')
    cat_count = 8
    for i in range(1,cat_count+1):
        cat_name = "LOLcat{}".format(i)
        print('Downloading cat {}'.format(cat_name))
        cat_service.get_cat(folder, cat_name)

    print("Done")


def show_cats(folder):
    print("Displaying cats")
    if platform.system() == "Windows":
        #subprocess.Popen('explorer ' + folder)
        subprocess.call(['explorer', folder])
    elif platform.system() == "Darwin":
        subprocess.call(['open', folder])
    elif platform.system() == "Linux":
        subprocess.call(['xgd-open', folder])
    else:
        print("We don't support your platform" + platform.system() + " :(" )




if __name__ == '__main__':
    main()