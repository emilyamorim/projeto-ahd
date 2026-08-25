document.addEventListener('DOMContentLoaded', function() {
  // Lógica para alternar (toggle) o tipo (Bolsistas/Cursistas) apenas visualmente por enquanto
  const toggleBtns = document.querySelectorAll('.type-toggle button');
  toggleBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      toggleBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');
    });
  });
});

// Função para abrir e fechar os detalhes do card da aluna
function toggleCard(btn) {
  // Encontra o container principal do card subindo na árvore do DOM
  const card = btn.closest('.aluna-card-wrap');
  const icon = btn.querySelector('i');
  const text = btn.querySelector('.btn-text');

  if (card.classList.contains('expanded')) {
    // Recolher
    card.classList.remove('expanded');
    text.textContent = 'Ver detalhes';
    icon.classList.remove('ti-chevron-up');
    icon.classList.add('ti-chevron-down');
  } else {
    // Expandir
    card.classList.add('expanded');
    text.textContent = 'Recolher';
    icon.classList.remove('ti-chevron-down');
    icon.classList.add('ti-chevron-up');
  }
}
