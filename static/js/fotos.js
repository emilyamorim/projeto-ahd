document.addEventListener('DOMContentLoaded', function() {
  
  // 1. Toggle visual das categorias (Pills)
  const catPills = document.querySelectorAll('.cat-pill');
  catPills.forEach(pill => {
    pill.addEventListener('click', function() {
      // Remove 'active' de todos
      catPills.forEach(p => p.classList.remove('active'));
      // Adiciona 'active' apenas no clicado
      this.classList.add('active');
    
  // 3. Filtro de Álbuns
  const albums = document.querySelectorAll('.album-card');
  // catPills was defined above
  catPills.forEach(pill => {
    pill.addEventListener('click', function() {
      const selectedCat = this.textContent.trim().toLowerCase();
      
      albums.forEach(album => {
        if (selectedCat === 'todas') {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
          return;
        }
        
        const tags = Array.from(album.querySelectorAll('.tag-pill')).map(t => t.textContent.trim().toLowerCase());
        
        if (tags.includes(selectedCat)) {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
        } else {
          album.style.opacity = '0'; 
          album.style.transform = 'scale(0.95)';
          setTimeout(() => { album.style.display = 'none'; }, 300);
        }
      });
    });
  });

  // 4. Lightbox (Modal de Fotos)
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxContent = document.getElementById('lightboxContent');
  const lightboxTitulo = document.getElementById('lightboxTitulo');
  const lightboxData = document.getElementById('lightboxData');
  
  document.querySelectorAll('.foto-item:not(.more-photos)').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Pegar cor de fundo
      const bgClass = Array.from(this.classList).find(c => c.startsWith('bg-grad-'));
      
      // Pegar textos
      const tituloElement = this.querySelector('.foto-titulo');
      const dataElement = this.querySelector('.foto-data');
      const titulo = tituloElement ? tituloElement.textContent : '';
      const data = dataElement ? dataElement.textContent : '';
      
      // Configurar Modal
      lightboxContent.className = 'lightbox-content ' + (bgClass || 'bg-grad-1');
      lightboxTitulo.textContent = titulo;
      lightboxData.textContent = data;
      
      // Mostrar Modal
      lightboxModal.classList.add('active');
    });
  });
  
  if (lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('active');
    });
  }
  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if(e.target === lightboxModal) {
        lightboxModal.classList.remove('active');
      }
    });
  }

  // 5. Relato Form Animation
  const btnPublicar = document.querySelector('.btn-publicar');
  if (btnPublicar) {
    btnPublicar.addEventListener('click', function() {
      if(textarea && textarea.value.trim() === '') return;
      
      this.innerHTML = '<i class="ti ti-loader" style="animation: spin 1s linear infinite;"></i> Enviando...';
      this.style.pointerEvents = 'none';
      this.style.opacity = '0.8';
      
      setTimeout(() => {
        const relatoBox = document.querySelector('.relato-box');
        if(relatoBox) {
          relatoBox.innerHTML = `
            <div style="text-align: center; padding: 40px 20px;">
              <div style="width: 64px; height: 64px; background: #e8f5e9; color: #4caf50; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px; margin: 0 auto 16px auto;">
                <i class="ti ti-check"></i>
              </div>
              <h3 style="color: #2e7d32; margin-bottom: 8px;">Relato publicado!</h3>
              <p style="color: var(--cinza-texto);">Muito obrigado por compartilhar sua história com o projeto Ampliando Horizontes Digitais.</p>
            </div>
          `;
        }
      }, 1500);
    });
  }

});
  
  // 3. Filtro de Álbuns
  const albums = document.querySelectorAll('.album-card');
  // catPills was defined above
  catPills.forEach(pill => {
    pill.addEventListener('click', function() {
      const selectedCat = this.textContent.trim().toLowerCase();
      
      albums.forEach(album => {
        if (selectedCat === 'todas') {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
          return;
        }
        
        const tags = Array.from(album.querySelectorAll('.tag-pill')).map(t => t.textContent.trim().toLowerCase());
        
        if (tags.includes(selectedCat)) {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
        } else {
          album.style.opacity = '0'; 
          album.style.transform = 'scale(0.95)';
          setTimeout(() => { album.style.display = 'none'; }, 300);
        }
      });
    });
  });

  // 4. Lightbox (Modal de Fotos)
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxContent = document.getElementById('lightboxContent');
  const lightboxTitulo = document.getElementById('lightboxTitulo');
  const lightboxData = document.getElementById('lightboxData');
  
  document.querySelectorAll('.foto-item:not(.more-photos)').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Pegar cor de fundo
      const bgClass = Array.from(this.classList).find(c => c.startsWith('bg-grad-'));
      
      // Pegar textos
      const tituloElement = this.querySelector('.foto-titulo');
      const dataElement = this.querySelector('.foto-data');
      const titulo = tituloElement ? tituloElement.textContent : '';
      const data = dataElement ? dataElement.textContent : '';
      
      // Configurar Modal
      lightboxContent.className = 'lightbox-content ' + (bgClass || 'bg-grad-1');
      lightboxTitulo.textContent = titulo;
      lightboxData.textContent = data;
      
      // Mostrar Modal
      lightboxModal.classList.add('active');
    });
  });
  
  if (lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('active');
    });
  }
  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if(e.target === lightboxModal) {
        lightboxModal.classList.remove('active');
      }
    });
  }

  // 5. Relato Form Animation
  const btnPublicar = document.querySelector('.btn-publicar');
  if (btnPublicar) {
    btnPublicar.addEventListener('click', function() {
      if(textarea && textarea.value.trim() === '') return;
      
      this.innerHTML = '<i class="ti ti-loader" style="animation: spin 1s linear infinite;"></i> Enviando...';
      this.style.pointerEvents = 'none';
      this.style.opacity = '0.8';
      
      setTimeout(() => {
        const relatoBox = document.querySelector('.relato-box');
        if(relatoBox) {
          relatoBox.innerHTML = `
            <div style="text-align: center; padding: 40px 20px;">
              <div style="width: 64px; height: 64px; background: #e8f5e9; color: #4caf50; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px; margin: 0 auto 16px auto;">
                <i class="ti ti-check"></i>
              </div>
              <h3 style="color: #2e7d32; margin-bottom: 8px;">Relato publicado!</h3>
              <p style="color: var(--cinza-texto);">Muito obrigado por compartilhar sua história com o projeto Ampliando Horizontes Digitais.</p>
            </div>
          `;
        }
      }, 1500);
    });
  }

});

  // 2. Contador de caracteres do Relato
  const textarea = document.getElementById('relatoInput');
  const charCount = document.getElementById('charCount');

  if (textarea && charCount) {
    textarea.addEventListener('input', function() {
      const currentLength = this.value.length;
      charCount.textContent = currentLength;
      
      // Opcional: mudar cor se chegar perto do limite
      if (currentLength >= 500) {
        charCount.style.color = '#ffcccb'; // aviso visual de limite atingido
      } else {
        charCount.style.color = 'var(--branco)';
      }
    
  // 3. Filtro de Álbuns
  const albums = document.querySelectorAll('.album-card');
  // catPills was defined above
  catPills.forEach(pill => {
    pill.addEventListener('click', function() {
      const selectedCat = this.textContent.trim().toLowerCase();
      
      albums.forEach(album => {
        if (selectedCat === 'todas') {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
          return;
        }
        
        const tags = Array.from(album.querySelectorAll('.tag-pill')).map(t => t.textContent.trim().toLowerCase());
        
        if (tags.includes(selectedCat)) {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
        } else {
          album.style.opacity = '0'; 
          album.style.transform = 'scale(0.95)';
          setTimeout(() => { album.style.display = 'none'; }, 300);
        }
      });
    });
  });

  // 4. Lightbox (Modal de Fotos)
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxContent = document.getElementById('lightboxContent');
  const lightboxTitulo = document.getElementById('lightboxTitulo');
  const lightboxData = document.getElementById('lightboxData');
  
  document.querySelectorAll('.foto-item:not(.more-photos)').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Pegar cor de fundo
      const bgClass = Array.from(this.classList).find(c => c.startsWith('bg-grad-'));
      
      // Pegar textos
      const tituloElement = this.querySelector('.foto-titulo');
      const dataElement = this.querySelector('.foto-data');
      const titulo = tituloElement ? tituloElement.textContent : '';
      const data = dataElement ? dataElement.textContent : '';
      
      // Configurar Modal
      lightboxContent.className = 'lightbox-content ' + (bgClass || 'bg-grad-1');
      lightboxTitulo.textContent = titulo;
      lightboxData.textContent = data;
      
      // Mostrar Modal
      lightboxModal.classList.add('active');
    });
  });
  
  if (lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('active');
    });
  }
  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if(e.target === lightboxModal) {
        lightboxModal.classList.remove('active');
      }
    });
  }

  // 5. Relato Form Animation
  const btnPublicar = document.querySelector('.btn-publicar');
  if (btnPublicar) {
    btnPublicar.addEventListener('click', function() {
      if(textarea && textarea.value.trim() === '') return;
      
      this.innerHTML = '<i class="ti ti-loader" style="animation: spin 1s linear infinite;"></i> Enviando...';
      this.style.pointerEvents = 'none';
      this.style.opacity = '0.8';
      
      setTimeout(() => {
        const relatoBox = document.querySelector('.relato-box');
        if(relatoBox) {
          relatoBox.innerHTML = `
            <div style="text-align: center; padding: 40px 20px;">
              <div style="width: 64px; height: 64px; background: #e8f5e9; color: #4caf50; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px; margin: 0 auto 16px auto;">
                <i class="ti ti-check"></i>
              </div>
              <h3 style="color: #2e7d32; margin-bottom: 8px;">Relato publicado!</h3>
              <p style="color: var(--cinza-texto);">Muito obrigado por compartilhar sua história com o projeto Ampliando Horizontes Digitais.</p>
            </div>
          `;
        }
      }, 1500);
    });
  }

});
  }


  // 3. Filtro de Álbuns
  const albums = document.querySelectorAll('.album-card');
  // catPills was defined above
  catPills.forEach(pill => {
    pill.addEventListener('click', function() {
      const selectedCat = this.textContent.trim().toLowerCase();
      
      albums.forEach(album => {
        if (selectedCat === 'todas') {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
          return;
        }
        
        const tags = Array.from(album.querySelectorAll('.tag-pill')).map(t => t.textContent.trim().toLowerCase());
        
        if (tags.includes(selectedCat)) {
          album.style.display = 'block';
          setTimeout(() => { album.style.opacity = '1'; album.style.transform = 'scale(1)'; }, 50);
        } else {
          album.style.opacity = '0'; 
          album.style.transform = 'scale(0.95)';
          setTimeout(() => { album.style.display = 'none'; }, 300);
        }
      });
    });
  });

  // 4. Lightbox (Modal de Fotos)
  const lightboxModal = document.getElementById('lightboxModal');
  const lightboxClose = document.getElementById('lightboxClose');
  const lightboxContent = document.getElementById('lightboxContent');
  const lightboxTitulo = document.getElementById('lightboxTitulo');
  const lightboxData = document.getElementById('lightboxData');
  
  document.querySelectorAll('.foto-item:not(.more-photos)').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      
      // Pegar cor de fundo
      const bgClass = Array.from(this.classList).find(c => c.startsWith('bg-grad-'));
      
      // Pegar textos
      const tituloElement = this.querySelector('.foto-titulo');
      const dataElement = this.querySelector('.foto-data');
      const titulo = tituloElement ? tituloElement.textContent : '';
      const data = dataElement ? dataElement.textContent : '';
      
      // Configurar Modal
      lightboxContent.className = 'lightbox-content ' + (bgClass || 'bg-grad-1');
      lightboxTitulo.textContent = titulo;
      lightboxData.textContent = data;
      
      // Mostrar Modal
      lightboxModal.classList.add('active');
    });
  });
  
  if (lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightboxModal.classList.remove('active');
    });
  }
  if (lightboxModal) {
    lightboxModal.addEventListener('click', (e) => {
      if(e.target === lightboxModal) {
        lightboxModal.classList.remove('active');
      }
    });
  }

  // 5. Relato Form Animation
  const btnPublicar = document.querySelector('.btn-publicar');
  if (btnPublicar) {
    btnPublicar.addEventListener('click', function() {
      if(textarea && textarea.value.trim() === '') return;
      
      this.innerHTML = '<i class="ti ti-loader" style="animation: spin 1s linear infinite;"></i> Enviando...';
      this.style.pointerEvents = 'none';
      this.style.opacity = '0.8';
      
      setTimeout(() => {
        const relatoBox = document.querySelector('.relato-box');
        if(relatoBox) {
          relatoBox.innerHTML = `
            <div style="text-align: center; padding: 40px 20px;">
              <div style="width: 64px; height: 64px; background: #e8f5e9; color: #4caf50; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 32px; margin: 0 auto 16px auto;">
                <i class="ti ti-check"></i>
              </div>
              <h3 style="color: #2e7d32; margin-bottom: 8px;">Relato publicado!</h3>
              <p style="color: var(--cinza-texto);">Muito obrigado por compartilhar sua história com o projeto Ampliando Horizontes Digitais.</p>
            </div>
          `;
        }
      }, 1500);
    });
  }

});
