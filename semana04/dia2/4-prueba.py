$(document).ready(()=>{

    const url = "https://criptoya.com/api/bitstamp/btc";
    $.get(url,function(respuesta,estado){

        console.log(respuesta);
        console.log(estado);
        if (estado === "success"){
            let misDatos = respuesta;
                $("body").prepend(`
                  <div>
                    <h3>${new Intl.NumberFormat().format(parseInt(misDatos.last))}</h3>    
                  </div>`);
        }   
    });
})