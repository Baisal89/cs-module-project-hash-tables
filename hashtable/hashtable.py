class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f"self.key {self.key}, self.value {self.value}, self.next {self.next}"


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        # begin out new table with and array
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        # Your code here
        return len(self.array)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        # Your code here

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for c in key.encode():
            hash = ((hash << 5) + hash) + c
            # code above is an optimaizer version of hash = hash * 33 + c
            hash &= 0xffffffff

        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        h_value = self.djb2(key)
        #return self.fnv1(key) % self.capacity
        return h_value % len(self.array)

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # Your code here
        # slot = self.hash_index(key)
        # self.array[slot] = HashTableEntry(key, value)
        index = self.hash_index(key)

        if self.array[index] == None:
            # set empty arr
            self.array[index] = []
        self.array[index].append([key, value])

        for i in range(0, len(self.array[index])):
            if self.array[index][i][0] == key:
                self.array[index][i][1] = value
        return index

        
    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Your code here
        # find the hash index
        index = self.hash_index(key)

        if self.array[index] == None:
            return None
        
        delete_this = ''

        # iterate through entire list
        for i in range(0, len(self.array[index])):
            # now through every bucket
            for t in self.array[index]:
                print('self.array[index][i]', [t])
                #if there are encountered a bucket then add to delete_this list 
                if [t][0][0] == key:
                    #set value to None
                    [t][0][1] = None
                    return [t][0]
                else:
                    return None

            print('self.array[index in delete()', self.array[index])

            print('self.array in delete()', self.array)

    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # Your code here
        # encountering the hash index 
        index = self.hash_index(key)

        if self.array[index]:
            for i in range(0, len(self.array[index])):
                if self.array[index][i][0] == key:
                    return self.array[index][i][1]
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        # Your code here
        # here we need to update our current capacity to the new capacity
        self.capacity = new_capacity

        # now we need create new array in order to place new items
        new_arr = [None] * new_capacity

        # iterate throught the old storage
        for c in self.array:
            # 
            cur = c[0]

            # iterate through liste while cur exists
            while cur is not None:
                # rehash our index
                index = self.hash_index(cur[0])

                #check if the index has a key: value or none
                if new_arr[index][cur] == None:
                    #create new empty arr
                    new_arr[index][cur] = []
                else:
                    # add the new node to the arr
                    new_arr[index].append([cur[0],cur[1]])
                cur += 1
        self.array = new_arr


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")