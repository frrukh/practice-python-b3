// simple array.
let array=[1,2,3,4,true];
console.log(array[1]);//2
// multi-dimentional array.
// 2-d
let array2d=[[12,2],[12,1]];
console.log(array2d[1][0]);//12
// 3-d
let array3d=[[[32,23,8],[23,24]]];
console.log(array3d);
console.log(array3d[0][1][1]);//24

// Objects---defines from curly braces and consist of keys and data differed by colon .
    let student_obj={
        firstName: "Ali",
        lastName:"Akbar",
        course:"Python",
        age:19
    }
    console.log(student_obj);

    //Access object values
    student_obj={
        firstName: "Ali",
        lastName:"Akbar",
        course:"Python",
        age:19
    }
        //method 1
        console.log(student_obj["lastName"]);
        //method 2---when we type (.) it suggests the all keys present in the given object.  
        console.log(student_obj.course);

    //Add new keys in object.
    student_obj={
        firstName: "Ali",
        lastName:"Akbar",
        course:"Python",
        age:19
    }
        //method 1 -inverted commas are essential here on both.
        student_obj["address"]="Lahore";
        console.log(student_obj);
        //method 2 -inverted commas are essential here on both.
        student_obj.tel="03012345678";
        console.log(student_obj);

    //Update existing key
        // Method 1
        student_obj["firstName"]="Abdullah";
        console.log(student_obj);
        // Method 2
        student_obj.lastName="Maqsood";
        console.log(student_obj);

    //delete object key
    delete student_obj["age"];
    console.log(student_obj);

    delete student_obj.lastName;
    console.log(student_obj);

    // reset any key 
    // in reseting we simply initialize the key according its datatype.
    student_obj={
        firstName: "Ali",
        lastName:"Akbar",
        course:"Python",
        age:19,
        phone:"020302020"
    }
    student_obj["firstName"]="";
    student_obj.age=-1;
    student_obj.phone="";
    console.log(student_obj);


    //............//
    student_obj={
        firstName: "Ali",
        lastName:"Akbar",
        course:"Python",
        age:19,
        phone:"03123456789"
    }
    //............//

    // get keys of any object in string formate.
    let keys=Object.keys(student_obj);
    console.log(keys);
    
    // get values of any object in string formate.
    let values=Object.values(student_obj);
    console.log(values);

    // get keys and values of any object in 2-d string formate.
    let entries=Object.entries(student_obj);
    console.log(entries);
    