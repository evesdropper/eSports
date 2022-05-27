# imports
import datetime
import os, utils
import pickle

# create save dir
CWD = os.getcwd()
SAVE_DIR = utils.join(CWD, "saved")
# subdirectories
GROUP_DIR = utils.join(SAVE_DIR, "groups")
HELPER_DIR = utils.join(SAVE_DIR, "helpers")
ARTICLE_DIR = utils.join(SAVE_DIR, "articles")
ALL_DIRS = [SAVE_DIR, GROUP_DIR, HELPER_DIR, ARTICLE_DIR]

# set values
PROOFREADER_EARNINGS = 20000

# helper group class
class Group:
    """
    init and str
    """
    members = {}

    def __init__(self, name, members = None):
        # make dirs
        for dir in ALL_DIRS:
            if not os.path.exists(dir):
                os.mkdir(dir)
        # setup a name
        self.name = name 
        if members is not None:
            for helper in members:
                helper.group = self
                self.members.update({helper.id: helper})
        utils.write_object(self, GROUP_DIR)
    
    def __str__(self):
        return f"{self.name}\n\nMembers:\n" + str(self.print_members())

    def __repr__(self):
        return self.name

    """
    cmd line
    """
    def make_group(name, members = None):
        return Group(name, members)

    def print_members(group):
        group = pickle.load(open(f"{GROUP_DIR}/{group}.txt", "rb"))
        helpers = ""
        for helper in group.members.values():
            helpers += (f"{helper.name} (ID: {helper.id})\n")
        print(helpers)

    """
    Print Weekly Stats
    """
    def display_stats(self, week, year=datetime.datetime.now().year):
        stats = f":crystals: **Payments for Week {week} | {year}** :flag_gb:\n\n" # opening line
        for helper in self.members.values():
            stats += f"<@{helper.id}> - {helper.earnings:0.2f} CRY\n" # float to 2 decimal places cause tanki
            helper.update_earnings()
        return stats

    """
    Retiring Members
    """
    def retire_member(self, name, retired):
        pass


# helper class
class Helper:
    """
    init and str methods
    """
    group = None

    def __init__(self, name, id, group=None): # nickname, discord id
        self.name = name
        self.id = id # basic attributes
        self.articles = [] # articles
        # add start time
        self.join_date = datetime.datetime.now().isoformat()
        if group is not None:
            self.update_group(group)
        # add earnings
        self.total_learnings = 0
        self.max_earnings = 0
        self.earnings = 0
        utils.write_object(self, HELPER_DIR)
    
    def __str__(self):
        # return Name, ID, Group, Date Joined, Total Earnings, Max Earnings
        return """Basic Info\n\nName: {}\nID: {}\nGroup: {}\nDate Joined: {}
        \nStats\n\nArticles Written: {}\nTotal Earnings: {} crystals\nMax Earnings: {} crystals""".format(self.name, self.id, self.group.name, self.join_date[:10], len(self.articles), self.total_learnings, self.max_earnings)

    def __repr__(self):
        return self.name

    def add_helper(args):
        name, id = args[0], args[1]
        if len(args) == 2:
            group = None
        else:
            group = args[2]
        return Helper(name, id, group)

    def update_group(self, group):
        # pickle.load((open(f"{GROUP_DIR}/{group}.txt"), "rb"))
        group = pickle.load(open(f"{GROUP_DIR}/{group}.txt", "rb"))
        group.members.update({self.id: self})
        utils.write_object(group, GROUP_DIR)

    def print_helper_stats(args):
        # print helper stats
        name = args[0]
        self = pickle.load(open(f"{HELPER_DIR}/{name}.txt", "rb"))
        print(self.group)

    """
    Earnings Methods: add earnings, reset earnings, update max earnings
    """
    def add_other_earnings(self, earnings):
        # add earnings
        utils.read_object(self, HELPER_DIR)
        self.earnings += earnings
        self.total_learnings += earnings
        utils.write_object(self, HELPER_DIR)

    def add_earnings(self, article):
        # add earnings
        utils.read_object(self, HELPER_DIR)
        self.earnings += article.earnings
        self.total_learnings += article.earnings
        utils.write_object(self, HELPER_DIR)

    def reset_earnings(self):
        # reset earnings
        self.earnings = 0
        utils.write_object(self, HELPER_DIR)

    def update_earnings(self):
        utils.read_object(self, HELPER_DIR)
        if self.earnings > self.max_earnings:
            self.max_earnings = self.earnings
        self.reset_earnings()
        

# article class
class Article:
    """
    Article Types:
    Short - 40000 crystals
    Medium - 60000 crystals
    Long - 80000 crystals
    """
    earnings = 0

    def __init__(self, id, type, author, proofreader, title=""):
        author = pickle.load(open(f"{HELPER_DIR}/{author}.txt", "rb"))
        proofreader = pickle.load(open(f"{HELPER_DIR}/{proofreader}.txt", "rb"))
        # create date, title, author, type
        self.id = id
        self.url = "https://tankisport.com/article/{}".format(self.id) # id & url
        self.type, self.author, self.proofreader = type, author, proofreader # type & author
        self.title, self.date = title, datetime.datetime.now().isoformat() # title and date
        # add article to author list
        self.author.articles.append(self)
        # determine how much article earns and add total to author's pay
        self.add_article_earnings()
        utils.write_object(self, ARTICLE_DIR)

    def __str__(self):
        # return URL, Author, Date
        return "Link: {}\nAuthor: {}\nPublished: {}".format(self.url, self.author.name, self.date[:10])

    def __repr__(self):
        return f"article{self.id}"

    def add_article_earnings(self):
        if self.type == "Medium":
            self.earnings = 60000
        elif self.type == "Long":
            self.earnings = 80000
        else:
            self.earnings = 40000
        self.author.add_earnings(self)
        self.proofreader.add_other_earnings(PROOFREADER_EARNINGS)

    def add_article(args):
        if len(args) == 4:
            title = None
        else:
            title = args[4]
        return Article(args[0], args[1], args[2], args[3], title) # id, type, author, title
    

# clean all files
def clean_files():
    dirs = [GROUP_DIR, HELPER_DIR, ARTICLE_DIR]
    for dir in dirs:
        utils.clean_dirs(dir)
