console.log("----------1----------");
// Find the last element of an array without giving a hard-coded index.

console.log("           -----method-1-----");
    // method 1---Array will disturbed.
let array=[1,23,34,5,64,75,686,76,465,45,53,34,434,4,2,23,32];
let lastValue=array.pop();
console.log(lastValue);
console.log(array);

console.log("           -----method 2-----");
// method 2---Array will not disturbed.
let array1=[1,23,24,24,25,3,355,53,356,3464,64];
let lastValue1=array1[array1.length -1];
console.log(lastValue1);


console.log("----------2----------");
//Check whether the first or the last index of an array has a specified value, let's say 5. 
let arr=[5,3,35,7,5];
console.log(arr);
if(arr[0]===arr[arr.length -1]){
    console.log("first and last index of array have same value")
}else{
    console.log("the first and last index of array not have same value")
}


console.log("----------3----------");
//Make an array to store the names of students and check whether that array has your own name or not and also return the index of that value.
let arr1=["ahmad","talha","ali","hammad","farrukh","muzammil"];
let my_name=arr1.includes("farrukh");
console.log("my name is present in array : "+my_name);
let indexOfMyName=arr1.indexOf("farrukh");
console.log("the index of my name is :"+indexOfMyName);


console.log("----------4----------");
//Add the array element at the specified index.

let a=[1,2,3,4,5,7];
a.splice(5,0,6);
console.log(a);


console.log("----------5----------");
//Delete the array element from the specified index.

let b=[1,2,34,5,6,7,];
b.splice(2,1);
console.log(b);