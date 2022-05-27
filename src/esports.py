# imports
import sys
from classes import Article, Helper, Group, clean_files

# main cmdline
def cmd_input(args):
    # switch case
    command = args[0]
    match command:
        case "--help":
            print("help")
            return 
        # initialization of groups
        case "makegroup":
            if len(args) < 3:
                Group.make_group(args[1])
            else:
                Group.make_group(args[1], args[2]) # currently not supported
            return
        case "addhelper":
            Helper.add_helper(args[1:])
        case "addarticle":
            Article.add_article(args[1:])

        # stats commands 
        case "groupstats":
            Group.print_members(args[1])
        case "helperstats":
            Helper.print_helper_stats(args[1:])
        # utils
        case "clean":
            clean_files()
        # default
        case _:
            print(f"No match found for given argument. {exception_text}")
            return
    # end match

docfile = "../docs.txt"
exception_text = "Try 'python esports.py --help' to search for a given command."
help_text = open(docfile, "r").read()

# get args cause python really do be like that
args = sys.argv[1:]
if len(args) == 0:
    print(f"No arguments given. {exception_text}")
else:
    cmd_input(args)


