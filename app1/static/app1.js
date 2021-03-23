function changeNav() {
  var nav = document.getElementById("mySidenav");
  if (nav.style.width == '75vw') {
    nav.style.width = '0vw';
  } else {
    nav.style.width = "75vw";
  }
}

function myFunction(x) {
  x.classList.toggle("change");
}