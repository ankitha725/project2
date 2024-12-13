const inp1= document.getElementsByTagName("input")

for (let tg=0; tg<inp1.length; tg++){
    const element=inp1[tg];
    element.addEventListener("mouseover",function(){
        element.style.boxShadow="5px 5px 5px  aliceblue";
        element.style.backgroundColor=" rgb(87, 75, 75)";
    })
    element.addEventListener("mouseleave",function(){
        element.style.boxShadow="";
        element.style.backgroundColor="";
    })

}