# ResComp Scavenger Hunt

* Clone this repo
* `vagrant up`
* `vagrant ssh`
* `$ bash /vagrant/scavenger.sh`

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
