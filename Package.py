import csv
from Hash_Table import HashTable

class Package():
    # object that holds all the info of a package
    def __init__(self, id, address, city, state, zip_code, delivery_deadline, mass, special_notes,
                delivery_timestamp, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.mass = mass
        self.special_notes = special_notes
        self.delivery_timestamp = delivery_timestamp
        self.status = status

    def get_address(self):
        return self.address

    def get_id(self):
        return self.id

    # overrides print to see the actual data instead of object location
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" %(self.id, self.address, self.city, self.state, self.zip_code,
                                                 self.delivery_deadline, self.mass, self.special_notes,
                                                 self.delivery_timestamp, self.status)

# Loads packaage data from excel data sheet
# O(N^2)
def load_packages():
        # object created from hash table, has a size of 40
        pkg_hash_table = HashTable(40)

        # this will read in data from the package.csv file  to be used
        # to fill in the hash table
        with open('package.csv') as csv_file:
            read_csv_file = csv.reader(csv_file, delimiter=',')
            # go through csv data rows and format them into [key, value] pairs

            # O(N^2)
            for row in read_csv_file: # O(N)
                # based on package.csv
                pkg_id = int(row[0])  # column names
                pkg_address = row[1]
                pkg_city = row[2]
                pkg_state = row[3]
                pkg_zip = row[4]
                pkg_delivery_deadline = row[5]
                pkg_mass = row[6]
                pkg_special_notes = row[7]

                # additional info about the delivery status
                delivery_time_stamp = None

                status = 'At Hub'  # all deliveries start here (default)
                # reads in the data to store in a Package object
                pkg_info = Package(pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_delivery_deadline,
                                   pkg_mass, pkg_special_notes, delivery_time_stamp, status)

                # insert the data read into hash table
                pkg_hash_table.insert(pkg_id, pkg_info) # O(N)

        return pkg_hash_table