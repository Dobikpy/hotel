from node import Node

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        cur_node = self.head
        if self.head == None:
            self.head = new_node
            return
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + "->"
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node != None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def push_front(self,data):
        new_node = Node(data)
        cur_node = self.head
        new_node.set_next(cur_node)
        self.head = new_node

    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()

    def value_at(self,index):
        cur_node = self.head
        count = 0
        while cur_node != None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    def insert(self,index,data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next != None:
            if index == 0:
                self.push_front(data)
                return
            elif count +1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    def remove(self,index):
        cur_node = self.head
        count = 0
        while cur_node.get_next != None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_remove = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_remove)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out to range")









