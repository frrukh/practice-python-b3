// check two given numbers and return true if one of them is 50 or if their sum is 50.
let num1 = 50;
let num2 = 50;
console.log("num1 =",num1);
console.log("num2 =",num2);
if(num1==50 || num2==50 || (num1+num2)==50){
    console.log("TRUE.");
}else{
    console.log("FALSE.");
}


//check from the given number, weather it is positive or negative.
let number=10;
console.log("number =",number);
if(number>0){
    console.log("the given number is POSITIVE.");
}else if(number<0){
    console.log("the given number is NEGATIVE.");
}else{
    console.log("the given number is = ZERO.");
}


//check weather a given number is even or odd.
let givenNumber=12;
console.log("given number =",givenNumber);
if(givenNumber%2==0){
    console.log("the given number is EVEN.");
}else{
    console.log("the given number is ODD.");
}


//check weather a given positive number is a multiple of 3.
let num=10;
console.log("num =",num);
if(num%3==0 && num>0){
    console.log("the given positive number is a multiple of 3.");
}else if(num%3!=0 && num>0){
    console.log("the given number is not a multiple of 3");
}else{
    console.log("plese enter a non-zero positive number.");
}


//determine weather a given year is a leap year.
let year = 1700;
console.log("year =",year);
if((year%4==0 && year%100!=0)|| year%400==0){
    console.log("the given year is a LEAP-YEAR");
}else{
    console.log("the given year is NOT a LEAP-YEAR");
}

//check from the given two numbers, weather the first number is "grater", "lesser" or "equal" to the second number.
let number1=0;
let number2=0;
console.log("number1=",number1);
console.log("number2=",number2);
if(number1>number2){
    console.log("number1 > number2");
}else if (number1<number2){
    console.log("number1 < number2");
}else{
    console.log("number1 = number2");
}


//check from the three sides of triangle. use conditions to determine and display weather the triangle is "Equilateral" (all sides are equal), "Isosceles" (two sides are equal), or "Scalane" (no sides are equal).
let side1=12;
let side2=12;
let side3=12;
console.log("side1=",side1);
console.log("side2=",side2);
console.log("side3=",side3);
if(side1==side2 && side2==side3){
    console.log("the triangele is EQUILATERAL (all sides are equal). ");
}else if(side1==side2 || side2==side3 || side3==side1){
    console.log("the triangle is ISOSCELES (two sides are equal).");
}else{
    console.log("the triangle is SCALANE (no sides are equal).");
}


//check from the given month (1-12) if its "Winter" (December-Feburary), "Spring" (March-May), "Summer" (June-August), or "Autumn" OR "Fall" (September-November).
let month=1;
console.log("month=",month);
if (month>12 || month<1){
    console.log("plese enter a valid month")
}else if(month==12 || month==1 || month==2){
    console.log("Winter🥶");
}else if (month==3 || month==4 || month==5){
    console.log("Spring🥰");
}else if (month==6 || month==7 || month==8){
    console.log("Summer😎");
}else{
    console.log("Autumn😪");
}


