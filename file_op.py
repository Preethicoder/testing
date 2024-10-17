import os

"""def extract_month(filename):
    # Your code here
    if len(filename.split("_")) < 3:
           return None
    return (filename.split("_")[2]).split(".")[0]


file_list = os.listdir("invoices")
month_list = list(set(map(extract_month, file_list)))
month_list.sort()
print(month_list)"""

"""print(os.getcwd())
try:
    for mon in month_list:
        os.mkdir("invoices/" + mon)
except FileExistsError:
    pass
except FileNotFoundError:
    pass"""
def move_folder(file_name):
    if "_" in file_name:
       month = (file_name.split("_")[2]).split(".")[0]
       new_path =os.path.join(month, file_name)
       os.rename(file_name, new_path)
print(os.getcwd())
print(os.listdir("invoices"))
os.chdir("invoices")
list_files = os.listdir()
for file_name in list_files:
    move_folder(file_name)



