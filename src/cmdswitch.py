# imports
import sys

def cmd_input(args):
    # switch case
    command = args[0]
    match command:
        case "help":
            print(help_text)
            return
        case _:
            print("No match found for given argument.")
            return
    # end match
help_text = "Read the docs: (Docs)"

# get args cause python really do be like that
args = sys.argv[1:]
if len(args) == 0:
    print("No arguments given.")
else:
    cmd_input(args)


