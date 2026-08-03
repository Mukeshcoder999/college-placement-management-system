window.addEventListener("load",function(){

    console.log("CPMS Loaded Successfully");

});

document.getElementById("year").textContent=new Date().getFullYear();

const buttons=document.querySelectorAll(".btn");

buttons.forEach(button=>{

    button.addEventListener("click",function(){

        this.style.transform="scale(0.95)";

        setTimeout(()=>{
            this.style.transform="scale(1)";
        },150);

    });

});

window.addEventListener("scroll",function(){

    const navbar=document.querySelector(".navbar");

    if(window.scrollY>20){

        navbar.style.boxShadow="0 3px 10px rgba(0,0,0,.2)";

    }else{

        navbar.style.boxShadow="none";

    }

});