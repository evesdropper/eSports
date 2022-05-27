from os import read
import pickle
from classes import Article, Helper, Group
import random

from utils import clean_dirs, read_object, write_object

"""
Test Sandbox for classes.py:
- Used to test features of classes.py to ensure they work as intended before release.
"""

"""
Tests
"""
# article tests
def article_stats_test(article):
    print(article)

def add_articles(num, helper):
    for i in range(num):
        Article(random.randint(1, 1000), random.choice(article_lengths), helper)

# helper tests
def helper_stats_test(helper):
    print(helper)

def check_articles(helper):
    print(helper.articles)

# group tests
def group_stats_test(group):
    print(group)
    
def group_disp_stats(group):
    print(group.display_stats(random.randint(1, 52)))
    
"""
Input
"""
test_helper = Helper("Test", 123456)
test_group = Group("testgroup", test_helper)

# test_helper2 = Helper("This should've been pickled", 1237291421, test_group)

