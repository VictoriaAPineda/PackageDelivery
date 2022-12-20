# Victoria Pineda ID: 006951257
import datetime
import Distance
from Distance import pkg_hash_table  # used to access hash table data

def MainModule():

    # Preloaded packages into trucks
    truck_1_pkgs = [27,35,1,2,40,29,22,24,13,14,15,16,19,20,37,34]
    truck_2_pkgs = [3,18,36,38,6,25,28,32,5,17,23,26,21,31,32]
    truck_3_pkgs = [9,8,10,11,12,39,21,30,4,33,7]

    # Chosen times for truck to leave the hub
    # Used timedelta for all comparisons of time
    truck_1_depart_time = datetime.timedelta(hours=8, minutes=0)
    truck_2_depart_time = datetime.timedelta(hours=9, minutes=5)
    truck_3_depart_time = datetime.timedelta(hours=9, minutes=45) # goes after both trucks are done

    # package delivery info. per truck (returns 3 items - [0] optimal route [1] total distance [2] time of deliveries)
    truck_1 = Distance.delivery_truckstop_route(truck_1_pkgs,truck_1_depart_time)
    truck_2 = Distance.delivery_truckstop_route(truck_2_pkgs, truck_2_depart_time)
    truck_3 = Distance.delivery_truckstop_route(truck_3_pkgs,truck_3_depart_time)

    # delivery route for each truck
    truck_1_optimal_route = truck_1[0]
    truck_2_optimal_route = truck_2[0]
    truck_3_optimal_route = truck_3[0]

    user_choice = input('\nWelcome to the Western Governors University Parcel Service'
          '\nSelect an option below:\n'
          '(1) Get package statuses based on an inputted time\n'
          '(2) View total distance traveled by trucks\n'
          '(3) Exit program\n')

    # Choice 1:
    if user_choice =='1':
        inputted_time = input('Enter a time to check package delivery statuses\n'
                              'Accepted Format: (HH:MM:SS) | Example: 08:25:00\n')
        (hr, min, sec) = inputted_time.split(':')
        # string input converted to time delta object
        user_selected_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))

        # scans each pkg
        for pkg_id in range(1,41):
            # gets data of a package based on its id
            pkg_object = pkg_hash_table.search(pkg_id)

            # Truck 1
            if pkg_id in truck_1_optimal_route:

                if pkg_object.delivery_timestamp < user_selected_time:
                    pkg_object.status = "Delivered"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} | Delivered at: {}".format(pkg_object.id, pkg_object.delivery_deadline,
                                                               pkg_object.status,
                                                               pkg_object.delivery_timestamp))
                elif truck_1_depart_time > user_selected_time:
                    pkg_object.status = "At Hub"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} ".format(pkg_object.id, pkg_object.delivery_deadline,pkg_object.status))
                else:
                    pkg_object.status = "En Route"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} ".format(pkg_object.id, pkg_object.delivery_deadline, pkg_object.status))

            # Truck 2
            if pkg_id in truck_2_optimal_route:

                if pkg_object.delivery_timestamp < user_selected_time:
                    pkg_object.status = "Delivered"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} | Delivered at: {}".format(pkg_object.id, pkg_object.delivery_deadline,
                                                               pkg_object.status,
                                                               pkg_object.delivery_timestamp))
                elif truck_2_depart_time > user_selected_time:
                    pkg_object.status = "At Hub"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} ".format(pkg_object.id, pkg_object.delivery_deadline, pkg_object.status))
                else:
                    pkg_object.status = "En Route"
                    pkg_object.status = "En Route"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} ".format(pkg_object.id, pkg_object.delivery_deadline, pkg_object.status))

            # Truck 3
            if pkg_id in truck_3_optimal_route:

                if pkg_object.delivery_timestamp < user_selected_time:
                    pkg_object.status = "Delivered"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} | Delivered at: {}".format(pkg_object.id, pkg_object.delivery_deadline,
                                                               pkg_object.status,
                                                               pkg_object.delivery_timestamp))
                elif truck_3_depart_time > user_selected_time:
                    pkg_object.status = "At Hub"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} ".format(pkg_object.id, pkg_object.delivery_deadline, pkg_object.status))
                else:
                    pkg_object.status = "En Route"
                    print("Package ID: {} | Delivery deadline: {} | "
                          " Status: {} ".format(pkg_object.id, pkg_object.delivery_deadline, pkg_object.status))

    # Choice 2:
    if user_choice == '2':
        truck_1_listed_route = Distance.delivery_truckstop_route(truck_1_pkgs, truck_1_depart_time)
        truck_1_distance = truck_1_listed_route[1]
        print('Truck 1 distance: {:.2f}'.format(truck_1_distance))

        truck_2_listed_route = Distance.delivery_truckstop_route(truck_2_pkgs, truck_2_depart_time)
        truck_2_distance = truck_2_listed_route[1]
        print('Truck 2 distance: {:.2f}'.format(truck_2_distance))

        truck_3_listed_route = Distance.delivery_truckstop_route(truck_3_pkgs, truck_3_depart_time)
        truck_3_distance = truck_3_listed_route[1]
        print('Truck 3 distance: {:.2f}'.format(truck_3_distance))

        print('Total distance: {:.2f}'.format(round(truck_1_distance + truck_2_distance + truck_3_distance)))

    # Choice 3:
    if user_choice == '3':
        print('Exiting program.')
        SystemExit


# program starts here
if __name__ == '__main__':
    MainModule()