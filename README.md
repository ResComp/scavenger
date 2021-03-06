# ResComp Scavenger Hunt

Everyone endorses "learning by doing", but then just tells new users to go
read the manpages. *Wait what?!*

Instead, we present `scavenger`: an interactive exploration of UNIX.

**[Spoiler]** You still have to read manpages. And *logs*.
*Please read the logs.*


<br /><br />


# Preparation

Before you begin:
* Make sure you have [vagrant](https://www.vagrantup.com/) installed.

# Beginning the Hunt
```
# We'll install it to your home directory
cd ~

# Clone this repository
git clone https://github.com/ResComp/scavenger

# Navigate to the repository you just cloned
cd ~/scavenger

# Start vagrant, this will take a while as the first run will download alot
vagrant up

# Enter vagrant
vagrant ssh

# Now that we're inside vagrant all we gotta do is run it!
scavenger

# Happy Hunting!
```

# Contributing to the Hunt

## How to write a Task

A Task is any executable file in `task/`, *but python is preferred*.

The structure of a Task is a `setup`, `run`, `check_submission`,
and `cleanup` function.

Run your custom Task with `scavenger -t sampleTask`

Take a look at [samplePython](task/samplePython) and
[sampleBash](task/sampleBash) for examples on how
to write a task.

## Developer Tips

* Run any task with `scavenger -t TASK`
* Vagrant mounts the directory with the file named `Vagrantfile` at
`/vagrant/` within the vagrant virtual machine. Inside vagrant,
remove the default checked out repository
(`rm -rf ~/scavenger`) and create a symbolic link to
it in the vagrant home directory named `scavenger` (`ln -s /vagrant
$HOME/scavenger`). Now changes made on the host machine (locally on your
computer) will show up inside vagrant.

# FAQ

**Q:** My Task seems to work properly but I'm getting a `Task Aborted` message.
What's going on?

**A:** A Task must exit cleanly (an exit code of `0`). Especially in the 
`cleanup`, you should be performing checks before every operation.
For example: before removing a file, check that the file exists. If this is
Bash, then you should have `set -e` in your Task, which makes it so
that *any* failure will cause an immediate exit with a non-zero exit code.
