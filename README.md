# ResComp Scavenger Hunt

### Preparation

Before you begin:
* Make sure you have [vagrant](https://www.vagrantup.com/) installed.

### Beginning the Hunt
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
cd ~/scavenger
./scavenger

# Happy Hunting!
```

# Contributing to the Hunt

### How to write a Task

You can write a Task in any language.

A Task is an executable file in `tasks/` that accepts 3 commands:
`setup`, `run`, and `cleanup`.

```
# For sampleTask to be a valid task, these 3 commands have to run successfully:
sampleTask setup
sampleTask run 
sampleTask cleanup

# Run sampleTask
./scavenger -t sampleTask
```

Take a look at [sampleTask](tasks/sampleTask) for an example on how
to write a task.

### Developer Tips

* Run any task with `./scavenger -t TASK`
* Since vagrant mounts the host working directory at `/vagrant`, you can create
a link to it in the vagrant home directory named `scavenger` (`ln -s /vagrant
$HOME/scavenger`) and work locally (on the host machine) and only drop into
vagrant to test changes.
