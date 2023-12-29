
import csv

### 3 trucks
### 2 drivers
### Drivers leave the hub no earlier than 8:00 a.m
### The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m. WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m. However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.

### 40 packages for two of the trucks
### Under 140 miles

# Package Class
#

class Package:
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, delivery_status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.delivery_status = delivery_status
        self.leaving_time = None
        self.delivery_time = None


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
    def ___init__(self, capacity, speed, load, packages, mileage, address, leave_time):
        self.capacity = capacity
        self.speed = speed
        self.load = load
        self.packages = packages
        self.mileage = mileage
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
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
      
    # Inserts a new item into the hash table.
    def insert(self, key, item): #  does both insert and update 
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # update key if it is already in the bucket
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            kv[1] = item
            return True
        
        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True
 
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        #print(bucket_list)
 
        # search for the key in the bucket list
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
            return kv[1] # value
        return None
 
    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
 
        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
          #print (key_value)
          if kv[0] == key:
              bucket_list.remove([kv[0],kv[1]])

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

