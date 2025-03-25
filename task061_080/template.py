from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description= "Task x")
    parser.add_argument( "xyz", help="what is does")
    parser.add_argument( "-a", "--abc", help="Alphabet")
    args = parser.parse_args()

if __name__ == "__main__":
    main() 