#!/bin/sh
while getopts ":f:t:" flag; do
    [[ ${OPTARG} == -* ]] && { echo "Missing argument for -${flag}" ; exit ;}
    case "${flag}" in
        f) pdf=${OPTARG};;
        t) title=${OPTARG};;
    esac
done

if [ -z "$pdf" ]; then 
 echo "Must enter projname!"
 exit 1
fi
if [ -z "$pdf" ]; then 
 echo "Using default Title"
 title=$pdf
fi
cat txt/$pdf-{1..236}.txt >Final/$pdf-bigfile.txt
pandoc Final/$pdf-bigfile.txt -o Final/$pdf.epub --metadata title="$title"
