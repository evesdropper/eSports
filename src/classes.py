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
dirs = [SAVE_DIR, GROUP_DIR, HELPER_DIR, ARTICLE_DIR]

# helper group class
class Group:
    """
    init and str
    """
    members = {}

    def __init__(self, name, members = None):
        # make dirs
        for dir in dirs:
            if not os.path.exists(dir):
                os.mkdir(dir)
        # setup a name
        self.name = name 
        if members is not None:
            for helper in members:
                helper.group = self
                self.members.update({helper.id: helper})
        utils.write_object(self, GROUP_DIR)

    def print_members(self):
        helpers = ""
        for helper in self.members.values():
            helpers += (f"{helper.name} (ID: {helper.id})\n")
        return helpers
    
    def __str__(self):
        return f"{self.name}\n\nMembers:\n" + str(self.print_members())

    def __repr__(self):
        return self.name

    """
    cmd line
    """
    def make_group(name, members = None):
        return Group(name, members)

    """
    Print Weekly Stats
    """
    def display_stats(self, week, year=datetime.datetime.now().year):
        stats = f":crystals: **Payments for Week {week} | {year}** :flag_gb:\n\n" # opening line
        for helper in self.members.values():
            stats += f"<@{helper.id}> - {helper.earnings:0.2f} CRY\n" # float to 2 decimal places cause tanki
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

    def add_helper(name, id, group = None):
        return Helper(name, id, group)

    def update_group(self, group):
        # pickle.load((open(f"{GROUP_DIR}/{group}.txt"), "rb"))
        group = pickle.load(open(f"{GROUP_DIR}/{group}.txt", "rb"))
        group.members.update({self.id: self})
        utils.write_object(group, GROUP_DIR)

    """
    Earnings Methods: add earnings, reset earnings, update max earnings
    """
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

    def __init__(self, id, type, author, title=""):
        author = pickle.load(open(f"{HELPER_DIR}/{author}.txt", "rb"))
        # create date, title, author, type
        self.id = id
        self.url = "https://tankisport.com/article/{}".format(self.id) # id & url
        self.type, self.author = type, author # type & author
        self.title, self.date =  title, datetime.datetime.now().isoformat() # title and date
        # add article to author list
        self.author.articles.append(self)
        # determine how much article earns and add total to author's pay
        if self.type == "Short":
            self.earnings = 40000
        elif self.type == "Medium":
            self.earnings = 60000
        elif self.type == "Long":
            self.earnings = 80000
        self.author.add_earnings(self)
        utils.write_object(self, ARTICLE_DIR)

    def __str__(self):
        # return URL, Author, Date
        return "Link: {}\nAuthor: {}\nPublished: {}".format(self.url, self.author.name, self.date[:10])

    def __repr__(self):
        return f"article{self.id}"

    def add_article(id, type, author, title=""):
        return Article(id, type, author, title)

# clean all files
def clean_files():
    dirs = [GROUP_DIR, HELPER_DIR, ARTICLE_DIR]
    for dir in dirs:
        utils.clean_dirs(dir)
