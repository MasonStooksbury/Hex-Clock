const off_color = '#000000';
const on_color = '#FF0000';
const colon_color = '#00FF00';

function openTab(evt, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

function initializeColors() {
    // Set color picker initial values
    document.getElementById('offColorPicker').value = off_color
    document.getElementById('onColorPicker').value = on_color
    document.getElementById('colonColorPicker').value = colon_color

    // Set small hex colors
    document.getElementById('SH1').style.backgroundColor = colon_color
    document.getElementById('SH2').style.backgroundColor = colon_color


    // Set off colors
    document.getElementById('H1T2').style.borderColor = `${off_color} transparent`
    document.getElementById('H1T4').style.borderColor = `${off_color} transparent`
    document.getElementById('H1T6').style.borderColor = `${off_color} transparent`
    document.getElementById('H2T1').style.borderColor = `${off_color} transparent`
    document.getElementById('H2T3').style.borderColor = `${off_color} transparent`
    document.getElementById('H2T5').style.borderColor = `${off_color} transparent`

    // Set on colors
    document.getElementById('H1T1').style.borderColor = `${on_color} transparent`
    document.getElementById('H1T3').style.borderColor = `${on_color} transparent`
    document.getElementById('H1T5').style.borderColor = `${on_color} transparent`
    document.getElementById('H2T2').style.borderColor = `${on_color} transparent`
    document.getElementById('H2T4').style.borderColor = `${on_color} transparent`
    document.getElementById('H2T6').style.borderColor = `${on_color} transparent`
}


document.addEventListener('DOMContentLoaded', function () {
    const offColorPicker = document.getElementById('offColorPicker');
    const onColorPicker = document.getElementById('onColorPicker');
    const colonColorPicker = document.getElementById('colonColorPicker');

    initializeColors()

    offColorPicker.addEventListener('input', function () {
        const color = offColorPicker.value;

        document.getElementById('H1T2').style.borderColor = `${color} transparent`
        document.getElementById('H1T4').style.borderColor = `${color} transparent`
        document.getElementById('H1T6').style.borderColor = `${color} transparent`
        document.getElementById('H2T1').style.borderColor = `${color} transparent`
        document.getElementById('H2T3').style.borderColor = `${color} transparent`
        document.getElementById('H2T5').style.borderColor = `${color} transparent`
    });

    onColorPicker.addEventListener('input', function () {
        const color = onColorPicker.value;

        document.getElementById('H1T1').style.borderColor = `${color} transparent`
        document.getElementById('H1T3').style.borderColor = `${color} transparent`
        document.getElementById('H1T5').style.borderColor = `${color} transparent`
        document.getElementById('H2T2').style.borderColor = `${color} transparent`
        document.getElementById('H2T4').style.borderColor = `${color} transparent`
        document.getElementById('H2T6').style.borderColor = `${color} transparent`
    });

    colonColorPicker.addEventListener('input', function () {
        const color = colonColorPicker.value;

        document.getElementById('SH1').style.backgroundColor = color
        document.getElementById('SH2').style.backgroundColor = color
    });
});