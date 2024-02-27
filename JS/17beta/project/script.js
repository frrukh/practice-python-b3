// Find the last element of an array without giving a hard-coded index.

    // mehtod--1
let array=[1,2,3,4,5,6,7,8,9,1110];
    // In this case we can display an array whose index is array.lenght-1 as index starts from 0 and array length starts from 1 so the length of array is 1 divit grater than the highest index of the array so we subtract 1 to targe the last index.
console.log(array[array.length -1]);

    // mehtod--2
array=[1,2,3,4,5,6,7,8,9,1110];
    //the pop function removes the last value and alwasys returns the removing value and we can store it in a variable like this.
let lastElement=array.pop();
console.log("lastElement is : "+ lastElement);


// Check whether the first or the last index of an array has a specified value, let's say 5.
let arr=[5,3,2,4,6,5];
console.log(arr);
if (arr[0]==arr[arr.length-1]){
    console.log("the first and last indexes of the array are specified i.e "+arr[arr.length-1])
}else{
    console.log("the first and last indexes of the array are not same.")
}

// Make an array to store the names of students and check whether that array has your own name or not and also return the index of that value.
let name_array=["Talha","Taha","Farhan","Ali","Ahmad","Farrukh","Abdullah","Faraz","Noman"];
console.log(name_array.includes("Farrukh"));
index=name_array.indexOf("Farrukh");
console.log("index of my name is : "+index);

//Add the array element at the specified index.
let add_array=[1,2,3,4,5,6];
add_array.splice(3,0,888);
console.log(add_array);

//Delete the array element from the specified index.
let del_array=[12,42,3.7,5,"delete",true,6];
delete del_array[4];
console.log(del_array);





console.log("----------------------------the asignment given from the institute is ended here------------------------")


































// find the type of the given variables
console.log("find the type of given");
let a=12;
let b=12.3;
let c=false;
let d="rockstar";
let e=[12,13,14,15,16];

console.log("type of a=12 : "+typeof a);
console.log("type of b=12.3 : "+typeof b);
console.log("type of c=false : "+typeof c);
console.log("type of d=rockstar : "+typeof d);
console.log("type of e=[12,13,14,15,16] : "+typeof e);

// check if these are instance of number string array or object or not.
console.log("Is instance of number/string /array/object or not.")

console.log("e=[12,13,14,15,16]");

console.log(e instanceof Number);
console.log(e instanceof Number);
console.log(e instanceof Boolean);
console.log(e instanceof String);
console.log(e instanceof Array);
console.log(e instanceof Object);
        //in case of instanceof concatination is not allowed if we concatinate it gives wrong answer. 
console.log("e : "+e instanceof Object);

//is array or not.
console.log("Is array of not.")
e=[12,13,14,15,16];
f="farrukh";
console.log(Array.isArray(f));
console.log(Array.isArray(e));










//  rough work.
let array1=[1,2,3,45,6,7,8];
let [first, ...middle]=array1;
console.log(first);
console.log(middle);
console.log(middle[middle.length-1]);



