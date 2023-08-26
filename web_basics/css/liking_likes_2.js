var count1 = 9;
var count2 = 12;
var count3 = 9;

var countElement1 = document.querySelector("#total-likes-1");
var countElement2 = document.querySelector("#total-likes-2");
var countElement3 = document.querySelector("#total-likes-3");

function ClickLike(buttonIndex) {
    if (buttonIndex === 1) {
        count1++;
        countElement1.innerText = count1 + " like(s)"
    } else if (buttonIndex === 2) {
        count2++;
        countElement2.innerText = count2 + " like(s)"
    } else if (buttonIndex === 3) {
        count3++;
        countElement3.innerText = count3 + " like(s)"

    }
}

