try {
  throw new Error("thrown error");
} catch (error) {
  console.error("Error", error);
} finally {
  console.log("program ended");
}

console.time("loop");

for (let i = 0; i <= 100; i++) {
  console.log(i);
}

console.timeEnd("loop");
