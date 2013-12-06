# Convert a sequence of integer to a Python array
#
# Usage: sequence-to-array.sh FILE [VALUES_PER_LINE]
#
# where
#
# 1) FILE is the path to a file with data for an integer sequence
# in the following format:
# * one line per value
# * on each line, the position starting at 1,
#   followed with a space character,
#   followed with the value of the sequence at given position
#
# 2) VALUES_PER_LINE is the number of values per line,
# which defaults to 10 when omitted
#
# 3) TOTAL_VALUES is the number of values to read from the FILE,
# which defaults to the number of lines in the file

if [ -z $1 ]
then
  echo 'Usage: sequence-to-array.sh FILE [VALUES_PER_LINE] [TOTAL_VALUES]';
  exit 1;
fi

fileName=$1
valuesPerLine=${2:-10}
totalValues=$3

position=1
echo -n '['
cut -f2 --delimiter=' ' "$fileName" | while read number
do
  if [ $position -gt 1 ]
  then
    echo -n ', '
    if [ $(( $position % $valuesPerLine )) -eq 1 ]
    then
      echo # newline
    fi
  fi
  echo -n $number
  position=$(($position + 1))
  if [ -n $totalValues -a $position -gt $totalValues ]
  then
    break
  fi
done
echo ']'
