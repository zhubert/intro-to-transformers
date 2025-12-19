// Force theme to always use system preference instead of localStorage
(function() {
  // Clear any stored theme preference
  localStorage.removeItem('theme');
  localStorage.removeItem('color-mode');
  localStorage.removeItem('myst-theme');

  // Function to apply system preference
  function applySystemTheme() {
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const html = document.documentElement;

    if (prefersDark) {
      html.classList.add('dark');
      html.classList.remove('light');
    } else {
      html.classList.add('light');
      html.classList.remove('dark');
    }
  }

  // Apply immediately
  applySystemTheme();

  // Listen for system preference changes
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', applySystemTheme);

  // Override any localStorage writes that might happen
  const originalSetItem = localStorage.setItem;
  localStorage.setItem = function(key, value) {
    // Block theme-related keys
    if (key === 'theme' || key === 'color-mode' || key === 'myst-theme') {
      return;
    }
    return originalSetItem.apply(this, arguments);
  };
})();

// Add hover effects for home link avatar
document.addEventListener('DOMContentLoaded', function() {
  const avatar = document.querySelector('.home-link-avatar');
  if (avatar) {
    avatar.addEventListener('mouseenter', function() {
      this.style.transform = 'scale(1.05)';
      this.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)';
    });

    avatar.addEventListener('mouseleave', function() {
      this.style.transform = 'scale(1)';
      this.style.boxShadow = 'none';
    });
  }
});
