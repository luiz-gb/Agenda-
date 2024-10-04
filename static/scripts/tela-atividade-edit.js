const formulario = document.querySelector('form')
const titulo = document.querySelector('.input-titulo')
const data = document.querySelector('.input-date')

const aviso_titulo = document.querySelector('.aviso-titulo')
const aviso_titulo_p = document.querySelector('.aviso-titulo p')
const aviso_data = document.querySelector('.aviso-date')
const aviso_data_p = document.querySelector('.aviso-date p')
const avisos = document.querySelectorAll('.aviso')
const inputs = document.querySelectorAll('.inputs')

const descricao = document.querySelector('.input-descricao')
const visibilidade = document.querySelector('.input-select')
const status = document.querySelector('.input-status')

const valortitulo_antes = titulo.value.trim()
const valordata_antes = data.value.trim()
const valordescricao_antes = descricao.value.trim()
const valorvisibilidade_antes = visibilidade.value
const valorstatus_antes = status.value

function submitform (event) {
    event.preventDefault()
    console.log(valortitulo_antes)

    const valortitulo = titulo.value.trim()
    const valordata = data.value.trim()
    const valordescricao = descricao.value.trim()
    const valorvisibilidade = visibilidade.value
    const valorstatus = status.value

    let tem_erro = false

    if (valortitulo === valortitulo_antes && valordata === valordata_antes && valordescricao === valordescricao_antes && valorvisibilidade === valorvisibilidade_antes && valorstatus === valorstatus_antes){
        aviso_titulo.style.display = 'flex'
        aviso_titulo_p.innerText = 'Dados iguais!'
        tem_erro = true
    }

    else if (valortitulo === '') {
        aviso_titulo.style.display = 'flex'
        aviso_titulo_p.innerText = 'Preencha o campo!'
        tem_erro = true
    }

    else if (valordata === '') {
        aviso_data.style.display = 'flex'
        aviso_data_p.innerText = 'Preencha o campo!'
        tem_erro = true
    }

    if (tem_erro) {
        console.log('Envio não concluído!')
    }
    else {
        formulario.submit()
    }
}

formulario.addEventListener('submit', submitform)

// tirat os avisos ao clicar no input

function tirar_aviso (aviso) {
    if (aviso.style.display === 'flex') {
        aviso.style.display = 'none'
    }
}

titulo.addEventListener('mouseover', () => tirar_aviso(aviso_titulo))
data.addEventListener('mouseover', () => tirar_aviso(aviso_data))
