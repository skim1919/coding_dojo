var count = 3;
var countElement = document.querySelector("#total-likes");



function ClickLike() {
    count++;
    countElement.innerText = count + " like(s)";
}
