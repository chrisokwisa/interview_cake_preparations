// variables that are declared with Let are block scoped
// variables that are defined with 'Let' will have a "Block level"scope
// variables that are declared with 'let' must be declared before usage

// see the following code snippet to understand how you can use 'Let'



// Let's declare a variable named 'emailaddress'

let emailaddress = 'someone@example.com'

// If accidentally we redeclare another variable with the same name
// then the compiler will throw an error, which is indeed a great practice

// Uncaught SyntaxError: Identifier 'emailaddress' has already been declared

// Now let's declare a variable within a loop

for (let i = 0; i < 10; i++) {
    // variable 'i' can be accessed within this loop only
    console.log(i);
}

// Now let's try to access the variable 'i' outside the loop
console.log(i);

// The compiler will thriw an error if you try to print the value of 'i' outside
// Uncaught ReferenceError: i is not defined

