let config_username = '~~username~~';
let config_password = '~~password~~';


/* Set local variables to values from the server's config file */
function initializeConfigVariables() {
    username_element = document.getElementById("username_variable")
    password_element = document.getElementById("password_variable")
    config_username = username_element.className;
    config_password = password_element.className;

    /* After we've read in the values, remove them from the HTML entirely */
    username_element.remove()
    password_element.remove()
}


/* On page load */
document.addEventListener('DOMContentLoaded', function () {
    /* Grab variables from HTML and set them here */
    initializeConfigVariables();

    /* Select the form */
    const form = document.querySelector('form');

    /* Add an event listener for the 'submit' event */
    form.addEventListener('submit', function(e) {
        /* Prevent the default form submission behavior */
        e.preventDefault();
        
        const username = form.querySelector('[name="username"]').value;
        const password = form.querySelector('[name="password"]').value;

        /* If the username and password match what's in the config file, submit the form */
        if (username === config_username && password === config_password) {
            errorMessage.style.display = 'none';
            form.submit()
        } else {
            errorMessage.style.display = 'block';
        }
    });
});