#!/bin/bash
#====================================================================================
# Author: Mohammad Zain Abbas
# Date: 2nd Nov, 2022
#====================================================================================
# This script is used to download the kaggle data for "I am something of a painter myself"
#====================================================================================

# Enable exit on error
set -e -u -o pipefail

log () {
    echo "[[ log ]] $1"
}

error () {
    echo "[[ error ]] $1"
}

#Function that shows usage for this script
function usage()
{
cat << HEREDOC
Setup for the Deep Learning Project
Usage: 
    
    $progname [OPTION] [Value]
Options:
    -h, --help              Show usage
Examples:
    $ $progname
    ⚐ → Installs all dependencies for your Deep Learning project.
HEREDOC
}

progname=$(basename $0)
env_name='deep_learning_project'

#Get all the arguments and update accordingly
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -h|--help)
        usage
        exit 1
        ;;
        *) printf "\n$progname: invalid option → '$1'\n\n⚐ Try '$progname -h' for more information\n\n"; exit 1 ;;
    esac
    shift
done

install_brew() {
    if [ ! $(type -p brew) ]; then
        error "'brew' not found. Installing it now ..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    else
        log "'brew' found ..."
    fi
}

install_git() {
    if [ ! $(type -p git) ]; then
        error "'git' not found. Installing it now ..."
        brew install git
    else
        log "'git' found ..."
    fi
}

conda_init() {
    conda init --all || error "Unable to conda init ..."
    if [[ $SHELL == *"zsh"* ]]; then
        . ~/.zshrc
    elif [[ $SHELL == *"bash"* ]]; then
        . ~/.bashrc
    else
        error "Please restart your shell to see effects"
    fi
}

install_conda() {
    if [ ! $(type -p conda) ]; then
        error "'conda' not found. Installing it now ..."
        wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
        bash miniconda.sh -b -p $HOME/miniconda
        export PATH="$HOME/miniconda/bin:$PATH"
        conda update --yes conda
    else
        log "'conda' found ..."
    fi
}

create_conda_env() {
    conda create -n $env_name python=3 -y || error "Unable to create new env '$env_name' ..."
    conda activate $env_name &> /dev/null || echo "" > /dev/null
}

log "Starting Setup Service"

install_brew
install_git
install_conda
create_conda_env

log "All done !!"