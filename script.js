//script for CV//

//counter for views//
var n = localStorage.getItem('on_load_counter');

if (n === null) {
    n = 0;
}
n++;

localStorage.setItem("on_load_counter",n);

nums = 

function counter_fn() {
    var counter = document.getElementById("cntr");
    var count = 0;
    count = parseInt(counter.innerHTML);
    count = count + 1;
    counter.innerHTML = count;
  }
  window.onload = counter_fn;