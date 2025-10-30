// Portfolio JavaScript Functionality

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all functionality
    initThemeToggle();
    initSkillsScroll();
    initScrollAnimations();
    initSmoothScroll();
});

// Theme Toggle Functionality
function initThemeToggle() {
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = themeToggle.querySelector('i');

    // Check for saved theme preference
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }

    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-mode');

        if (body.classList.contains('dark-mode')) {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
            localStorage.setItem('theme', 'dark');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
            localStorage.setItem('theme', 'light');
        }
    });
}

// Project Toggle Functionality
function toggleProject(projectId) {
    const projectDetails = document.getElementById(projectId);
    const icon = document.getElementById('icon-' + projectId);

    if (projectDetails.classList.contains('hidden')) {
        projectDetails.classList.remove('hidden');
        icon.classList.add('rotate-180');
    } else {
        projectDetails.classList.add('hidden');
        icon.classList.remove('rotate-180');
    }
}

// Skills Scrolling - Duplicate items for infinite scroll effect
function initSkillsScroll() {
    const skillScrolls = document.querySelectorAll('.skill-scroll');

    skillScrolls.forEach(scroll => {
        const icons = scroll.innerHTML;
        scroll.innerHTML += icons; // Duplicate for seamless loop
    });
}

// Scroll Animations
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Observe elements for animation
    const animatedElements = document.querySelectorAll(
        '.highlight-card, .project-card, .experience-card, .education-card, .cert-card'
    );

    animatedElements.forEach(el => {
        observer.observe(el);
    });
}

// Smooth Scroll for anchor links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Scroll to Top functionality (optional)
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Add scroll progress indicator (optional)
window.addEventListener('scroll', function() {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;

    // If you want to add a progress bar, uncomment below
    // const progressBar = document.getElementById('progress-bar');
    // if (progressBar) {
    //     progressBar.style.width = scrolled + '%';
    // }
});

// Form Validation (if contact form is added later)
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const name = form.querySelector('input[name="name"]').value.trim();
        const email = form.querySelector('input[name="email"]').value.trim();
        const message = form.querySelector('textarea[name="message"]').value.trim();

        if (!name || !email || !message) {
            alert('Please fill in all fields');
            return false;
        }

        if (!isValidEmail(email)) {
            alert('Please enter a valid email address');
            return false;
        }

        // Process form submission
        console.log('Form submitted successfully');
        return true;
    });
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Keyboard Navigation Enhancement
document.addEventListener('keydown', function(e) {
    // Press 'T' to toggle theme
    if (e.key === 't' || e.key === 'T') {
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
            themeToggle.click();
        }
    }
});

// Utility function to detect mobile devices
function isMobileDevice() {
    return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

// Disable hover effects on mobile
if (isMobileDevice()) {
    document.body.classList.add('mobile-device');
}

// Performance: Debounce function for scroll events
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Add loading animation
window.addEventListener('load', function() {
    document.body.classList.add('loaded');
});

// Console message
console.log('%c👋 Hi there! Welcome to my portfolio', 'color: #21808d; font-size: 16px; font-weight: bold;');
console.log('%cInterested in the code? Check out the GitHub repos linked on the page!', 'color: #6b7280; font-size: 12px;');
