import pandas as pd
import matplotlib.pyplot as plt
from tkinter.messagebox import *
while True:
    op = int(input("To plot data of salary of employee press 1 to use start stop method : \npress 2 to use start stop step method : "))
    if op ==1:
        n1 = int(input("Enter the start"))
        n2 = int(input("Enter the stop"))
        data1 = pd.read_csv("Employee Data.csv")
        #print(data1[n1:n2])

        data = data1[n1:n2]
 
        name = data['name'].tolist()
        basic_salary = data['basic_salary'].tolist()
        net_salary = data['net_salary'].tolist()
        pf = data['pf'].tolist()
        conveyance = data['conveyance'].tolist()

        plt.plot(name,basic_salary,linewidth=3,marker='o',markersize=10,label="Basic Salary")
        plt.plot(name,net_salary,linewidth=3,marker='o',markersize=10,label="Net Salary")
        plt.plot(name,pf,linewidth=3,marker='o',markersize=10,label="Pf")
        plt.plot(name,conveyance,linewidth=3,marker='o',markersize=10,label="Conveyance")

        plt.xlabel("Name")
        plt.ylabel("Salary Amounts")
        plt.title("Employee Salary Record")

        plt.legend()
        plt.grid()
        plt.show()
        plt.close()
        import employee
    elif op == 2:
        n1 = int(input("Enter the start"))
        n2 = int(input("Enter the stop"))
        n3 = int(input("Enter the step"))
        data1 = pd.read_csv("Employee Data.csv")
        #print(data1[n1:n2:n3])

        data = data1[n1:n2:n3]

        name = data['name'].tolist()
        basic_salary = data['basic_salary'].tolist()
        net_salary = data['net_salary'].tolist()
        experience = data['experience'].tolist()
        pf = data['pf'].tolist()
        conveyance = data['conveyance'].tolist()

        plt.plot(name,basic_salary,linewidth=3,marker='o',markersize=10,label="Basic Salary")
        plt.plot(name,net_salary,linewidth=3,marker='o',markersize=10,label="Net Salary")
        plt.plot(name,pf,linewidth=3,marker='o',markersize=10,label="Pf")
        plt.plot(name,conveyance,linewidth=3,marker='o',markersize=10,label="Conveyance")


        plt.xlabel("Name")
        plt.ylabel("Salary Amounts")
        plt.title("Employee Salary Record")

        plt.legend()
        plt.grid()
        plt.show()
        plt.close()
        import employee
    else:
        break
        





