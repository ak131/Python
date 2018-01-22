import sys


def main():
        
    file_name = "binary_file.jpg"

    try:
        with open(file_name,"rb") as file1:
            for line in file1:
                print(line)
    except IOError as e:
        print("There was an error reading file '{}'.".format(file_name))
        print(e.strerror)

        sys.exit()

if __name__ == "__main__":
    main()
