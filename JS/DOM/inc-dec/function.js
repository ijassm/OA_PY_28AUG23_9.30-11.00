// function statement / function declaration

// function greeting(name) {
//   console.log(`Hello ${name}`);
// }

// greeting("asoon");
// console.log("Hello");
// greeting("goutham");
const h1 = document.createElement("h1");
h1.textContent = "Hello";
h1.style.color = "green";
console.log(h1.style);
console.log(h1);
document.body.appendChild(h1);
const doc = document;

function increament() {
  const h1 = doc.getElementsByTagName("h1")[0];
  h1.textContent = parseInt(h1.textContent) + 1;
}

function decreament() {
  const h1 = doc.getElementsByTagName("h1")[0];
  let value = parseInt(h1.textContent);
  if (value > 0) h1.textContent = value - 1;
}

function reset() {
  const h1 = doc.getElementsByTagName("h1")[0];
  h1.textContent = 0;
}

// console.log(greeting);
// console.log(window.greeting);
