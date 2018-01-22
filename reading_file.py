import sys


def main():
        
    file_name = "dummy_text.txt"

    try:
        file1 = open(file_name,"r")
    except IOError as e:
        print("There was an error reading file '{}'.".format(file_name))
        print(e.strerror)

        sys.exit()

    file_text = file1.read()
    file1.close()

    print(file_text)

if __name__ == "__main__":
    main()
