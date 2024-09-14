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
    if (expanded.style.display === 'inline-block') {
        expanded.style.display = 'none'
    }
    else {
        expanded.style.display = 'inline-block'
    }
}

//calendario

perfil.addEventListener('click', aparecer_expanded)

document.addEventListener('DOMContentLoaded', function() {
    flatpickr(".input-date", {
        inline: true,  // Mantém o calendário sempre visível
        dateFormat: "Y-m-d", // Formato da data
        locale: "pt",  // Define o idioma para português
    });
});