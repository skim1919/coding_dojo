// sudo code
// write a function called fizzbuzz(done)
// write for loop starting at 1 going to 100




// For each number that is a multiple of 3, print console.log "Fizz"
// For each number that is a multiple of 5, print console.log "Buzz"
// For numbers which are a multiple of both 3 and 5, print console.log "FizzBuzz"
// All other numbers should just print normally

function fizzbuzz() {
    for ( var num = 1; num <= 100; num++ ) {
        if ( num % 15 == 0 ) {
            console.log( "FizzBuzz" );
        }
        else if ( num % 5 == 0 ) {
            console.log( "Buzz" );
        }
        else if ( num % 3 == 0 ) {
            console.log( "Fizz" );
        }
        else {
            console.log( num );
        }
    }
}
fizzbuzz();