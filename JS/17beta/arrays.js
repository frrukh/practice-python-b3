// Arrays
//we can store any type of data in array, even store an array in an array.
//Declaration of array.
    //Method 1----
    //syntax ----  let arrayName=[item1,item2,item3...];
    let a = [12,12.3,true,"farrukh",["abdullah","farhan",12]];
    console.log(a);

    // Method 2---- in this method first we declare the array and then declare the items in different lines.
    //syntax ---- let arrayName=[];  arrayName[0]=12; arrayName[1]=12.2; arrayName[2]=true;
    let b = [];
    b[0]=11;
    b[1]=14.2;
    b[2]=false;
    b[3]="farrukh.";
    console.log(b);

    //Method 3----
    //syntax ---- let arrayName = new Array(14,14.76,true,"talha"...);
    let c = new Array(13,19.4,true,"Maqsood Ahmed");
    console.log(c);
    let farrukh=new Array(12);


//Array Access.
    //to access any item of array we can call that with its index number.
    //index number starts from 0 then 1 then 2 and so on.
let d = [98,41,23.3,"farrukh",[true,[34,"farrukh","farhan",[12,23,345]]]];
console.log(d[0]);
console.log(d[1]);
console.log(d[2]);
console.log(d[3]);
    // we can make array in side an array and call it by index number like this.
console.log(d[4][1][3][2]);

// to check the type of any variable.

    //  1-- typeof arrayName.
let num=12;
let dec=12.21;
let bool=true;
let str="farrukh";
let arr=[14,24.5,true,"farqan",[1,"farrukh"]];
console.log(typeof num);
console.log(typeof dec); // it treets decimal as a number.
console.log(typeof bool);
console.log(typeof str);
console.log(typeof arr);// it treets array as an object.
console.log(typeof arr[4][1]);

    //  2-- arrayName instanceof Array/Object/Number/String---(instance means example.)
    // it gives the value in true of false. we generaly use it to check if it is an array of not.
let array=["farrukh","farhan"];
console.log(array instanceof Number);
console.log(array instanceof String);
console.log(array instanceof Array);
console.log(array instanceof Object);

    //  3-- Array.isArray(arrayName)
//it also gives the answer in true and false and tells than it is array of not.
let Arr=["farrukh",123,false,12.3];
console.log(Array.isArray(Arr));


                        // Array Functions

//convert the array into a string.
    // 1--- tostring()----arrayName.tostring();
let aarry=[12,13.3,132,21,"farrukh",true];
let arr_to_str=aarry.toString();
console.log(arr_to_str);
    //2--- join()---arrayName.join(the symbol you want to add between the items insteed of comaas)
let array_to_str=aarry.join("#");
console.log(array_to_str);



// make changes in array.
    //push---to add the values in the LAST of an array.
    //syntax-- arrayName.push(values you want to add);
let arrayPush=[12,31,true,500,"farrukh"];
console.log(arrayPush);
arrayPush.push(111,11,1);
console.log(arrayPush);
    //pop---to delete a single value from the LAST of an array. 
    //syntax-- arrayName.pop(); 
let arrayPop=[1,2,3,4,5,6,7,8,9]
arrayPop.pop();
arrayPop.pop();
arrayPop.pop();
arrayPop.pop();
arrayPop.pop();
arrayPop.pop();
arrayPop.pop();
console.log(arrayPop);
    //unshift---to add value at the START of an array.
    //syntax--- arrayName.unshift(values you want to add);
let arrayUnshift=[1,2,3,4];
arrayUnshift.unshift(-4,-3,-2,-1,0);
console.log(arrayUnshift);
    //shift---to remove a single value from the Start of an array.
    //syntax--- arrayName.shift();
let arrayShift=[1,2,3,4,5];
arrayShift.shift();
arrayShift.shift();
arrayShift.shift();
console.log(arrayShift);
    //splice---this function is used to add and remove the values from start,end and also in between an array.
    //syntax--- arrayname.splice(index number of the place you want to add or remove,  number of values you want to remove,  values you want to add);
//removing values.
let arraySpliceRemove=[12,13,14,15,16,17,18,19,9999,999,99,9,0];
arraySpliceRemove.splice(2,3);
console.log(arraySpliceRemove);
//adding values
let arraySpliceAdd=[12,13,14,15,16,17,18,19,9999,999,99,9,0];
arraySpliceAdd.splice(1,0,12.2,12.4,12.6,12.8)
console.log(arraySpliceAdd);
//adding and removing.
let arraySplice=[12,13,14,15,16,17,18,19,9999,999,99,9,0];
arraySplice.splice(4,4,"16-19");
console.log(arraySplice);

    //slice---to get a chunk/slice from an array without affecting the original array.
    //syntax---arrayName.slice(from-index(included),to-index(not included));
let pizza=[0,1,2,3,4,5,6,7,8,9,10];
let slice=pizza.slice(3,7);
console.log(slice);


                    // functions ended---



    //delete---to delete a single index from an array.
    //syntax---delete arranName[index you want to delete];
let del=[0,1,2,3,4,5,6];
delete del[2];
console.log(del);
    //updating the index value.
let updatingArray=[12,13,14,12];
updatingArray[1]=99999;
console.log(updatingArray);



//Concatination.
    //string
    console.log('apple'+'mango');
    //concat--- array  (this is a function.)
let a1=[1,2,3];
let a2=[4,5,6];
let concated=a1.concat(a2);
console.log(concated);




//indexof---get index of any value of array.
//if there are some same values in an array it gives the index of first one.
//index---arrayName.indexof(value present in array);
let indexArr=[1,4,6,4,5,4];//there are three 4 but it maps only the first one.
let index=indexArr.indexOf(4);
console.log(index);

let index1=indexArr.indexOf(4.2389);
console.log(index1);//if the value is not present in array it shows -1.

//lastIndexOf---if there are some same values in an array it gives the index of last one.
let l_ind=[1,2,3,2,4,2,6];
let lastIndex=l_ind.lastIndexOf(2);
console.log(lastIndex);

//includes---check if the given value is present in array or nor and gives the answer in true and false.
// syntax---arrayName.includes(value);
let value=[12,13,4,24,5,35,64,4];
console.log(value.includes(12));
console.log(value.includes(1));





let myArray = [1, 2, 3, 4, 5];

// Using the pop() method
let lastItem = myArray.pop();

console.log(lastItem); // Output: 5
console.log(myArray);   // Output: [1, 2, 3, 4]