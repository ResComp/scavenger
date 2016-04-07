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

You can write a Task in any language.

A Task is any executable file in `task/`

The structure of a Task is a `setup()`, `run()`, `check_submission()`,
and `cleanup()` function.

Run your custom Task with `scavenger -t sampleTask`

Take a look at [sampleBash](task/sampleBash) and
[samplePython](task/samplePython) for examples on how
to write a task.

## Developer Tips

* Run any task with `scavenger -t TASK`
* Since vagrant mounts the host working directory at `/vagrant`, you can create
a link to it in the vagrant home directory named `scavenger` (`ln -s /vagrant
$HOME/scavenger`) and work locally (on the host machine) and only drop into
vagrant to test changes.
