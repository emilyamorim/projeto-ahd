document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.querySelector('.foto-carousel');
  if (!carousel) return;
  
  let isHovered = false;

  // Pausar o carrossel se o mouse estiver por cima
  carousel.addEventListener('mouseenter', () => isHovered = true);
  carousel.addEventListener('mouseleave', () => isHovered = false);
  // Pausar também no touch
  carousel.addEventListener('touchstart', () => isHovered = true);
  carousel.addEventListener('touchend', () => {
    setTimeout(() => isHovered = false, 2000); // Volta 2s depois de soltar
  });

  setInterval(() => {
    if (isHovered) return;
    
    // Só rola se houver imagens a mais (scroll)
    if (carousel.scrollWidth <= carousel.clientWidth) return;
    
    const cell = carousel.querySelector('.foto-strip-cell');
    const scrollStep = cell ? cell.clientWidth : 300;
    
    // Se chegou no final (com margem de erro de 10px), volta para o início
    if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10) {
      carousel.scrollTo({ left: 0, behavior: 'smooth' });
    } else {
      // Passa para a próxima imagem
      carousel.scrollBy({ left: scrollStep, behavior: 'smooth' });
    }
  }, 3500); // Passa a cada 3.5 segundos

  // --- ANIMAÇÃO DOS NÚMEROS (STATS) ---
  const statNums = document.querySelectorAll('.stat-num');
  
  const animateStats = (entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = parseInt(entry.target.innerText);
        if (isNaN(target)) return;
        
        // Pára de observar o elemento para não animar de novo
        observer.unobserve(entry.target);
        
        const duration = 2000; // 2 segundos de animação
        let startTimestamp = null;
        
        const step = (timestamp) => {
          if (!startTimestamp) startTimestamp = timestamp;
          // Calcula o progresso de 0 a 1
          const progress = Math.min((timestamp - startTimestamp) / duration, 1);
          
          // Função ease-out (começa rápido e desacelera no final)
          const easeOut = 1 - Math.pow(1 - progress, 4);
          
          entry.target.innerText = Math.floor(easeOut * target);
          
          if (progress < 1) {
            window.requestAnimationFrame(step);
          } else {
            // Garante que termina exatamente no número alvo
            entry.target.innerText = target;
          }
        };
        
        entry.target.innerText = '0';
        window.requestAnimationFrame(step);
      }
    });
  };

  if ('IntersectionObserver' in window && statNums.length > 0) {
    const statsObserver = new IntersectionObserver(animateStats, {
      threshold: 0.5 // Inicia quando estiver 50% visível na tela
    });
    
    statNums.forEach(num => {
      statsObserver.observe(num);
    });
  }
});