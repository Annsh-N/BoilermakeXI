var iconElement = document.getElementById('icon');

// Check the current icon class
if (iconElement.classList.contains('fa-star')) {
    // Change to another icon when the current one is 'fa-star'
    iconElement.classList.remove('fa-star');
    iconElement.classList.add('fa-heart');
}