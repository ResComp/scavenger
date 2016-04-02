# ResComp Scavenger Hunt

How to begin the hunt:

* Clone this repo
* `vagrant up`
* `vagrant ssh`
* `$ cd ~/scavenger`
* `$ ./scavenger`

# How to write a task

Create an executable file in `tasks/` that accepts 3 commands:
`setup`, `run`, `cleanup`.

You can take a look at [sampleTask](tasks/sampleTask) for an example on how
to write a task.

```
# For sampleTask to be a valid task, these 3 commands have to run successfully:

$ sampleTask setup
$ sampleTask run 
$ sampleTask cleanup
```

# Developer Tips

* Since vagrant mounts your working directory at `/vagrant`, you can create
a link to it in your home directory named `scavenger` (`ln -s /vagrant
$HOME/scavenger`) and work locally (on the host machine) and only drop into
vagrant to test your changes.
