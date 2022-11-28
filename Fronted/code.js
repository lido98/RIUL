// Create new space for document////////////////////////////////////////////////////////////////////////
const doc = document.querySelector(".documents_section")

function createItem(docIn,linkIn,textPagrIn,textLinkIn){
    let link = document.createElement("a")
    link.setAttribute("href", linkIn)
    link.appendChild(document.createTextNode(textLinkIn))
    let pagr = document.createElement("p")
    pagr.innerHTML = textPagrIn
    let div = document.createElement("div")
    div.classList.add("doc_object")
    div.appendChild(link)
    div.appendChild(pagr)
    docIn.appendChild(div)
}

function highlightWordInText(pagraph, word_in){
    let wordChain = pagraph.split(' ')
    for (word in wordChain){
        if (word_in == wordChain[word]){
           pagraph = pagraph.replace(wordChain[word], '<b>'+wordChain[word]+'</b>')
        }
    }
    return pagraph
}
function highlightWords(pagraph, words){
    let result = pagraph
    for (word in words){
        result = highlightWordInText(result,words[word])
    }
    return result
}
function createDocSpace(docIn,link,textLink,consult,passage){
    createItem(docIn,link, highlightWords(passage,consult),textLink)
}

// set and send consult for GET API////////////////////////////////////////////////////////////////////

const consultParam = "El parametro que se le paso a la talla esta"
const inputConsult = document.querySelector('#consult')
let value = inputConsult.value

function fullDocuments(){
    if (value != ""){
        getAndCreateDocuments(value)
    }
}

inputConsult.addEventListener("keyup", e => { 

    if (e.keyCode === 13) {
        inputConsult.value = consultParam
        location.assign("docs.html")
        
        // let docs = document.querySelectorAll("div.doc_object")
        // for (let i = 0; i < docs.length; i++){
        //     // console.log(documents[i])
        //     docs[i].remove()
        // }

        // fullDocuments()    
    }
})


const xhr = new XMLHttpRequest()
function getAndCreateDocuments(consult){
    xhr.open("GET","http://127.0.0.1:8000/consult/"+consult, false)
    xhr.send()
    
    let documents = JSON.parse(xhr.responseText)
    for (i in documents){
        let link = documents[i]['link']
        let passage = documents[i]['passage']
        let consult = documents[i]['consult'].split(' ')
        let textLink = documents[i]['tittle']
        createDocSpace(doc,link, textLink,consult,passage)
    }
}

fullDocuments()
