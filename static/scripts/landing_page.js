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

const formulario = document.querySelector('form')
const nome = document.querySelector('.input-nome')
const email = document.querySelector('.input-email')
const descricao = document.querySelector('.input-descricao')

const aviso_nome = document.querySelector('.aviso-nome')
const aviso_nome_p = document.querySelector('.aviso-nome p')
const aviso_email = document.querySelector('.aviso-email')
const aviso_email_p = document.querySelector('.aviso-email p')
const aviso_descricao = document.querySelector('.aviso-descricao')
const aviso_descricao_p = document.querySelector('.aviso-descricao p')

function submitform (event) {
    console.log('oi')
    event.preventDefault()

    const valor_nome = nome.value.trim()
    const valor_email = email.value.trim()
    const valor_descricao = descricao.value.trim()

    let tem_erro = false
    
    if (valor_nome === "" || valor_email === "" || valor_descricao === "") {
        aviso_nome.style.display = "flex"
        aviso_nome_p.innerText = "Preencha todos os campos"
        tem_erro = true
    }

    else if (valor_nome.length < 3) {
        aviso_nome.style.display = "flex"
        aviso_nome_p.innerText = "Nome curto"
        tem_erro = true
    }

    else if (!valor_email.includes('@gmail.com') && !valor_email.includes('@academico.ifpb.edu.br')) {
        aviso_email.style.display = "flex"
        aviso_email_p.innerText = "Email incorreto"
        tem_erro = true
    }

    else if (valor_descricao.length < 8) {
        aviso_descricao.style.display = "flex"
        aviso_descricao_p.innerText = "Comentário curto"
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

nome.addEventListener('mouseover', () => tirar_aviso(aviso_nome))
email.addEventListener('mouseover', () => tirar_aviso(aviso_email))
descricao.addEventListener('mouseover', () => tirar_aviso(aviso_descricao))