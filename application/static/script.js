//script for CV//

//counter for views//

const counter = document.querySelector('#cntr');

const getCount = () => {
    const response = fetch("https://api.countapi.xyz/get/www.mikescv.co.uk/1234");
    const data = response.json();
    setValue(data.value);
  };
  
const incrementCount = () => {
    const response = fetch("https://api.countapi.xyz/hit/www.mikescv.co.uk/1234");
    const data = response.json();
    setValue(data.value);
  };

const setValue = (num) => {
      counter.innerHTML = num;
  };

if (localStorage.getItem("hasVisited") == null) {
    incrementCount()
      .then(() => {
        localStorage.setItem("hasVisited", "true");
      })
      .catch((err) => console.log(err));
  } else {
    getCount()
      .catch((err) => console.log(err));
  }

