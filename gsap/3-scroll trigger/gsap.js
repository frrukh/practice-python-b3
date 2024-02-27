const tl = gsap.timeline()

tl.from(".page1 .box",{
    // opacity:0,
    scale:0,
    delay:1,
    duration:1,
    rotate:360
})

tl.from("#page2 .box",{
    opacity:0,
    scale:0.7,  
    scrollTrigger:{
        trigger:"#page2 .box",
        scroll:"body",
        // markers:true,
        start:"top 60%",
        end:"top 40%",
        scrub:1
    }
})

tl.from(".page3 .box",{
    opacity:0,
    scale:0.7,
    scrollTrigger:{
        trigger:".page3 .box",
        scroll:"body",
        markers:true,
        start:"top 60%",
        end:"top 40%",
        scrub:2
    }
})