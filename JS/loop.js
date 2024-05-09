// for loop

// for (let i = 0; i <= 10; i++) console.log(i);

// for (let i = 10; i >= 0; i--) {
//   if (i % 2 === 0) {
//     console.log("even -", i);
//   } else {
//     console.log("odd -", i);
//   }
// }

// nested loops

// for (let i = 1; i < 3; i++) {
//   for (let j = 1; j < 3; j++) {
//     for (let k = 1; k < 2; k++) {
//       console.log(i, j, k);
//     }
//   }
// }

// i = 1
// -----j = 1
// ----------k = 1
// -----j = 2
// ----------k = 1

// i = 2
// -----j = 1
// ----------k = 1
// -----j = 2
// ----------k = 1

// console.log(i);

let i = 128269;

// while (i <= 129522) {
//   document.write(`<span style='margin:10px;'>&#${++i}</span>`);
// }

// do {
//   console.log(++i);
// } while (i < 10);

for (let i = 1; i <= 5; i++) {
  for (let j = 1; j <= 5; j++) {
    document.write(`<span>${j}</span>`); 
  }
  document.write(`<br>`);
}
