window.addEventListener('load', async ()=>{
    await CargaInicial()
})

const diasSemana = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"];


function CargaInicial(){
     
     fetch('./get_dias_horarios')
        .then((data)=>data.json())
        .then((data) => data.dias_horarios.forEach((element)=>{
            let table = document.createElement('table')
            
            table.style.width = '100%'
            table.style.display = 'flex'
            table.style.justifyContent = 'center'
            table.style.flexWrap = 'wrap'
            table.style.marginBottom = '3rem'
            element.Horarios.forEach((e)=>{
                let row = document.createElement("td")
                let tr = document.createElement('tr')
                row.innerHTML = e
                tr.append(row)
                table.append(tr)
                document.body.append(table)
            })            
        }))
    
}