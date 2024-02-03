class Node(object):
    """Node of a singlelinklist."""
    def __init__(self, item):
        
        # Item means data in the singlelinklist.
        self.item = item

        # Next is the signal of next node.
        self.next = None

class SingleLinkList(object):
    """A singlelinklist."""
    def __init__(self):
        self.head = None


class SingleLinkList(object):
    """"A single link list."""
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        """Whether the singlinklist is null or not."""
        return self.head is None
    
    def length(self):
        """The length of the singlelinklist."""
        # The initial pointer points to head.
        cur = self.head
        count = 0 
        # When cur points to none, that means get to the end.
        while cur is not None:
            count += 1
            # the pointer points to next.
            cur = cur.next
        return count
    
    def items(self):
        """Iterate the singlelinklist."""
        # Get the pointer of the head.
        cur = self.head
        # Loop the iteration.
        while cur is not None:
            # Return the generator.
            yield cur.item
            
            # the pointer points to next.
            cur = cur.next

    def add(self, item):
        """Add items in the head."""
        node = Node(item)
        # The new node pointer point into former head pointer.
        node.next = self.head

        # Chane the head pointer into new pointer
        self.head = node
    
    def append(self, item):
        """Add itemss in the end."""
        node = Node(item)
        # Whether the singlelinklist is null or not.
        if self.is_empty():
            # Head points to new node.
            self.head = node
        else:
            # The singlelinklist is not null.
            # The endnode.next points to new node.
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    
    def insert(self, index, item):
        """Insert items in the pointed location."""
        # Insert items before the first item.
        if index <= 0:
            self.add(item)
        
        # Insert items after the end item.
        elif index > (self.length() - 1):
            self.append(item)
        else:
            # Set item nodes.
            node = Node(item)
            cur = self.head
            # Loop until find the pointed location.
            for i in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node
    
    def remove(self, item):
        """Delete nodes."""
        cur = self.head
        pre = None
        while cur is not None:
            # Find the pointed item.
            if cur.item == item:
                # If the first item is the item required to delete.
                if not pre:
                    # Point the head next into the one after the head.
                    self.head = cur.next
                else:
                    # Point the previous next into the node after current one.
                    pre.next = cur.next
                return True
    
    def find(self, item):
        """Confirm whether the item in the singlinklist or not."""
        return item in self.items()

if __name__ == "__main__":
    # Set a linklist.
    link_list = SingleLinkList()

    # Add items in the end.
    for i in range(5):
        link_list.append(i)
    
    # Add items in the beginning.
    link_list.add(6)

    # Iterate the items in the linklist.
    for i in link_list.items():
        print(i, end = "\t")
    
    # Insert items in the linklist.
    link_list.insert(3, 9)
    print("\n", list(link_list.items()))

    # Delete items in the linklist.
    link_list.remove(9)

    # Find the items in linklist.
    print(link_list.find(4))



    """
    # Set nodes.
    node1 = Node(1)
    node2 = Node(2)

    # Add the nodes into linklist.
    link_list._head = node1
    node1.next = node2

    # Access the linklist.
    print(link_list._head.item)
    print(link_list._head.next.item)
    """


    
