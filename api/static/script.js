function displayInputKlineInterval(thisTag) {
    var option = thisTag.options[thisTag.selectedIndex];

    if (option.value=='klines') {
        document.getElementById('klineparams').style.display="block";
        document.getElementById('keepGettingData').style.display="block";
    } else {
        document.getElementById('klineparams').style.display="none";
        document.getElementById('keepGettingData').style.display="none";
    }
}

//function ackDataAdded(){
//
//
//}
