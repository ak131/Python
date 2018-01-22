"""
This program read text file using "with open(file_name) as file"
"""

import sys


def main():
        
    file_name = "dummy_text2.txt"

    try:
        with open(file_name,"r") as file1:
            for line in file1:
                print(line)
    except IOError as e:
        print("There was an error reading file '{}'.".format(file_name))
        print(e.strerror)

        sys.exit()

if __name__ == "__main__":
    main()
