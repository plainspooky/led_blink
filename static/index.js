/*
    Funções da página de visualização dos registros inseridos.
*/

// armazena o valor atual do led
var led=false;

// quando a página estiver pronta, faça...
$(document).ready(function(){
    // status do 'LED1'
    setInterval("getStatus()",2000)
});

// função que retorna o status do led
function getStatus(){
    var status=led;
    var jsonUrl='/led/1';
    $.getJSON(jsonUrl,function(data){
        switch(data['value']){
            case 0:
                led=0;
                break;
            case 1:
                led=1;
                break;
            default:
                leds=false;
            }
            updateStatus(led);
        });
}

// função que altera o status do botão de acordo com o valor do led
function updateStatus(value){
    var justNow=new Date(Date.now());
    switch(value){
        case 0:
            $("#led1").addClass("btn-default");
            $("#led1").removeClass("btn-success");
            $("#led1").text("DESLIGADO");
            break;
        case 1:
            $("#led1").removeClass("btn-default");
            $("#led1").addClass("btn-success");
            $("#led1").text("LIGADO");
            break;
        default:
            $("#led1").removeClass("btn-default");
            $("#led1").removeClass("btn-success");
            $("#led1").text("indefinido");
    }
    $("#conn-log").text(justNow.toString());
}

// função que alterna o status do botão
function changeStatus(){
    var novoStatus=1-led;
    var jsonUrl='/led/1/'+novoStatus;
    $.ajax({
        url: jsonUrl,
        type: "PUT",
	beforeSend: updateStatus(novoStatus)});
}
