const apiKey='84d306a138152677bdc85122e47988cf';
let form=document.getElementById('form');

form.addEventListener('submit',async function(e){
    e.preventDefault();
    let cityName=document.getElementById('input');
    if(cityName.value==''){
        cityName.setAttribute('placeholder','Plese Enter a valid City Name');
    }else{
        cityName.setAttribute('placeholder','Enter City Name');
        let api_url=`https://api.openweathermap.org/data/2.5/weather?q=${cityName.value}&appid=${apiKey}`;
        let response=await fetch(api_url);
        let data =await response.json();
        console.log(response);
        console.log(data);
        console.log(api_url);

        get_date(data);
        get_location(data);
        get_temp(data);
        feels_like(data);
        humidity(data);
        pressure(data);
       
        document.getElementById('input').value='';
    }
    

});


function get_date(data){

    let dt=(data.dt)*1000;//convert seconds to miliseconds
    let dateObj=new Date(dt);
    let month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    let monthIndex=dateObj.getMonth();
    let finalMonth=month[monthIndex];
    let date=dateObj.getDate();
    let hours=dateObj.getHours();
    let minutes=dateObj.getMinutes();
    let ampm='';
    if(hours>12){
        ampm='PM';
        hours-=12;
    }else{
        ampm='AM';
    }
    final_date=`${finalMonth} ${date}, ${hours}:${minutes}${ampm}`;
    document.getElementById('date').innerText=final_date;
}

function get_location(data){
    let city=data.name;
    let country=data.sys.country;
    let final_location=`${city},${country}`;
    document.getElementById('location').innerText=final_location;
}

function get_temp(data){
    // it gives the temprature in kelvin and as (temp in C =temp in K - 273.15)
    // after this conversion it gives the value in decimals like 16.99000000000001 so we can control this using toFixed().
    // toFixed() --- syntax : value.toFixed(number of digits you want after decimal point);
    let temp=(data.main.temp-273.15).toFixed(2);
    let final_temp=`Temperature: ${temp}&deg; C`;
    document.getElementById('temp').innerHTML=final_temp;
}

function feels_like(data){
    let temp_feels_like=(data.main.feels_like-273.15).toFixed(2);//-273.15 is to convert from kelvin to celsius.
    let weatherCondition=data.weather[0].main;
    console.log(weatherCondition);
    let final=`Feels Like ${temp_feels_like} &deg; C  ${weatherCondition}`
    document.getElementById('feels_like').innerHTML=final;
}

function humidity(data){
    let humidity=data.main.humidity;
    let final=`Humidity : ${humidity}%`
    document.getElementById('humidity').innerText=final;
}

function pressure(data){
    let pressure=data.main.pressure;
    let final=`Pressure : ${pressure} hPa`;
    document.getElementById('pressure').innerText=final;
}