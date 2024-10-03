// calendário
const monthYear = document.getElementById('month-year');
const calendarDays = document.getElementById('calendar-days');
const prevMonthBtn = document.getElementById('prev-month-btn');
const nextMonthBtn = document.getElementById('next-month-btn');

let currentDate = new Date();

function renderCalendar(date) {
    const year = date.getFullYear();
    const month = date.getMonth();

    // Define o primeiro dia do mês
    const firstDay = new Date(year, month, 1).getDay();

    // Número total de dias no mês
    const totalDays = new Date(year, month + 1, 0).getDate();

    // Atualiza o cabeçalho com o mês e o ano
    monthYear.textContent = date.toLocaleDateString('pt-BR', { month: 'long', year: 'numeric' });

    // Limpa os dias do calendário
    calendarDays.innerHTML = '';

    // Adiciona dias em branco para alinhamento
    for (let i = 0; i < firstDay; i++) {
        const emptyDiv = document.createElement('div');
        calendarDays.appendChild(emptyDiv);
    }

    // Preenche os dias do mês
    for (let i = 1; i <= totalDays; i++) {
        const dayDiv = document.createElement('div');
        dayDiv.textContent = i;

        // Destaca o dia atual
        if (
            i === new Date().getDate() &&
            month === new Date().getMonth() &&
            year === new Date().getFullYear()
        ) {
            dayDiv.classList.add('current-day');
        }

        calendarDays.appendChild(dayDiv);
    }
}

// Navegação pelos meses
prevMonthBtn.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() - 1);
    renderCalendar(currentDate);
});

nextMonthBtn.addEventListener('click', () => {
    currentDate.setMonth(currentDate.getMonth() + 1);
    renderCalendar(currentDate);
});

// Renderiza o calendário ao carregar a página
renderCalendar(currentDate);

 

