# imports
import sys
from classes import Article, Helper, Group, clean_files

# main cmdline
def cmd_input(args):
    # switch case
    command = args[0]
    match command:
        case "--help":
            print(help_text)
            return 
        # more cases
        case "makegroup":
            if len(args) < 3:
                Group.make_group(args[1])
            else:
                Group.make_group(args[1], args[2]) # currently not supported
            return
        case "addhelper":
            if len(args) < 4:
                Helper.add_helper(args[1], args[2])
            else:
                Helper.add_helper(args[1], args[2], args[3])
        case "addarticle":
            if len(args) < 4:
                Article.add_article(args[1], args[2])
            else:
                Article.add_article(args[1], args[2], args[3])
        case "clean":
            clean_files()
        # default
        case _:
            print(f"No match found for given argument. {exception_text}")
            return
    # end match

docfile = "../docs.md"
exception_text = "Try 'python esports.py --help' to search for a given command."
help_text = open("../docs.txt", "r").read()

# get args cause python really do be like that
args = sys.argv[1:]
if len(args) == 0:
    print(f"No arguments given. {exception_text}")
else:
    cmd_input(args)


