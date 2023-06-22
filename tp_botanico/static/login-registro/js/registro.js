const errores = document.querySelectorAll(".msj-error");

function inputError(){
    for(let i = 0;i<errores.length;i++){
        if(errores[i].querySelector("ul")){
            console.log("error " + i)
            document.querySelectorAll(".registro-campo")[i].classList.add("input-error");
        } else {
            document.querySelectorAll(".registro-campo")[i].classList.remove("input-error");
        }
    }
}

inputError()