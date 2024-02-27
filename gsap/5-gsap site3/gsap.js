var tl = gsap.timeline()


// a=0
// let intervalID = setInterval(() => {
//         if(a<100){
//             a=a+ Math.floor(Math.random()*20)
            
//             document.getElementById('loader_digits').innerText=a+'%';
//         }else{
//             console.log('lo')
//             document.getElementById('loader_digits').innerText='100%';
//             clearInterval(intervalID);
//         }
//     }, 100);


function time(){
    a=0
    let inc = setInterval(() => {
        if(a<100){
            a=a+ Math.floor(Math.random()*20)
            
            document.getElementById('loader_digits').innerText=a+'%';
        }else{
            console.log('Loading Completed!')
            document.getElementById('loader_digits').innerText='100%';
            clearInterval(inc)
        }
    }, 100);
}

time();

tl.to(".loader_page h1",{
    delay:1.4,
    scale:1.2
})

tl.to(".loader_page",{
    delay:1,
    duration:1,
    top:'-100%'
})



gsap.to(".page1 .main_text",{
    transform:"translateX(-160%)",
    fontWeight:700,
    color: '#ee6',
    scrollTrigger:{
        trigger:".page1 .main_text",
        scroll:"body",
        // markers:true,
        start:"top 0%",
        scrub:true,
        pin:true
    }
})

gsap.from(".page2 .box",{
    rotate:20,
    scale:0.3,
    opacity:0,
    scrollTrigger:{
        trigger:".page2 .box",
        scroll:"body",
        // markers:true,
        start:"top 90%",
        end:"top 50%",
        scrub:5,
    }
})