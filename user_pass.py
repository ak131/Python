from getpass import getuser, getpass, win_getpass


def main():
    user = getuser()
    print("User is '{}'".format(user))
    passwd = getpass("Enter Password: ")
    # passwd = win_getpass("Enter Password: ")
    print("Password is '{}'".format(passwd))


if __name__ == '__main__':
    main()