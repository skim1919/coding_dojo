function hide( element ) {
    element.remove();
}

var count1 = 3;
var count2 = 5;
var count3 = 8;

var pettingElement1 = document.querySelector( "#totalPettings-1" )
var pettingElement2 = document.querySelector( "#totalPettings-2" )
var pettingElement3 = document.querySelector( "#totalPettings-3" )

function clickPetting( buttonIndex ) {
    if ( buttonIndex === 1 ) {
        count1++;
        pettingElement1.innerText = count1 + " petting(s)"
    }
    else if ( buttonIndex === 2 ) {
        count2++;
        pettingElement2.innerText = count2 + " petting(s)"
    }
    else if ( buttonIndex === 3 ) {
        count3++;
        pettingElement3.innerText = count3 + " petting(s)"
    }
}

function changingPet(element) {
    alert("You are looking for a " + element.value);
}




