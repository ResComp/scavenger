#!/bin/bash

sudo ln -sf "/vagrant" "/scavenger"
source "/scavenger/lib/libbash"

# So what do we want to teach them about?
# - XXX READING THE LOGS
# - shell tools
# - dotfiles (config files in general)
# - where to find things (/etc vs /bin vs /usr ...etc.)
# - services
# - firewall (just let them know it exists)
# - selinux (just let them know it exists)
# - how-to write shell
# - XXX READING THE LOGS

# Ideas
# - process that spawns others that print to screen, have them use ps, tr, cut,
#   and kill

newChapter() {
    title=$1

    Announce 0 "Chapter $curChapter: $title"
    curChapter=$((curChapter + 1))
    while true; do
        read -p "$(Text 0 "Do you want to skip this chapter? ")" yn
        case $yn in
            yes ) return 1;;
            no ) return 0;;
            * ) Text 2 "Please answer yes or no.\n";;
        esac
    done
}

runTasks() {
    tasks=$@

    for task in $tasks; do
        if ! runSingleTask "$task"; then
            Announce 2 "ERROR: task $task aborted"
        fi
    done
}

runSingleTask() {
    taskName=$1

    taskFile="$taskDir/$taskName"
    if [ ! -f "$taskFile" ]; then
        Text 2 "$taskFile does not exist or is not a file\n"
        return 1
    fi
    if [ ! -x "$taskFile" ]; then
        Text 2 "$taskFile is not executable\n"
        return 1
    fi

    if ! $taskFile "setup"; then
        $taskFile "cleanup"
        return 1
    fi
    if ! $taskFile "run"; then
        $taskFile "cleanup"
        return 1
    fi
    if ! $taskFile "cleanup"; then
        return 1
    fi
    return 0
}

doSetup() {
    echo -n "Initializing..."

    sudo ln -sf "$sourceDir/submit" "$binDir/submit"
    sudo rm -rf "$PipeDir"
    sudo mkdir -p -m 777 "$PipeDir"
    sudo mkfifo -m 666 $SubmitPipe

    echo "Done!"
}

### Begin Main Script ###

set -e

curChapter=0

binDir="/usr/local/bin"
sourceDir="/scavenger"
taskDir="$sourceDir/tasks"

Announce 0 "Welcome to the ResComp Scavenger Hunt!"
doSetup

if newChapter "Life in the Shell"; then
    runTasks "sampleTask"
fi

Announce 1 "You've completed the ResComp Scavenger Hunt!"
