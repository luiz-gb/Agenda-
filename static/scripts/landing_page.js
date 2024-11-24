function scrollToSection(event, sectionId) {
    event.preventDefault(); // Previne o comportamento padrão de navegação

    const section = document.getElementById(sectionId); // Acessa a seção com o ID correto
    const offsetTop = section.offsetTop; // Posição no topo da seção

    // Usando requestAnimationFrame para animação suave
    let start = null;
    let scrollPosition = window.scrollY || window.pageYOffset;

    function animateScroll(timestamp) {
        if (!start) start = timestamp;
        let progress = timestamp - start;
        let distance = offsetTop - scrollPosition;

        // Definindo a duração da animação (aqui 800ms)
        let duration = 800;
        let move = Math.min(progress / duration, 1) * distance;

        window.scrollTo(0, scrollPosition + move);

        if (progress < duration) {
            requestAnimationFrame(animateScroll); // Continuar a animação até terminar
        } else {
            window.scrollTo(0, offsetTop); // Garantir que o scroll termine exatamente na seção
        }
    }

    requestAnimationFrame(animateScroll); // Inicia a animação suave
}

// Mostrar ou esconder o botão baseado na rolagem
window.onscroll = function () {
    const scrollButton = document.getElementById('rolar-cima');

    if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
        // Mostrar o botão quando rolar para baixo 100px
        scrollButton.style.display = "flex";
    } else {
        // Esconder o botão quando estiver no topo
        scrollButton.style.display = "none";
    }
};

// Rolagem suave até o topo quando o botão for clicado
document.getElementById('rolar-cima').addEventListener('click', function (event) {
    event.preventDefault(); // Previne o comportamento padrão do link

    window.scrollTo({
        top: 0,
        left: 0,
        behavior: 'smooth' // Aplica o scroll suave
    });
});