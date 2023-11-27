// Color of 0s when shown on the clock
let off_color = '#000000';
// Color of 1s when shown on the clock
let on_color = '#FF0000';
// Color of the colons in the middle of the clock (will fade between black and this color and back)
let colon_color = '#FF0000';

// Array of options for preset colors dropdown
const presetColors = [
    { value: '000000,FFFFFF,FFFFFF', text: 'Classy' },
    { value: '000000,FAE500,FAE500', text: 'Radioactive' },
];

let show_current_time = false;



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



function initializeColors(new_off_color, new_on_color, new_colon_color) {
    // Set color picker initial values
    document.getElementById('offColorPicker').value = new_off_color
    document.getElementById('onColorPicker').value = new_on_color
    document.getElementById('colonColorPicker').value = new_colon_color

    // Set small hex colors
    document.getElementById('SH1').style.backgroundColor = new_colon_color
    document.getElementById('SH2').style.backgroundColor = new_colon_color

    // Set off colors
    document.getElementById('H1T2').style.borderColor = `${new_off_color} transparent`
    document.getElementById('H1T4').style.borderColor = `${new_off_color} transparent`
    document.getElementById('H1T6').style.borderColor = `${new_off_color} transparent`
    document.getElementById('H2T1').style.borderColor = `${new_off_color} transparent`
    document.getElementById('H2T3').style.borderColor = `${new_off_color} transparent`
    document.getElementById('H2T5').style.borderColor = `${new_off_color} transparent`

    // Set on colors
    document.getElementById('H1T1').style.borderColor = `${new_on_color} transparent`
    document.getElementById('H1T3').style.borderColor = `${new_on_color} transparent`
    document.getElementById('H1T5').style.borderColor = `${new_on_color} transparent`
    document.getElementById('H2T2').style.borderColor = `${new_on_color} transparent`
    document.getElementById('H2T4').style.borderColor = `${new_on_color} transparent`
    document.getElementById('H2T6').style.borderColor = `${new_on_color} transparent`
}



// Function to add options to select
function populateSelect(selectId) {
    const selectElement = document.getElementById(selectId);
    presetColors.forEach(option => {
        selectElement.add(new Option(option.text, option.value));
    });
}



function getCurrentTime() {
    return ['000111', '111100']
}


function changeCurrentTimeColors(color, oneOrZero) {
    const time_pieces = getCurrentTime()
    const hours_triangles = [
        document.getElementById('H1T6'),
        document.getElementById('H1T5'),
        document.getElementById('H1T4'),
        document.getElementById('H1T3'),
        document.getElementById('H1T2'),
        document.getElementById('H1T1')
    ]

    const minutes_triangles = [
        document.getElementById('H2T6'),
        document.getElementById('H2T5'),
        document.getElementById('H2T4'),
        document.getElementById('H2T3'),
        document.getElementById('H2T2'),
        document.getElementById('H2T1')
    ]

    Array.from(time_pieces[0]).forEach((bit, index) => {
        if (bit === oneOrZero) {
            hours_triangles[index].style.borderColor = `${color} transparent`;
        }
    });
    
    Array.from(time_pieces[1]).forEach((bit, index) => {
        if (bit === oneOrZero) {
            minutes_triangles[index].style.borderColor = `${color} transparent`
        }
    });
}


function showCurrentTime() {
    changeCurrentTimeColors(off_color, '0')
    changeCurrentTimeColors(on_color, '1')
}


function showPreviewTime() {
    initializeColors(off_color, on_color, colon_color);
}




// On page load
document.addEventListener('DOMContentLoaded', function () {
    // Open the first tab by default
    document.getElementsByClassName("tablinks")[0].click();

    // Set the color of everything
    initializeColors(off_color, on_color, colon_color);

    // Populate the preset colors dropdown with options
    populateSelect('presetColorsDropdown')

    const showCurrentTimeSlider = document.getElementById('showCurrentTimeSlider');

    showCurrentTimeSlider.addEventListener('input', function () {
        this.show_current_time = !this.show_current_time
        if (this.show_current_time) {
            showCurrentTime()
        } else {
            showPreviewTime()
        }
    })




    const offColorPicker = document.getElementById('offColorPicker');
    const onColorPicker = document.getElementById('onColorPicker');
    const colonColorPicker = document.getElementById('colonColorPicker');

    // Watch for changes to the offColorPicker
    offColorPicker.addEventListener('input', function () {
        const color = offColorPicker.value;
        off_color = color;

        if (this.show_current_time) {
            changeCurrentTimeOffColors(color)
        } else {
            document.getElementById('H1T2').style.borderColor = `${color} transparent`
            document.getElementById('H1T4').style.borderColor = `${color} transparent`
            document.getElementById('H1T6').style.borderColor = `${color} transparent`
            document.getElementById('H2T1').style.borderColor = `${color} transparent`
            document.getElementById('H2T3').style.borderColor = `${color} transparent`
            document.getElementById('H2T5').style.borderColor = `${color} transparent`
        }

    });

    // Watch for changes to the onColorPicker
    onColorPicker.addEventListener('input', function () {
        const color = onColorPicker.value;
        on_color = color;

        if (this.show_current_time) {
            changeCurrentTimeOnColors()
        } else {
            document.getElementById('H1T1').style.borderColor = `${color} transparent`
            document.getElementById('H1T3').style.borderColor = `${color} transparent`
            document.getElementById('H1T5').style.borderColor = `${color} transparent`
            document.getElementById('H2T2').style.borderColor = `${color} transparent`
            document.getElementById('H2T4').style.borderColor = `${color} transparent`
            document.getElementById('H2T6').style.borderColor = `${color} transparent`
        }

    });

    // Watch for changes to the colonColorPicker
    colonColorPicker.addEventListener('input', function () {
        const color = colonColorPicker.value;
        colon_color = color;

        document.getElementById('SH1').style.backgroundColor = color
        document.getElementById('SH2').style.backgroundColor = color
    });
});