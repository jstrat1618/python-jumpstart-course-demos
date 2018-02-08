import requests
import os
import shutil


def get_cat(folder, name):
    '''
    :param folder: The folder to save the cate to
    :param the name of the cat image
    :return:
    '''
    url = 'http://consuming-python-services-api.azurewebsites.net/cats/random'

    cat_data = get_data_from_url(url)

    save_image(folder, name, cat_data)


def get_data_from_url(url):
    response = requests.get(url, stream=True)
    return response.raw

def save_image(folder, name, data):
    filename = os.path.join(folder, name + '.jpg')
    with open(filename, 'wb') as fout:
        shutil.copyfileobj(data, fout)


