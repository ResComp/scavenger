#!/bin/bash

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

text() {
    setting="$1" # "0" = bold, "1" = blue, "2" = red
    message=$2

    normal=$(tput sgr0)
    different=$(tput bold)
    if [ "$setting" = "1" ]; then
        different="${different}$(tput setaf 4)"
    elif [ "$setting" = "2" ]; then
        different="${different}$(tput setaf 1)"
    fi

    echo -e "${different}${message}${normal}"
}

announce() {
    setting="$1" # "0" = bold, "1" = blue, "2" = red
    message=$2
    
    text "$setting" "\n${message}\n"
}

### Begin Main Script ###

announce 0 "Welcome to the ResComp Scavenger Hunt!"
