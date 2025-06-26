import csv

#GET product information by categories and excluded unavailable product (null stock must be considered as unavailable)
def get_product_info(file_path):
    reader = csv.DictReader(open(file_path, 'r'))
    for row in reader:
        print(row['Name'] + ': ' + row['Price'])

product_info = get_product_info('products-100.csv')
#print(product_info)