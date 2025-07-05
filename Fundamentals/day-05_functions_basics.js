// Day 5 - Functions,Paramenters 

//Part 1: Basic Functions

function greet(){
    console.log("Hiya Stephanie Zai");
}
greet ();

function introduce(){
    console.log( "My name is Stephanie");
}
introduce();


function favouriteColour(){
    console.log( "My fave colour is blue"); 
}
favouriteColour();


function motivate(){
    console.log( " You're doing great!"); 
}
motivate();


//  original code 
function dailyMessage(){
    console.log( "My name is Stephanie");
    console.log( "My fave colour is blue"); 
    console.log( " You're doing great!"); 
}
dailyMessage();


//  refactored code 
function dailyMessage() {
    introduce();
    favouriteColour();
    motivate();
}

// Part 2:  Paramenters & Arguments 

//sayHello

function sayHello(name){
console.log("Hello " + name + ", Welcome back!");

}
sayHello("Stephanie");
sayHello("Zai");

function favouriteFood(foodItem){
    console.log("I could eat " + foodItem + " all day!");
    
    }
    favouriteFood("Avocado");
    favouriteFood("Prawn Fried Rice");
    

function cheerUp(aName){
    console.log(aName + " , you're stronger than you think!");
        
        }
        cheerUp("Jessica");
        cheerUp("Harvey");
        