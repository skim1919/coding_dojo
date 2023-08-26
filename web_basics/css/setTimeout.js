
function codeToRunLater() {
    for(var i=0; i<1111; i++) {
            console.log("running: " + i);
        }
}
setTimeout(codeToRunLater, 3000);
        // function to be called, delay in milliseconds

console.log("END");

