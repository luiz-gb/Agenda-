const formulario = document.querySelector('form')
const matricula = document.querySelector('.input-cpf')
const senha = document.querySelector('.input-senha')
const card = document.querySelector('.card')

function submitform (event) {
    event.preventDefault()

    const valormatricula = matricula.value.trim()
    const valorsenha = senha.value.trim()

    let tem_erro = false

    if (valormatricula === ''){
        matricula.classList.add('input-erro')
        tem_erro = true
    }

    if (valorsenha === '') {
        senha.classList.add('input-erro')
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


// barra temporizada

function tirar_card () {
    if (card) {
        card.style.display = 'none'
    }
}

function startProgressBar(duration) {
    const barra2 = document.querySelector('.barra2');
    if (barra2) {
        barra2.style.transitionDuration = `${duration}ms`;
        barra2.style.transform = `scaleX(0)`;
    }
}

// Tempo em milissegundos 
const tempoDeExibicao = 2000;

window.onload = function() {
    startProgressBar(tempoDeExibicao);
    setTimeout(tirar_card, tempoDeExibicao);
};