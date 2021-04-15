import os
n1 = input("enter the file name with extension : ")
n2 = input("enter the disk in which you have to find the file in give format Name_of_Disk: ")
def find_files(filename, search_path):
   result = []
   for root, dir, files in os.walk(search_path):
      if filename in files:
         return('Yes')
      else:
         return('no')
print(find_files(n1,n2)) 