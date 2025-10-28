try:
    file_name = input("Enter the file name: ")
    with open(file_name, "r") as file:
        content  = file.read()
        print(content)
except:
    print("File not found. Please check the file name and try again.")