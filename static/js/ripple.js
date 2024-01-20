var rippleDarkBackgrounds = []
var rippleWhiteBackgrounds = []
var rippleLightBackgrounds = []
var rippleYellowBackgrounds = []
var rippleBrandBackgrounds = []
var rippleMediumDarkBackgrounds = []
var rippleWideDarkBackgrounds = []
var rippleWideLightBackgrounds = []
var rippleDarkButtons = document.getElementsByClassName("ripple-dark")
var rippleWhiteButtons = document.getElementsByClassName("ripple-white")
var rippleLightButtons = document.getElementsByClassName("ripple-light")
var rippleYellowButtons = document.getElementsByClassName("ripple-yellow")
var rippleBrandButtons = document.getElementsByClassName("ripple-brand")
var rippleMediumDarkButtons = document.getElementsByClassName("ripple-medium-dark")
var rippleWideDarkButtons = document.getElementsByClassName("ripple-wide-dark")
var rippleWideLightButtons = document.getElementsByClassName("ripple-wide-light")


// FIXED //


for (var num = 0; num < rippleWhiteButtons.length; num++) {
  rippleWhiteButtons[num].setAttribute("data-identifier", num)
  rippleWhiteButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft
    var mouseY = event.clientY - this.offsetTop
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-white-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleWhiteBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(35)"
    }, 10);
  }

  rippleWhiteButtons[num].onmouseup = function() {
    element = rippleWhiteBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleWhiteButtons[num].onmouseleave = function() {
    if (typeof element !== 'undefined') {
      element = rippleWhiteBackgrounds[parseInt(this.getAttribute("data-identifier"))]
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// LIGHT //


for (var num = 0; num < rippleLightButtons.length; num++) {
  rippleLightButtons[num].setAttribute("data-identifier", num)
  rippleLightButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft + window.pageXOffset
    var mouseY = event.clientY - this.offsetTop + window.pageYOffset
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-light-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleLightBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(35)"
    }, 10);
  }

  rippleLightButtons[num].onmouseup = function() {
    element = rippleLightBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleLightButtons[num].onmouseleave = function() {
    if (typeof element !== 'undefined') {
      element = rippleLightBackgrounds[parseInt(this.getAttribute("data-identifier"))]
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// DARK //


for (var num = 0; num < rippleDarkButtons.length; num++) {
  rippleDarkButtons[num].setAttribute("data-identifier", num)
  rippleDarkButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft + window.pageXOffset
    var mouseY = event.clientY - this.offsetTop + window.pageYOffset
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-dark-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(35)"
    }, 10);
  }

  rippleDarkButtons[num].onmouseup = function() {
    element = rippleDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleDarkButtons[num].onmouseleave = function() {
    element = rippleDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    if (element) {
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// YELLOW //


for (var num = 0; num < rippleYellowButtons.length; num++) {
  rippleYellowButtons[num].setAttribute("data-identifier", num)
  rippleYellowButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft
    var mouseY = event.clientY - this.offsetTop
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-yellow-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleYellowBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(35)"
    }, 10);
  }

  rippleYellowButtons[num].onmouseup = function() {
    element = rippleYellowBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleYellowButtons[num].onmouseleave = function() {
    element = rippleYellowBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    if (element) {
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// BRAND //


for (var num = 0; num < rippleBrandButtons.length; num++) {
  rippleBrandButtons[num].setAttribute("data-identifier", num)
  rippleBrandButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft
    var mouseY = event.clientY - this.offsetTop
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-brand-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleBrandBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(70)"
    }, 10);
  }

  rippleBrandButtons[num].onmouseup = function() {
    element = rippleBrandBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleBrandButtons[num].onmouseleave = function() {
    element = rippleBrandBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    if (element) {
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// MEDIUM DARK //


for (var num = 0; num < rippleMediumDarkButtons.length; num++) {
  rippleMediumDarkButtons[num].setAttribute("data-identifier", num)
  rippleMediumDarkButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft + window.pageXOffset
    var mouseY = event.clientY - this.offsetTop + window.pageYOffset
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-medium-dark-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleMediumDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(100)"
    }, 10);
  }

  rippleMediumDarkButtons[num].onmouseup = function() {
    element = rippleMediumDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleMediumDarkButtons[num].onmouseleave = function() {
    element = rippleMediumDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    if (element) {
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// WIDE DARK //


for (var num = 0; num < rippleWideDarkButtons.length; num++) {
  rippleWideDarkButtons[num].setAttribute("data-identifier", num)
  rippleWideDarkButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft + window.pageXOffset
    var mouseY = event.clientY - this.offsetTop + window.pageYOffset
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-wide-dark-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleWideDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(200)"
    }, 10);
  }

  rippleWideDarkButtons[num].onmouseup = function() {
    element = rippleWideDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleWideDarkButtons[num].onmouseleave = function() {
    element = rippleWideDarkBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    if (element) {
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}


// WIDE LIGHT //


for (var num = 0; num < rippleWideLightButtons.length; num++) {
  rippleWideLightButtons[num].setAttribute("data-identifier", num)
  rippleWideLightButtons[num].onmousedown = function() {
    var mouseX = event.clientX - this.offsetLeft + window.pageXOffset
    var mouseY = event.clientY - this.offsetTop + window.pageYOffset
    offsetElement = this
    while(true) {
      if (offsetElement.offsetParent){
        offsetElement = offsetElement.offsetParent
        mouseX -= offsetElement.offsetLeft
        mouseY -= offsetElement.offsetTop
      } else {
        break
      }
    }
    var element = document.createElement("SPAN")
    this.append(element)
    element.classList.add("background-wide-light-circle")
    element.style.left = mouseX - 7 + "px"
    element.style.top = mouseY - 5 + "px"
    rippleWideLightBackgrounds[parseInt(this.getAttribute("data-identifier"))] = element
    setTimeout(function() {
      element.style.transform = "scale(100)"
    }, 10);
  }

  rippleWideLightButtons[num].onmouseup = function() {
    element = rippleWideLightBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    element.style.opacity = "0"
    setTimeout(function() {
      element.remove()
    }, 300)
  }

  rippleWideLightButtons[num].onmouseleave = function() {
    element = rippleWideLightBackgrounds[parseInt(this.getAttribute("data-identifier"))]
    if (element) {
      element.style.opacity = "0"
      setTimeout(function() {
        element.remove()
      }, 300)
    }
  }
}
