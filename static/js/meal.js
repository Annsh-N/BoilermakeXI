function like(num) {
    var like = document.getElementById("like-" + num);
    var dislike = document.getElementById("dislike-" + num);
    if (like.classList.contains('material-icons-outlined')) {
        like.classList.remove('material-icons-outlined')
        like.classList.add('material-icons')
        dislike.classList.remove('material-icons')
        dislike.classList.add('material-icons-outlined')
    } else {
        like.classList.remove('material-icons')
        like.classList.add('material-icons-outlined')
    }
}

function dislike(num) {
    var like = document.getElementById("like-" + num)
    var dislike = document.getElementById("dislike-" + num)
    if (dislike.classList.contains('material-icons-outlined')) {
        dislike.classList.remove('material-icons-outlined')
        dislike.classList.add('material-icons')
        like.classList.remove('material-icons')
        like.classList.add('material-icons-outlined')
    } else {
        dislike.classList.remove('material-icons')
        dislike.classList.add('material-icons-outlined')
    }
}