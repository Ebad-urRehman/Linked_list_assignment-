# creating a class node with two fields data and next
class Node:
    # calling the constructor and assigning data to node
    def __init__(self, data):
        self.data = data
        self.next = None


# creating empty linked list
class Singly_Linked_List:
    def __init__(self):
        self.head = None

    # linklist from user
    def get_linklist(self, total_nodes, count):
        for n in range(total_nodes):
            data = input(f"Please Enter data of node {n + 1}\n")
            newnode = Node(data)
            if not self.head:
                self.head = newnode
                count[0] += 1
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = newnode
                count[0] += 1

    # function for appending link list
    def aappend(self, data, count):
        # global node_count
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            count[0] += 1
            # node_count += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            count[0] += 1
            # node_count += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
        # print(node_count)

    def insert_node(self, pos, data, count):
        pos = int(pos) - 1
        current = self.head
        # iterating until desired position to insert element
        if pos == 0:
            newnode = Node(data)
            nextnode = current
            self.head = newnode
            newnode.next = nextnode
            count[0] += 1

        # last position
        elif pos + 1 == count[0]:
            newnode = Node(data)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            newnode.previous = current
            count[0] += 1
        # after last position
        elif pos + 1 > count[0]:
            print("Over flow")
        # before first position
        elif pos + 1 < 1:
            print("Under flow")
        # nth position
        else:
            newnode = Node(data)
            for n in range(pos - 1):
                current = current.next
            # saving the node at position to insert
            nextnode = current.next
            # adding new node to next of previous node
            current.next = newnode
            # adding saved node as next node in front of node inserted
            newnode.next = nextnode
            count[0] += 1
            # node_count += 1

    def insert_node_last(self, data, count):
        newnode = Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode
        count[0] += 1

    def del_node(self, pos, count):
        current = self.head
        pos = int(pos) - 1
        if current.next is None:
            print("The only node in list is deleted")
            self.head = None
        elif pos == 0:
            self.head = current.next
        # deleting from last node
        elif pos + 1 == count[0]:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            count[0] -= 1
        elif pos + 1 > count[0]:
            print("Overflow")
        elif pos + 1 < 1:
            print("Underflow")
        # deleting from n position
        else:
            for n in range(pos - 1):
                current = current.next
            nextnode = current.next.next
            current.next = nextnode
        count[0] -= 1

    def del_node_end(self, count):
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        count[0] -= 1

    def search_list_pos(self, data, count):
        current = self.head
        for n in range(int(count[0])):
            if current.data == data:
                pos = n + 1
                return pos
            current = current.next
        print("value not found")

    def search_list_ele(self, pos):
        current = self.head
        pos = int(pos) - 1
        for n in range(pos):
            current = current.next
        print(current.data)

    def get_first_node(self):
        return self.head

    def merge_list(self, list2, count, count2):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = list2
        count[0] += count2[0]

    def sort_list_asc(self, count):
        current = self.head
        if self.head is None:
            print("List is empty")
        elif current.next is None:
            print("List only have one element")
        else:
            sorted_ele = 0
            while sorted_ele != count[0]:
                while current.next is not None:
                    if current.data >= current.next.data:
                        temp = current.data
                        current.data = current.next.data
                        current.next.data = temp
                    current = current.next
                current = self.head
                sorted_ele = sorted_ele + 1


class Doubly_Node:
    # calling the constructor and assigning data to node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = None

    # linklist from user
    def get_linklist(self, total_nodes, count):
        for n in range(total_nodes):
            data = input(f"Please Enter data of node {n + 1}\n")
            newnode = Doubly_Node(data)
            if not self.head:
                self.head = newnode
                newnode.next = None
                newnode.previous = None
            elif self.head.next is None:
                self.head.next = newnode
                newnode.previous = self.head
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = newnode
                newnode.previous = current
            count[0] += 1
            print(count[0])

    # function for appending link list
    def aappend(self, data, count):
        # global node_count
        new_node = Doubly_Node(data)
        if not self.head:
            self.head = new_node
            # node_count += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.previous = current
        count[0] += 1

    #         # node_count += 1
    #
    def print_list(self):
        current = self.head
        print("None<- ", end="")
        while current:
            print(current.data, end=" <--> ")
            current = current.next
        print("None")

    def print_list_rev(self):
        current = self.head
        print("None<- ", end="")
        while current.next:
            current = current.next
        while current is not None:
            print(current.data, end=" <--> ")
            current = current.previous
        print("None")
        # print(node_count)

    #
    def insert_node(self, pos, data, count):
        pos = int(pos) - 1
        current = self.head
        # iterating until desired position to insert element
        newnode = Doubly_Node(data)
        # first position
        if pos == 0:
            nextnode = current
            self.head = newnode
            nextnode.previous = newnode
            newnode.next = nextnode
            newnode.previous = None
            count[0] += 1
        # last position
        elif pos + 1 == count[0]:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
            newnode.previous = current
            count[0] += 1
        # after last position
        elif pos + 1 > count[0]:
            print("Over flow")
        # before first position
        elif pos + 1 < 1:
            print("Under flow")
        # nth position
        else:
            for n in range(pos - 1):
                current = current.next
            # saving the node at position to insert
            nextnode = current.next
            # adding new node to next of previous node
            current.next = newnode
            newnode.previous = current
            # adding saved node as next node in front of node inserted
            newnode.next = nextnode
            # giving previous node to new node
            # current.previous = nextnode.previous
            nextnode.previous = newnode
            count[0] += 1
        # node_count += 1

    def insert_node_last(self, data, count):
        newnode = Doubly_Node(data)
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = newnode
        newnode.previous = current
        count[0] += 1

    #
    def del_node(self, pos, count):
        current = self.head
        pos = int(pos) - 1
        # when there is only one node
        if current.next is None:
            print("The only node in list is deleted")
            self.head = None
            count[0] -= 1
        # deleting from 1st position
        elif pos == 0:
            self.head = current.next
            if self.head is not None:
                self.head.previous = None
            count[0] -= 1
        # deleting from last node
        elif pos + 1 == count[0]:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            count[0] -= 1
        elif pos + 1 > count[0]:
            print("Overflow")
        elif pos + 1 < 1:
            print("Underflow")
        # deleting from n position
        else:
            for n in range(pos):
                current = current.next
            nextnode = current.next.next
            current.next = nextnode
            nextnode.previous = current
            count[0] -= 1

    def del_node_end(self, count):
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        count[0] -= 1

    def search_list_pos(self, data, count):
        current = self.head
        for n in range(int(count[0])):
            if current.data == data:
                pos = n + 1
                return pos
            current = current.next
        print("value not found")

    def search_list_ele(self, pos):
        current = self.head
        pos = int(pos) - 1
        for n in range(pos):
            current = current.next
        print(current.data)

    def get_first_node(self):
        return self.head

    #
    def merge_list(self, list2, count, count2):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = list2
        list2.previous = current
        count[0] += count2[0]

    #
    def sort_list_asc(self, count):
        current = self.head
        if self.head is None:
            print("List is empty")
        elif current.next is None:
            print("List only have one element")
        else:
            sorted_ele = 0
            while sorted_ele != count[0]:
                while current.next is not None:
                    if current.data >= current.next.data:
                        temp = current.data
                        current.data = current.next.data
                        current.next.data = temp
                    current = current.next
                current = self.head
                sorted_ele = sorted_ele + 1

    #
    # # def sort_list_bubb(self, count):
    # #     current = self.head
    # #     if current.next is None:
    # #         print("List only have one element")
    # #     else:
    # #         for i in range(count[0]-1):
    # #             current = self.head
    # #             for j in range(count[0]-i-1):
    # #                 if current.data > current.next.data:
    # #                     temp = current.data
    # #                     current.data = current.next.data
    # #                     current.next.data = temp
    # #                 current = current.next

    def sort_list_des(self, count):
        current = self.head
        if self.head is None:
            print("List is empty")
        elif current.next is None:
            print("List only have one element")
        else:
            sorted_ele = 0
            while sorted_ele != count[0]:
                while current.next is not None:
                    if current.data <= current.next.data:
                        temp = current.data
                        current.data = current.next.data
                        current.next.data = temp
                    current = current.next
                current = self.head
                sorted_ele = sorted_ele + 1


class Singly_Cir_Linked_List:
    # link list from user
    def __init__(self):
        self.head = None


    def get_linklist(self, total_nodes, count):
        for n in range(total_nodes):
            data = input(f"Please Enter data of node {n + 1}\n")
            newnode = Singly_cir_Node(data)
            if not self.head:
                self.head = newnode
                newnode.next = self.head
                count[0] += 1
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = newnode
                newnode.next = self.head
                count[0] += 1

    # function for appending link list
    def aappend(self, data, count):
        # global node_count
        new_node = Singly_cir_Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            count[0] += 1
            # node_count += 1
        else:
            current = self.head
            while current.next is not self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            count[0] += 1
            # node_count += 1

    def print_list(self):
        current = self.head
        while current.next != self.head:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data, end="")
        print(f"->First = {current.next.data}")
        # print(node_count)

    # def insert_node(self, pos, data, count):
    #     pos = int(pos) - 1
    #     current = self.head
    #     # iterating until desired position to insert element
    #     if pos == 0:
    #         newnode = Node(data)
    #         nextnode = current
    #         self.head = newnode
    #         newnode.next = nextnode
    #         count[0] += 1
    #
    #     # last position
    #     elif pos + 1 == count[0]:
    #         newnode = Node(data)
    #         current = self.head
    #         while current.next is not None:
    #             current = current.next
    #         current.next = newnode
    #         newnode.previous = current
    #         count[0] += 1
    #     # after last position
    #     elif pos + 1 > count[0]:
    #         print("Over flow")
    #     # before first position
    #     elif pos + 1 < 1:
    #         print("Under flow")
    #     # nth position
    #     else:
    #         newnode = Node(data)
    #         for n in range(pos - 1):
    #             current = current.next
    #         # saving the node at position to insert
    #         nextnode = current.next
    #         # adding new node to next of previous node
    #         current.next = newnode
    #         # adding saved node as next node in front of node inserted
    #         newnode.next = nextnode
    #         count[0] += 1
    #         # node_count += 1
    #
    # def insert_node_last(self, data, count):
    #     newnode = Node(data)
    #     current = self.head
    #     while current.next is not None:
    #         current = current.next
    #     current.next = newnode
    #     count[0] += 1
    #
    # def del_node(self, pos, count):
    #     current = self.head
    #     pos = int(pos) - 1
    #     if current.next is None:
    #         print("The only node in list is deleted")
    #         self.head = None
    #     elif pos == 0:
    #         self.head = current.next
    #     # deleting from last node
    #     elif pos + 1 == count[0]:
    #         current = self.head
    #         while current.next.next is not None:
    #             current = current.next
    #         current.next = None
    #         count[0] -= 1
    #     elif pos + 1 > count[0]:
    #         print("Overflow")
    #     elif pos + 1 < 1:
    #         print("Underflow")
    #     # deleting from n position
    #     else:
    #         for n in range(pos - 1):
    #             current = current.next
    #         nextnode = current.next.next
    #         current.next = nextnode
    #     count[0] -= 1
    #
    # def del_node_end(self, count):
    #     current = self.head
    #     while current.next.next is not None:
    #         current = current.next
    #     current.next = None
    #     count[0] -= 1
    #
    # def search_list_pos(self, data, count):
    #     current = self.head
    #     for n in range(int(count[0])):
    #         if current.data == data:
    #             pos = n + 1
    #             return pos
    #         current = current.next
    #     print("value not found")
    #
    # def search_list_ele(self, pos):
    #     current = self.head
    #     pos = int(pos) - 1
    #     for n in range(pos):
    #         current = current.next
    #     print(current.data)
    #
    # def get_first_node(self):
    #     return self.head
    #
    # def merge_list(self, list2, count, count2):
    #     current = self.head
    #     while current.next is not None:
    #         current = current.next
    #     current.next = list2
    #     count[0] += count2[0]
    #
    # def sort_list_asc(self, count):
    #     current = self.head
    #     if self.head is None:
    #         print("List is empty")
    #     elif current.next is None:
    #         print("List only have one element")
    #     else:
    #         sorted_ele = 0
    #         while sorted_ele != count[0]:
    #             while current.next is not None:
    #                 if current.data >= current.next.data:
    #                     temp = current.data
    #                     current.data = current.next.data
    #                     current.next.data = temp
    #                 current = current.next
    #             current = self.head
    #             sorted_ele = sorted_ele + 1


# creating this class child class so we assign newnode to self.head every time we created a new node
class Singly_cir_Node(Singly_Cir_Linked_List):
    # calling the constructor and assigning data to node
    def __init__(self, data):
        super().__init__()  # Call the parent class constructor
        self.data = data
        self.next = self.head


if __name__ == "__main__":
    pass
