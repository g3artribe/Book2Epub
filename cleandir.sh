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
echo "Removing $pdf pagescans"
rm tiffs/$pdf*
echo "Removing $pdf ocrtxt"
rm txt/$pdf*
echo "Removing $pdf finalfiles"
rm Final/$pdf*