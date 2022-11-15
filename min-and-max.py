list = [-2,-3,-4,-7]
list1 = [-3,-4,-5,-6]
list2 = [0,0,0,0]
 
if len(list) == 0 or len(list1) == 0 or len(list2) == 0:
    print("[]") 
    print("NONE")
else:
    print("The largest and smallest number are: " ,max(list) , min(list))
    print("The largest and smallest number are: " ,max(list1) , min(list1))
    print("The largest and smallest number are: " ,max(list2) , min(list2))
