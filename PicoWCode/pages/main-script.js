/* Color of 0s when shown on the clock */
let off_color = '#000000';
/* Color of 1s when shown on the clock */
let on_color = '#000000';
/* Color of the colons in the middle of the clock (will fade between black to this color and back) */
let colon_color = '#000000';
let time = '04:16';
let username = '';
let password = '';


/* Array of options for preset colors dropdown */
const presetColors = [
    { value: '#000000,#FFFFFF,#FFFFFF', text: 'Classy' },
    { value: '#000000,#FAE500,#FAE500', text: 'Radioactive' },
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


/* Set local variables to values from the server's config file */
function initializeConfigVariables() {
    time = document.getElementById("time_variable").className;
    off_color = document.getElementById("off_color_variable").className;
    on_color = document.getElementById("on_color_variable").className;
    colon_color = document.getElementById("colon_color_variable").className;
    username = document.getElementById("username_variable").className;
    password = document.getElementById("password_variable").className;
}

/* Set small hex colors */
function setColonColor(new_colon_color) {
    document.getElementById('SH1').style.backgroundColor = new_colon_color;
    document.getElementById('SH2').style.backgroundColor = new_colon_color;
}

/* Set color picker initial values */
function setPickerColors(new_off_color, new_on_color, new_colon_color) {
    document.getElementById('offColorPicker').value = new_off_color;
    document.getElementById('onColorPicker').value = new_on_color;
    document.getElementById('colonColorPicker').value = new_colon_color;
}

/* Set global color variables */
function setColorVariables(new_off_color, new_on_color, new_colon_color) {
    off_color = new_off_color;
    on_color = new_on_color;
    colon_color = new_colon_color;
}


function initializeColors(new_off_color, new_on_color, new_colon_color) {
    /* Set color picker initial values */
    setPickerColors(new_off_color, new_on_color, new_colon_color);

    /* Set off colors */
    document.getElementById('H1T2').style.borderColor = `${new_off_color} transparent`;
    document.getElementById('H1T4').style.borderColor = `${new_off_color} transparent`;
    document.getElementById('H1T6').style.borderColor = `${new_off_color} transparent`;
    document.getElementById('H2T1').style.borderColor = `${new_off_color} transparent`;
    document.getElementById('H2T3').style.borderColor = `${new_off_color} transparent`;
    document.getElementById('H2T5').style.borderColor = `${new_off_color} transparent`;

    /* Set on colors */
    document.getElementById('H1T1').style.borderColor = `${new_on_color} transparent`;
    document.getElementById('H1T3').style.borderColor = `${new_on_color} transparent`;
    document.getElementById('H1T5').style.borderColor = `${new_on_color} transparent`;
    document.getElementById('H2T2').style.borderColor = `${new_on_color} transparent`;
    document.getElementById('H2T4').style.borderColor = `${new_on_color} transparent`;
    document.getElementById('H2T6').style.borderColor = `${new_on_color} transparent`;

    /* Set small hex colors */
    setColonColor(new_colon_color);
}



/* Function to add options to select */
function populateSelect(selectId) {
    const selectElement = document.getElementById(selectId);
    presetColors.forEach(option => {
        selectElement.add(new Option(option.text, option.value));
    });
}


function getCurrentTimeInBinary() {
    const time_pieces = time.split(':');

    return [Number(time_pieces[0]).toString(2).padStart(6, '0'), Number(time_pieces[1]).toString(2).padStart(6, '0')];
}


function changeCurrentTimeColors(color, oneOrZero) {
    const time_pieces = getCurrentTimeInBinary();
    const hours_triangles = [
        document.getElementById('H1T6'),
        document.getElementById('H1T5'),
        document.getElementById('H1T4'),
        document.getElementById('H1T3'),
        document.getElementById('H1T2'),
        document.getElementById('H1T1')
    ];

    const minutes_triangles = [
        document.getElementById('H2T6'),
        document.getElementById('H2T5'),
        document.getElementById('H2T4'),
        document.getElementById('H2T3'),
        document.getElementById('H2T2'),
        document.getElementById('H2T1')
    ];

    Array.from(time_pieces[0]).forEach((bit, index) => {
        if (bit === oneOrZero) {
            hours_triangles[index].style.borderColor = `${color} transparent`;
        }
    });
    
    Array.from(time_pieces[1]).forEach((bit, index) => {
        if (bit === oneOrZero) {
            minutes_triangles[index].style.borderColor = `${color} transparent`;
        }
    });
}


function showCurrentTime(new_off_color, new_on_color, new_colon_color) {
    changeCurrentTimeColors(new_off_color, '0');
    changeCurrentTimeColors(new_on_color, '1');
    setColonColor(new_colon_color);
    setPickerColors(new_off_color, new_on_color, new_colon_color);
}


function showPreviewTime() {
    initializeColors(off_color, on_color, colon_color);
}


function getColorsFromPreset(preset_value) {
    const colors = preset_value.split(',');
    return {"off_color": colors[0], "on_color": colors[1], "colon_color": colors[2]};
}




/* On page load */
document.addEventListener('DOMContentLoaded', function () {
    /* Open the first tab by default */
    document.getElementsByClassName("tablinks")[0].click();

    /* Grab variables from HTML and set them here */
    initializeConfigVariables();

    /* Set the color of everything to the first preset */
    const preset_colors = getColorsFromPreset(presetColors[0].value);
    setColorVariables(preset_colors['off_color'], preset_colors['on_color'], preset_colors['colon_color']);
    initializeColors(preset_colors['off_color'], preset_colors['on_color'], preset_colors['colon_color']);

    /* Populate the preset colors dropdown with options */
    populateSelect('presetColorsDropdown');

    
    /* Watch for changes to the showCurrentTime slider */
    const showCurrentTimeSlider = document.getElementById('showCurrentTimeSlider');
    showCurrentTimeSlider.addEventListener('input', function () {
        show_current_time = !show_current_time;
        if (show_current_time) {
            showCurrentTime(off_color, on_color, colon_color);
        } else {
            showPreviewTime();
        }
    });


    /* Watch for changes to the presetColorsDropdown */
    const presetColorsDropdown = document.getElementById('presetColorsDropdown');
    presetColorsDropdown.addEventListener('input', function () {
        /* Get colors from the preset value */
        const colors = getColorsFromPreset(presetColorsDropdown.value);
        /* Set global color variables to the new colors */
        setColorVariables(colors['off_color'], colors['on_color'], colors['colon_color']);

        if (show_current_time) {
            showCurrentTime(colors['off_color'], colors['on_color'], colors['colon_color']);
        } else {
            initializeColors(colors['off_color'], colors['on_color'], colors['colon_color']);
        }
    });



    const offColorPicker = document.getElementById('offColorPicker');
    const onColorPicker = document.getElementById('onColorPicker');
    const colonColorPicker = document.getElementById('colonColorPicker');

    /* Watch for changes to the offColorPicker */
    offColorPicker.addEventListener('input', function () {
        const color = offColorPicker.value;
        off_color = color;

        if (show_current_time) {
            changeCurrentTimeColors(color, '0');
        } else {
            showPreviewTime();
            /* document.getElementById('H1T2').style.borderColor = `${color} transparent` */
            /* document.getElementById('H1T4').style.borderColor = `${color} transparent` */
            /* document.getElementById('H1T6').style.borderColor = `${color} transparent` */
            /* document.getElementById('H2T1').style.borderColor = `${color} transparent` */
            /* document.getElementById('H2T3').style.borderColor = `${color} transparent` */
            /* document.getElementById('H2T5').style.borderColor = `${color} transparent` */
        }

    });

    /* Watch for changes to the onColorPicker */
    onColorPicker.addEventListener('input', function () {
        const color = onColorPicker.value;
        on_color = color;

        if (show_current_time) {
            changeCurrentTimeColors(color, '1');
        } else {
            showPreviewTime();
            /* document.getElementById('H1T1').style.borderColor = `${color} transparent` */
            /* document.getElementById('H1T3').style.borderColor = `${color} transparent` */
            /* document.getElementById('H1T5').style.borderColor = `${color} transparent` */
            /* document.getElementById('H2T2').style.borderColor = `${color} transparent` */
            /* document.getElementById('H2T4').style.borderColor = `${color} transparent` */
            /* document.getElementById('H2T6').style.borderColor = `${color} transparent` */
        }

    });

    /* Watch for changes to the colonColorPicker */
    colonColorPicker.addEventListener('input', function () {
        const color = colonColorPicker.value;
        colon_color = color;

        setColonColor(color);
    });
});