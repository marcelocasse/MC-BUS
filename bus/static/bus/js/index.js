window.addEventListener('load', async ()=>{
    await CargaInicial()
})


//const diasSemana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];

let dict_horario_inicio = {'titulo' : '', 'horarios': ''}
let dict_horario_fin = {'titulo':'', 'horarios': ''}

const ListarLugares = async (id_localidad) => {
    const response = await fetch(`./api/sector/${id_localidad}`)
    const data = await response.json()

    let optionlugar = ``
    data.lugares.forEach((element) => {
        optionlugar+= `<option value=${element.id_lugar}>${element.nombre_lugar}</option>`
    })
    lugarinicio.innerHTML = optionlugar

}

const ListarLocalidades = async () =>{
    try {
        fetch('./api/sectores')
        .then((data) => data.json())
        .then((data) => data.data.forEach((element) => {
            let option = document.createElement("option")
            console.log(element.localidad)
            option.innerHTML = element.localidad
            option.value = element.id
            localidades.append(option)
        }))
    } catch (error) {
        console.log(error)
    }
}

const ListarLugarFinal = async (id_localidad) => {
    
    const response = await fetch(`./api/lugaresfinales/${id_localidad}`)
    const data = await response.json()

    let optionlugarfinal = ``
    data.data.lugares.forEach((element) => {
        optionlugarfinal+= `<option value=${element.id_lugar}>${element.nombre_lugar}</option>`
    })
    lugarfinal.innerHTML = optionlugarfinal
}

const  mostrarhorarios = async (lugar_inicio,valor) => {

    const response = await fetch(`./api/lugar/${lugar_inicio}/horarios`)
    const data = await response.json()

        switch (valor){
            case "inicio":
                dict_horario_inicio['horarios'] = data.data.Horarios
                dict_horario_inicio['titulo'] = data.data.Lugar
                break;
            case "fin":
                dict_horario_fin['horarios'] =  data.data.Horarios
                dict_horario_fin['titulo'] = data.data.Lugar
                break;
        }
}

const creartarjetas = async (titulo,hora) => {
    tarjeta=`
        <div class="col-5 col-sm-4">
            <div class="card shadow rounded-4 text-center mb-3 mt-3">
                <div class="card-header bg-primary rounded-top-4 text-white fs-4 p-2">test</div>
                    <div class="card-body m-0 p-0">
                        <p class="card-text fs-4 text-wrap p-2">${titulo}</p>
                    </div>
                <div class="card-footer fw-bold fs-4">${hora}</div>
            </div>
        </div>
    `
    sectiontest.innerHTML+= tarjeta
}


const ponerhorarios = async () => {

    for (let index = 0; index < dict_horario_inicio['horarios'].length; index++) {
        creartarjetas(dict_horario_inicio['titulo'],dict_horario_inicio['horarios'][index])
        creartarjetas(dict_horario_fin['titulo'],dict_horario_fin['horarios'][index])
    }
}



const CargaInicial= async() => {
    await ListarLocalidades()
    
    localidades.addEventListener('change',(event)=>{
        ListarLugares(event.target.value)
        sectiontest.innerHTML = ''
    })

    lugarinicio.addEventListener('change',(event) =>{
        ListarLugarFinal(event.target.value)
        mostrarhorarios(event.target.value,"inicio")
        sectiontest.innerHTML = ''
    })
    lugarfinal.addEventListener('change', (event) => {
        mostrarhorarios(event.target.value,"fin")
        sectiontest.innerHTML = ''
    })
}

let btnhorarios = document.getElementById("btnhorarios")

btnhorarios.addEventListener('click',() => {
    ponerhorarios()
})