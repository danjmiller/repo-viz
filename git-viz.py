from git import *
import argparse
import os
import time
import matplotlib.pyplot as plt

def commitHourHist(repo):
    head_commit = repo.commit("master")
    all_commits = head_commit.list_traverse()
    commit_hours = []

    for c in all_commits:
        hour = time.strftime("%H",time.localtime(c.committed_date))
        commit_hours.append(int(hour))

    plt.hist(commit_hours)
    plt.xlim([0,23])
    plt.show()

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--repo", help="Path to a Git Repository (default is current directory)", default=".")
parser.add_argument("-b", "--branch", help="Branch to Start from, (default is \"master\")", default="master")
args = parser.parse_args()

if os.path.exists(args.repo):
    print "Valid Path"
else:
    print "Invalid Path"
    quit()

repo = Repo(args.repo)
commit = repo.commit(args.branch)

commitHourHist(repo)

