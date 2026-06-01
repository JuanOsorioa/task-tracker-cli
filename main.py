import sys
from tasks import add_task

def main():
    argument = sys.argv[1:]
    if not argument:
        print("ERROR: You must type arguments")
        return
    command = argument[0]
    if command == "add":
        description = " ".join(argument[1:]).strip()
        if not description:
            print("ERROR: You must provide a description for the task")
            return
        add_task(description)

if __name__ == "__main__":
    main()