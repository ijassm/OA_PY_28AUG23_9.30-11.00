const address = {
  city: "Bangalore",
  state: "Karnataka",
  country: "India",
};

const obj = {
  firstName: "Goutham",
  lastName: "Kumar",
  age: 20,
  fullName: function () {
    console.log(this.firstName + " " + this.lastName);
  },
  //   ...address,
  address,
};

// obj.address = address;

// syntax to update object
// obj[key] = value;
// obj.key = value;

// obj.name = "Goutham";
// obj["age"] = 20;

// console.log(obj["name"]);
// console.log(obj.age);
// console.log(typeof obj);

// obj.fullName();

console.log(obj);

// Destruction

const { firstName, address: location, ...restObj } = obj;

console.log(firstName);
console.log(location);
console.log(restObj);
