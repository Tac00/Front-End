let idade = parseInt(prompt("Qual a sua idade"))

function verificar(idade){
    if (idade <= 12){
        return "criança";
    }else if (idade >= 13 && idade <= 17){
        return "adolecente";
    }else if (idade >= 18 && idade <= 59){
        return "adulto";
    }else if (idade >= 60){
        return "idoso";
    }
}
let resultado = verificar(idade);
 alert("você é " + resultado);