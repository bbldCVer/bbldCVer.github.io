const menuToggle = document.querySelector('.menu-toggle');
const siteNav = document.querySelector('.site-nav');

if (menuToggle && siteNav) {
  menuToggle.addEventListener('click', () => {
    const open = siteNav.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', String(open));
  });

  siteNav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      siteNav.classList.remove('is-open');
      menuToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

const sections = [...document.querySelectorAll('.section-anchor')];
const navLinks = [...document.querySelectorAll('.nav-link:not(.nav-link--accent)')];

if ('IntersectionObserver' in window && sections.length && navLinks.length) {
  const visibleSections = new Map();
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => visibleSections.set(entry.target.id, entry));
    const active = [...visibleSections.values()]
      .filter((entry) => entry.isIntersecting)
      .sort((a, b) => Math.abs(a.boundingClientRect.top) - Math.abs(b.boundingClientRect.top))[0];
    if (!active) return;
    navLinks.forEach((link) => link.classList.toggle('is-active', link.getAttribute('href') === `#${active.target.id}`));
  }, { rootMargin: '-28% 0px -58% 0px', threshold: 0 });

  sections.forEach((section) => observer.observe(section));
}

const year = document.querySelector('#current-year');
if (year) year.textContent = new Date().getFullYear();
