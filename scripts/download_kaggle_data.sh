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

Download kaggle data for the Deep Learning Project

Usage: 
    
    $progname [OPTION] [Value]

Options:

    -p, --path              Path for data to be stored. (by default uses 'data')
    -h, --help              Show usage

Examples:

    $ $progname
    ⚐ → Download kaggle data for your Deep Learning project.

HEREDOC
}

progname=$(basename $0)
data_dir="data"

#Get all the arguments and update accordingly
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -p|--path) data_dir="$2"; shift ;;
        -h|--help)
        usage
        exit 1
        ;;
        *) printf "\n$progname: invalid option → '$1'\n\n⚐ Try '$progname -h' for more information\n\n"; exit 1 ;;
    esac
    shift
done

setup_kaggle_env() {
    echo '{"username":"mohammadzainabbas","key":"648d4a46bff4f3fd9380f74378844993"}' > ~/.kaggle/kaggle.json && chmod 600 ~/.kaggle/kaggle.json
}

download_kaggle_data() {
    kaggle competitions download -c gan-getting-started -p "$data_dir" --force
}

cleanup() {
    rm -rf "$data_dir"/raw_data || echo "Unable to find '$data_dir'/raw_data directory"
    unzip -q "$data_dir/gan-getting-started.zip" "photo_jpg/*" -d "$data_dir"/raw_data -f
}

log "Starting Setup Service"

setup_kaggle_env
download_kaggle_data
cleanup

log "All done !!"
