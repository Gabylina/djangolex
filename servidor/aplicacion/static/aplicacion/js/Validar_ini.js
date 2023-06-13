function b() {
    swal("Ingresa tu correo para poder cambiar la contraseña", {
        content: "input",
    })
        .then((value) => {
            swal(`Se a enviado un correo para cambio de contraseña.`);
        });
}


function login(){
    var user,contra
    user=document.getElementById("username").value;
    contra=document.getElementById("password").value;

    if(user=="nico" && contra=="nico"){
        location.href ="http://127.0.0.1:8000/solicitudes";
    }else{
        swal("Usuario o contraseña incorrectos","","warning");
    }

}

function login_tec_juri(){
    var user,contra
    user=document.getElementById("username").value;
    contra=document.getElementById("password").value;

    if(user=="tecnico" && contra=="123"){
        location.href ="http://127.0.0.1:8000/indextecjuri";
    }else{
        swal("Usuario o contraseña incorrectos","","warning");
    }

}