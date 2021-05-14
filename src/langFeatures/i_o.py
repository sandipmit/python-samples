import json

def repr_vs_print():
    """repr() print interpreter readable output vs print() print human readable output"""
    hello = repr("Hello World\n")
    print(hello)
    print("Hello World\n")

def str_format():
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

def str_format_by_name():
    print('{scientist} had a laboratory at {city}'.format(scientist="Thomas A. Edison", city="Edison"))

def str_format_with_dictionary():
    table = {'scientist':"Thomas Alva Edison", 'city':"Edison"}
    print('{scientist} had a laboratory at {city}'.format(**table))

def read_file_line_by_line():
    with open("README.md") as f:
        for line in f:
            print(line)

def populate_list_with_file_content():
    with open("README.md") as f:
        lines = list(f)
        print(lines)


def saving_complex_obj_as_json():
    file_name = "json.txt"

    # w+ mode means its open for write, also will create file if does not exist
    with open(file_name, 'w+') as f:
        sales_transaction = {'item': 'Sample Item', 'qty': 20, 'price': 10.1}
        json.dump(sales_transaction, f)

    # r mode means its open for read only; you can do r+ for read/write
    with open(file_name, 'r') as json_file:
        json_str = json.load(json_file)
        print('Saved sales transaction {}'.format(json_str))

    #look at the raw json string saved in the file
    with open(file_name, 'r') as json_text:
        json_str = json_text.read()
        print('Raw saved sales transaction in a file {}'.format(json_str))

if __name__ == "__main__":
    #repr_vs_print()
    #str_format()
    #str_format_by_name()
    #str_format_with_dictionary()
    #read_file_line_by_line()
    #populate_list_with_file_content()
    saving_complex_obj_as_json()