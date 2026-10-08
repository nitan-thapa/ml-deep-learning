#list (it is mutable)
    #info =["nitan","thapa",21]
    #index, +, - 
    #get, change,  ,
    #delete (del info[1])  unlike js it remove whole memory space
    
#slicing value[start:end:step]  end index is exluded
#by default step size is 1
# info = [0,1,2,3,4,5]
    #info[0:5]  =>[0,1,2,3,4]
    #info[0:5:2]  =>[0,2,4]
    #info[:5]  =>[0,1,2,3,4]
    #info[2:]  =>[2,3,4,5]
    #info[-3:]  =>[3,4,5] by default step is 1
    #info[-1::-1]  =>[5,4,3,2,1,0]   (reverse)

#indexion in string (same as list)
#string slicing (same as list)




#replacing chunk
    # info = [0,1,2,3,4,5]
    # info[3]=333
    # info[0:3] =[111]  => wrapper must be list (not necessary to have same length)
    # info  => [111, 333, 4, 5]


#adding and removing  => all methode only change original list but does not return  (except copy)
    # l1 = [1,2,3]
    # #add element
        # l1.append(4) #[1,2,3,4]  => change original list => add element at last index
        # l1.insert(2,1)#[1,2,1,3,4]  => change original list => add element at specific index l1.insert(index,element)
    # #remove elemnet 
        # l1.pop()# [1,2,1,3]it remove last index 
        # l1.pop(1)# [1,1,3] remove element at specific index
        # l1.remove(1)# [1,3]remove first 1 element
        #pop remove by index and remove remove by value

#reverse
    #l1.reverse()

# sorting
# l2=["a","A","b","B"]
# l3= [1,10,9]
# l4=[1,"A"]
    # l2.sort()#["A","B","a","b"]
    # l2.sort(reverse=True)#["b","a","B","A"]
    # l3.sort() #[1,9,10]
    # # ##l4.sort()  this sort will not work as it is the combination of number and string
            


#split (convert string to list)
    #"nitan thapa".split(" ")  

#join (convert list to string)
    #",".join(["nitan","thapa"]


#length function 
    # len([1,2,3])


#sum function 
#   sum([1,2,3])


#max function 
#   max([1,2,3])


#min function 
#   min([1,2,3])


#list function
#generatin list from 1 to 10
    #  numList = list(range(1,11))  #11 is exclusive 


#copy  (all methode change original list but copy,split,join methode does not change original list and return new list)
# a1=[1,2,3]
    # a2=a1
    # a3=a1.copy()# called shallow copy,changin a1 will not change a3    (here copy methode retur new list)
# #    a3= a1[:]  is is same as a1.copy()
    # a1.append(4)#changin a1 will change a2
    # print(a1,a2,a3)#[1,2,3,4] [1,2,3,4] [1,2,3]

#==  (it check value and type)
    # 1==1#True
    # 1=="1"#False
    # [1,2]==[1,2]#True (unlike js it check value not reference)


#== and is     in array
#is check if memory are same or not
#== check if value are are same or not
# a1=[1,2]
# a2=[1,2]
    # print(a1==a2) #True
    # print(a1 is a2) #False

#note while creating memory if a variable is copy of another it will share mermor independed (primitive or non primitive like js) (there is no concept of primitive and non primitive)
#when we change variable directly it will create another mermoy

#question check if a given string is palindrome or not
#question chedk if two data are anagram or not

