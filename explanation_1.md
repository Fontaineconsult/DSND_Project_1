LRU Cache
    
    The LRU Cache works by using two different data structures, a linked
    list and a hashmap (dictionary).
    
    The hashmap is used to lookup and store values of the cache, while 
    the linkedlist is used to track whether or not we want to remove a 
    value from the cache.
    
    _Because we use a hashmap for lookup, checking the cache for a value
    happens in O(1) time._ 
    
    If we get a cache hit, we need to reorder the linked list. Reording
    a linked list simply requires re-setting the pointers in the nodes
    to the left and right of the node we are moving. Each opperation happens
    in O(1) time. 
    
    If there is a cache miss, we don't have to do anything with the linked
    list, just check the hashmap, which happens in O(1) time.
    
    I just use the python dict object as a hashmap as the implentation of
    the dict object uses hashing.  
    
    https://stackoverflow.com/questions/114830/is-a-python-dictionary-an-example-of-a-hash-table

    Because both major opperations in the LRU cache work in O(1) time, we 
    can say our LRU Cache in total works in O(1) time. There are no other 
    operations that use time complexity hither than O(1)
    
    _Using Hash and Linked lists are ideal for LRU cache as they are both (O)1 when looking up and reordering._
    
    Worst case is O(1)
    
    Space complexity for a linked list and hashtable is O(N). We use one of each and they both store the 
    same data, so space compexity would be O(N2)
    

File Recursion

    The file recursion is a simple recursive fuction. The function is called 
    recursively for each folder in a folder. Each time the function is called it
    loops through all items in a folder. If a file is found, it is appended to a list
    if a folde is found the function is called again with that folder passed in.
    
    The function itself contains two loops. 
    
    Each call first loops through the items in the directory passed in. If the
    item is a folder, the function is called again with that folder. If the item 
    is a file it is appeded to a list. Each time the function is called it will
    return a list if files which are then looped through and appended to the 
    list.
    
    Recursion stops when no more folders are found.
    
    _Using Recursion is efficient as we only call the function once for each folder._  
    
    Recursive function = O(N) depth of the recursion
    Two loops = O(N) + O(N) number of files and folders, number of files. 
    
    Worst case time complexity: O(N + (O(N) + O(N))) ???
    
    Space complexity for recursive functions is O(NM), where n the depth of the recursive stack
    and M is the size of each function call. The space complexity for the file recursion would
    depend on how deeply nested the folder structure is that we are searching. 
    
    
    

Huffman Tree

    The Huffman Encoder relies on the Tree data structure. 
    
    There are two primary activities, encoding an input string into a huffman tree 
    and creating a "bit string (not actually though, in python)", and
    and using the huffman tree to decode the bit string back into the
    original input string.
    
    The encoder has quite a few operations.
    
    First, we loop through the input and create a dict to get the set
    of all characters in the input. Each time a character is found we count it.
    
        Loop + dict check = O(N)
        
        
    We then convert that dict to a list and loop through it creating a Node for each item.
    
        Looping through dict ~= O(N)
        
        https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
        
    We then order that list in descending order
    
        Python .sort is O(n Log n)
        https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-this-python-sort-method
        
        This could probably be improved by using a linked list and "poping" the tail twice. However, we only have
        to call .sort one time, when we first create the list. Since python .insert is O(N) and searching a linked-list
        is O(N) it wouldn't matter too much.
 

    Then we pop the last two items and create a new nodes and bind thsoe items as its children. The new node
    is inserted back into the order list in order.
    
        Insert into list = O(N)
        https://wiki.python.org/moin/TimeComplexity
        
    This process contintues until the ordered list is empty.
    
        O(N)
        
    We now have a tree. Next we need to do a breadth first search to constuct a binary encoding for each node.
    
        O(N) for bfs + O(N) to loop through the returned value and add a 1 or 0
        
    The BFS search returns a list of lists. We then create a dict that will store each character and its binary
    encoding.
    
        looping through a list of lists = O(N)
    
    Finally we loop through the original input text and lookup each character in our encoding dict and add each binary
    encoding to an ouput string and return it.
    
        O(N)
        
        
    Since most opperations are O(N), we can say:
    
        Worst Case: (N Log N) + 9N where N is length of input string
        
        
    Space complexity for a binary tree is O(N), so the space complexity is O(N), where N is the size of the 
    input string.

Active Directory

    The active directory exercise is simple a recursive function the terminates the recursive stack when a True state
    is reached. 
    
    _Recursion is the most elegant datastructure for this exercise as it only called until it finds the name._ 
    
    Time complexity would be (O)N + (O)M where N is the depth of the recursive search and M is the lengh of each user list
    
    Worse case: O(N)
    
    Like the File Recursion exercise the Active Directory exercise relies on recursion, therefor the space complexity
    is O(NM) where N is the number of user groups we have to search. Worst case is all of them, best case is
    the user is found in the parent directory. 
     

Blockchain

    The blockchain is just a linkedlist. Adding a Block to the list happens in O(1) time since the blockchain 
    tracks the tail_node. All we need to do reasign the previous tail's next pointer.
    
       Worst case: O(1)
       
    Space complexity for blockchain is O(N) for a singly-linked list.
    

Union Intersection

    The Intersection problem uses a Hashmap and a LinkedList. The linked list is used to store values and the hashmap
    is used to track previously visited values in the linkedlist.
    
    
    The perform the union operation, we create a set of all the values in the first list, by storing them in a hash and
    appending the values to a return list. We then traverse the second lnked list and check the hash of the value already
    exists. If it doesn't exist we add it to the hash and append the value to our return list.
    
    For the intersection we must create two hashes to track our progres when we traverse the linked lists. This is to
    avoid adding duplicates to our ouput from the second linked list. The first hash is a set of values from the first 
    linked list, the second hash stores vales from the second linked list. If a value from the second linked list is
    already in the first hash, but NOT in the second hash, we added to our ouput then add it to the hash.
    
        Worst case: O(N) for traversing linked list.
    
    
    Not sure if the Linked Lists used in this exercise would count towards the space complexity as they are
    not technically part of the datastructure used to solve the problem. Anyway, we have two linked lists, so 
    space complexity would be O(N2)