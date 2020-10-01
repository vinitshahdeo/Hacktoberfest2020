Maths=[]
Science=[]
English=[]
IT=[]

print("Enter Marks of 10 students for Maths subject out of 100 : ")
for i in range (11):
    Maths.append(int(input()))
print("Enter Marks of 10 students for Science subject out of 100 : ")
for i in range (11):
    Science.append(int(input()))
print("Enter Marks of 10 students for English subject out of 100 : ")
for i in range (11):
    English.append(int(input()))
print("Enter Marks of 10 students for IT subject out of 100 : ")
for i in range (11):
    IT.append(int(input()))
student=[Maths,Science,English,IT]
maximum_marks=[max(Maths),max(Science),max(English),max(IT)]
minimum_marks=[min(Maths),min(Science),min(English),min(IT)]
average_marks=[sum(Maths)/10,sum(Science)/10,sum(English)/10,sum(IT)/10]
subjects=["Maths","Science","English","IT"]
print("For maths :\n","\bmaximum marks : ",maximum_marks[0],"\n","\bMinimum marks : ",minimum_marks[0],"\n","\bAverage Marks : ",average_marks[0])
print("For Science :\n","\bmaximum marks : ",maximum_marks[1],"\n","\bMinimum marks : ",minimum_marks[1],"\n","\bAverage Marks : ",average_marks[1])
print("For English :\n","\bmaximum marks : ",maximum_marks[2],"\n","\bMinimum marks : ",minimum_marks[2],"\n","\bAverage Marks : ",average_marks[3])
print("For IT :\n","\bmaximum marks : ",maximum_marks[3],"\n","\bMinimum marks : ",minimum_marks[3],"\n","\bAverage Marks : ",average_marks[3])
print ("overall : \n","\bMaximum marks : ",max(maximum_marks),"\n","\bMinimum marks : ",min(minimum_marks),"\n","\bAverage marks : ",(sum(Maths)+sum(Science)+sum(English)+sum(IT))/4)
