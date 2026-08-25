
document.addEventListener('DOMContentLoaded', function() {
  
  // 1. Filtro de Categorias
  const filtroBtns = document.querySelectorAll('.filtro-btn');
  const cards = document.querySelectorAll('.noticias-card-grande');

  filtroBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // Ativar botão clicado
      filtroBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');

      const filtro = this.textContent.trim().toLowerCase();

      cards.forEach(card => {
        const tagElement = card.querySelector('.card-tag');
        if (!tagElement) return;
        
        const tag = tagElement.textContent.trim().toLowerCase();

        if (filtro === 'todas' || tag === filtro) {
          card.style.display = 'flex';
          setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          }, 10);
        } else {
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
          setTimeout(() => {
            card.style.display = 'none';
          }, 400); // tempo da transição no css
        }
      });
    });
  });

  // 2. Falso Botão Carregar Mais
  const btnCarregar = document.getElementById('btnCarregarMais');
  const containerCarregar = document.getElementById('carregarContainer');

  if (btnCarregar) {
    btnCarregar.addEventListener('click', function() {
      const originalHtml = this.innerHTML;
      this.innerHTML = '<i class="ti ti-loader" style="animation: spin 1s linear infinite;"></i> Carregando...';
      this.style.pointerEvents = 'none';
      
      setTimeout(() => {
        containerCarregar.innerHTML = '<p style="color: var(--cinza-texto); font-weight: 600;">Você já leu todas as novidades recentes!</p>';
      }, 1500);
    });
  }

});
