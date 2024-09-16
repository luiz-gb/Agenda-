const card = document.querySelector('.card')

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