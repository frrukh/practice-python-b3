// PROJECT
// Sum all the array elements by using a loop.
    console.log("---------------finding Sum---------------");
    // by for loop.
        let arr=[10,20,30,40,50];
        let sum=0;
        for(i=0; i<arr.length; i++){
            sum=sum+arr[i];
        }
        console.log("By for loop   : "+sum);
    
    // by for in loop.
        arr=[10,20,30,40,50,60,70];
        sum=0;
        for(let i in arr){
            sum = sum+arr[i];
        }
        console.log("By for in loop   : "+sum);

    // by for of loop
        arr=[10,20,30];
        sum=0;
        for(let i of arr){
            sum=sum+i;
        }
        console.log("By for of loop   : "+sum);
    
    // by for Each loop
        
        arr=[10,20,30];
        sum=0;
        let sum1=0;
        arr.forEach((val,ind)=>{
            sum=sum+val;// calculating sum by value.
            sum1=sum1+arr[ind];//doing same thing by using index.
        }
        )
        console.log("sum by value  : "+sum);
        console.log("sum by index  : "+sum1);
    
    // by while loop
        arr=[10,20,30,40,50,60];
        let ind=0;
        sum=0;
        let condition=true;
        while(condition==true){
            sum=sum + arr[ind];
            ind++
            if (ind==arr.length){
                condition=false;
            }
        }
        console.log("By while loop   : "+sum);
    
    // by do while loop.
        arr=[10,20,30,40,50];
        ind=0;
        sum=0;
        do{
            sum=sum+arr[ind];
            ind++;

        }while(ind<arr.length)
        console.log("By do while loop   : "+sum);


// Reverse the array by using a loop.
console.log("---------------finding Reverse of array---------------");

    // by for loop
        let array=[12,13,14,15,16,17,18,19,20];
        let result=[];
        for(i=array.length-1; i>=0; i--){
            result.push(array[i]);
        }
        console.log("By for loop  : "+result);
    
    // by for in loop
        array=[12,13,14,15,16,17,18,19,20];
        result=[];
        for(let i in array){
            result.unshift(array[i]);
        }
        console.log("By for in loop  : "+result);

    // by for of loop
        array=[12,13,14,15,16,17,18,19,20];
        result=[];
        for(let i of array){
            result.unshift(i);
        }
        console.log("By for of loop  : "+ result);
        
        // by for Each loop
        array=[12,13,14,15,16,17,18,19,20];
        result=[];
        array.forEach(function(value){
            result.unshift(value)
        }
        )
        console.log("By for Each loop  : "+ result);

    // by while loop
        array=[12,13,14,15,16,17,18,19,20];
        result=[];
        let len=array.length-1;
        while(len>=0){
            result.push(array[len]);
            len--;
        }
        console.log('By while loop  : '+result);

    // by do while loop
        array=[12,13,14,15,16,17,18,19,20];
        result=[];
        len=array.length-1;
        do{
            result.push(array[len]);
            len--;
        }while(len>=0);
        console.log("by do while loop  : "+result);
    
// Make a table of the given number with all possible loops.
console.log("---------------Creating Table---------------");

    // by for loop
        console.log("----------BY FOR LOOP----------");
        let num=2;
        for(i=1; i<11; i++){
            console.log(num+" X "+i+'  =  '+num*i);
        }
    
    // by for in loop 
        console.log("----------BY FOR IN LOOP----------");
        num=[1,2,3,4,5,6,7,8,9,10];
        let number=12;
        for(let a in num ){
            let b=num[a];
            console.log(number+'  X  '+b+'  :  '+number*b);
        }
            

    // by for of loop
        console.log("----------BY FOR OF LOOP----------");
        num=[1,2,3,4,5,6,7,8,9,10]
        number=3;
        for(let a of num){
            console.log(number+'  X  '+a+'  :  '+number*a);
        }
    // by for each loop
        console.log("----------BY FOR EACH LOOP----------");
        num=[1,2,3,4,5,6,7,8,9,10]
        number=21;
        num.forEach((value)=>{
            console.log(number+"  X  "+value+"  :  "+number*value)
        }
        )

    // by while loop
    console.log("----------BY WHILE LOOP----------");
    num=3;
    i=0;
    while(i<11){
        console.log( num+" X "+i+'  =  '+num*i);
        i++;
    }

    // BY DO While loop
    console.log("----------BY DO WHILE LOOP----------");
    num=7;
    i=0;
    do{
        console.log(num+'  X  '+i+'  =  '+num*i);
        i++;
    }while(i<11);


// Find the largest number in an array by using a loop.
console.log("---------------finding the largest number---------------");

    // by for loop
        arr=[12,13,43,54,204,296,386,423,42,3];
        let L_Num=arr[0];
        for(let i=1; i<arr.length; i++){
            if(L_Num<arr[i]){
                L_Num=arr[i];
            }
        }
        console.log("By for loop  : "+L_Num);

    // by for in loop
        arr=[12,13,43,54,204,296,386,423,42,3];
        L_Num=arr[0];
        for(let a in arr){
            if(arr[a]>L_Num){
                L_Num=arr[a];
            }
        }
        console.log("By for in loop  : "+L_Num);
        
    // by for of loop
        arr=[12,13,43,54,204,296,386,423,42,3];
        L_Num=arr[0];
        for(let a of arr){
            if(a>L_Num){
                L_Num=a;
            }
        }
        console.log("By for of loop  : "+L_Num);

    // by for each loop
        arr=[12,13,43,54,204,296,386,423,42,3];
        L_Num=arr[0];
        arr.forEach((value)=>{
            if(value>L_Num){
                L_Num=value;
            }
        }
        )
        console.log("by for each loop  : "+L_Num);

    // by while loop
        arr=[12,13,43,54,204,296,386,423,42,3];
        L_Num=arr[0];
        i=0;
        while(i<arr.length){
            if(L_Num<arr[i]){
                L_Num=arr[i];
            }
            i++
        }
        console.log("by while loop  : "+L_Num);

    // by do while loop
        arr=[12,13,43,54,204,296,386,423,42,3];
        L_Num=arr[0];
        i=0;
        do{
            if(arr[i]>L_Num){
                L_Num=arr[i]
            }
            i++;
        }while(i<arr.length);
        console.log("by do while loop  : "+L_Num);


// Find the smallest number in an array by using a loop.
console.log("---------------finding the smallest number---------------");

    // by for loop
        arr=[12,13,43,54,204,1,296,386,423,42,3];
        Smallest=arr[0];
        for(let i=0;i<arr.length;i++){
            if(arr[i]<Smallest){
                Smallest=arr[i];
            }
        }     
        console.log("by for loop  :  "+Smallest);
    
    // by for in loop
        arr=[12,13,43,54,204,1,296,386,423,42,3];
        Smallest=arr[0];
        for(let i in arr){
            if(arr[i]<Smallest){
                Smallest=arr[i];
            }
        }
        console.log("by for in loop  :  "+Smallest);

    // by for of loop
        arr=[12,13,43,54,204,1,296,386,423,42,3];
        Smallest=arr[0];
        for(let i of arr){
            if(i<Smallest){
                Smallest=i;
            }
        }
        console.log("By for of loop   :  "+Smallest);

    // by for each loop
        arr=[12,13,43,54,204,1,296,386,423,42,3];
        Smallest=arr[0];
        arr.forEach((value)=>{
            if(value<Smallest){
                Smallest=value;
            }
        }
        )
        console.log('by for each loop  :  '+Smallest);

    // by while loop
        arr=[12,13,43,54,204,1,296,386,423,42,3];
        Smallest=arr[0];
        let y=0;
        while(y<arr.length){
            if(y<Smallest){
                Smallest=arr[y];
            }
            y++;
        }
        console.log('by while loop  :  '+Smallest);

    // by do while loop
        arr=[12,13,43,54,204,1,296,386,423,42,3];
        Smallest=arr[0];
        let j=0;
        do{
            if(arr[j]<Smallest){
                Smallest=arr[j];
            }
            j++;
        }while(j<arr.length)
        console.log('by do while loop  :  '+Smallest);



// Make an array to store the name of 5 students and iterate with for and foreach loop.
console.log("---------------simpley consoling the array---------------");

    // by for loop
        let s_name=['Farrukh','Waqas','Ali','Ahmed','Farhan'];
        for(let i=0; i<s_name.length; i++){
            console.log('Student no  '+(i+1)+'  is  :  '+s_name[i]);
        }
    // by for each loop
        s_name=['Farrukh','Waqas','Ali','Ahmed','Farhan'];
        s_name.forEach(function(value,index){
            console.log('Student No  '+(index+1)+'  is  :'+value);
        }
        )


// Make an object to store the information of a student and iterate with a for-in loop.
console.log("---------------simpley consoling the object---------------");
// by for in loop
        let obj={
            firstName:'Farrukh',
            lastName:'Maqsood',
            age:18,
            course:'python',
            address:'sheikhupura'
        }
        for(let a in obj){
            console.log(a+'      :      '+obj[a]);
        }
            
     

        