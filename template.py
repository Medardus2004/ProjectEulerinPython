from argparse import ArgumentParser

def function(n):

def main():
    parser = ArgumentParser(description= "Task x")
    parser.add_argument( "xyz", help="what is does")
    parser.add_argument( "-a", "--abc", help="Alphabet")
    args = parser.parse_args()
    print(function(int(args.xyz)))

if __name__ == "__main__":
    main() 