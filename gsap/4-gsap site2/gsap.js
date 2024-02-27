const tl = gsap.timeline()

tl.from(".nav",{
    delay:1,
    opacity:0,
    y:20,
})

tl.from(".nav>h1>span",{
    opacity:0,
    y:-20,
    stagger:0.3
})

tl.from(".nav p",{
    opacity:0,
    y:-20,
    stagger:0.3
})

gsap.from(".page2 .box",{
    opacity:0,
    y:50,
    scrollTrigger:{
        trigger:".page2 .box",
        scroll:"body",
        // markers:true,
        start:"bottom 100%",
        end:"top 60%",
        // scrub:3
    }
})