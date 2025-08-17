
// Day 3 - Loops Practice 

// Repeat mantra 7 times 
for (let mantra = 0; mantra < 7; mantra++ ) {
console.log("I am a JavaScript Developer ")
}

//Counts down from 10 to 1
for (let i = 10; i >= 1; i-- ){
    console.log("Count down:" + i)
}

//Runs a count up from 0 to 10
for (let CountStrt = 0; CountStrt <= 10; CountStrt++) {
    console.log("Count Up:" + CountStrt)
}

//Skip count up by 3
for (let CountStrt = 0; CountStrt <= 20; CountStrt+= 3) {
     //Runs a count and skip 3
    console.log("Count Up:" + CountStrt)
}

//Practiced Sun 17 Aug
let shopList = [" chick", "beef", "lamb"];

for ( let i = 0; i < shopList.length; i++) {
    console.log(`BBQ buy: ${shopList[i]}`);
}

let iceCream = ["Pistachio", "Mango", "Coconut","Bubble Gum"];

for (let i = 0; i < iceCream.length; i++) {
    console.log(`My Favourite Ice Cream is : ${iceCream[i]}`);
}

let dogBreed = ["Cavapoos", "Golden Retrievers", "Dobermans" ]

for (let i = 0; i < dogBreed.length; i++){
    console.log(`I love Dog Breeds like: ${dogBreed[i]}`)
}

for (let numberplot = 0; numberplot <= 30; numberplot = numberplot + 5) {
    console.log(numberplot);
}

let myCars = ["BMW i4","Mercedes GL","VW Amarok "]

for (let i = 0; i < myCars.length; i++){
    console.log(`I own a: ${myCars[i]}`);
}