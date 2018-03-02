import csv
import os


def main():
    #print header
    print_header()
    #get data
    file = get_data_file()
    #print(file)
    data = load_data(file)

    query_data(data)

    #do statistics
    #report numbers

def print_header():
    print("-----------------------------------------")
    print("              REAL ESTATE APP            ")
    print("-----------------------------------------")

def get_data_file():
    base_folder = os.path.dirname(__file__) #gets the folder where this file (program.py) is found
    file = os.path.join(base_folder, "data", "SacramentoRealEstateTransactions2008.csv")

    return file

def load_data(file):

    with open(file) as myfile:
        reader = csv.DictReader(myfile)
        for row in reader:
            print(row)
            print("Bed count: {}".format(row['beds']))

    #Another LESS efficient way
    #with open(file) as myfile:
        #header = myfile.readline().strip()
        #reader = csv.reader(myfile)
        #for row in reader:
            #print(row)



def query_data(data):
    pass

if __name__ == '__main__':
    main()