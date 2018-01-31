"""
This is the Journal Module
"""

import os


def load_journal(name):
    """
    This method creates and loads a new ourn
    :param name: the name of the journal
    :return: a list with entries in the journal as its elements
    """
    data = []
    filename = get_journal_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def add_entry(entry, data):
    """
    Appends entry to journal data
    :param entry: The entry of our journal
    :param data: The journal data structure
    :return: None
    """
    data.append(entry)

def  save_journal(name, data):
    """
    writes and saves the data in the journal
    :param the name of the file to be written to
    :param the journal
    :return: None
    """
    filename = get_journal_path(name)
    print("....saving to '{}'".format(filename))

    with open(filename, 'w') as fout:

        for entry in data:
            fout.write(entry +  "\n")

def get_journal_path(name):
    """
    Gets the full path to the journal
    :param the name of the journal
    :return: The filepath to the journal
    """
    filename = os.path.abspath(os.path.join(".", "journals", name + '.jrl'))
    return filename



