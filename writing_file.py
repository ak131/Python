import os


def main():
    data = "This is sample data."    
    file_name = "text_file.txt"

    if os.path.exists(file_name):
        print("'{}' file is present. Opening in append mode.".format(file_name))
        mode = "a"
    else:
        mode = "w"

    with open(file_name, mode=mode) as file1:
        file1.write(data+"\n")

if __name__ == "__main__":
    main()
