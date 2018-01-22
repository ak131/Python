def main():
    data = "This is sample data."    
    file_name = b"binary_file.bin"

    with open(file_name, "wb") as file1:
        file1.write(data+"\n")

if __name__ == "__main__":
    main()
