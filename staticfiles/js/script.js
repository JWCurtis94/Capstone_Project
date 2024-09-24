document.addEventListener('DOMContentLoaded', function() {

    const navButtons = document.querySelectorAll('nav button');

    navButtons.forEach(button => {
        button.addEventListener('click', function() {

            const url = this.getAttribute('data-url');
            window.location.href = url;
        });
    });
});
