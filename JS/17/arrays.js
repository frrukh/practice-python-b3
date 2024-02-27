// Declaration of array
    // method-1
        let array=[1,2,3,4,5,6];
    // method-2
        let arr=new Array (2,3,4,5);
        console.log(arr);
    // method-3
        let arr1=[];
        arr1[0]=12;
        arr1[1]=13;
        arr1[2]=14;
        console.log(arr1);
    
// Check Data Type
    // typeof 
        let a=12;
        let b=12.3;
        let c="false";
        let d=true;
        let e=[12,13,14,15];
        console.log(typeof a);
        console.log(typeof b);
        console.log(typeof c);
        console.log(typeof d);
        console.log(typeof e);
    // instanceof
        e=[12,13,14,15];
        console.log(e instanceof Array);
        console.log(e instanceof Object);
        console.log(e instanceof String);
        console.log(e instanceof Number);

            let f = e instanceof Array;
            console.log(f);
    // isarray
        a=12;
        b=12.3;
        c="false";
        d=true;
        e=[12,13,14,15];
        console.log(Array.isArray(a));
        console.log(Array.isArray(b));
        console.log(Array.isArray(c));
        console.log(Array.isArray(d));
        console.log(Array.isArray(e));

            let g= Array.isArray(e);
            console.log(g);
        
// Array Functions.
    // Array conversion.
        // toString()
            e=[12,13,14,15];
            console.log(e.toString());
                let h=e.toString();
                console.log(h);
        // join()
            e=[12,13,14,15];
            console.log(e.join("---"));
                let i=e.join("+");
               console.log(i);

    // Adding and Removing Elements.
        //push()--add in end.
            e=[12,13,14,15];
            e.push(1,2,3);
            console.log(e);
                let j = e.push(4,5,6); // it is returning the length of the array.
                console.log(j);
                console.log(e);
        // pop()---remove single vlaue form end
            e=[12,13,14,15];
            e.pop();
            console.log(e);
                let k=e.pop();  // it is returning the value that is removing through pop().
                console.log(k);  
                console.log(e);
        // unshift()---add in start.
            e=[12,13,14,15];
            e.unshift(9,10,11);
            console.log(e);
                let l = e.unshift(6,7,8); // it is also returning the lenght of the array.
                console.log(l);
                console.log(e);
        // shift()---remove single value from start.
            e=[12,13,14,15];
            e.shift();
            console.log(e);
                let m=e.shift();  //it is retyrning the value that is removing through shift().
                console.log(m);
                console.log(e);
        //  splice()---add or remove a number of valus from any index.
        //  syntax arrayname.splice(form which index(included),   how many values to remove,    value1 to add,value 2 to add,value 3 to add...)
            e=[12,13,14,15,16,17,18];
            e.splice(1,3,31,41,51);
            console.log(e);
                e=[12,13,14,15,16,17,18];
                let n=e.splice(3,2);    // returning the vlaues remove by splice in array form.
                console.log(n);

                e=[12,13,14,15,16,17,18];
                let o=e.splice(2,0,13.3,13.6,13.9);  // returning empty array.
                console.log(o);

                e=[12,13,14,15,16,17,18];
                let p=e.splice(1,2,15);  // returning only the values that are removed by splice.
                console.log(p);
                console.log(e);
        //  slice()---to get a slice from the pizza I means array without disturbing the orignal array so we always store it in a variable or display directly.
        //syntax---arrayname.slice(from index(included),to index(not included))
            e=[12,13,14,15,16,17,18];
            let q=e.slice(1,3);
            console.log(q);
        
        //  delete--- this is a keyword not a function.it can delete a single element of an array and can't delete a compelete array.
            e=[12,13,14,15,16,17,18];
            delete e[0];    // it will not delete that index, it only deletes its value so in array the deleted index is showen as [empty,13,14,15,16,17,18]
            console.log(e);
        
    // Concatenation of Arrays.
        // the concatenation of strinos is like :
                    console.log("muhammad "+"farrukh");
        //concat()
            let r=[-3,-2,-1,0,1,2];
            let s=[3,4,5,6,7,8];
            console.log(r.concat(s));
                let t=r.concat(s); // returning full array after concatenation.
                console.log(t);
    // Find the index of any value in Array.
        //  indexOf()
            e=[12,13,14,15,16,17,12,78,90,12,18];
            console.log(e.indexOf(17));
            console.log(e.indexOf (12));// if there are same values present on multi indexes it shows the index of first one.
            console.log(e.indexOf(171));// if the value is unavailable in array it shows -1.
            let u=e.indexOf(18);    // simple...returning the index of give value i.e 18.
            console.log(u);
        //  lastIndexOf() if there are same values present on multi indexes it shows the index of the last one.
            e=[12,13,14,15,16,17,12,78,90,12,18];
            console.log(e.lastIndexOf (12));
            console.log(e.lastIndexOf (13));//also works like indexOf if the value is unique in the array.
                let v=e.lastIndexOf(12);// stores the index.
                console.log(v);
        
    //Check wether the value is present in array or not.
        // includes()---result=true/false.
            e=[12,13,14,15,16,17,18];
            console.log(e.includes(14));//true,
            console.log(e.includes(140));//false.
                let w=e.includes(18);//returning the boolean value.
                console.log(w);