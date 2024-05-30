// setTimeout(() => console.log("CB executed"), 0);

// console.time("loop");

// for (let i = 0; i < 100000; i++) {
//   console.log(i);
// }

// console.timeEnd("loop");

// setTimeout(function a() {
//   console.log("a");
// }, 1000);

// setTimeout(function b() {
//   console.log("b");
// }, 500);

// setTimeout(function c() {
//   console.log("c");
// }, 0);

// function d() {
//     console.log("d");
// }

// d();

let c = Number(localStorage.getItem("c"));

const increament = setInterval(() => {
  document.write(`<h1>${c}</h1>`);
  localStorage.setItem("c", ++c);
}, 1000);

if (c >= 410) clearInterval(increament);
