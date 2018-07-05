# Week 2 Git

This week we will spend time on learning and using `git`. 

## Prework

1. Complete the Basic git workflow and git branching at: https://www.codecademy.com/learn/learn-git
2. Create all new notes in another branch besides `branchalpha`, that starts from `master`
    * all commands typed into codeacademy
3. Create a mr (merge request) for your new branch into `master` and `branchalpha`

## Basic Git commands

* `git status` - check the status of changes/tracked/untracked files
* `git add` - add files/changes to be tracked and commited
    - `git add -A` - add all untracked/chagned files
* `git commit` - commit a change
    - `git commit -m "your commit message"` - leave a commit message (do this because you **always** have to leave a commit message and you then avoid leaving one in `nano` or `vim`)
    - `git commit -a` - adds all tracked file changes to be committed
    - `git commit -am "your commit message"`
* `git pull` - pull from the server
* `git push` - push to the server
* `git branch` - see what branches exist (current branch will be highlighted and marked with `*`)
* `git checkout` - checkout/change the branch
    - `git checkout -b new_branch_name` - checkout a new branch
* `git merge branch_to_merge` - merges `branch_to_merge` into current branch

#
