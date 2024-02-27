let country=document.getElementById('dropdown');
let container=document.getElementById('input_container');

country.addEventListener('input',()=>{
    let selected=country.value;
        console.log(container);
        console.log(selected);

        if(selected=='.'){
            container.innerHTML='';
        }else if(selected=='amarica'){
            container.innerHTML='';
            let state=document.createElement('input');
            state.setAttribute('type','text');
            state.setAttribute('name','state');
            state.setAttribute('placeholder','Enter your state');

            let zipCode=document.createElement('input');
            zipCode.setAttribute('type','text');
            zipCode.setAttribute('name','zipCode');
            zipCode.setAttribute('placeholder','Enter zip code');

            container.append(state,zipCode);
        }else if(selected=='england'){
            container.innerHTML='';
            let city=document.createElement('input');
            city.setAttribute('type','text');
            city.setAttribute('name','city');
            city.setAttribute('placeholder','Enter your city');

            let postal_adr=document.createElement('input');
            postal_adr.setAttribute('type','text');
            postal_adr.setAttribute('name','postal_adr');
            postal_adr.setAttribute('placeholder','Enter postal address');

            container.append(city,postal_adr);
        }else if(selected=='india'){
            container.innerHTML='';

            let city=document.createElement('input');
            city.setAttribute('type','text');
            city.setAttribute('name','city');
            city.setAttribute('placeholder','Enter your city');

            let streNo=document.createElement('input');
            streNo.setAttribute('type','text');
            streNo.setAttribute('name','streNo');
            streNo.setAttribute('placeholder','Enter street #');

            container.append(city,streNo);
        }else{
            container.innerHTML='';

            let province=document.createElement('input');
            province.setAttribute('type','text');
            province.setAttribute('name','province');
            province.setAttribute('placeholder','Enter your province');

            let area=document.createElement('input');
            area.setAttribute('type','text');
            area.setAttribute('name','area');
            area.setAttribute('placeholder','Enter area');

            container.append(province,area);
        }
});

let form=document.getElementById('form');
    form.addEventListener('submit',function(e){
        let selected=country.value;
        console.log(selected);
        if(selected=='.'){
            e.preventDefault();
            container.innerHTML='Plese select a country'
        }
    }); 
