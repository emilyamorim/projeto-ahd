function toggleMobileMenu() {
  const collapse = document.querySelector('.navbar-collapse');
  const icon = document.getElementById('mobile-menu-icon');
  const overlay = document.querySelector('.menu-overlay');
  
  if (overlay) overlay.classList.toggle('active');
  collapse.classList.toggle('active');
  
  if (collapse.classList.contains('active')) {
    if (icon) { icon.classList.remove('ti-menu-2'); icon.classList.add('ti-x'); }
  } else {
    if (icon) { icon.classList.remove('ti-x'); icon.classList.add('ti-menu-2'); }
  }
}

// Fechar o menu mobile ao clicar fora dele
document.addEventListener('click', function(e) {
  const collapse = document.querySelector('.navbar-collapse');
  const btn = document.querySelector('.mobile-menu-btn');

  if (collapse && collapse.classList.contains('active') && !collapse.contains(e.target) && !btn.contains(e.target)) {
    collapse.classList.remove('active');
    const overlay = document.querySelector('.menu-overlay');
    if (overlay) overlay.classList.remove('active');
    const icon = document.getElementById('mobile-menu-icon');
    if (icon) {
      icon.classList.remove('ti-x');
      icon.classList.add('ti-menu-2');
    }
  }
});
