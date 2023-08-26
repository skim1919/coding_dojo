var cookieDiv = document.querySelector( ".cookie-policy" );
var temp1 = document.querySelector( "#temp1" );
var temp2 = document.querySelector( "#temp2" );
var temp3 = document.querySelector( "#temp3" );
var temp4 = document.querySelector( "#temp4" );
var temp5 = document.querySelector( "#temp5" );
var temp6 = document.querySelector( "#temp6" );
var temp7 = document.querySelector( "#temp7" );
var temp8 = document.querySelector( "#temp8" );


function loading( element ) {
    // alert("Loading weather report...");
    alert( element );
    console.log( element );
}

function accept() {
    cookieDiv.remove();
}


function convert( element ) {
    console.log( temp1.innerText );
    console.log( element.value );
    if ( element.value === "°F" ) {
        // temp1.innerText = "sarang kim";
        temp1.innerText = Math.round((temp1.innerText * 9/5) + 32)
        temp2.innerText = Math.round((temp2.innerText * 9/5) + 32)
        temp3.innerText = Math.round((temp3.innerText * 9/5) + 32)
        temp4.innerText = Math.round((temp4.innerText * 9/5) + 32)
        temp5.innerText = Math.round((temp5.innerText * 9/5) + 32)
        temp6.innerText = Math.round((temp6.innerText * 9/5) + 32)
        temp7.innerText = Math.round((temp7.innerText * 9/5) + 32)
        temp8.innerText = Math.round((temp8.innerText * 9/5) + 32)
        
        

    }
    else if ( element.value === "°C" ) {
        temp1.innerText = Math.round((temp1.innerText - 32) * 5/9)
        temp2.innerText = Math.round((temp2.innerText - 32) * 5/9)
        temp3.innerText = Math.round((temp3.innerText - 32) * 5/9)
        temp4.innerText = Math.round((temp4.innerText - 32) * 5/9)
        temp5.innerText = Math.round((temp5.innerText - 32) * 5/9)
        temp6.innerText = Math.round((temp6.innerText - 32) * 5/9)
        temp7.innerText = Math.round((temp7.innerText - 32) * 5/9)
        temp8.innerText = Math.round((temp8.innerText - 32) * 5/9)
    }
}


