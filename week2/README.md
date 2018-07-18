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
	- `git branch -d branch_name` - Deletes the branch specified
* `git checkout branch_name` - checkout/change the branch to `branch_name`
    - `git checkout -b new_branch_name` - checkout a new branch
* `git merge branch_to_merge` - merges `branch_to_merge` into current branch

## Basic Git Workflow

Places may differ about branch naming conventions and the *main working branch* (e.g. `master`, `develop`, or `development`), but the majority of the time the git workflow stays the same.

**Keep in mind** this is for starting work on a specific task/feature/bug fix.

1. `git checkout <main_working_branch>`
	- see the above note about the main working branch
	- you do this step to make sure you can get the most updated code
2. `git pull`
	- get the most updated code from the server on the main working branch
3. `git checkout -b <new_branch>`
	- create your branch
	- naming conventions differ, but a lot of people use `feature/branch_name` (if its a feature) and `bug/branch_name` if its a bug
	- often the branch name has the ticket/issue number in it to track
4. do the work!
5. `git add`
6. `git commit -m 'small commit messge'`
7. `git push`
	- steps 4, 5, 6 do often and repeat often. 
	- git commit is saving your work with git, so that you can go back to previous saves if need be
	- do 7 often is because you are saving your work on a remote server so if you computer dies or you dont have it or whatever your work is saved!
	- also 7 allows for other people to pull your branch, help you out, and work on the branch if need be
8. Create a merge request (MR) or pull request (PR) and have your code reviewed
	- settle conflicts [look below](Settling_conflits_locally)
9. Merge in code and start all over

### Settling conflits locally
From your working branch that has conflicts:
```bash
git pull origin master # or whatever the main working branch
# pay attenion to the console output! it will have
# CONFLICT (content): Merge conflict in ./path/to/file/withConflicts.txt
# solve all of those conflicts
git commit -am "resolved conflicts"
git push
```

conflicts in a file will look like this:
```
>>>>>>>>>>>>>>>>>>>>>> (head)
some changes I made in my branch
blah blah blah
======================
some changes made a while a go
blah
<<<<<<<<<<<<<<<<<<<<<< ( #823nu)
```
with this info choose what you want to keep and delete the rest. **Make sure to delete all:** `<<<<` && `>>>>` && `====`
