const formulario = document.querySelector('form')
const titulo = document.querySelector('.input-titulo')
const data = document.querySelector('.input-date')

const aviso_titulo = document.querySelector('.aviso-titulo')
const aviso_titulo_p = document.querySelector('.aviso-titulo p')
const aviso_data = document.querySelector('.aviso-date')
const aviso_data_p = document.querySelector('.aviso-date p')
const avisos = document.querySelectorAll('.aviso')
const inputs = document.querySelectorAll('.inputs')

function submitform (event) {
    event.preventDefault()

    const valortitulo = titulo.value.trim()
    const valordata = data.value.trim()

    let tem_erro = false

    if (valortitulo === ''){
        aviso_titulo.style.display = 'flex'
        aviso_titulo_p.innerText = 'Preencha o campo'
        tem_erro = true
    }

    else if (valordata === ''){
        console.log('oi')
        aviso_data.style.display = 'flex'
        aviso_data_p.innerText = 'Preencha o campo'
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
