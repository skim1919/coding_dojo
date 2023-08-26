// Fibonacci Array
// Fibonacci numbers have been studied for years and appear often in nature. Write a function that will return an array of Fibonacci numbers up to a given length n. Fibonacci numbers are calculated by adding the last two values in the sequence together. So if the 4th value is 2 and the 5th value is 3 then the next value in the sequence is 5.

function fibonacciArray( n ) {
    // the [0, 1] are the starting values of the array to calculate the rest from
    if ( n <= 0 ) {
        return []
    } else if ( n === 1 ) {
        return [0]
    }
    var fibArr = [0, 1];
    while ( fibArr.length < n ) {
        var prev = fibArr[fibArr.length - 1];
        var prevprev = fibArr[fibArr.length - 2];
        fibArr.push( prev + prevprev );
        // loop 1: [0, 1, 1]
        // loop 2: [0, 1, 1, 2]
        // loop 3: [0, 1, 1, 2, 3]
        // loop 4: [0, 1, 1, 2, 3, 5]
        // loop 5: [0, 1, 1, 2, 3, 5, 8]
        // loop 6: [0, 1, 1, 2, 3, 5, 8, 13]
        // loop 7: [0, 1, 1, 2, 3, 5, 8, 13, 21]
        // loop 8: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        // loop 9: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    }
    return fibArr;
}

var result = fibonacciArray( 10 );
console.log( result ); // we expect back [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
