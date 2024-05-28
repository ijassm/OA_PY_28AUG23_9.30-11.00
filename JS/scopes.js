// Scope determines the accessibility (visibility) of variables.

// JavaScript variables have 3 types of scope:

// Block scope🎈
// {
//     let a = 10;
//     const b = 20;

//     console.log(a);
//     console.log(b);
// }

// console.log(a);
// console.log(b);

// Function scope🎈

// function greeting() {
//   var a = "XYZ";
// }

// greeting();

// console.log(a);

// Global scope🎈

// global - var
// script - let & const

var a = "hello js";
let b = "hello";
const c = "hello js";

{
  var a = "changed";
  let b = "block scope1";
  const c = "block scope2";
  console.log(b);
  console.log(c);
}

function greeting() {
  var name = "XYZ";
  return (() => {
    return b + " " + name;
  })();
}

greeting();

console.log(a);
console.log(b);
console.log(c);
