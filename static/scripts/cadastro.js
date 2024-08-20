const formulario = document.querySelector('form')

const nome = document.querySelector('.input-nome')
const matricula = document.querySelector('.input-cpf')
const email = document.querySelector('.input-email')
const senha = document.querySelector('.input-senha')
const senha2 = document.querySelector('.input-senha2')

const aviso_nome = document.querySelector('.aviso-nome')
const aviso_nome_p = document.querySelector('.aviso-nome p')
const aviso_matricula = document.querySelector('.aviso-matricula')
const aviso_matricula_p = document.querySelector('.aviso-matricula p')
const aviso_email = document.querySelector('.aviso-email')
const aviso_email_p = document.querySelector('.aviso-email p')
const aviso_senha = document.querySelector('.aviso-senha')
const aviso_senha_p = document.querySelector('.aviso-senha p')
const aviso_senha2 = document.querySelector('.aviso-senha2')
const aviso_senha2_p = document.querySelector('.aviso-senha2 p')

function submitform (event) {
    event.preventDefault()

    const valor_nome = nome.value.trim()
    const valor_matricula = matricula.value.trim()
    const valor_email = email.value.trim()
    const valor_senha = senha.value.trim()
    const valor_senha2 = senha2.value.trim()

    let tem_erro = false

    if (valor_nome === '' || valor_matricula === '' || valor_email === '' || valor_senha === ''
        || valor_senha2 === '') {
            aviso_nome.style.display = 'flex'
            aviso_nome_p.innerText = 'Preencha tudo'
            tem_erro = true
        }

    else if (valor_nome.length < 4) {
        aviso_nome.style.display = 'flex'
        aviso_nome_p.innerText = 'Nome muito curto'
        tem_erro = true
    }

    else if (matricula.length < 4) {
        aviso_matricula.style.display = 'flex'
        aviso_matricula_p.innerText = 'Matrícula curta'
        tem_erro = true
    }

    else if (!valor_email.includes('@gmail.com')) {
        aviso_email.style.display = 'flex'
        aviso_email_p.innerText = 'Email incorreto'
        tem_erro = true
    }

    else if (valor_senha.length < 4) {
        console.log('oi')
        aviso_senha.style.display = 'flex'
        aviso_senha_p.innerText = 'Senha muito curta'
        tem_erro = true
    }

    else if (valor_senha !== valor_senha2) {
        aviso_senha.style.display = 'flex'
        aviso_senha_p.innerText = 'Senhas diferentes'
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

nome.addEventListener('focus', () => tirar_aviso(aviso_nome))
matricula.addEventListener('focus', () => tirar_aviso(aviso_matricula))
email.addEventListener('focus', () => tirar_aviso(aviso_email))
senha.addEventListener('focus', () => tirar_aviso(aviso_senha))
senha2.addEventListener('focus', () => tirar_aviso(aviso_senha2))