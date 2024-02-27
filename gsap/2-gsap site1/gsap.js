const tl = gsap.timeline()
const tl1 = gsap.timeline()

tl.from("#main h1",{
    delay:1,
    opacity:0,
    y:100,
    stagger:0.5,
})

tl1.from("#nav img,#nav p,#nav button",{
    y:-100,
    opacity:0,
    delay:0.5,
    duration:1,
    delay:2,
    stagger:0.3,
})


tl1.from("#main>img",{
    opacity:0,
    scale:0.8,
    ease: "power.in",
    duration:1,
})

tl1.from("#scroll_down",{
    opacity:0,
    y:40
})

tl1.to("#scroll_down",{
    delay:1,
    y:-10,
    repeat:-1,
    yoyo:true
})
