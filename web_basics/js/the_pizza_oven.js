// var sandwich = {
//     bread: "sourdough",
//     protein: "london broil",
//     cheese: "lacey swiss cheese",
//     toppings: ["romaine lettuce", "heirloom tomatoes", "horseradish sauce"]
// };

// function sandwichFactory( bread, protein, cheese, toppings ) {
//     var sandwich = {}
//     sandwich.bread = bread;
//     sandwich.protein = protein;
//     sandwich.cheese = cheese;
//     sandwich.toppings = toppings;
//     return sandwich;
// }

// var s1 = sandwichFactory( "wheat", "turkey", "provolone", ["mustard", "fried onions", "arugula"] );
// console.log( s1 );


// var pizza = {
//     crustType: "thin",
//     sauceType: "alfredo",
//     cheeses: "mozzarella",
//     toppings: ["sauceage", "olives", "jalepeno"]
// }

// function pizzaOven( crustType, sauceType, cheese, toppings ) {
//     var pizza = {}
//     pizza.crustType = crustType;
//     pizza.sauceType = sauceType;
//     pizza.cheese = cheese;
//     pizza.toppings = toppings;
//     return pizza;
// }

// var p1 = pizzaOven( "deep dish", "traditional", ["mozzarella"], ["pepperoni", "sausage"] );
// console.log( p1 );

// var p2 = pizzaOven( "hand tossed", "marinara", ["mozzarella", "feta"], ["mushrooms", "olives", "onions"] );
// console.log( p2 );

var crustType = [
    "deep dish",
    "hand tossed",
    "thin and crispy",
    "cauliflower",
    "gluten free",
    "hawaian bread"
];

var sauceType = [
    "traditional",
    "marinara",
    "bbq",
    "white sauce",
    "nacho cheese",
    "tikka masala"
];

var cheese = [
    "mozzarella",
    "cheddar",
    "feta",
    "swiss",
    "blue cheese",
    "goat cheese",
    "provolone",
    "parmesan",
    "vegan cheese"
];

var toppings = [
    "pepperoni",
    "sausage",
    "chicken",
    "corn",
    "olives",
    "bell peppers",
    "onions",
    "mushrooms",
    "anchovies"
];

function randomRange( max, min ) {
    return Math.floor( Math.random() * max - min ) + min;

}
function randomPick( arr ) {
    var i = Math.floor( arr.length * Math.random() );
    return arr[i];
}
function randomPizza() {
    var pizza = {};
    pizza.crustType = randomPick( crustType );
    pizza.sauceType = randomPick( sauceType );
    pizza.cheese = [];
    pizza.toppings = [];
    for ( var i = 0; i < randomRange( 5, 1 ); i++ ) {
        pizza.cheese.push( randomPick( cheese ) );
    }
    for ( var i = 0; i < randomRange( 4, 0 ); i++ ) {
        pizza.toppings.push( randomPick( toppings ) );
    }
    return pizza;
}

console.log( randomPizza() );