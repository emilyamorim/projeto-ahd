function toggleSidebar() {
  const sidebar = document.getElementById('sidebarSuap');
  const icon = document.getElementById('toggleIcon');
  if (sidebar) {
    sidebar.classList.toggle('collapsed');
    if (sidebar.classList.contains('collapsed')) {
      icon.classList.remove('ti-chevron-left');
      icon.classList.add('ti-chevron-right');
    } else {
      icon.classList.remove('ti-chevron-right');
      icon.classList.add('ti-chevron-left');
    }
  }
}

function toggleMobileMenu() {
  const overlay = document.querySelector('.menu-overlay');
  const isActive = document.body.classList.toggle('menu-open');
  if (overlay) overlay.classList.toggle('active', isActive);
}

// Fechar o menu mobile ao clicar fora dele
document.addEventListener('click', function(e) {
  const collapse = document.querySelector('.navbar-collapse');
  const btn = document.querySelector('.mobile-menu-btn');

  if (document.body.classList.contains('menu-open') && collapse && !collapse.contains(e.target) && !btn.contains(e.target)) {
    document.body.classList.remove('menu-open');
    const overlay = document.querySelector('.menu-overlay');
    if (overlay) overlay.classList.remove('active');
  }
});
