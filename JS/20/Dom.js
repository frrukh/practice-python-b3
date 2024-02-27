//Get HTML elements in JavaScript.
    // getting by id.
    let h=document.getElementById("heading");
    console.log(h);
    let p1=document.getElementById("p1");
    console.log(p1);


    // getting by class.
    // ---against getting by id, it will be an array because the same class can be assigned to the multiple tags.
    let p=document.getElementsByClassName('par');
    console.log(p);
        // as it is an array we can access a single element by using its index.
        console.log(p[0]);
        console.log(p[1]);
        console.log(p[2]);
        console.log(p[3]);

        // we can also do the same thing using loop.
        console.log("----------BY USING LOOP----------")
        for(let a of p){
            console.log(a);
        }


    // getting by tag name.
    let tagName=document.getElementsByTagName('img');
    console.log(tagName);
    console.log(tagName[0]);


    // getting a single element using id , class or tagName.
    // its result will never be an array.
        // by tag name--- it will give a single tag as it targets only the topest element.
        let anyone=document.querySelector('h1');
        console.log(anyone);
        // by class ---assinged by ( . )--- it will also give a single value although it is a class that can be given to the multiple tags but the querySelector function only give the single topest element.
        let anyClass=document.querySelector('.par');
        console.log(anyClass);
        // by id.
        let byId=document.querySelector('#a');
        console.log(byId);


    // getting all elements using id ,class or tagName.
    // its result will always be an array even in case of id.
        // by tag name--- it will give an array and we can target a single element by using index.
        let byTagName=document.querySelectorAll('p');
        console.log(byTagName);
        console.log(byTagName[0]);
        console.log(byTagName[1]);
        console.log(byTagName[2]);
        console.log(byTagName[3]);
        // by class 
        let byClass=document.querySelectorAll('.par');
        console.log(byClass);
        console.log(byClass[0]);
        console.log(byClass[1]);
        console.log(byClass[2]);
        console.log(byClass[3]);
        // by id --- as the id is unique ,it will give an array of a single index
        let byId1=document.querySelectorAll("#heading");
        console.log(byId1);
        console.log(byId1[0]);


    // getting content of any tag. (maps only with getElementById)
        // inner text.
            // method 1-- to save element and its data.
                let data=document.getElementById('innerText');
                let innerText=data.innerText;
                console.log(innerText);
            // method 2--  to save only the data.
                let data1=document.getElementById('innerText').innerText;
                console.log(data1);
        // inner html.
            // method 1--- to save element and its data.
                let data11=document.getElementById("innerHtml");
                let innerHtml=data11.innerHTML
                console.log(innerHtml);
            // method 2--- to save only the data.
                let inner_html=document.getElementById('innerHtml').innerHTML
                console.log(inner_html);


        

