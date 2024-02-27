// methods to display output in browser
// 1.
// alert('farrukh maqsood is the developer of this page!12');

// 2.
// console.log("Farrukh Maqsood!12");

// 3.
// document.write("My Name Is Farrukh Maqsood.!@12");
// document.write(" <h1>My Name Is Farrukh Maqsood.!@13</h1>")


// datatypes

// 1. integers/numbers

let a = 10;
console.log(a);

// 2.  decimal

let b = 10.122;
console.log(b);

// 3. string (strings are always written in qutation marks)

let c="this is string 12@# 12.2";
console.log(c);
    // String Interpolation.(To create string in which we can perform the operation and or write expression like a+b or Math.floor(Mate.random()*100) etc.)
        // in string datatype we also have tempelate literals.the strings are written by inverted comaas (""/'') where the tempelate literals are written by backticks (``) that is before 1 in the keyboard.
        // Advantage--- in tempelate literals we can write the variable , perform operation ,write expressions or anything that we do without inverted commas, with out closing it by using ${} .
        // NOTE-- Tempelate literal first convert your value into string and then log on console window or perform the specific task.
        // syntax `string text ${expression} string text`
        console.log(`-----------object literals------------`);
        let OL1=12;
        let OL2=38;
        console.log(`the sum of ${OL1} and ${OL2} is :${OL1+OL2}`);

    // Escape charactors in javascript.
        console.log(`-----------Escape Characters------------`);
        // Escape characters in JavaScript strings are used to represent characters that are difficult or impossible to type directly in the code. Escape characters are preceded by a backslash \. 
        // Here are some common escape characters in JavaScript:
        // 1 \n (for next line)
        console.log('the line has been broken now\nand see the result.');
        // 2 \t (for a tab space )
        let esc='the tab space is applied\tnow .....enjoy.'
        console.log(esc);
        
        console.log(`-----------String Methods------------`);
    // String Methods.---(the buildin functions to manipulate the string.)
    // "IN JAVASCRIPT THE STRINGS ARE IMMUTABEL" due to this the methods can not change the origenal strings weather we can save the method's output in a new variable. 

    // there are a lot of methods , some of them are follwing:
        // 1-- Str.toUpperCase()
        let newString='Books';
        console.log(newString.toUpperCase());
        // 2-- Str.toLowerCase()
        newString='BOOKS';
        console.log(newString.toLowerCase());
        // 3-- Str.trim()---used to trim the spaces from start and last not the middle.
        newString='                BOOKS are good      Friends.     ';
        console.log(newString.trim());
        // 4-- Str.slice(start index,ending index (not included))--- to get a part of string.
        newString='Slice';
        console.log(newString.slice(1,4));
        // can be useable by single parameter i.e from the starting index to the last of the string.
        console.log(newString.slice(1));
        // 5-- Str1.concat(str2)
        newString='Ali';
        let newString1=' Faraz';
        console.log(newString.concat(newString1));
        // 6-- Str.replace(serchValue,newValue); --- if there are two or more letters you serched then it will triggre the first one.
        newString='Hello';
        console.log(newString.replace('l','m'));
        // *> str.replaceAll(serchVal,newVal);--- to change all the same letters you serched
            newString='Helllllo';
            console.log(newString.replaceAll('l','m'));
        // 7-- Str.charAt(index);
        newString='Farrukh';
        console.log(newString.charAt(0));
        console.log(newString.charAt(1));
        // also works like array
        console.log(newString[2]);
        console.log(newString[3]);
        console.log(newString[4]);
        console.log(newString[5]);
        console.log(newString[6]);



    // the strings are immutable in javascript
        newString='IMLearningJS';
        newString[0]='U';
        console.log(newString);//the answer will : IMLearningJS -- not UMLearning JS because the strings are immuatable in javasctipt.
        // to do this we can use replace method.


// 4.  boolean/bool

let d = true;
let e = false; 
let f = 1;
let g = 0;
console.log(d);
console.log(e);
console.log(f);
console.log(g);

// 5.  array (array can store a number of data in it. we can target each of the data with it index number , index number is just like a roll number , the first value of array has index number (0) then (1) then(2) and ... )
    // the arrays are mutable in javascript.
     
let h = [1,22,24,12,];
console.log(h);
console.log(h[0]);
console.log(h[1]);
console.log(h[2]);
console.log(h[3]);

    // we can store any type of data in array

    let i = [1,2.3,'farrukh maqsood 12    @#$',true,[1,2,3,4]];
    console.log(i);
    console.log(i[2]);
    console.log(i[4][2]);

    //there are major two types of array
        // 1. two dimentional array
        
        let j=[1,2,[3,4,5]];
        console.log(j[2][1]);

        // 2.  three dimentional array

        let k=[1,2,[3,4,[5,6]]];
        console.log(k[2][2][1]);


// OPERATORS
console.log("ASSINGMENT OPERATORS");
    // 1.assignment operators (= ,+= ,-= ,*= , /=,%= ,**=)

    // =
    let l = 2;//right value is assigned to the left one.

    // +=
    let a1 = 6;
    console.log("a1=",a1);
    a1 += 4;//a1=a1+4
    console.log("after (a1 += 4), a1=",a1);//10

    //-=
    let b1 = 7;
    console.log("b1=",b1);
    b1 -= 4;//b1=b1-4
    console.log("afer (b1 -= 4) b1=",b1);//3

    //*=
    let c1 = 5;
    console.log("c1=",c1);
    c1 *= 4;//c1 = c1 * 4
    console.log("after (c1 *= 4), c1=",c1);//20

        // /=
        let c11 = 5;
        console.log("c11=",c11);
        c11 /= 4;//c11 = c11 / 4
        console.log("after (c11 /= 4), c11=",c11);//1.25

    //%=
    let d1 = 35;
    console.log("d1=",d1);
    d1 %= 10;//d1 = d1 % 10
    console.log("after (d1 %= 10), d1=",d1);//5

    //**=
    let e1 = 2;
    console.log("e1=",e1);
    e1 **= 3;//e1 = e1 **3
    console.log("after (e1 **= 3), e1=",e1);//8






    // 2.arithmatic operators (+ - * / % ** ++ --)
    let m = 10;
    let n = 15;

        //  +
        console.log(m+n);
        console.log(m+10);

        //  -
        console.log(m-n);

        //  *
        console.log(m*n);
        console.log(m*2);

        //  /
        console.log(m/n);
        console.log(m/2);

        // % (it devides two values just like this 12/5 and gives the reminder/modulus  bw two values like 2 is reminder in this case)
        console.log(m%3);
        console.log(m%n);

        // ** (it is used to generate the power of any vlaue like 3**2=the square of 3)
        console.log(3**2);
        console.log(m**n);

        //  ++ (it is used to add 1 in the vlaue (z=z+1)=(z++) )
        // m=m+1;





        let x = 12; 
        let y = 10;
        console.log("x=",x);
        console.log("y=",y);
        // this is called post increment (a++) it changes the value from next line
            console.log( "value of x++ =", x++);//the value of x will be 13 from the next line.
            console.log("now x =",x);//now it is 13.
        // this is called pre increment (++a) it changes the value in same line
        console.log("value of ++y =", ++y );

        
        m++;
        console.log(m);

        let o=12.12;
        o++;
        console.log(o);

        let p=false;
        p++;
        console.log(p);

        let q=[1,2];
        q[1]++;
        console.log(q);




        // -- (it is used to subtract 1 from the vlaue (z=z-1)=(z--) )
        let r=10;

        // r=r-1;
        r--
        console.log(r);

        let s=12.12;
        s--;
        console.log(s);

        let t=false;
        t--;
        console.log(t);

        let u=[1,2];
        u[1]--;
        console.log(u);

        

        let z1 = 12; 
        let z2 = 10;
        console.log("z1=",z1);
        console.log("z2 =",z2);
        // this is called post decrement (a--) it changes the value from next line
            console.log( "the value of z1-- =", z1--);//the value of x will be 13 from the next line.
            console.log("now z1 =",z1);//now it is 13.
        // this is called pre increment (++a) it changes the value in same line
        console.log("value of --z2 =", --z2 );

