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
const params= new URLSearchParams(document.URL.split('?')[1]);
const inputConsult = document.querySelector('#consult')
inputConsult.value = params.get('consult')
let value = inputConsult.value;

document.querySelector('#tittle').innerHTML = params.get('consult') + " - Buscando con RIUL"

function fullDocuments(){
    if (value != ""){
        getAndCreateDocuments(value);
    }
}

inputConsult.addEventListener("keyup", e => { 

    if (e.keyCode === 13) {
        let tempValue = inputConsult.value
        inputConsult.value = value

        location.assign("docs.html?consult="+tempValue)
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
        
        let maxChars = 370
        if (passage.length > maxChars){
            passage = passage.substring(0,maxChars)
            passage += '...'
        }
        if (textLink.length > 70){
            textLink = textLink.substring(0,70)
            textLink += '...'
        }
        

        createDocSpace(doc,link, textLink,consult,passage)

    }
}

fullDocuments()

// let params= new URLSearchParams(document.URL.split('?')[1]);
// document.getElementById("consult").value = params.get('consult');