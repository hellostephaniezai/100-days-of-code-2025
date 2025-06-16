
//Basic Expressions

//Assigning the value of 7 to x 
let x = 7;

//Assigning the value of 4 to y
let y = 3;

let z = x + y;
console.log(z);


let s = 20; 
let t = 3;
let e = 7; 

let p = s + t + e;
console.log(p);

// Day 2 Challenge: A - Pass/Fail Checker 
let score1 = 60;
let score2 = 44;
let score3 = 52;

let AvgScr = (score1 + score2 + score3) / 3; 
let pass = AvgScr >= 50;

if (pass) {
    console.log('You passed!');
} else {
    console.log('You failed.');
};

// Day 2 Challenge: B - Highest Test Score
let test1 = 92;
let test2 = 44;
let test3 = 63;

if (test1 > test2 && test1 > test3) {
    console.log('Test 1 had the highest score');
} else if (test2 > test1 && test2 > test3) {
    console.log('Test 2 had the highest score');
} else if (test3 > test1 && test3 > test2) {
    console.log('Test 3 had the highest score');
    } else {
    console.log('There was a tie');}
