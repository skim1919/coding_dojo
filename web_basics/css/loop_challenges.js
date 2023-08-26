// /*1. <Print odds 1-20> (done)
//  Using a loop write code that will console.log all of the odd values from 1 up to 20.
// 2. <Decreasing Multiples of 3> (done)
// Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0.
//  3. <Print the sequence> (done)
// Using a loop write code that will console.log the values in this sequence 4, 2.5, 1, -0.5, -2, -3.5.
// 4. <Sigma> (done)
//  Write code that will add all of the values from 1-100 onto some variable sum and at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100. We should get back 5050 at the end.
// 5. <Factorial> (done)
// Write code that will multiply all of the values from 1-12 onto some variable product and at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end./*





for ( var num = 0; num <= 20; num++ ) {
    if ( num % 2 === 1 ) {
        console.log( num );
    }
}

for ( var num = 100; num >= 0; num -= 3 ) {
    console.log( num );
}

for ( var num = 4; num >= -3.5; num -= 1.5 ) {
    console.log( num );
}

var sum = 0
for ( var i = 1; i <= 100; i++ ) {
    sum += i;

}
console.log( sum );

var sum = 1
for ( var i = 1; i <= 12; i++ ) {
    sum = sum * i;
}
console.log( sum );
