"""
Reference:
https://pymotw.com/2/getopt/
https://docs.python.org/2/library/getopt.html
https://stackoverflow.com/questions/6562616/command-line-options-and-arguments-using-getopt
https://www.tutorialspoint.com/python/python_command_line_arguments.htm
"""
import getopt
import sys


def main():
    version = '1.0'
    verbose = False
    output_filename = 'default.out'
    
    print('ARGV      :', sys.argv[1:])
    
    try:
        options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['output=', 'verbose', 'version='])
        print('OPTIONS   :', options)
    except getopt.GetoptError as e:
        print(e.msg)
        sys.exit()

    for opt, arg in options:
        if opt in ('-o', '--output'):
            output_filename = arg
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt == '--version':
            version = arg

    print('VERSION   :', version)
    print('VERBOSE   :', verbose)
    print('OUTPUT    :', output_filename)
    print('REMAINING :', remainder)

if __name__ == "__main__":
    main()