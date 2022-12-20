import csv
import datetime
from Package import Package, load_packages

# csv files
distanceCSV = 'distance.csv'
addressCSV = 'addresses.csv'

# Access to hash table that holds the info. on each package
pkg_hash_table = load_packages()

# opens the files
# Holds the distances
distance_data = []
with open(distanceCSV) as dist_file:
    distances = csv.reader(dist_file,delimiter =',')
    for distance in distances:
        distance_data.append(distance) # list into a list / 2d array

# Holds the addresses
address_data = []
with open(addressCSV) as addr_file:
    addresses = csv.reader(addr_file, delimiter=',')
    for address in addresses:
        address_data.append(address[2])

# Calculates distance between street addresses
# Parameters: Accepts two address strings address 1 goes to address 2
# Returns: Distance
# O(N)
def distanceBetweenAddresses(addr_1, addr_2):

    # converts the address string to the address's id
    row = getAddressIDByStreet(addr_1) # O(N)
    col = getAddressIDByStreet(addr_2) # O(N)

    distance = distance_data[row][col]
    # if the location on the file is blank ''
    # flip the coordinates to find the mirrored distance
    # (based on how the data is file is organized in Excel file, this is valid)
    if distance == '':
        distance = distance_data[col][row]

    return float(distance) # file reads it as a string '', should be cast as a number

# Find the shortest distance for the truck to head to next based on the packages on truck
# Parameter: Current street address (string) and the list of package ids on truck
# Returns: Package id of the package that is closest and the distance
# O(N^2)
def minDistanceFromCurrentAddr(currentStreetAddress, truckPkgs): # [WIP...Rework]

    # variables to hold data
    min_distance = 40  # a random number to start comparing with
    pkgs_on_truck= []  # a list that will hold the full data of each package that is in truck currently

    # scans through the list of package  by their ids
    # appends them into pkgs_on_truck list
    # O(N^2)
    for id in truckPkgs: # based this on id O(N)
        pkg = pkg_hash_table.search(id) # O(N)
        pkgs_on_truck.append(pkg)

    # gets the address from each package and calculates the distance
    # O(N^2)
    for pkg in pkgs_on_truck: # O(N)
        address = pkg.get_address() # gets only the address from each package object
        calc_nearest_dist = distanceBetweenAddresses(currentStreetAddress, address) # O(N)

        if calc_nearest_dist < min_distance:
            min_distance = calc_nearest_dist
            pkg_id = pkg.get_id()

    # pkg_id[0] (be used to remove pkg from truck list), min_distance[1] (be used to calc total distance)
    return pkg_id , min_distance

# calculate how much TIME it will take for the truck to make a delivery to a location
# Parameters: Current time and distance from package drop off
# Returns: Time it takes to reach a delivery location
# O(1)
def truck_time_to_delivery(currentTime, distanceToDropOff):
    # Truck's speed is 18 miles per hour
    hoursTraveled =  distanceToDropOff / 18
    minutesTraveled = hoursTraveled * 60
    # timedelta - object rep. difference between two times/dates
    time = currentTime + datetime.timedelta(minutes=minutesTraveled)
    return time

# Gets the address's id by the name of the street
# Parameter: Street address
# Returns: address id
# O(N)
def getAddressIDByStreet(addressInput):
    index = -1
    for address in address_data:
        index = index + 1
        if address == addressInput:
            return index
    return -1

# Algorithm that will create an optimal truck route
# Parameters: List of packages on truck (their ids) and the time the truck is set to depart from hub
# Returns: An optimal delivery route list, total distance truck travels on that route
# O(N^2)
def delivery_truckstop_route(pkgs_on_truck, departureTime):
    # time that the route starts, keeps the departure time separate
    curr_time = departureTime

    optimal_route = [0] # delivery route order (0 is the hub where trucks start and ENDS)
    pkgs = pkgs_on_truck.copy() # copy of the existing list to modify
    pkgs_onboard_truck_data = []
    time_of_delivery = []
    total_truck_distance = 0
    curr_truck_address = '4001 South 700 East' # Truck starts here (Hub)

    # get data from each package on the truck from hash table
    # O(N^2)
    for pkg_id in pkgs: # O(N)
        pkg_object = pkg_hash_table.search(pkg_id) # O(N)
        pkgs_onboard_truck_data.append(pkg_object)

    # scans through list and forms a route order to deliver
    # determines the next stop, removes id (pkg delivered), keeps track of total distance
    # i variable is not used, we're just focusing on looping till end of list
    # O(N^2)
    for i in pkgs_onboard_truck_data: # O(N)
        pkg_stop_info = minDistanceFromCurrentAddr(curr_truck_address, pkgs) # O(N)
        pkg_id_delivered = pkg_stop_info[0] # grabs the pkg id
        pkg_distance_traveled = pkg_stop_info[1] # grabs the min distance to calc
        pkg_object = pkg_hash_table.search(pkg_id_delivered) # searches for id in hash table O(N)
        curr_truck_address = pkg_object.get_address() # gets address
        pkgs.remove(pkg_id_delivered)

        # calc/add to the current time, based on when the pkg is delivered
        # O(1)
        curr_time = truck_time_to_delivery(curr_time,pkg_distance_traveled)

        # stamp the time in the pkg object
        pkg_object.delivery_timestamp = curr_time

        pkg_object.departureTime = departureTime

        # construct the optimal route
        optimal_route.append(pkg_id_delivered)

        # calc the distance of the truck as the deliveries are made
        total_truck_distance = total_truck_distance + pkg_distance_traveled

        # time the pkg(s) were delivered
        time_of_delivery = curr_time

    return optimal_route , total_truck_distance, time_of_delivery # 0 , 1, 2 indexes
