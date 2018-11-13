$("#btnEnviar").click(function(event) {
    var form = $("#formulario")[0];
    var run = $("#run");
    var fecNac = $("#fecNac");
    
    if(!validarFecha(fecNac.val())){
        fecNac[0].setCustomValidity("Fecha inválida");
    }
    else{
        fecNac[0].setCustomValidity("");
    }
    
    if(!validarRun(run.val())){
        run[0].setCustomValidity("Ingrese un run válido sin puntos");
    }
    else{
        run[0].setCustomValidity("");
    }
    if (form.checkValidity() === false) {
        event.preventDefault();
        event.stopPropagation();
    }
    else {
        alert("Formulario enviado con exito");
    }
    $("#formulario").addClass('was-validated');
});
function validarRun(run){
    try {
        var runSplit = run.split("-");
        var runInicio = runSplit[0];
        var dv = runSplit[1].toLowerCase();
        return dgv(runInicio)==dv;
    } catch (error) {
        return false;
    }
    
}
function validarFecha(fechaString){
    try {
        var fechaSplit = fechaString.split("-");
        return fechaSplit[0]<2001;
    } catch (error) {
        return false;
    }
}
function dgv(T)    //digito verificador
{  
    var M=0,S=1;
    for(;T;T=Math.floor(T/10))
    S=(S+T%10*(9-M++%6))%11;
    return S?S-1:'k';
}