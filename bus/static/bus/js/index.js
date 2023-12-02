window.addEventListener('load', async ()=>{
    await CargaInicial()
})

let btnhorarios = document.getElementById("btnhorarios")


btnhorarios.addEventListener('click',async () => {
    sectiontest.innerHTML = ''
    if (dict_horario_fin.horarios.length > 0 && dict_horario_inicio.horarios.length > 0){
        await ponerhorarios()
    }else{
        sectiontest.innerHTML = `
        <div class="alert alert-danger" role="alert">
            No hay horarios existentes <i class="fa-solid fa-circle-exclamation"></i>
        </div>`
    }
})

let bus_id_persistente = ''

let paradas = []

let dict_horario_inicio = {'titulo' : '', 'horarios': ''}
let dict_horario_fin = {'titulo':'', 'horarios': ''}

const ListarLugares = async (id_bus) => {
    try {
        const response = await fetch(`./api/bus/${id_bus}`)
        const data = await response.json()

        paradas=data

        cargarhorarios(data[0].id,"inicio")
        ListarLugarFinal(data[0].id)

        let optionlugar = ``
        data.forEach((element) => {

            optionlugar+= `<option value=${element.id}>${element.nombre_parada}</option>`
        })
        lugarinicio.innerHTML = optionlugar
    } catch (error) {
        console.error(error)
    }

}

const ListarLocalidades = async () =>{
    try {
        await fetch('./api/sectores')
        .then((data) => data.json())
        .then((data) => {
            data.data.forEach((element) => {
            let option = document.createElement("option")
            option.innerHTML = element.sector_nombre
            option.value = element.id
            localidades.append(option)
        })})
    } catch (error) {
        console.error(error)
    }
}

const ListarLugarFinal = async (id_parada) => {

    try {
        
        let paradasfinales = paradas.filter((parada) => parada.id != id_parada)

        cargarhorarios(paradasfinales[0].id,"fin")

        let optionlugarfinal = ``
        paradasfinales.forEach((element) => {
            optionlugarfinal+= `<option value=${element.id}>${element.nombre_parada}</option>`
        })
        lugarfinal.innerHTML = optionlugarfinal
    } catch (error) {
        console.error(error)
    }
}



const  cargarhorarios = async (lugar_inicio,valor) => {

    try {
        
        const response = await fetch(`./api/parada/${lugar_inicio}/horarios`)
        const data = await response.json()

            switch (valor){
                case "inicio":
                    dict_horario_inicio['horarios'] = data.data.horarios
                    dict_horario_inicio['titulo'] = data.data.parada
                    break;
                case "fin":
                    dict_horario_fin['horarios'] =  data.data.horarios
                    dict_horario_fin['titulo'] = data.data.parada
                    break;
            }
    } catch (error) {
        console.error(error)
    }
}

const creartarjetas = async (titulo,lugar,hora) => {
    tarjeta=`
        
            <div class="card shadow rounded-4 text-center mb-3 mt-3" id="card-w">
                <div class="card-header bg-primary rounded-top-4 text-white fs-4 p-2">${titulo}</div>
                    <div class="card-body" id="card-body">
                        <p class="card-text text-wrap p-2">${lugar}</p>
                    </div>
                <div class="card-footer fw-bold fs-4">${hora}</div>
            </div>
    `
    sectiontest.innerHTML+= tarjeta
}

const ponerhorarios = async () => {

    console.log(dict_horario_inicio.horarios.length +" === "+ dict_horario_fin.horarios.length)
    if (dict_horario_inicio.horarios.length === dict_horario_fin.horarios.length){
        for (let index = 0; index < dict_horario_inicio.horarios.length; index++) {
            if (dict_horario_inicio.horarios[index] < dict_horario_fin.horarios[index]){
                creartarjetas("Sale",dict_horario_inicio.titulo,dict_horario_inicio.horarios[index])
                if (dict_horario_fin.horarios[index]){
                    creartarjetas("Llega",dict_horario_fin.titulo,dict_horario_fin.horarios[index])
                }
            }else{
                sectiontest.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    No hay horarios existentes <i class="fa-solid fa-circle-exclamation"></i>
                </div>`
            }
        }
    }
    if (dict_horario_fin.horarios.length > dict_horario_inicio.horarios.length){
        dict_horario_fin.horarios.shift()
        for (let index = 0; index < dict_horario_inicio.horarios.length; index++) {
            if (dict_horario_inicio.horarios[index] < dict_horario_fin.horarios[index]){
                creartarjetas("Sale",dict_horario_inicio.titulo,dict_horario_inicio.horarios[index])
                if (dict_horario_fin.horarios[index]){
                    creartarjetas("Llega",dict_horario_fin.titulo,dict_horario_fin.horarios[index])
                }
            }else{
                sectiontest.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    No hay horarios existentes <i class="fa-solid fa-circle-exclamation"></i>
                </div>`
            }
        }
    }
    if (dict_horario_inicio.horarios.length > dict_horario_fin.horarios.length){
        dict_horario_inicio.horarios.shift()
        for (let index = 0; index < dict_horario_inicio.horarios.length; index++) {
            if (dict_horario_inicio.horarios[index] < dict_horario_fin.horarios[index]){
                creartarjetas("Sale",dict_horario_inicio.titulo,dict_horario_inicio.horarios[index])
                if (dict_horario_fin.horarios[index]){
                    creartarjetas("Llega",dict_horario_fin.titulo,dict_horario_fin.horarios[index])
                }
            }else{
                sectiontest.innerHTML = `
                <div class="alert alert-danger" role="alert">
                    No hay horarios existentes <i class="fa-solid fa-circle-exclamation"></i>
                </div>`
            }
        }
    }
    // for (let index = 0; index < dict_horario_inicio['horarios'].length; index++) {
        
    //     console.log(
    //         dict_horario_inicio['horarios'][index] +" | "+ dict_horario_fin['horarios'][index]
    //     )
    //     if (dict_horario_inicio['horarios'][index] < dict_horario_fin['horarios'][index]){
    //         creartarjetas("Sale",dict_horario_inicio['titulo'],dict_horario_inicio['horarios'][index])
    //         if (dict_horario_fin['horarios'][index]){
    //             creartarjetas("Llega",dict_horario_fin['titulo'],dict_horario_fin['horarios'][index])
    //         }
    //     }
        
    // }

    // const horariosMostrados = new Set();

    // for (let i = 0; i <= dict_horario_inicio['horarios'].length; i++) {
    //     let horaInicio = dict_horario_inicio['horarios'][i];
    //     let horaFin = dict_horario_fin['horarios'][i];

    //     const horariosPermitidos = ['06:10', '06:15', '06:20', '06:40'];


    //     if (dict_horario_inicio['horarios'].length == dict_horario_fin['horarios'].length){
    //         console.log(horaInicio + " | " + horaFin)
    //         while (horaInicio >= horaFin) {
    //             console.log("Bucle -"+horaInicio + " | " + horaFin)
    //             i++; // Avanzar al siguiente horario en horaFin
    //             if (i >= dict_horario_fin['horarios'].length) {
    //             break; // No hay más horarios en horaFin, salir del bucle
    //             }
    //             horaFin = dict_horario_fin['horarios'][i];
    //         }
    
    //         if (horaInicio < horaFin && !horariosMostrados.has(horaInicio)) {
    //             creartarjetas("Sale",dict_horario_inicio['titulo'],horaInicio)
    //             creartarjetas("Llega",dict_horario_fin['titulo'],horaFin)
    //             //console.log(`Horario Inicio: ${horaInicio}, Horario Fin: ${horaFin}`);
    //             horariosMostrados.add(horaInicio);
    //         }
    //     }
    //     else
    //     {
    //         if (horariosPermitidos.includes(horaInicio) || horariosPermitidos.includes(horaFin)){
    //             while (horaInicio >= horaFin) {
    //                 i++; 
    //                 if (i >= dict_horario_fin['horarios'].length) {
    //                 break; 
    //                 }
    //                 horaFin = dict_horario_fin['horarios'][i];
    //             }
        
    //             if (horaInicio < horaFin && !horariosMostrados.has(horaInicio)) {
    //                 creartarjetas("Sale",dict_horario_inicio['titulo'],horaInicio)
    //                 creartarjetas("Llega",dict_horario_fin['titulo'],horaFin)
    //                 //console.log(`Horario Inicio: ${horaInicio}, Horario Fin: ${horaFin}`);
    //                 horariosMostrados.add(horaInicio);
    //             }
    //         }
    //     }

        
    // }

}



const CargaInicial= async() => {
    await ListarLocalidades()
    
    localidades.addEventListener('change',(event)=>{
        ListarLugares(event.target.value)
        bus_id_persistente = event.target.value
        sectiontest.innerHTML = ''
    })

    lugarinicio.addEventListener('change',(event) =>{
        ListarLugarFinal(event.target.value)
        cargarhorarios(event.target.value,"inicio")
        sectiontest.innerHTML = ''
    })
    lugarfinal.addEventListener('change', (event) => {
        cargarhorarios(event.target.value,"fin")
        sectiontest.innerHTML = ''
    })

}

