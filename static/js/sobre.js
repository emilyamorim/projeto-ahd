document.addEventListener('DOMContentLoaded', function() {
  const tabBtns = document.querySelectorAll('.tab-btn');
  const abaContents = document.querySelectorAll('.aba-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', function() {
      // 1. Remove active das abas (botões)
      tabBtns.forEach(b => b.classList.remove('active'));
      
      // 2. Remove active dos conteúdos
      abaContents.forEach(c => c.classList.remove('active'));
      
      // 3. Adiciona active no botão clicado
      this.classList.add('active');
      
      // 4. Mostra o conteúdo correspondente baseado no data-target
      const targetId = this.getAttribute('data-target');
      document.getElementById(targetId).classList.add('active');
    });
  });
  // 5. Animacao de Contadores
  const counters = document.querySelectorAll('.counter');
  let countersAnimated = false;

  const animateCounters = () => {
    counters.forEach(counter => {
      const target = +counter.getAttribute('data-target');
      const suffix = counter.getAttribute('data-suffix');
      const duration = 2000; // 2 seconds
      const stepTime = Math.abs(Math.floor(duration / target));
      let current = 0;
      
      const timer = setInterval(() => {
        current += Math.ceil(target / 50); // Increment step
        if (current >= target) {
          current = target;
          clearInterval(timer);
        }
        // Format with dot if >= 1000
        let displayValue = current >= 1000 ? current.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".") : current;
        counter.textContent = displayValue + suffix;
      }, 30);
    });
  };

  // Animar se aba 1 for clicada ou se já estiver visível
  const observer = new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting && !countersAnimated) {
      countersAnimated = true;
      animateCounters();
    }
  });
  if(document.querySelector('.resultados-grid')) {
    observer.observe(document.querySelector('.resultados-grid'));
  }

  // 6. Filtro de Bolsistas
  const searchInput = document.getElementById('searchBolsistas');
  if (searchInput) {
    searchInput.addEventListener('input', function(e) {
      const term = e.target.value.toLowerCase();
      const cards = document.querySelectorAll('.bolsista-card');
      
      cards.forEach(card => {
        const name = card.textContent.toLowerCase();
        if (name.includes(term)) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  }

}); // Fim do DOMContentLoaded

// 7. Copiar Hex Code
window.copyHex = function(hex, element) {
  navigator.clipboard.writeText(hex).then(() => {
    element.classList.add('copied');
    setTimeout(() => {
      element.classList.remove('copied');
    }, 1500);
  });
};
