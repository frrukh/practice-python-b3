let data=[
    {
        name:"Ali",
        age:14,
        registrationNumber:4323,
        course:"website development",
        favorateProgrammingLanguages:["C#","C","JavaScript","SQL","Swift"],
        subjectMarks:{
            english:98,
            urdu:81,
            math:90,
            physics:96,
            chemistry:100
        }
        
    },{
        name:"Ahmed",
        age:18,
        registrationNumber:4321,
        course:"application development",
        favorateProgrammingLanguages:["C","C++","Java","Python","JavaScript"],
        subjectMarks:{
            english:88,
            urdu:80,
            math:99,
            physics:90,
            chemistry:73
        }
    },{
        name:"Raju",
        age:20,
        registrationNumber:7832,
        course:"Python",
        favorateProgrammingLanguages:["Cobol","C++","Java","Python","Dart","C","JavaScript","HTML","CSS"],
        subjectMarks:{
            english:90,
            urdu:89,
            math:100,
            physics:76,
            chemistry:89
        }
    }
]

console.log("------details of Ali------");
console.log("Name : "+data[0].name);
console.log("Age : "+ data[0].age);
console.log("Registration number : "+ data[0].registrationNumber);
console.log("Course : "+ data[0].course);
console.log("Favorate Programming Languages : "+ data[0].favorateProgrammingLanguages);
console.log("Marks : ");
console.log("   ---> English:"+data[0].subjectMarks["english"]);
console.log("   ---> Urdu:"+data[0].subjectMarks["urdu"]);
console.log("   ---> Math :"+data[0].subjectMarks["math"]);
console.log("   ---> Physics :"+data[0].subjectMarks["physics"]);
console.log("   ---> Chemistry:"+data[0].subjectMarks.chemistry);
console.log("------details of Ahmed------");
console.log(data[1]);

console.log("------details of Ahmed------");
console.log("Name : "+data[1].name);
console.log("Age : "+ data[1].age);
console.log("Registration number : "+ data[1].registrationNumber);
console.log("Course : "+ data[1].course);
console.log("Favorate Programming Languages : "+ data[1].favorateProgrammingLanguages);
console.log("Marks : ");
console.log("   ---> English:"+data[1].subjectMarks["english"]);
console.log("   ---> Urdu:"+data[1].subjectMarks["urdu"]);
console.log("   ---> Math :"+data[1].subjectMarks["math"]);
console.log("   ---> Physics :"+data[1].subjectMarks["physics"]);
console.log("   ---> Chemistry:"+data[1].subjectMarks.chemistry);
console.log("------details of Ahmed------");
console.log(data[1]);

console.log("------details of Raju------");
console.log("Name : "+data[2].name);
console.log("Age : "+ data[2].age);
console.log("Registration number : "+ data[2].registrationNumber);
console.log("Course : "+ data[2].course);
console.log("Favorate Programming Languages : "+ data[2].favorateProgrammingLanguages);
console.log("Marks : ");
console.log("   ---> English:"+data[2].subjectMarks["english"]);
console.log("   ---> Urdu:"+data[2].subjectMarks["urdu"]);
console.log("   ---> Math :"+data[2].subjectMarks["math"]);
console.log("   ---> Physics :"+data[2].subjectMarks["physics"]);
console.log("   ---> Chemistry:"+data[2].subjectMarks.chemistry);
console.log("------details of Raju------");
console.log(data[2]);


console.log("FAVORATE PROGRAMMING LANGUAGES OF RAJU");
let fav_lang_length= [data[2].favorateProgrammingLanguages.length]-1

console.log("First : "+data[2].favorateProgrammingLanguages[0]);
console.log("Last : "+data[2].favorateProgrammingLanguages[fav_lang_length]);


