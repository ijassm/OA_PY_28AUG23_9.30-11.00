// conditional statements

// let age = parseInt(prompt("Enter your age: "));

// console.log(age);
// console.log(typeof age);

// if (age >= 18) console.log("eligible for vote");
// else if (age < 0) console.log("invalid age: " + age);
// else console.log("not eligible for vote");

let a = 10;
let b = 20;
let c = 30;

if (a > b && a > c) {
  console.log("a is greater");
  if (b < c) {
    console.log("b is smaller");
  } else {
    console.log("c is smaller");
  }
} else if (b > c) {
  console.log("b is greater");
  if (a < c) {
    console.log("a is smaller");
  } else {
    console.log("c is smaller");
  }
} else {
  console.log("c is greater");
  if (a < b) {
    console.log("a is smaller");
  } else {
    console.log("b is smaller");
  }
}

let day = 1;

switch (day) {
  case 1:
    console.log("Sunday");
    break;
  case 2:
    console.log("Monday");
    break;
  case 3:
    console.log("Tuesday");
    break;
  case 4:
    console.log("Wednesday");
    break;
  case 5:
    console.log("Thursday");
    break;
  case 6:
    console.log("Friday");
    break;
  case 7:
    console.log("Saturday");
    break;

  default:
    console.log("invalid date");
    break;
}
