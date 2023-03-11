#!/bin/sh

while getopts ":f:l:" flag; do
    [[ ${OPTARG} == -* ]] && { echo "Missing argument for -${flag}" ; exit ;}
    case "${flag}" in
        f) pdf=${OPTARG};;
        l) lang=${OPTARG};;
    esac
done
if [ -z "$pdf" ]; then 
 echo "Must enter projname!"
 exit 1
fi
if [ -z "$lang" ]; then 
 
 lang="ben"
fi
echo "Parsing $pdf with lang $lang" 
for f in tiffs/$pdf-{1..1000}.png 
do 
  if test -f "$f"; then 
    echo "$f" 
    tesseract -l $lang "$f" txt/"$(basename "$f" .png)"
  fi
done