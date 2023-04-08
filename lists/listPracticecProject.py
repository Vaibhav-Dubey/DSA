# a project that finds the average temperature for days entered, and then tells what is average temp and how many days the temp was more than avg temp


def findTemp(n):
    arr1=[]
    for i in range(n):
        
        arr1.append(int(input("Day {i} \' s average temperature".format(i=i+1))))
    print(arr1,n)
    averageTempe=sum(arr1)/n
    print("Average = ", averageTempe)
    count=0
    for j in range(n):
        if(arr1[j]>averageTempe):
            count+=1
    print(count, "Day(s) above average")

n=int(input("How many days temperature?"))
findTemp(n)