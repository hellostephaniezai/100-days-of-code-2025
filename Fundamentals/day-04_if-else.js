
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