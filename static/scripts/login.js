const formulario = document.querySelector('form')
const matricula = document.querySelector('.input-cpf')
const senha = document.querySelector('.input-senha')
const card = document.querySelector('.card')

const aviso_senha = document.querySelector('.aviso-senha')
const aviso_senha_p = document.querySelector('.aviso-senha p')
const aviso_matricula = document.querySelector('.aviso-matricula')
const aviso_matricula_p = document.querySelector('.aviso-matricula p')
const avisos = document.querySelectorAll('.aviso')
const inputs = document.querySelectorAll('.inputs')

function submitform (event) {
    event.preventDefault()

    const valormatricula = matricula.value.trim()
    const valorsenha = senha.value.trim()

    let tem_erro = false

    if (valormatricula === '' || valorsenha === ''){
        aviso_matricula.style.display = 'flex'
        aviso_matricula_p.innerText = 'Preencha o formulário totalmente'
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


// tirat os avisos ao clicar no input

function tirar_aviso (aviso) {
    if (aviso.style.display === 'flex') {
        aviso.style.display = 'none'
    }
}

matricula.addEventListener('focus', () => tirar_aviso(aviso_matricula))
senha.addEventListener('focus', () => tirar_aviso(aviso_senha))