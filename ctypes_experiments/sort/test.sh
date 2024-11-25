#!/bin/bash

testCount=$1

if [ "$testCount" == "" ]
then

    echo "usage: $0 TEST_COUNT"

    exit 1

fi

gcc -o pure_test.o pure_test.c

gcc -shared -fPIC -o sort.so pure_test.c

shuf -i 0-100000 > input.txt

function get_seconds {

    timeStr=$1

    minutes=$(( $( echo $timeStr | cut -d 'm' -f 1 ) * 60 ))

    seconds=$( echo $timeStr | cut -d 'm' -f 2 | tr ',' '.' | tr -d 's')

    seconds=$( python3 -c "print( $minutes + $seconds )" )

    echo $seconds
}

function pure_test_c {

    total=0

    for (( i = 0; i < $testCount; ++i ))
    do

        result=$( \
            ( time ./pure_test.o ) 2>&1 | \
            grep real | \
            cut -f 2 \
        )

        total=$( python3 -c "print( $total + $( get_seconds $result ) )" )

    done

    total=$( python3 -c "print( $total / $testCount )" )

    echo -e "pure_test_c\t\t$total"
}

function pure_test_py {

    total=0

    for (( i = 0; i < $testCount; ++i ))
    do

        result=$( \
            ( time ./pure_test.py ) 2>&1 | \
            grep real | \
            cut -f 2 \
        )

        total=$( python3 -c "print( $total + $( get_seconds $result ) )" )

    done

    total=$( python3 -c "print( $total / $testCount )" )

    echo -e "pure_test_py\t\t$total"
}

function ctypes_test_py {

    total=0

    for (( i = 0; i < $testCount; ++i ))
    do

        result=$( \
            ( time ./ctypes_test.py ) 2>&1 | \
            grep real | \
            cut -f 2 \
        )

        total=$( python3 -c "print( $total + $( get_seconds $result ) )" )

    done

    total=$( python3 -c "print( $total / $testCount )" )

    echo -e "ctypes_test_py\t\t$total"
}

pure_test_c

pure_test_py

ctypes_test_py

rm pure_test.o sort.so input.txt