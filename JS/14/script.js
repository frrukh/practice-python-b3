// conditional operators
// > , < , >= , <= , == , === , != , !==



let age1 = 10;
console.log("age1=",age1);
if(age1>9){
    console.log("The age1 is grater than nine.");
}


let age2 = 17;
console.log("age2=",age2)
if(age2<9){
    console.log("The age2 is less than nine.");
}else{
    console.log(" The age2 is grater than nine. ")
}


let age3 = 12;
console.log("age3=",age3);
if(age3<9){
    console.log("The age3 is less than nine.");
}else if(age3>=12){
    console.log("The age3 is grater than of equal to twelve")
}

let age4 = 14;
let x = "14";
console.log("age 4=",age4);
console.log("x=",x);
if(age4<=12){
    console.log("the age4 is grater than of equals to 12");
}else if(age4==13){
    console.log("the age4 is equal to 13");
}else if(age4===x){
    console.log("the value of age4 is equal to the vlaue of x");
}else{
    console.log("the value or data-type of age4 is different from x and the vlaue of age4 is grater than 13");
}

let age5 = 9;
console.log("age5=",age5);
if(age5!=9){
    console.log("age5 is not equal to nine");
}else{
    console.log("the value of age5 is equal to nine")
}

let age6 = '12';
let y = '12';
console.log("age6 =",age6);
if(age6!==y){
    console.log("the value or data-type of age6 is not equals to the value and data-type of y");
}else{
    console.log("the vlaue of age6 is equal to the vlaue of y.");
}

let a =100;
let b =31;
console.log("a=",a);
console.log("b=",b);
//logical operators
// AND (&&) , OR (||) , NOT (!)
if(a>b && b==31){
    console.log("the value of a is grater than 31 and the value of b is 31");
}else{
    console.log("the value of a and b is unknown.");
}

let c ='10';
let d =10;
console.log("c=",c);
console.log("d=",d);
if(c>d || c===d){
    console.log("the value of c is grater than d or the value and data-type of c is equals to d");
}else{
    console.log("the value of c is less than d or the value of c is equals to the value of d and the data-type of c is not equals to the data-type of d");
}

let e = 12;
let f = 110;
console.log("e=",e);
console.log("f=",f);
if(!e>f){
    console.log("e is smaller");
} else{
    console.log("e is smaller or eequal to f");
}





//ternary operators
// it works just like if else statement
// aa>12 ? bb = 12 : bb =11; means if aa>12 then b=12 else b=11
let aa=13;
let bb;
console.log("aa=",aa);
console.log("bb=",bb);
aa>12 ? bb=12 : bb=11;
console.log("bb=",bb);


let cc=18;
console.log("c=",c);

cc>=18 ? console.log("adult") : console.log("not adult");