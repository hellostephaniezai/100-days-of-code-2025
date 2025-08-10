//------------------
// Day 7 - Array Method Practice
//------------------

//Part 1: Simple Array Access

let fruits = ["Kiwi", "Apple", "Melon", "Orange"];
console.log(fruits[1]) // Apple 
console.log(fruits[ 3]) // Orange

//Part 2: Array of Objects

let allFruits = [
    {name: "Kiwi", sweet: false },
    {name: "Mango", sweet: true },
    {name: "Lemon", sweet: false },
    {name: "Strawberry", sweet: true },
    {name: "coconut", sweet: false },

];

// Filer Examples 

let sweetOnly = allFruits.filter(fruit => fruit.sweet === true);
console.log(sweetOnly)

let notSweet = allFruits.filter(fruit => fruit.sweet === false);
console.log(notSweet)

// Mapping Examples

let fruitNamesUpper = allFruits.map(fruit => fruit.name.toUpperCase())
console.log(fruitNamesUpper);

let fruitNamesLower = allFruits.map(fruit =>fruit.name.toLowerCase())
console.log(fruitNamesLower);

//Find and Boolean Check 

let firstSweet = allFruits.find(fruit => fruit.sweet === true);
console.log(firstSweet);

hasSweet = allFruits.some(fruit => fruit.sweet)
console.log("At least one sweet fruit?", hasSweet);

let allAreSweet = allFruits.every(fruit => fruit.sweet);
console.log("Are all fruit sweet?:", allAreSweet);

// Add/ Remove

allFruits.push({ name: "Papaya",sweet: true });
console.log( "After Push", allFruits)

let removeFruit = allFruits.pop()
console.log("Removed Fruit:", removeFruit);
