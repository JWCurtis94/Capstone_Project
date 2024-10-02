// Wait until the DOM content is fully loaded
document.addEventListener('DOMContentLoaded', function() {

    // Select all button elements inside the <nav> tag
    const navButtons = document.querySelectorAll('nav button');

    // Iterate over each button and add a click event listener
    navButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Retrieve the URL from the 'data-url' attribute of the clicked button
            const url = this.getAttribute('data-url');
            
            // Redirect the user to the specified URL
            window.location.href = url;
        });
    });
});