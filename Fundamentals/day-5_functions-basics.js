
// Basic Functions

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
