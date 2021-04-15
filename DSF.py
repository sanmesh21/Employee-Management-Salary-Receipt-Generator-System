import pandas 

data = pandas.read_csv("Employee Data.csv")
#print(data)
#print(data.shape)
while True:
    op = int(input("press 1 to find data of hr_locations :\n press 2 to find data of gender :\npress 3 to find data of age :\npress 4 to find data of status :\n press 5 to find data of experience :"))
    if op ==1:
        n = input("Enter the Hired Location : ")
        d = data[data.hr_location == n]
        print(d)
    elif op == 2:
        n = input("Enter the gender : ")
        d = data[data.gender == n]
        print(d)
    elif op == 3:
        op = int(input("press1 if you want to find particular age record: \nor\n press 2 if you want to find age in range :"))
        if op == 1:
            n = int(input("Enter the age :"))
            d = data[data.age == n ]
            print(d)
        elif op == 2:
            print("Enter the Age limits: ")
            n1 = int(input("Enter the start limit of age :"))
            n2 = int(input("Enter the end limit of age :"))

            d =  data[(data.age >= n1) & (data.age <=n2) ]
            print(d)
    elif op == 4:
        n = input("Enter the status : ")
        d = data[data.status == n]
        print(d)
    elif op == 5:
        op = int(input("press1 if you want to find particular experience record: \nor\n press 2 if you want to find experience in range :"))
        if op == 1:
            n = int(input("Enter the experience :"))
            d = data[data.experience == n]
            print(d)
        elif op == 2:
            print("Enter the experience limits: ")
            n1 = int(input("Enter the start limit of experience :"))
            n2 = int(input("Enter the end limit of experience :"))

            d =  data[(data.age >= n1) & (data.age <=n2) ]
            print(d)
    else:
        print("Invalid Choice")
        break
import employee