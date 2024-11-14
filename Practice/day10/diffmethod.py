import os

def list_files(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder not folder"
    except PermissionError:
        return None, "Permission denied"
    
def main():
    folders = input("enter the folder names ").split()

    for folder in folders:
        files, error_message = list_files(folder)
        if files :
            print("Files in --" + folder)
            for file in files:
                print(file)
        else:
            print("Error in" + folder + error_message )

if __name__ == "__main__":
    main()