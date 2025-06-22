// Day 4 - if else 

// If/Else - Conditionals 

// Time conditions
let time = 8;

if (time < 9) {
    console.log('you are on time');
}

// Tempreture conditions
let tempreture = 30;

if (tempreture > 24){
    console.log('Its hot out there!');
} else {
    console.log('Its alright out there');
}

//Codewars Kata - make value negative 
function makeNegative(num){
    if (num < 0) {
        return num;
    } else {
        return num * -1;
    }
}

//tests 
console.log(makeNegative(-2))
console.log(makeNegative(6))
console.log(makeNegative(0))


//while loops

let count = 2;

while (count <= 5) {
    if (count === 3) {
    console.log ("we're half way there!"); 
} else {
    console.log ("Current count is" +  count);
}
count++;
}


let num = 10;

while (num >= 1){
    if (num % 2 === 0) {
        console.log(num + " is Even !!");  
    } else {
        console.log(num + " is Odd!!"); 
    }
    num--;
}
