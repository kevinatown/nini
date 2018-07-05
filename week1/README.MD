# Week 1 Setup and UNIX command line

This week we are going to spend a little time reacquainting with interacting with a computer through the command line.

## Prework

1. Install a text editor. Text editors are like the basic word processing programs that aare focused on writing code/markup text. They will help with syntax highlighting and some do autocomplete and are almost IDE (intergrated development enviroment). Here are some options:
  * [SublimeText](https://www.sublimetext.com/3) - I use this one
  * [BBEdit](https://www.barebones.com/products/bbedit/download.html)
  * [VSCode](https://code.visualstudio.com) - prob. one of the most popular now, and very close to an IDE
  * [Atom](https://atom.io)
2.  [Create a github account](https://github.com/). We will use this to share code. Also git (we'll cover it either week 2 or 3) is used to as a version control for code and is a **must** these days.
3.  Create a directory/folder or workspace on your computer for code to live and to work out of.
4.  Install [Homebrew](https://brew.sh) - A package manager for OSX (you might want to wait on doing this)
5.  **Let me think on this so dont just start**  Install [Anaconda](https://www.anaconda.com/download/#macos)

## Basix UNIX file system
UNIX/LINUX/Darwin (osx) file system is layed out like a tree (a single directory that has files and other directories inside of it). We'll cover the basics of it and will spend sometime poking though the system. Here are some basics:
* `/` - the root directory, i.e. the directory that containes everything
* `~` - home on osx it's `/Users/{username}`, on ubuntu (a LINUX distro) its: `/home/{username}`
* `.` - current directory
* `..` - parent directory

## Basic UNIX command line common commands
* `man` - open the manual
* `cd` - change directory
* `nano` - basic command line text editor
* `vi` | `vim` - basic command line text editor
    - `i` to enter insert mode (you will see this at the bottom left of the screen)
    - `:` used to enter commands
        - `wq` to write (save) and quit
        - `q!` to quit with out saving
* `mv` - move or rename files
* `cp` - copy files/directory
* `mkdir` - make a dirctory
* `ls` - list contents of directory
* `rm` - remove a file/directory
* `sudo` - superuser do
* `touch` - touches file, updates time stamp 

## Homework
Use these commands on the command line. Poke around your system some more.


