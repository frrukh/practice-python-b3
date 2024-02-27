let num = prompt("enter your number's percentage (0-100)");

console.log("num.in % =",num);
if(num<101 && num >= 0){
    if(num<50){
        console.log("fail");
    }else if(num>=50 && num<60){
        console.log("E Grade");
    }else if(num>=60 && num<70){
        console.log("D Grade");
    }else if(num>=70 && num<80){
        console.log("C Grade");
    }else if(num>=80 && num<90){
        console.log("B Grade");
    }else if(num>=90){
        console.log("A Grade");
    }
}else{
    console.log("plese refresh the page and enter the valid percentage")
}