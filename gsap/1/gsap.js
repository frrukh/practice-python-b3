// gsap.to is used to make the element from initial position to final position
// syntax: gsap.to("selector like css",{key:value,key:value...})
gsap.to(".h1",{
    x:500,
    duration:1,
    delay:0.5,
    repeat:-1,
    yoyo:true,
})

// gsap.from is used to make the element from final position to initial  position
// syntax: gsap.from("selector like css",{key:value,key:value...})
gsap.from("h2",{
    y:-100,
    color:'red',
    duration:1,
    repeat:-1,
    yoyo:true,
    delay:1,
})

/*
what if we want to add the animation to the elements one by one i.e when first element completes 
its animation the second element will start the animation and when second element completes
its animation the third element will start the animation and so on...
*/
// to solve this problem we have two solutions. 
// 1---
/*
to the second element,we can add delay equal to the duration of the first element and to third element 
we can add delay equal to sum of duration of first and second element and so on... 
but in this case the elements moves independently and this is not the correct and efficient solution 
because in large projects the are a large number of elements.
*/
// gsap.to("#h11",{
//     x:500,
//     duration:2,
//     delay:1,
// })

// gsap.to("#h12",{
//     x:500,
//     duration:2,
//     // as h11 completes its animation in 3 seconds.
//     delay:3,
// })

// gsap.to("#h13",{
//     x:500,
//     duration:2,
//     // as h11 completes its animation in 3 seconds and h12 completes its animation in 2 seconds.
//     delay:5,
// })

// 2---
/*
we can make a timeline in which we add the animation to the elements one by one and it will 
execute the animation one by one.
let discuss how we can make a timeline.
*/

// first we have to get the timeline method from gsap and save it in a variable
const tl = gsap.timeline()
// now we can use the variable instead of gsap like tl.from or tl.to.
// this will execute the animations of same timeline one by one. 
tl.to("#h11",{
    x:500,
    color: "#434343",
    duration: 1,
    delay: 1
})


tl.to("#h12",{
    x:600,
    color: "red",
    // delay: 1,
})


tl.to("#h13",{
    x:700,
    color: "green",
})