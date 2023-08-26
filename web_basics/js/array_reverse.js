// Array Reverse
// Write a function that will reverse the values an array and return them.

function reverse( arr ) {
    // your code here
    var left = 0;
    var right = arr.length - 1;
    while ( left < right ) {
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
    return arr;
}


var result = reverse( ["a", "b", "c", "d", "e"] );
console.log( result ); // we expect back ["e", "d", "c", "b", "a"]
