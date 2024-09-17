const formulario = document.querySelector('form')
const nome = document.querySelector('.input-nome')
const email = document.querySelector('.input-email')
const senha = document.querySelector('.input-senha')
const label_file = document.querySelector('.label-input-file')
const file = document.getElementById('input-file');

const aviso_nome = document.querySelector('.aviso-nome')
const aviso_nome_p = document.querySelector('.aviso-nome p')
const aviso_email = document.querySelector('.aviso-email')
const aviso_email_p = document.querySelector('.aviso-email p')
const aviso_senha = document.querySelector('.aviso-senha')
const aviso_senha_p = document.querySelector('.aviso-senha p')
const aviso_file = document.querySelector('.aviso-file')
const aviso_file_p = document.querySelector('.aviso-file p')
const avisos = document.querySelectorAll('.aviso')
const inputs = document.querySelectorAll('.inputs')


const valornome_pre = nome.value.trim()
const valoremail_pre = email.value.trim()
const valorsenha_pre = email.value.trim()
const senha_escondida = document.querySelector('.senha-escondida').textContent

function submitform (event) {
    event.preventDefault()

    const valornome = nome.value.trim()
    const valoremail = email.value.trim()
    const valorsenha = senha.value.trim()

    let file_i = file.files[0]; // Obtém o primeiro arquivo (se houver)
    let valorfile = '';
    let extensaofile = '';

    if (file_i) {
        valorfile = file_i.name; // Obtém o nome do arquivo
        extensaofile = valorfile.split('.').pop();
    }

    console.log(extensaofile)
    let tem_erro = false

    if (valornome === valornome_pre && valoremail === valoremail_pre && valorsenha === '' && valorfile === ''){
        aviso_nome.style.display = 'flex'
        aviso_nome_p.innerText = 'Dados iguais!'
        tem_erro = true
    }

    else if (valornome === valornome_pre && valoremail === valoremail_pre && valorfile === '' && valorsenha.length < 4){
        aviso_senha.style.display = 'flex'
        aviso_senha_p.innerText = 'Senha curta!'
        tem_erro = true
    }

    else if (valornome === valornome_pre && valoremail === valoremail_pre && valorfile === '' && valorsenha === senha_escondida){
        aviso_senha.style.display = 'flex'
        aviso_senha_p.innerText = 'Senha antiga inserida!'
        tem_erro = true
    }

    else if (valornome === '') {
        aviso_nome.style.display = 'flex'
        aviso_nome_p.innerText = 'Campo vazio!'
        tem_erro = true
    }

    else if (!valoremail.includes('@gmail.com')) {
        aviso_email.style.display = 'flex'
        aviso_email_p.innerText = 'Email incorreto!'
        tem_erro = true
    }

    else if (valoremail === '') {
        aviso_email.style.display = 'flex'
        aviso_email_p.innerText = 'Campo vazio!'
        tem_erro = true
    }

    
    else if (extensaofile !== 'jpg' && extensaofile !== 'png' && extensaofile !== '') {
        aviso_file.style.display = 'flex'
        aviso_file_p.innerText = 'Arquivo inválido!'
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
senha.addEventListener('mouseover', () => tirar_aviso(aviso_senha))
label_file.addEventListener('mouseover', () => tirar_aviso(aviso_file))