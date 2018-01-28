import os


def load_journal(name):
    data = []
    filename = get_journal_path(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def add_entry(entry, data):
    data.append(entry)

def  save_journal(name, data):
    filename = get_journal_path(name)
    print("....saving to '{}'".format(filename))

    with open(filename, 'w') as fout:

        for entry in data:
            fout.write(entry +  "\n")

def get_journal_path(name):
    filename = os.path.abspath(os.path.join(".", "journals", name + '.jrl'))
    return filename



