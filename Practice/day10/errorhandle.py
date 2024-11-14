import os

folders = input("enter the folder names with spaces: ").split()

for folder in folders:
   try:
       files = os.listdir(folder)
   except FileNotFoundError:
      print("give the correct folder name -" + folder)
      continue
   except PermissionError:
      print("permission is denied for this folder")
      continue
   print("==== list of the files in the " + folder)
  
   for file in files:
     print(file)