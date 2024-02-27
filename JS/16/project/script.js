//Create a function that takes two numbers as input and returns the largest of the two.
    // by anonymeous returning function.
let check_number=function (a,b){
    console.log("a  : " + a);
    console.log("b  : " + b);
    if(a>b){
        return "a is grater"
    }else if(a<b){
        return "b is grater"
    }else{
        return "a = b"
    }
}
let result=check_number(12,11);
console.log(result);

    // by arrow returning function.
let check_number1=(a,b)=>{
    console.log("a : " + a);
    console.log("b : " + b);
    if(a>b){
        return "a is grater";
    }else if (a<b){
        return "b is grater";
    }else{
        return "a = b"
    }
}
let result1=check_number1(12,13);
console.log(result1);

//create a function that takes two strings as input and returns a new string that concatenates both if them.
    // by anonymeous returning function.
let concatenate=function(a,b){
    console.log("a : "+ a);
    console.log("b : "+ b);
    return a+b
}
let answer=concatenate("Farrukh ","Maqsood.");
console.log("concatenation of a and b = "+answer);
    // by arrow returning function.
let concatenate1=(a,b)=>{
    console.log("a : "+a);
    console.log("b : "+b);
    return a+b;
}
let answer1=concatenate1("Talha ","Maqsood.");
console.log("concatenation of a and b ="+answer1);

//Write a function that takes a temperature in celsius and converts it to Fahrenheit.
    // by anonymeous returning function.
let temp=function(a){
    console.log("temperature in celsius : "+a);
    return (a*1.8)+32;
}
let temp_fahrenheit=temp(100);
console.log("temperature in fahrenheit : "+temp_fahrenheit);
    //by arrow returning function.
let temp1=(a)=>{
    console.log("temperature in celsius : "+a);
    return (a*1.8)+32;
}
let temp_fahrenheit1=temp1(102);
console.log("temperature in fahrenheit : "+temp_fahrenheit1);

//Write a program that takes the age and checks if they are eligible for voting (e.g 18 or older).
    // by anonymeous returning function.
let check=function(age){
    console.log("age : "+age);
    if(age>=0){
        if(age>=18){
            return"eligibel for voting.";
        }else{
            return "not eligibel for voting."
        }
    }else{return "plese enter a VALID AGE."}
}
let eligibility=check(-12);
console.log(eligibility);
    // by arrow returning function.
let check1=(age)=>{
    console.log("age : "+age);
    if(age>=0){
        if(age>=18){
            return "eligible for voting."
        }else{
            return "not eligible for voting."
        }
    }else {
        return "plese enter a VALID AGE."
    }
}
let eligibility1=check1(12);
console.log(eligibility1);

//Implement a function that checks if a given number is positive, negative, or zero and return the result.
    // by anonymeous returning function.
let check_num=function(num){
    console.log("given number : "+num);
    if(num>0){
        return "Positive."
    }else if(num<0){
        return "Negative"
    }else {
        return "Zero"
    }
}
let number_check=check_num(-10);
console.log(number_check);
    // by arrow returning function.
let check_num1=(num)=>{
    console.log("given number : "+num);
    if(num>0){
        return "Positive"
    }else if(num<0){
        return "Negative"
    }else{
        return "Zero"
    }
}
let number_check1=check_num1(0);
console.log(number_check1);

//create a function that takes two numbers as input and returns their product  using arithmetic operations. (e.g the product of 2 and 3 is 6).
    // by anonymeous returning function.
let product=function(a,b,operator){
    console.log("a : "+a);
    console.log("b : "+b);
    return operator(a,b);
}
let ans=product(12,3,function(c,d){return c*d});
console.log(ans);
    // by arrow returning function.
let product1=(a,b,operator)=>{
    console.log("a : "+a);
    console.log("b : "+b);
    return operator(a,b);
}
let ans1=product1(13,3,(c,d)=> c*d);
console.log(ans1);

//implement a function that takes two strings as input and checks if they are equal.
    // by anonymeous returning function
let checkString=function(a,b){
    console.log("a : "+a);
    console.log("b : "+b);
    if(a===b){
        return "both strings are equal."
    }else {
        return "both stirngs are not equal."
    }
}
let res=checkString("farrukh","farrukh");
console.log(res);
    // by arrow returning function.
let checkString1=(a,b)=>{
    console.log("a : "+a);
    console.log("b : "+b);
    if(a===b){
        return "both strings are equal."
    }else{
        return "both stirngs are not equal."
    }
}
let res1=checkString1("farrukh","farukkh");
console.log(res1);

//implement a function that takes two strings as input and checks if their lenghts are equal.
    // by anonymeous returning function.
let checkLength=function(a,b){
    console.log("a : "+a);
    console.log("b : "+b);
    if(a.length === b.length){
        return "the lengths of both strings are equal."
    }else{
        return "the lengths of both strings are not equal."
    }
}
let answ=checkLength("farrukh1 MAQSOOD","abdullah maqsood");
console.log(answ);
    // by arrow retyrning function.
let checkLength1=(a,b)=>{
    console.log("a : "+a);
    console.log("b : "+b);
    let lengthOf_a=a.length;
    let lengthOf_b=b.length;
    if(lengthOf_a===lengthOf_b){
        return "the lengths of both strings is equal."
    }else{
        return "the lengths of both strings are not equal."
    }
}
let answ1=checkLength1("farrukh","Talha");
console.log(answ1);

// Write a function that takes a number as input and returns the absolute value of the number
    // by anonymeous returning function.
let absolute=function(a){
    console.log("a : "+a);
    if (a>=0){
        return a;
    }else{
        return a*-1;
    }
}
let abs_value=absolute(-12);
console.log(abs_value);
    // by arrow returning function.
let absolute1=(a)=>{
    console.log("a : "+a);
    return Math.abs(a);
}
let abs_value1=absolute(-20);
console.log(abs_value);