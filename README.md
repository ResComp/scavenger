# ResComp Scavenger Hunt

* Clone this repo
* `vagrant up`
* `vagrant ssh`
* `$ bash /vagrant/scavenger.sh`

# How to write a task

Create an executable file in `tasks/` that accepts 3 commands:
`setup`, `run`, `cleanup`.

```
# For a task "sampleTask"

$ sampleTask setup
$ sampleTask run 
$ sampleTask cleanup

# Must all be valid commands
```
