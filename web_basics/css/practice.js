function foo( a ) {
    console.log( a )
    console.log( a + 10 )
    console.log( a + 20 )
}

function bar( x ) {
    y = x * 2
    z = y * 2
    return x + y + z
}

k = bar( 10 ) + bar( 20 ) + bar( 30 )
console.log( k )