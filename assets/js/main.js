/* main.js — comportamiento del blog */

(function () {
  'use strict';

  // Scroll-triggered animations via animate.css
  function initScrollAnimations() {
    const targets = document.querySelectorAll('.post-card, .archive-month, .tag-index-item');

    if (!('IntersectionObserver' in window)) {
      targets.forEach(el => el.classList.add('animate__animated', 'animate__fadeInUp'));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate__animated', 'animate__fadeInUp');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );

    targets.forEach(el => observer.observe(el));
  }

  // Shrink navbar on scroll
  function initNavbarScroll() {
    const nav = document.getElementById('main-nav');
    if (!nav) return;

    window.addEventListener('scroll', () => {
      if (window.scrollY > 40) {
        nav.classList.add('navbar-scrolled');
      } else {
        nav.classList.remove('navbar-scrolled');
      }
    }, { passive: true });
  }

  // Active nav link based on current URL
  function initActiveNavLink() {
    const links = document.querySelectorAll('.site-navbar .nav-link');
    const path = window.location.pathname;

    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href && href !== '/' && path.startsWith(href)) {
        link.classList.add('active');
      } else if (href === '/' && path === '/') {
        link.classList.add('active');
      }
    });
  }

  // Smooth anchor scroll
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      const href = anchor.getAttribute('href');
      if (!href || href === '#') return;
      anchor.addEventListener('click', (e) => {
        try {
          const target = document.querySelector(href);
          if (target) {
            e.preventDefault();
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
          }
        } catch (_) {}
      });
    });
  }

  // Run on DOM ready
  document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initNavbarScroll();
    initActiveNavLink();
    initSmoothScroll();
  });
})();
