const editButtons = document.querySelectorAll('.editBtn');
const closeButtons = document.querySelectorAll('.closeBtn');

editButtons.forEach((button, index) => {
    button.addEventListener('click', () => {
        const dialog = button.parentNode.querySelector('dialog');
        dialog.showModal();
    });
});

closeButtons.forEach(button => {
    button.addEventListener('click', () => {
        const dialog = button.parentNode.parentNode.querySelector('dialog');
        dialog.close();
    });
});
