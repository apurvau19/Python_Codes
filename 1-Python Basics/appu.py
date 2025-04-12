# # def bubble_sort(arr):
# #     n = len(arr)
# #     for i in range(n - 1):  
# #         for j in range(n - i - 1):  
# #             if arr[j] > arr[j + 1]:  
# #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  

                
                

# # # Example usage
# # arr = [100, 64, 34, 25, 12, 22, 11, 90]
# # bubble_sort(arr)
# # print("Sorted array:", arr)

# # n=0
# # while n<=3:

# #     sum = sum+n
# #     n=n+1
# # print(sum)
# # try:
# #     my_num = int(input("Enter my_num"))
# #     num=5
# #     def example_execeptio_hand():
# #         try:
# #             res = num/my_num
# #             print(res)
            
# #         except Exception as e:
# #             print(f"Not possible because : {e}")

# # except Exception as e:
# #     print(e) 

# # example_execeptio_hand()

# # my_list = [24,45,54,60,63,71,89,100]


# # def find_my_key_index(my_list,key):
# #     start=0
# #     end= len(my_list)-1
# #     while start <= end:
# #         mid = int((start+end)/2)
# #         if key == my_list[mid]:
# #             return mid

# #         elif key > my_list[mid]:
# #             start = mid+1
# #         else:   #this means key < my_list[mid]
# #             end =  mid-1
# #     return -1


# # result_index = find_my_key_index(my_list,54)

# # if result_index == -1 :
# #     print("key not found")
# # else:
# #     print("key found at index: ",result_index)



# # Base/Parent class
# class Person:
#     def __init__(self, name = None, age = None):
#         self.name = name
#         self.age = age
        

#     def display_info(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

#     def method1(self):
#         print("this is method1 ")



# # child/sub class
# class Student(Person):
#     def __init__(self, name, age, student_id):
#         # Call the constructor of the base class
#         super().__init__(name, age)
#         self.student_id = student_id

#     def display_student_info(self):
#         # Use method from base class
#         self.display_info()
#         print(f"Student ID: {self.student_id}")
    



# # Creating an object of Student
# student1 = Student("John", 20, "S12345")

# # Calling methods
# student1.display_student_info()
# student1.method1()







# #set directly
# # p1 = Person()
# # p1.display_info()
# # p1.name ='sourabh'
# # p1.age=28
# # p1.display_info()






# # #set through constructor

# # p2= Person('Appu',27)
# # p2.display_info()




# class Animal:
#     def speak(self):
#         print("Animal makes sound")

# class Dog(Animal):
#     def speak(self):  # Overriding the speak method
#         print("Dog barks")

# class Cat(Animal):
#     def speak(self):  # Overriding the speak method
#         print("Cat meows")

# class Fuglu(Animal):
#    pass


# animal1 = Animal()

# fuglu1 = Fuglu()
# fuglu1.speak()



# dog1 = Dog()
# dog1.speak()

# cat1 =  Cat()
# cat1.speak()

# # class have data members( variables ) and member methods (methods/functions)













class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


a = ListNode(10)
b = ListNode(20)
c = ListNode(30)
d = ListNode(40) 


a.next = b
b.next = c
c.next = d
d.next = b


def displayList(head):
    current = head
    while current!= None:
        print(current.data," --> ", end=" ")
        current = current.next


def is_there_a_cycle(head):
    current= head 
    slow=fast=current

    while fast!= None:
        slow = slow.next
        fast = fast.next.next
        if(slow==fast):
            return True
    return False

# displayList(a)

print("cycle: ",is_there_a_cycle(a))


print("Linklist")
print("Linklist")
