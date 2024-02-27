let form=document.getElementById('form');
form.addEventListener('submit',(e)=>{
    e.preventDefault();
    console.log('the form was submited');

    let f_name=document.getElementById('f_name').value;
    let f_name_error=document.getElementById('f_name_error');
    if(f_name==''){
        f_name_error.innerText='*First name is required';
    }else{
        f_name_error.innerText='';
    }

    let l_name=document.getElementById('l_name').value;
    let l_name_error=document.getElementById('l_name_error');
    if(l_name==''){
        l_name_error.innerText='*Last name is required';
    }else{
        l_name_error.innerText='';
    }

    let age=document.getElementById('age').value;
    let age_error=document.getElementById('age_error');
    if(age==0){
        age_error.innerText='*`Age is required';
    }else if(age<18 || age>65){
        age_error.innerText='*Age should be 18-65';
    }else{
        age_error.innerText='';
    }

    let tel=document.getElementById('tel').value;
    let tel_error=document.getElementById('tel_error');
    if(tel==0){
        tel_error.innerText='*Phone Number is required';
    }else if(tel.length!=11){
        tel_error.innerText='*Phone Number should be of 11 digits'
    }else{
        tel_error.innerText='';
    }

    let email=document.getElementById('email').value;
    let email_error=document.getElementById('email_error');
    if(email==''){
        email_error.innerText='*Email is required';
    }else if(!email.includes('@') || !email.includes('.')){
        email_error.innerText='*Plese enter a valid email';
    }else{
        email_error.innerText='';
    }

    let password=document.getElementById('password').value;
    let password_error=document.getElementById('password_error')
    if(password==''){
        password_error.innerText='*Password is required'
    }else if(password.length<8 || password.length>20){
        password_error.innerText='*Password should be of 8-20 digits';
    }else{
        password_error.innerText='';
    }

    let confirm_password=document.getElementById('confirm_password').value;
    let confirm_password_error=document.getElementById('confirm_password_error');
    if(confirm_password==''){
        confirm_password_error.innerText='*Confirm your password';
    }else if(confirm_password!=password){
        confirm_password_error.innerText='*Password does\'t match';
    }else{
        confirm_password_error.innerText='';
    }
});