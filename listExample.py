#!/usr/bin/env python3

mylist = [1, 2, 3]
print(mylist[0])

alpha_list = list((1, 2, 3))
alpha_list.append('Ibrahim')
print(alpha_list)

#beta_list =["apple", "banana", "orange"]
#beta_list.insert("2 grape")
#print(beta_list)

print("How to remove from a List")
betalist = ["Zainab", "Muhammad", "Haidar"]
betalist.remove("Zainab")
print(betalist)


print("How to remove the specified or last element from a List")
betalist = ["Zainab", "Muhammad", "Haidar"]
betalist.pop(2)
print(betalist)


print("How to remove the specifies or last element from a List")
betalist = ["Zainab", "Muhammad", "Haidar"] 
del betalist[1]
print(betalist)


print("How to add two or more List together")
mylist = [1, 2, 3]
mylist2 = ["a", "b", "c"]
combolist = mylist + mylist2
print(combolist)


print("Nested List")
mynestedlist = [mylist, mylist2]
print(mynestedlist)


print("slice a List")
alphaList = [34, 12, 54, 62, 13, 77]
print(alphaList[0:4])


print("change item value on the List")
betalist = ["apple", "mango", "fruit"]
betalist[1] = "Banana"
print(betalist)


print("copy a List")
beta_list = ["apple", "banana", "orange"]
beta_list = beta_list.copy()
print(beta_list)


print("copying list with the list")
beta_list = ["apple", "banana", "orange"]
beta_list = list (beta_list)
print(beta_list)


number_list = [x ** 2 for x in range(10) if x % 2 == 0]
print(number_list)

    print('Date and time example')
      now = datetime.now()
        then = datetime(2016, 5, 23)
        delta = now - then
        print(delta.days)
        print(delta.seconds)
        print()
