function changeIconLike() {
    var iconElementLike = document.getElementById('iconLike');
    var iconElementDislike = document.getElementById('iconDislike');

    // Check the current icon class
    if (iconElementLike.classList.contains('bi-hand-thumbs-up')) {
        // Change to another icon when the current one is 'fa-star'
        iconElementLike.classList.remove('bi-hand-thumbs-up');
        iconElementLike.classList.add('bi-hand-thumbs-up-fill');
        if (iconElementDislike.classList.contains('bi-hand-thumbs-down-fill')) {
            // Change to another icon when the current one is 'fa-star'
            iconElementDislike.classList.remove('bi-hand-thumbs-down-fill');
            iconElementDislike.classList.add('bi-hand-thumbs-down');
        }
    } else {
        // Change back to the original icon when the current one is 'fa-heart'
        iconElementLike.classList.remove('bi-hand-thumbs-up-fill');
        iconElementLike.classList.add('bi-hand-thumbs-up');
    }
}
function changeIconDislike() {
    var iconElementDislike = document.getElementById('iconDislike');
    var iconElementLike = document.getElementById('iconLike');

    // Check the current icon class
    if (iconElementDislike.classList.contains('bi-hand-thumbs-down')) {
        // Change to another icon when the current one is 'fa-star'
        iconElementDislike.classList.remove('bi-hand-thumbs-down');
        iconElementDislike.classList.add('bi-hand-thumbs-down-fill');
        if (iconElementLike.classList.contains('bi-hand-thumbs-up-fill')) {
            // Change to another icon when the current one is 'fa-star'
            iconElementLike.classList.remove('bi-hand-thumbs-up-fill');
            iconElementLike.classList.add('bi-hand-thumbs-up');
        }
    } else {
        // Change back to the original icon when the current one is 'fa-heart'
        iconElementDislike.classList.remove('bi-hand-thumbs-down-fill');
        iconElementDislike.classList.add('bi-hand-thumbs-down');
    }
}
