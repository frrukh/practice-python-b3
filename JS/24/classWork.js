// click to change background color,
    let color=document.getElementById('color');
    color.addEventListener('click',function(){
        color.classList.toggle('bclr');
    });

    let col=document.getElementById('col');
    col.addEventListener('click',()=>{
        if(col.style.backgroundColor=='yellow'){
            col.style.backgroundColor='white';
        }else{
            col.style.backgroundColor='yellow';
        }
    });

// increment and decrement

    let reset=document.getElementById('reset');
    let decrement=document.getElementById('decrement');
    let increment=document.getElementById('increment');
    let div=document.getElementById('div');
    let count=div.value;
    console.log(count);
    decrement.addEventListener('click',function(){
        div.value=--count;
        console.log(count);
    });
    increment.addEventListener('click',function(){
        div.value=++count;
    });
    reset.addEventListener('click',()=>{
        count=0;
        div.value=count;
    });

// removint items
    let item1=document.getElementById('item1');
    let item2=document.getElementById('item2');
    let item3=document.getElementById('item3');
    let item4=document.getElementById('item4');
    let item5=document.getElementById('item5');

    item1.addEventListener('click',function(){
        item1.style.display='none';
    });

    item2.addEventListener('click',function(){
        item2.style.display='none';
    });

    item3.addEventListener('click',function(){
        item3.style.display='none';
    });

    item4.addEventListener('click',function(){
        item4.style.display='none';
    });

    item5.addEventListener('click',function(){
        item5.style.display='none';
    });

// image rezizing
    let img=document.getElementById('img');
    let btn=document.getElementById('btn');
    let width='500px';
    btn.addEventListener('click',function(){
        console.log('event triggered')
        if(img.style.width!=width){
            img.style.width=width;
            btn.innerText='Click to resmall the imange'
        }else{
            img.style.width='150px';
            console.log('done')
            btn.innerText='Click to enlarge the image'
        }
    });

// change background color
let clr=document.getElementById('clr');
clr.addEventListener('input',function(){
    let color1=clr.value;
    let body=document.querySelector('body');
    body.style.backgroundColor=color1;
});

// add new input field.
let count1=1;
let container=document.getElementById('container');
let btn1=document.getElementById('btn1');
btn1.addEventListener('click',function(){
    count1++;
    let new_inp=document.createElement('input');
    new_inp.setAttribute('name','input'+count1);
    new_inp.setAttribute('placeholder','input-'+count1);
    new_inp.style.display='block';
    container.append(new_inp);
});

// luckey draw
let names=['Ali','Ahmed','Arsalan','Azad chaiwala','Anas','Akram','Akmal','Aslam','Arham'];
console.log(names.length);
let btn2=document.getElementById('btn2');

btn2.addEventListener('click',()=>{
    alert(names[Math.floor(Math.random()*names.length)]);
});