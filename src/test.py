from classes import Article, Helper, Group
import random

"""
Test Sandbox for classes.py
"""
test_helper = Helper("Person_Random", 462677714109857792)
test_helper_2 = Helper("Apost", 479721534550704129)

test_helpers = [test_helper, test_helper_2]
test_group = Group("Test Group", test_helpers)

test_article = Article(891, "Short", test_helper)
test_article_2 = Article(892, "Short", test_helper_2)

article_lengths = ["Short", "Medium", "Long"]
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

"""
Input
"""
# add_articles(10, test_helper)
# article_stats_test(test_article)
# helper_stats_test(test_helper)
# check_articles(test_helper)
group_stats_test(test_group)