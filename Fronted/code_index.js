const inputConsult = document.querySelector('#consult')

inputConsult.addEventListener("keyup", e => { 
    if (e.keyCode === 13) {
        let tempValue = inputConsult.value
        // inputConsult.value = ""
        location.assign("docs.html?consult="+tempValue)
    }
})