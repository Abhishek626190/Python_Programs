str=["Java", "SQL","C", "Reactjs","C" ,"Javascript", "Python"]
print("Before Sorting list")
print(str)
for i in range(len(str)):
    temp=""
    for j in range(len(str)):
        if(str[i]<str[j]):
            temp=str[i]
            str[i]=str[j]
            str[j]=temp
print("After sorting list")
print(str)