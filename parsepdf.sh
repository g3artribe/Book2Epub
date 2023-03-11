#!/bin/sh
while getopts ":f:r:" flag; do
    [[ ${OPTARG} == -* ]] && { echo "Missing argument for -${flag}" ; exit ;}
    case "${flag}" in
        f) pdf=${OPTARG};;
        r) res=${OPTARG};;
    esac
done
if [ -z "$pdf" ]; then 
 echo "Must enter projname!"
 exit 1
fi
if [ -z "$res" ]
  then
    res=500
fi
echo "Parsing $pdf with resolution $res" 
gs  -r${res}x${res} -dNOPAUSE -sDEVICE=png16m -dBATCH -sOutputFile="tiffs/$pdf-%d.png" $pdf.pdf  -c quit 