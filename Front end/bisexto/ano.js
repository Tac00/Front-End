let ano = parseInt(prompt("Digite o ano"));
function verificar(ano) {
    if (ano % 4 == 0 && ano % 100 != 00 || ano % 400 == 0){
        return "ano bisexto";
    }else{
        return "ano não bisexto";
    }
    
}
let resultado = verificar(ano);
alert("O ano " + ano + " E: " + resultado);