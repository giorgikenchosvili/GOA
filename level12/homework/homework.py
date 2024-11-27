let number = parseInt(prompt("შეიტანეთ რიცხვი:"));

if (number % 2 === 0) {
  console.log("even");
} else {
  console.log("odd");
}

for (let i = 1; i <= 50; i++) {
  if (i % 2 === 0) {
    console.log(i);
  }
}


let numbers = [3, 5, 7, 11, 15, 9, 12, 20, 4, 8];
for (let i = 0; i < numbers.length; i++) {
  if (numbers[i] > 10) {
    console.log(numbers[i]);
  }
}


let numbers = [2, 5, 8, 3, 6, 9, 12, 15, 18, 21];

let first = numbers[0];
let last = numbers[numbers.length - 1];

console.log("სხვაობა: " + (last - first));
console.log("ჯამი: " + (first + last));
console.log("ნამრავლი: " + (first * last));



let userNumber = parseInt(prompt("შეიტანეთ რიცხვი:"));
let names = ["გიო", "ნიკა", "ანუ", "მარი", "თეა"];

if (userNumber >= 0 && userNumber < names.length) {
  console.log(names[userNumber]);
} else {
  console.log("არასწორი ინდექსი");
} 
