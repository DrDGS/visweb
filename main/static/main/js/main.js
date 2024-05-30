function SmoothScroll(){
    var footer = document.getElementById("ftr");
    footer.scrollIntoView({behavior: "smooth"});
}

function copyPhoneNumber(){
    let elemText = "+79295852627";
    let inputElem = document.createElement('input');
    inputElem.setAttribute('value', elemText);

    document.body.appendChild(inputElem);
    inputElem.select();
    document.execCommand('copy');

    inputElem.parentNode.removeChild(inputElem);

    alert("Скопировано в буфер обмена.");
}