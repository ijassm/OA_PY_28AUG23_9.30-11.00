console.log("Types of Functions in JS");

// var a = "hello";

// Function statement / Function declaration
// function greeting(name) {
//   return "Hello " + name;
// }

// greeting("hello");

// Function expression

// Named function
let a = function greeting(name) {
  return "Hello " + name;
};

// Anonymous function
let b = function (name) {
  return "Hello " + name;
};

console.log(a("XYZ"));
console.log(b("ABC"));

// ES6 => Arrow function

let c = (name) => name + " " + "hello";

console.log(c("ABX"));

// IIFE

let d = (() => "Arrow")();

console.log(d);

(function () {
  console.log("Anonymous");
})();

(function name() {
  console.log("Named");
})();
