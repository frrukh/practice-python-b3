let form = document.getElementById("form")
let api="84d306a138152677bdc85122e47988cf"
form.addEventListener("submit",async function(e){

    e.preventDefault()
    let input = document.getElementById("input").value
    let data1 =`https://pro.openweathermap.org/data/2.5/forecast/hourly?q=${input}&appid=${api};`

    let response =await fetch(data1);
    console.log(response)

    let data = await response.json()

    console.log(data)

})