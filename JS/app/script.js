let apiKey='84d306a138152677bdc85122e47988cf';
let form=document.getElementById('form');

form.addEventListener('submit',async function(e){
    e.preventDefault();
    let inputTag=document.getElementById('input');
    let input=document.getElementById('input').value;
    if(input==''){
        inputTag.setAttribute('placeholder','Plese Enter a City Name')
    }else{
        inputTag.setAttribute('placeholder','Enter City Name')
        let apiUrl=`https://api.openweathermap.org/data/2.5/weather?q=${input}&appid=${apiKey}`
        let apidata=await fetch(apiUrl);
        let data=await apidata.json();
        console.log(data);
        console.log(apidata);
        console.log(apiUrl);
        getDate(data);
        getLocation(data);
        getTemp(data);
        feelsLike(data);
        humidity(data);
        pressure(data);
        inputTag.value='';
    }
});

function getDate(data){
    dateInMilisec=data.dt*1000;
    let dateObj=new Date(dateInMilisec);
    let months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    let days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
    let monthInd=dateObj.getMonth();
    let month=months[monthInd];
    let date=dateObj.getDate();
    let dayInd=dateObj.getDay();
    let day=days[dayInd];
    let hours=dateObj.getHours();
    let min=dateObj.getMinutes();
    let ampm='';
    if(hours>12){
        hours-=12;
        ampm='PM';
    }else{
        ampm='AM';
    }
    let finalDate=`${month} ${date},${hours}:${min} ${ampm},${day}`;
    document.getElementById('date').innerText=finalDate;
}
function getLocation(data){
    let city=data.name;
    let country=data.sys.country;
    let final=`Location : ${city},${country}`;
    document.getElementById('location').innerHTML=final;
}
function getTemp(data){
    let kelvinUnit=273.15;
    let tempInCelsius=(data.main.temp)-kelvinUnit;
    let temp=tempInCelsius.toFixed(2);//it gives 2 values after decimal point.
    let final=`Temprature : ${temp}&deg; C;`;
    document.getElementById('temp').innerHTML=final;
}

function feelsLike(data){
    let kelvinUnit=273.15;
    let feelsLikeTempInCelsius=((data.main.feels_like)-kelvinUnit).toFixed(2);
    let weather=data.weather[0].main;
    let final=`Feels Like : ${feelsLikeTempInCelsius}&deg; C ${weather}`;
    document.getElementById('feels').innerHTML=final;
}
function humidity(data){
    let humidity=data.main.humidity;
    let final=`Humidity : ${humidity}%`;
    document.getElementById('humidity').innerText=final;
}

    function pressure(data){
    let pressure=data.main.pressure;
    let final=`Air Pressure : ${pressure} hPa`
    document.getElementById('pressure').innerText=final;
}


