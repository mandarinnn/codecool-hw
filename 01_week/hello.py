import sys

def main(argv):
    if len(argv) == 0:
        hello("World")
    else:
        hello(list_to_string(argv))

def hello(who):
    print("Hello " + who + "!")

def list_to_string(strings):
    result = ""
    for s in strings:
        result += s + " "
    return result.strip()

if __name__ == "__main__":
    arguments = sys.argv[1:]
    main(arguments) 
