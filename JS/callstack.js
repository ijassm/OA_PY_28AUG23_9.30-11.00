function m1() {
  console.log("completed m1 excution");
}

function m2() {
  m1();
  console.log("completed m2 excution");
}

function m3() {
  m2();
  console.log("completed m3 excution");
}

m3();
