// Day 7 - Arrays

//Part 1:

let fruits = ["Kiwi", "Apple", "Melon", "Orange"];
console.log(fruits[1])
console.log(fruits[ 3])


//Part 2:

let allFruits = [
    {name: "Kiwi", sweet: false },
    {name: "Mango", sweet: true },
    {name: "Lemon", sweet: false },
    {name: "Strawberry", sweet: true },
    {name: "coconut", sweet: false },
];

let sweetOnly = allFruits.filter(fruit => fruit.sweet === true);
console.log(sweetOnly)

let notSweet = allFruits.filter(fruit => fruit.sweet === false);
console.log(notSweet)