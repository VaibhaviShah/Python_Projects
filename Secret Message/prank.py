import os

def rename_files():
    # get file names from folder
    file_list = os.listdir(r"D:\IntelliJ Projects\Secret Message\prank")

    print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory: "+saved_path)
    os.chdir(r"D:\IntelliJ Projects\Secret Message\prank")

    for file_name in file_list:
        print("Old Name: "+file_name)
        # renaming file by removing numbers
        new_file_name = file_name.translate(file_name.maketrans('', '', '1234567890'))
        os.rename(file_name, new_file_name)
        print("New Name: "+new_file_name)

    os.chdir(saved_path)

rename_files()
