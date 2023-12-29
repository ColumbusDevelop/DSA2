
import csv

### 3 trucks
### 2 drivers
### Drivers leave the hub no earlier than 8:00 a.m
### The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

### 40 packages for two of the trucks
### Under 140 miles

# Package Class
#
#

class Package:
    def __init__(self, ID, address, city, state, zipcode, Deadline_time, weight, status):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.Deadline_time = Deadline_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.nearest = None

    def __str__(self):
        return f"Package - Address: {self.address}, Deadline: {self.deadline}, City: {self.city}, Zipcode: {self.zipcode}, Weight: {self.weight} kg, Status: {self.status}, Time: {self.time}"

    def update_status(self, convert_timedelta):
        if self.delivery_time < convert_timedelta:
            self.delivery_status = "Delivered"
        elif self.leaving_time > convert_timedelta:
            self.delivery_status = "En route"
        else:
            self.delivery_status = "At Hub"

# Truck Class
#

class Truck:
    def ___init__(self, truck_id, packages, package_limit = 16, miles_driven, address, leave_time):
        self.truck_id = truck_id
        self.packages = packages
        self.package_limit = package_limit
        self.miles_driven = miles_driven
        self.address = address
        self.leave_time = leave_time
        self.time = leave_time

    def __str__(self):
        return f"Truck ID: {self.truck_id}, Packages: {self.packages}, Miles Driven: {self.miles_driven}, Address: {self.address}, Departure Time: {self.depart_time}"

##################    def add(self, package):
##################        pass

##################    def remove(self, package):
##################        pass

# CSV Reading
#

### Read Package CSV

with open("csv/package.csv") as packageFile:
    packageReader = csv.reader(packageFile)
    packageReader = list(packageReader)

### Read Distance CSV

with open("csv/distance.csv") as distanceFile:
    distanceReader = csv.reader(distanceFile)
    distanceReader = list(distanceReader)

### Read Address CSV

with open("csv/address.csv") as addressFile:
    addressReader = csv.reader(addressFile)
    addressReader = list(addressReader)

###### Parsing Package Data



### Manually loading trucks 1, 2 and 3
#

truck1 = Truck()

truck2 = Truck()

truck3 = Truck()


# Hash Table
#

class HashTable:
    def __init__(self):
        self.table = []

    def insert(self, key):
        pass

    def delete(self, key):
        pass

    def search(self, key):
        pass

# Nearest_Neighbor Algorithm
#

def nearest():
    pass:

# Main with User Interface
# 1. Provide screenshots to show the status of all packages loaded onto each truck at a time between 8:35 a.m. and 9:25 a.m.
# 2. Provide screenshots to show the status of all packages loaded onto each truck at a time between 9:35 a.m. and 10:25 a.m.
# 3. Provide screenshots to show the status of all packages loaded onto each truck at a time between 12:03 p.m. and 1:12 p.m.

if __name__ == "__main__":
    # Mohmoud Mohamed - 002439508
    print()

