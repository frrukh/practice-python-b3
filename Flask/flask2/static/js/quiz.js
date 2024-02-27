let questions=[
    {
        title:'What is 100 / 5 ?',
        options:[20,30,10,50],
        'correctAnswer':20
    },
    {
        title:'What is 100 * 5 ?',
        options:[200,300,250,500],
        'correctAnswer':500
    },
    {
        title:'What is 9 / 2 ?',
        options:[5,4.5,3,4],
        'correctAnswer':4.5
    },
    {
        title:'What is the capital of India ?',
        options:['Kolkata','New Dehli','Hyderabad','Mumbai'],
        'correctAnswer':'New Dehli'
    },
    {
        title:'Which country is superpower currently ?',
        options:['Japan','Amarica','China','India'],
        'correctAnswer':'Amarica'
    }
]

let index=0;
let score=0;
let currentQuestion=questions[index];
start()
function start(){
    index=0;
    score=0;
    let button=document.querySelector('button');
    button.addEventListener('click',function(){
        addButtons();
    });
}

let container=document.querySelector('div')
function addButtons(){
    currentQuestion=questions[index];
    container.innerHTML='<h1>'+currentQuestion.title+'</h1>';
    
    let options=currentQuestion.options;
    for(let option of options){
        const btn=document.createElement('button');
        btn.innerText=option;
        btn.setAttribute('type','button');
        container.append(btn);

        btn.addEventListener('click',()=>{
        if(btn.innerText==currentQuestion.correctAnswer){
            score++;
        }
            check();
        });
    }

}

function check(){
   
    index++;
    if(index<questions.length){
        addButtons();
    }else{
        gameover()
        // console.log('gameover')
    }
}
function gameover(){
    if(score<3){
    container.innerHTML='<h1>Game Over!😑</h1> <br> <h1>'+score+'/'+questions.length+'</h1>'
}else if(score>3){
    container.innerHTML='<h1>Game Over!🤩</h1> <br> <h1>'+score+'/'+questions.length+'</h1>'
}else{
    container.innerHTML='<h1>Game Over!😯</h1> <br> <h1>'+score+'/'+questions.length+'</h1>'
}
    let button=document.createElement('button');
    button.setAttribute('type','button');
    button.innerText='Restart';
    container.append(button);
    start();
}