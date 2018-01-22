import datetime


def main():

    # Print current date and time
    print("Date and time is: {}".format(datetime.datetime.today()))

    format = "%Y-%m-%d"

    # Print formatted date
    today = datetime.datetime.today()
    print(today.strftime(format))

    # Print formatted previous 30 days date
    previous = today - datetime.timedelta(days=30)
    print(previous.strftime(format))


if __name__ == '__main__':
    main()