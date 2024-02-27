//general functions
function add(a,b) {
    let sum = a+b;
    console.log(sum);
}
add(12,15);
    // we can use return keyword to return the value to the calling place and generaly store it in a variable for reuseability.(also called returning functions)
function add1(a,b) {
    let sum = a+b;
    return sum
}
let sum=add1(12,13);
console.log(sum);



//anonymeous functions.
    // in anonymeous and arrow functions we will not give it any name,but we only assign the function to a variable.
    // syntax let variabel = function (parameters){body}
let add2=function(a,b){
    let sum = a+b;
    console.log(sum);
}
add2(12,10);
    //anonymeous returning-function.
let add3=function(a,b){
    return a+b
}
let result=add3(10,10);
console.log(result);



//arrow functions.
    // in anonymeous and arrow functions we will not give it any name,but we only assign the function to a variable.

// let add4=(a,b)=>{console.log(a+b);}
let add4=(a,b)=> console.log(a+b); //we can also writ it like this if it is one-line function.
add4(1,2);
    //arrow returning function.
// let add5=(a,b)=>{return a+b}
let add5=(a,b)=> a+b //we can also write like this,the return function is by default if use without {}
let result1=add5(50,50);
console.log(result1);


//examples of general , anonymous and arrow  returning-functions.
//general returning function.
function cube(a){
    let cube=a**3;
    return cube;
}
console.log(cube(4));

let answer=cube(2);
console.log(answer);

//anonymeous function.
let cube1=function (a){
    return a**3;
}
console.log(cube1(3));

let answer1=cube1(2);
console.log(answer1);

//arrow function.
let cube2=(a)=> a**3;
console.log(cube2(5));

let answer2=cube2(6);
console.log(answer2);




//single line if else statement.
//syntax: condition?(if)true:(else)false
let b=10;
console.log("b:"+b);
b>11?console.log("b is grater than 11"):console.log("b is smaller than 11");

    //mostly it is used in arrow function to make a single line function.
let check_number=(a)=> (a%2)==0? "even" :"odd" ; //here we did not use return because in arrow function if we remove the curly-braces from the body,the return will be the default behaviour.
let even_odd=check_number(13);
console.log(even_odd);




//function as a parameter.
    // general.
function logic_undefined(a,b,logic){
    console.log(logic(a,b));
}
logic_undefined(12,13,function(a,b){return a+b});
logic_undefined(21,2,(c,d)=>c-d);
    // anonymeous.
let logic_undefined1=function(a,b,log){
    return log (a,b);
}
let result2=logic_undefined1(12,10,function(a,b){a-b});
console.log(result);

    // arrow.
let logic_undefined3=(a,b,mul)=>{
    return mul(a,b);
}
let ans=logic_undefined3(12,3,(c,d)=>c*d);
console.log(ans);

















//to check the length of a string we use lenght keyword
//syntax: string_name.length

let app="123456";
console.log(app.length);