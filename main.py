import sys

def main():
    argument = sys.argv[1:] 
    if not argument:
        print("ERROR: You must type arguments")
        return
    command = argument[0]

    if command == "add":
        def create_task (name_task):
            name_task = argument[1]
            

        
    else:
        print(f"Comando desconocido: {command}" )
if __name__ == "__main__":
    main()