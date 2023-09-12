from functions import Node, Singly_Linked_List, Doubly_Linked_List, Singly_Cir_Linked_List

# count variable to keep track of no of node of all lists
s_count = [0]
d_count = [0]
sc_count = [0]
dc_count = [0]

# getting a linked list and its size
print("How many elements you want in linked list")
total_nodes = int(input())

list_menu_msg = """
----------List Menu----------
1. Singly Link List
2. Doubly Link List
3. Singly Circulate Link List
4. Doubly Circular Link List
5. Exit
"""

MainMenu_Msg = """
----------Main Menu----------
Which operation you want to perform on your List : 
-> I for Insert(Insert new element at desired position)
-> S for Sort (Ascending/Descending)
-> Q for search an element in List
-> D for deleting an element
M for Merge(Add new List to existing List at last)
T for Edit(Edit Old element from your desired position)
A for append(Add a new element at last)
X for deleting the whole List
E for Exit to list menu
"""

while True:
    list_choice = input(list_menu_msg)
    match list_choice:
        case '1':
            # creating empty list and getting data
            my_list = Singly_Linked_List()
            my_list.get_linklist(total_nodes, s_count)
            print("Your Linked list is : \n")
            my_list.print_list()
            print(f"Total Nodes : {s_count[0]}")

            while True:
                print("-------------SINGLY LINK LIST-------------")
                choice = input(MainMenu_Msg)
                choice = choice.capitalize()
                match choice:
                    case 'I':

                        insert_msg = """\
----------Insertion Menu-----------
Where you want to insert the element
F. At First Press F
L. At Last Press L
N. At nth Position Press N
E. For Exit
            """
                        while True:
                            ins_choice = input(insert_msg)
                            ins_choice = ins_choice.capitalize()
                            match ins_choice:
                                case 'F':
                                    data = input("Enter the node data you want to input at First position")
                                    my_list.insert_node(1, data, s_count)
                                    my_list.print_list()

                                case 'L':
                                    data = input("Enter the node data you want to input at Last position")
                                    my_list.insert_node_last(data, s_count)
                                    my_list.print_list()

                                case 'N':
                                    pos = input("On which position you want to insert the node")
                                    data = input(f"Enter the node data you want to input at {pos} position")
                                    my_list.insert_node(pos, data, s_count)
                                    my_list.print_list()
                                case 'E':
                                    break

                    case 'Q':
                        search_msg = """\
How you want to search the element
S. Search by element(Enter a element to found its position)
P. Search by position(Enter a position to check data on that position)
E. Exit\n"""
                        while True:
                            search_choice = input(search_msg)
                            search_choice = search_choice.capitalize()
                            match search_choice:
                                case 'S':
                                    print("The elements in your list are")
                                    my_list.print_list()
                                    data = input("Enter value of the element to find its position")
                                    pos = my_list.search_list_pos(data, s_count)
                                    print(f"{data} found at position {pos}")

                                case 'P':
                                    print("The elements in your list are")
                                    my_list.print_list()
                                    pos = input("Enter position to find data at that position : ")
                                    data = my_list.search_list_ele(pos)
                                case 'E':
                                    break
                                case _:
                                    print("Please Enter a Correct value Lower and upper cases both are allowed : ")


                    case 'D':
                        del_msg = """\
----------Deletion Menu-----------
From where you want to delete the element
F. At First Press F
L. At Last Press L
N. At nth Position Press N
E. Exit
            """
                        while True:
                            del_choice = input(del_msg)
                            del_choice = del_choice.capitalize()
                            print("The elements in your list are")
                            my_list.print_list()
                            match del_choice:
                                case 'F':
                                    my_list.del_node(1, s_count)
                                    print("First element Deleted : ")
                                    my_list.print_list()
                                case 'L':
                                    my_list.del_node_end(s_count)
                                    print("Last element Deleted : ")
                                    my_list.print_list()
                                case 'N':
                                    pos = input("Enter a position to delete value from : ")
                                    my_list.del_node(pos, s_count)
                                    print(f"{pos} element deleted")
                                    my_list.print_list()
                                case 'E':
                                    break
                                case _:
                                    print("Please Enter a Correct value Lower and upper cases both are allowed")


                    case 'S':
                        sort_msg = """
A. Sort in ascending order\
D. Sort in descending order
E. Exit
"""
                        sort_choice = input(sort_msg)
                        sort_choice = sort_choice.capitalize()
                        match sort_choice:
                            case 'A':
                                print("----------Sorting List Ascending Order----------")
                                my_list.sort_list_asc(s_count)
                                print("               ---After Sorting---               ")
                                my_list.print_list()

                            case 'D':
                                print("----------Sorting List Descending Order----------")
                                my_list.sort_list_des(s_count)
                                print("               ---After Sorting---               ")
                                my_list.print_list()
                            case 'E':
                                break
                            case _:
                                print("Please Enter a Correct value Lower and upper cases both are allowed")

                    case 'A':
                        data = input("Enter a value to append at last of Linked list")
                        my_list.aappend(data, s_count)
                        my_list.print_list()
                    case 'M':
                        merge_msg = """\
"Enter a new list to merge with previous list"
Total Number you want in new list : """
                        # creating new list for merging into old list
                        m_count = [0]
                        m_total_nodes = int(input(merge_msg))
                        my_list2 = Singly_Linked_List()

                        # taking input for linked list 2
                        my_list2.get_linklist(m_total_nodes, m_count)
                        print("Your second list is")
                        my_list2.print_list()

                        # Merging inked lists
                        print("----Merging Lists in progress-----")
                        first_node = my_list2.get_first_node()

                        # first node is first node of linked list 2
                        my_list.merge_list(first_node, s_count, m_count)
                        print("List after merging is : ")
                        my_list.print_list()

                    case 'T':
                        my_list.print_list()
                        edit_msg = """\
Enter the position from where you want to edit : """
                        pos = int(input(edit_msg))
                        data = input("Enter new data to place at that position")
                        my_list.del_node(pos, s_count)
                        my_list.insert_node(pos, data, s_count)
                        print("Your list is now")
                        my_list.print_list()

                    case 'E':
                        break

                    case _:
                        print("Please Enter a Correct value Lower and upper cases both are allowed")
                count_text = str(s_count).replace('[', '').replace(']', '')
                print(f"total node = {count_text}")

        case '2':
            # creating empty list and getting data
            my_list = Doubly_Linked_List()
            my_list.get_linklist(total_nodes, d_count)
            print("Your Linked list is : \n")
            print(f"\nTotal Nodes : {d_count[0]}")

            while True:
                print("-------------DOUBLY LINK LIST-------------")
                print("current list is")
                print("Forward order : ")
                my_list.print_list()
                print("Reversed order : ")
                my_list.print_list_rev()
                choice = input(MainMenu_Msg)
                choice = choice.capitalize()
                match choice:
                    case 'I':

                        insert_msg = """\
----------Insertion Menu-----------
Where you want to insert the element
F. At First Press F
L. At Last Press L
N. At nth Position Press N
E. For Exit
"""
                        while True:
                            ins_choice = input(insert_msg)
                            ins_choice = ins_choice.capitalize()
                            match ins_choice:
                                case 'F':
                                    data = input("Enter the node data you want to input at First position")
                                    my_list.insert_node(1, data, d_count)
                                    my_list.print_list()

                                case 'L':
                                    data = input("Enter the node data you want to input at Last position")
                                    my_list.insert_node_last(data, d_count)
                                    my_list.print_list()

                                case 'N':
                                    pos = input("On which position you want to insert the node")
                                    data = input(f"Enter the node data you want to input at {pos} position")
                                    my_list.insert_node(pos, data, d_count)
                                    my_list.print_list()
                                case 'E':
                                    break

                    case 'Q':
                        search_msg = """\
How you want to search the element
S. Search by element(Enter a element to found its position)
P. Search by position(Enter a position to check data on that position)
E. Exit\n"""
                        while True:
                            search_choice = input(search_msg)
                            search_choice = search_choice.capitalize()
                            match search_choice:
                                case 'S':
                                    print("The elements in your list are")
                                    my_list.print_list()
                                    data = input("Enter value of the element to find its position")
                                    pos = my_list.search_list_pos(data, d_count)
                                    print(f"{data} found at position {pos}")

                                case 'P':
                                    print("The elements in your list are")
                                    my_list.print_list()
                                    pos = input("Enter position to find data at that position : ")
                                    data = my_list.search_list_ele(pos)
                                case 'E':
                                    break
                                case _:
                                    print("Please Enter a Correct value Lower and upper cases both are allowed : ")

                    case 'D':
                        del_msg = """\
----------Deletion Menu-----------
From where you want to delete the element
F. At First Press F
L. At Last Press L
N. At nth Position Press N
E. Exit
"""
                        while True:
                            del_choice = input(del_msg)
                            del_choice = del_choice.capitalize()
                            print("The elements in your list are")
                            my_list.print_list()
                            match del_choice:
                                case 'F':
                                    my_list.del_node(1, d_count)
                                    print("First element Deleted : ")
                                    my_list.print_list()
                                case 'L':
                                    my_list.del_node_end(d_count)
                                    print("Last element Deleted : ")
                                    my_list.print_list()
                                case 'N':
                                    pos = input("Enter a position to delete value from : ")
                                    my_list.del_node(pos, d_count)
                                    print(f"{pos} element deleted")
                                    my_list.print_list()
                                case 'E':
                                    break
                                case _:
                                    print("Please Enter a Correct value Lower and upper cases both are allowed")
        #
                    case 'S':
                        sort_msg = """
A. Sort in ascending order\
D. Sort in descending order
E. Exit
"""
                        sort_choice = input(sort_msg)
                        sort_choice = sort_choice.capitalize()
                        match sort_choice:
                            case 'A':
                                print("----------Sorting List Ascending Order----------")
                                my_list.sort_list_asc(d_count)
                                print("               ---After Sorting---               ")
                                my_list.print_list()

                            case 'D':
                                print("----------Sorting List Descending Order----------")
                                my_list.sort_list_des(d_count)
                                print("               ---After Sorting---               ")
                                my_list.print_list()
                            case 'E':
                                break
                            case _:
                                print("Please Enter a Correct value Lower and upper cases both are allowed")
        #
                    case 'A':
                        data = input("Enter a value to append at last of Linked list")
                        my_list.aappend(data, d_count)
                        my_list.print_list()
                    case 'M':
                        merge_msg = """\
"Enter a new list to merge with previous list"
 Total Number you want in new list : """
                        # creating new list for merging into old list
                        d_m_count = [0]
                        d_m_total_nodes = int(input(merge_msg))
                        my_list2 = Doubly_Linked_List()

                        # taking input for linked list 2
                        my_list2.get_linklist(d_m_total_nodes, d_m_count)
                        print("Your second list is")
                        my_list2.print_list()

                        # Merging inked lists
                        print("----Merging Lists in progress-----")
                        first_node = my_list2.get_first_node()

                        # first node is first node of linked list 2
                        my_list.merge_list(first_node, s_count, d_m_count)
                        print("List after merging is : ")
                        my_list.print_list()

                    case 'T':
                        my_list.print_list()
                        edit_msg = """\
Enter the position from where you want to edit : """
                        pos = int(input(edit_msg))
                        data = input("Enter new data to place at that position")
                        my_list.del_node(pos, d_count)
                        my_list.insert_node(pos, data, d_count)
                        print("Your list is now")
                        my_list.print_list()

                    case 'E':
                        break

                    case _:
                        print("Please Enter a Correct value Lower and upper cases both are allowed")
                count_text = str(s_count).replace('[', '').replace(']', '')
                print(f"total node = {count_text}")

        case '3':
            Singly_cir_Menu = """
----------Main Menu----------
Which operation you want to perform on your List : 
-> I for Insert(Insert new element at desired position)
-> Q for search an element in List
-> D for deleting an element"""
            # creating empty list and getting data
            my_list = Singly_Cir_Linked_List()
            my_list.get_linklist(total_nodes, sc_count)
            print("Your Linked list is : \n")
            my_list.print_list(sc_count)
            print(f"Total Nodes : {sc_count[0]}")

            while True:
                print("-------------SINGLY CIRCULAR LINK LIST-------------")
                choice = input(Singly_cir_Menu)
                choice = choice.capitalize()
                match choice:
                    case 'I':

                        insert_msg = """\
----------Insertion Menu-----------
Where you want to insert the element
F. At First Press F
L. At Last Press L
N. At nth Position Press N
E. For Exit
"""
                        while True:
                            ins_choice = input(insert_msg)
                            ins_choice = ins_choice.capitalize()
                            match ins_choice:
                                case 'F':
                                    data = input("Enter the node data you want to input at First position")
                                    my_list.insert_node(1, data, sc_count)
                                    my_list.print_list(sc_count)

                                case 'L':
                                    data = input("Enter the node data you want to input at Last position")
                                    my_list.insert_node_last(data, sc_count)
                                    my_list.print_list(sc_count)

                                case 'N':
                                    pos = input("On which position you want to insert the node")
                                    data = input(f"Enter the node data you want to input at {pos} position")
                                    my_list.insert_node(pos, data, sc_count)
                                    my_list.print_list(sc_count)
                                case 'E':
                                    break

                    case 'Q':
                        search_msg = """\
        How you want to search the element
        S. Search by element(Enter a element to found its position)
        P. Search by position(Enter a position to check data on that position)
        E. Exit\n"""
                        while True:
                            search_choice = input(search_msg)
                            search_choice = search_choice.capitalize()
                            match search_choice:
                                case 'S':
                                    print("The elements in your list are")
                                    my_list.print_list(sc_count)
                                    data = input("Enter value of the element to find its position")
                                    pos = my_list.search_list_pos(data, sc_count)
                                    print(f"{data} found at position {pos}")

                                case 'P':
                                    print("The elements in your list are")
                                    my_list.print_list(sc_count)
                                    pos = input("Enter position to find data at that position : ")
                                    data = my_list.search_list_ele(pos)
                                case 'E':
                                    break
                                case _:
                                    print("Please Enter a Correct value Lower and upper cases both are allowed : ")

                    case 'D':
                        del_msg = """\
----------Deletion Menu-----------
From where you want to delete the element
F. At First Press F
L. At Last Press L
N. At nth Position Press N
E. Exit
                    """
                        while True:
                            del_choice = input(del_msg)
                            del_choice = del_choice.capitalize()
                            print("The elements in your list are")
                            my_list.print_list(sc_count)
                            match del_choice:
                                case 'F':
                                    my_list.del_node(1, sc_count)
                                    print("First element Deleted : ")
                                    my_list.print_list(sc_count)
                                case 'L':
                                    my_list.del_node_end(sc_count)
                                    print("Last element Deleted : ")
                                    my_list.print_list(sc_count)
                                case 'N':
                                    pos = input("Enter a position to delete value from : ")
                                    my_list.del_node(pos, sc_count)
                                    print(f"{pos} element deleted")
                                    my_list.print_list(sc_count)
                                case 'E':
                                    break
                                case _:
                                    print("Please Enter a Correct value Lower and upper cases both are allowed")

                    case 'E':
                        break

                    case _:
                        print("Please Enter a Correct value Lower and upper cases both are allowed")
                count_text = str(s_count).replace('[', '').replace(']', '')
                print(f"total node = {count_text}")