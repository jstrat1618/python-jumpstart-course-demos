import csv
import os
#Add try catch because python 2 doesn't have statistics module
try:
    import statistics
except:
    import statistics_standin as statistics


from data_types import Purchase


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


def load_data(filename):
    with open(filename, 'r') as myfile:
        # with open(filename, 'r') as fin:
        reader = csv.DictReader(myfile)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

def query_data(data):
    #what is the most expensive house
    #what is the least expensive house
    #what is the average price of a house
    #what is the average price of a 2 bedroom house

    data.sort(key=lambda p: p.price)

    high_purchase = data[-1]
    low_purchase = data[0]

    print("This most expensive house is ${:,} with {} beds, and {} baths.".format(high_purchase.price,
            high_purchase.beds, high_purchase.baths))
    print("This least expensive house is ${:,} with {} beds, and {} baths.".format(low_purchase.price,
            low_purchase.beds, low_purchase.baths))

    #INSTEAD OF THIS
    #prices = []
    #for dat in data:
    #    prices.append(dat.price)

    #WE CAN USE THIS
    prices = [dat.price for dat in data]

    ave_price = statistics.mean(prices)

    print("Average price is ${:,}.".format(round(ave_price, 2)))

    #INSTEAD OF THIS
    #prices = []
    #for dat in data:
    #    if dat.beds==2:
    #        prices.append(dat.price)
    #
    #WE CAN USE THIS
    prices = [dat.price for dat in data if dat.beds == 2]

    ave_price_2_bdrm = statistics.mean(prices)

    print("Average price of 2 bedroom house ${:,}.".format(round(ave_price_2_bdrm,2)))

    #get two bedroom houses via generator expressions
    two_bed_homes = (
        p
        for p in data
        if announce(p, '2-bedrooms, found {}'.format(p.beds)) and p.beds == 2  # test / condition
    )

    #Take up to the first 5 homes in two_bed_homes
    homes = []
    for h in two_bed_homes:
        if len(homes)>5:
            break
        homes.append(h)

    ave_price = statistics.mean(announce(p.price, 'Price') for p in homes)
    ave_baths = statistics.mean(p.baths for p in homes)
    ave_sqft = statistics.mean((p.sq__ft for p in homes))

    print("Average 2-bedroom home costs ${:,}, has {} baths, and {:,} sq ft ".format(
        int(ave_price), round(ave_baths, 1), round(ave_sqft, 1)))







def announce(item, msg):
    print("Pulling item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()