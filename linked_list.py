class Node:
    def __init__(self,data):

        # initialize an item
        self.item = data

        # pointer to the next node
        self.ref = None

class LinkedList:
    def __init__(self):

        # the first node
        self.start_node = None

    def insert_item(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        last_item = self.start_node
        while last_item.ref is not None:
            last_item = last_item.ref
        last_item.ref = new_node

    # Function to merge two sorted linked list.
    def merge_lists(self,linked_list1_head, linked_list2_head):

        # create a temporary node and set it to NULL
        temp_var = None

        # linked_list1_head is empty then return linked_list2_head
        if linked_list1_head is None:
            return linked_list2_head

        # if linked_list2_head is empty then return linked_list1_head
        if linked_list2_head is None:
            return linked_list1_head

        # If linked_list1_head's data is smaller or
        # equal to linked_list2_head's data
        if linked_list1_head.item <= linked_list2_head.item:

            # assign temp_var to linked_list1_head data
            temp_var = linked_list1_head

            # Again check linked_list1_head's data is smaller or equal linked_list2_head's
            # data and call mergeLists function.
            temp_var.ref = self.merge_lists(linked_list1_head.ref, linked_list2_head)

        else:
            # If linked_list2_head's data is greater than or equal linked_list2_head's
            # data assign temp to linked_list2_head
            temp_var = linked_list2_head

            # Again check linked_list2_head's data is greater or equal linked_list1_head's
            # data and call mergeLists function.
            temp_var.ref = self.merge_lists(linked_list1_head, linked_list2_head.ref)

        # return the temp list.
        return temp_var

    # print the lists
    def print_lists(self):
        temp_var = self.start_node
        while(temp_var):
            print (temp_var.item),
            temp_var = temp_var.ref

def main():
    first_linked_list = LinkedList()

    first_linked_list.insert_item(2)
    first_linked_list.insert_item(4)
    first_linked_list.insert_item(6)
    first_linked_list.insert_item(8)


    second_linked_list = LinkedList()

    second_linked_list.insert_item(5)
    second_linked_list.insert_item(10)
    second_linked_list.insert_item(15)
    second_linked_list.insert_item(20)


    list3 = LinkedList()
    list3.start_node = list3.merge_lists(
        first_linked_list.start_node, second_linked_list.start_node)

    list3.print_lists()


if __name__ == '__main__':
    main()

# Then time complexity of the linked list algorithm is 0(n)(Linear)
# because the execution time will increase with increase in the number of inputs