let input = document.getElementById('input');
let form = document.getElementById('form');
let ul = document.getElementById('ul');
ul.innerHTML=localStorage.getItem('tasks');

// this is to make the input preselected when the page is opened or refreshed.
window.onload=function (){
    input.focus();
}
highlight();

form.addEventListener('submit', function (e) {
    e.preventDefault();
    addtask();
    highlight();
    store();
});

function addtask() {
    highlight();
    let task = input.value;
    let li = document.createElement('li');
    li.innerHTML = `<span>${task}</span><button class='del'>X</button>`;
    li.classList.add('li_item')
    ul.prepend(li);
    input.value = '';
    deleteTodo();
    store();
}


deleteTodo();
function deleteTodo() {
    let del = document.getElementsByClassName('del');
    for (let i of del) {
        i.addEventListener('click', function () {
            i.parentElement.remove();
            store();
        })
    }
}

let li = document.getElementsByTagName('li');
li.addEventListener('click',()=>{
    highlight();
});

function highlight(){
    let li = document.getElementsByTagName('li');
    for(let i of li){
        i.addEventListener('click',function(){
            i.classList.toggle('todoitem');
            store();
        });
    }
}

function store(){
    let tasks=ul.innerHTML;
localStorage.setItem('tasks',tasks)
}