import argparse


def main():    
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', required=False, help='set format of output')
    parser.parse_args()


if __name__ == "__main__":
    main()
