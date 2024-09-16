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
