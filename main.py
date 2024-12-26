import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name")

args = parser.parse_args()

def main():
    print("Hello " + args.name)

if __name__ == '__main__':
    main()