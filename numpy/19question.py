import numpy as np

#letst suppose we have student data  each student have
#columns =[Age,Math_marks, Science_marks]
data = np.array([
    [18,35,78],
    [19,92,88],
    [17,76,95],
    [18,65,70],
    [20,90,85]
])

#get the shape of the matrixs
print(data.shape)


#find ages of all students
print(data[:,0])

#find average age of students
print(data[:,0].mean())


#find heighes age  of students
print(data[:,0].max())


#get students who schore more than 80 in math

print(data[data[:,1]>80])


#increase math marks of all students by 1
data[:,1] =data[:,1] +1
print(data)

#find totla number of students whow are younger than 18
print(len(data[data[:,0]<18]))



#calculate the average marks in each subject
subjectOnly = data[:,1:]
print(subjectOnly.mean(axis=0))


 

#find  studenst who get more than or equal to 80 in both subject

print(data[(data[:,1]>=80) &(data[:,2]>=80)])


#Replace all Science marks less than80 withh 0
data[:,2] = [ 0 if el<80  else el   for el in data[:,2]  ]
print(data)





#add one columne as total marks of math and science
data = np.column_stack((data,data[:,1]+data[:,2]))
print(data)


# add one row as total sum of each column
data = np.vstack((data,data.sum(axis=0)))
print(data)



