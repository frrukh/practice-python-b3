let questions=[
    {
        'title':'What is 10 / 2 ?',
        'options':[10,5,6,20],
        'correctAnswer':5
    },
    {
        'title':'What is 9 X 2 ?',
        'options':[17,18,95,20],
        'correctAnswer':18
    },
    {
        'title':'What is 6 X 4 ?',
        'options':[1,28,12,24],
        'correctAnswer':24
    },
    {
        'title':'What is the capital of Pakistan ?',
        'options':['Lahore','Karachi','Kashmir','Islamabad'],
        'correctAnswer':'Islamabad'
    },
    {
        'title':'Which animal can live in land and watter ?',
        'options':['Lion','Monkey','Hippo','goat'],
        'correctAnswer':'Hippo'
    }

]
console.log('options length : '+questions.length)

let index=0;
let score=0;
let current_question=questions[index]
start();

function start(){
let btn=document.getElementById('btn');
btn.addEventListener('click',function(){
   addButtons();
});
}

function addButtons(){
current_question=questions[index];
let container=document.getElementById('container');
container.innerHTML='<h1>'+current_question.title+'</h1>';
for(let option of current_question.options){
    let newBtn=document.createElement('button');
    newBtn.setAttribute('type','button');
    newBtn.innerText=option;
    container.append(newBtn);
}
check()
}

function check(){
let options = document.querySelectorAll('button');
for(let option of options){

    option.addEventListener('click',()=>{
        if(option.innerText==current_question.correctAnswer){
            score++;
        }
        index++;
        if(index<questions.length){
        addButtons()
        }else{
            gameOver()
        }
    });
}
}

function gameOver(){
container.innerHTML='<h1>Game Over!</h1> <br><br> <h1>'+score+'/'+questions.length+'</h1>';
let button=document.createElement('button');
button.setAttribute('type','button');
button.setAttribute('id','btn');
button.innerText='Restart';
container.append(button);
button.addEventListener('click',function(){
    index=0;
    score=0;
    start();
});
}