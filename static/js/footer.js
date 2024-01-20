var footer = document.getElementById("footer");
var form = document.getElementById("subscribe-email");
var offsetCalculator = document.getElementById("footer-offset-calculator")
fillScreenSpace();

document.body.onresize = function() {fillScreenSpace()};

function fillScreenSpace() {
  var screenSpaceOccupied = offsetCalculator.offsetTop + footer.offsetHeight;
  if (screenSpaceOccupied > window.innerHeight) {
    footer.classList.remove("footer-empty");
  } else {
    footer.classList.add("footer-empty");
  }
}

document.getElementById("footer-credit").innerHTML = '© Copyright ' + new Date().getFullYear() + ' <a class="footer-link" href="/">Campus Crunch</a>. All Rights Reserved.';
