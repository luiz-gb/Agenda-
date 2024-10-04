const searchIcon = document.getElementById('search-icon');
        const searchContainer = document.querySelector('.navbar-search');

        searchIcon.addEventListener('click', function() {
            searchContainer.classList.toggle('active');
            if (searchContainer.classList.contains('active')) {
                searchContainer.querySelector('input').focus();
            }
        });

        document.addEventListener('click', function(e) {
            if (!searchContainer.contains(e.target) && !searchIcon.contains(e.target)) {
                searchContainer.classList.remove('active');
            }
        });

// profile

const perfil = document.querySelector('.navbar-profile')
const expanded = document.querySelector('.perfil-expanded')

function aparecer_expanded () {
        expanded.style.display = 'inline-block'
    
}

function tirar_expanded () {
    expanded.style.display = 'none'
}

perfil.addEventListener('mouseover', aparecer_expanded)
expanded.addEventListener('mouseleave', tirar_expanded)

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