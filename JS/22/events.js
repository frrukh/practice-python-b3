// -----------------EVENTS-----------------
// in events we set a functon to do when the user perform a specific task.
    // addEventListenet--- we use addEvenetListener to add any event.
    // syntax---variabel.addEventListener('specific words to tell the computer that when the event will works',function that runs when the user perform that specific task,this parameter is optional)
// methods to use addEventListener.
        // method 1 using general function
        let btn = document.getElementById('button');

        btn.addEventListener('click',fung);//---(here click means if the user click on it the event will tracked)

        function fung(){
            btn.style.backgroundColor='pink';
            btn.innerText='Clicked(General)';
        }

        // method 2 using anonymeous function
        let btn1=document.getElementById('button1');

        btn1.addEventListener('click',function(){
            btn1.style.backgroundColor='yellow';
            btn1.innerText='Clicked(Anonymeous)';
        });

        // method 3 using arrow function
        let btn2=document.getElementById('button2');

        btn2.addEventListener('click',()=>{
            btn2.style.backgroundColor='orange';
            btn2.innerText='Clicked(Arrow)'
        });


// using different specified words in first parameter of addEventListener.
        // mouseover---(if the cursore come in the boundary the event will tracked)
        let mouse_over=document.getElementById('mouse_over');

        mouse_over.addEventListener('mouseover',function(){
            mouse_over.style.backgroundColor='black';
            mouse_over.style.color='white';
            mouse_over.innerText='mouse over mapped';
        });

        // mouseout----(if the cursor comes in the boundary and now when the cursor go out from the boundary the event will tracked.)
        let mouse_out=document.getElementById("mouse_out");
        
        mouse_out.addEventListener('mouseout',()=>{
            mouse_out.style.backgroundColor='orange';
            mouse_out.innerText='mouse out mapped';
        });

        // focus (on input we use it.)---(if we come to input without using mouse like using tab , in that case we can't use mouseover and mouseout so in that case we have to use focus now when the user come to input section in applied event he does not use mouse.)
        let Focus=document.getElementById('focus');

        Focus.addEventListener('focus',()=>{
            Focus.style.backgroundColor='pink';
        });

        // blur (on input we use it.)---(after selecting the input if we click outside of that input or if we go out through tab or any othr method the blur event will targated)
        let Blur=document.getElementById('blur');

        Blur.addEventListener('blur',function(){
            Blur.style.border='1px solid red';
            Blur.style.borderRadius='3px';
        });

        // ---------------------- using multi functions on a single element. ----------------------
        // on BUTTON 
        let multi1=document.getElementById('click_mouse_over_out');

        multi1.addEventListener('mouseover',()=>{
            multi1.style.backgroundColor='orange';
            multi1.style.border='1px solid red';
            multi1.style.borderRadius='10px';
        });

        multi1.addEventListener('mouseout',function(){
            multi1.style.backgroundColor='#FFFFFF';
            multi1.style.border='1px solid grey';
            multi1.style.borderRadius='7px';
        });
        
        multi1.addEventListener('click',()=>{
            multi1.style.backgroundColor='red';
            multi1.style.border='1px solid blue';
            multi1.style.borderRadius='4px';
        });

        // on INPUT
        let  multi2=document.getElementById('focus_blur');

         multi2.addEventListener('focus',()=>{
             multi2.style.backgroundColor='orange';
             multi2.style.border='none';
             multi2.style.borderRadius='5px';
            });
            
            multi2.addEventListener('blur',()=>{
                multi2.style.backgroundColor='#BFFFFF';
                multi2.style.border='1px solid red';
                multi2.style.borderRadius='5px';
        });

        // prevent default---it is used to stop the default behaviour of any element.
        // flow---every element of html have a lot of properties.the function, that is used in second parameter of the addEventListener, some times used without a parameter but if we enter a parameter to that function the properties of that element(on which the event listener is applied) will passed in that parameter and then we can use that in the function to manipulate accordingly.

        // in addEventListener the first parameter is submit that is for submitint the form.
        let form=document.getElementById('prev_default');
        console.log(form)

        form.addEventListener('submit',(e)=>{
            e.preventDefault();
            console.log('clicked');
        });

        // use event at once
        let once=document.getElementById('once');

        once.addEventListener('click',function1);
        
        function function1(){
            console.log('one');
            once.removeEventListener('click',function1)
        }
        
    
// propagation(means spreading)
    // there are two major phases in which the events run.
        // capturing phase--- in this phase the events executed from parent(root) to child (targated) element.
        // bubbling phase---it is the default phase in which the evnets executed from child to the parent(root) element.

        // bubbling phase.---the event execution is child to parent.
        let div1=document.getElementById('d1');
        div1.addEventListener('click',()=>{
            console.log('1');
        });
        let div2=document.getElementById('d2');
        div2.addEventListener('click',()=>{
            console.log('2');
        });
        let div3=document.getElementById('d3');
        div3.addEventListener('click',()=>{
            console.log('3');
        });
        let div4=document.getElementById('d4');
        div4.addEventListener('click',()=>{
            console.log('4');
        });


        // capturing phase.---the event execution is parent to child.
        // to use capturing phase we just have to add a third parameter in addEventListener function i.e true.
        let dd1=document.getElementById('dd1');
        dd1.addEventListener('click',()=>{
            console.log('1');
        },true);
        let dd2=document.getElementById('dd2');
        dd2.addEventListener('click',()=>{
            console.log('2');
        },true);
        let dd3=document.getElementById('dd3');
        dd3.addEventListener('click',()=>{
            console.log('3');
        },true);
        let dd4=document.getElementById('dd4');
        dd4.addEventListener('click',()=>{
            console.log('4');
        },true);

    // parameter.stopPropagation()---this is used to block the propagation(capturing and bubbling phase)

    // stoping propagation in bubbling phase.
        let stop1=document.getElementById('stop1');
        let stop2=document.getElementById('stop2');
        let stop3=document.getElementById('stop3');
        let stop4=document.getElementById('stop4');
        let stop5=document.getElementById('stop5');

        stop1.addEventListener('click',function(e){
            console.log('bubbling1');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        });
        
        stop2.addEventListener('click',function(e){
            console.log('bubbling2');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        });
        
        stop3.addEventListener('click',function(e){
            console.log('bubbling3');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            e.stopPropagation();
        });
        
        stop4.addEventListener('click',function(e){
            console.log('bubbling4');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        });
        
        stop5.addEventListener('click',function(e){
            console.log('bubbling5');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        });

    // stoping propagation in capturing phase.

        let stoop1=document.getElementById('stoop1');
        let stoop2=document.getElementById('stoop2');
        let stoop3=document.getElementById('stoop3');
        let stoop4=document.getElementById('stoop4');
        let stoop5=document.getElementById('stoop5');

        stoop1.addEventListener('click',function(e){
            console.log('bubbling1');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        },true);
        
        stoop2.addEventListener('click',function(e){
            console.log('bubbling2');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        },true);
        
        stoop3.addEventListener('click',function(e){
            console.log('bubbling3');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            e.stopPropagation();
        },true);
        
        stoop4.addEventListener('click',function(e){
            console.log('bubbling4');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        },true);
        
        stoop5.addEventListener('click',function(e){
            console.log('bubbling5');
            this.style.borderRadius="15px";
            this.style.border='2px solid red';
            // e.stopPropagation();
        },true);


// disabling right click nemu.
    // contextmenu--- this event is used to trigger the right click.
    // on any element if we triggre this event and apply prevent default on it , the element will stop showing right click menu.
    let contextmenu=document.getElementById('contextmenu');
    contextmenu.addEventListener('contextmenu',function(e){
        e.preventDefault();
        console.log('contextmenu is triggered')
    });
  
    // disabling right click on body.
        //  let body=document.querySelector('body');
        // body.addEventListener('contextmenu',(e)=>{
        //     e.preventDefault();
        //     console.log('prevent default triggered on the body.')
        // });
