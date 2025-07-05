// Day 6 - Functions return

// Functions - Returns 

//Return a calculation 

// Part 1: 
function multiply (a,b){
return a * b;
}

let result = multiply (3,4);
console.log(result);


// Part 2:  Return a String 


function createGreeting(name, timeOfDay){
        return "Good " + timeOfDay + ", " + name + "! ";
}

let greeting = createGreeting("Stephanie", "evening");
console.log(greeting); 


function remindMe(name, theMessage,){
    return "Hey! " + theMessage + ", " + name + "!"
}

let reminder = remindMe("Stephanie", "Keep Going")
console.log(reminder)

// Part 3:  Return a conversion 

function toPounds(kg){
    return kg * 2.20462;
}

let weightInPounds = toPounds(60);
console.log(weightInPounds);


function toKilograms(lbs){
    return lbs / 2.20462;
}

let weightToKilograms = toKilograms(145);
    console.log(weightToKilograms);