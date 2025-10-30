document.addEventListener('DOMContentLoaded', () => {
    // Active navigation link highlighting on scroll
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');

    function changeActiveLink() {
        let index = sections.length;

        // Find the current section in view
        while(--index && window.scrollY + 50 < sections[index].offsetTop) {}

        // Remove 'active' class from all nav links
        navLinks.forEach((link) => link.classList.remove('active'));

        // Add 'active' class to the current nav link
        if (navLinks[index]) {
            navLinks[index].classList.add('active');
        }
    }

    // Initial check and event listener for scrolling
    changeActiveLink();
    window.addEventListener('scroll', changeActiveLink);

    // Project item dropdown functionality
    document.querySelectorAll('.project-item').forEach(item => {
        item.addEventListener('click', (event) => {
            const details = item.querySelector('.project-details');
            const icon = item.querySelector('.fa-chevron-down, .fa-chevron-up');

            // Toggle display and icon
            if (details.style.display === 'block') {
                details.style.display = 'none';
                if (icon) {
                    icon.classList.remove('fa-chevron-up');
                    icon.classList.add('fa-chevron-down');
                }
            } else {
                details.style.display = 'block';
                if (icon) {
                    icon.classList.remove('fa-chevron-down');
                    icon.classList.add('fa-chevron-up');
                }
            }
        });
    });

    // Certifications carousel functionality
    const track = document.querySelector('.carousel-track');
    if (track) {
        const items = Array.from(track.children);
        const prevButton = document.getElementById('prevBtn');
        const nextButton = document.getElementById('nextBtn');
        let currentIndex = 0;
        let autoScrollInterval;

        // Function to update the carousel's position
        function updateCarousel() {
            if (items.length > 0) {
                const itemWidth = items[0].getBoundingClientRect().width;
                track.style.transform = `translateX(-${currentIndex * itemWidth}px)`;
            }
        }

        // Function to start auto-scrolling
        function startAutoScroll() {
            autoScrollInterval = setInterval(() => {
                currentIndex = (currentIndex + 1) % items.length;
                updateCarousel();
            }, 5000); // Scroll every 5 seconds
        }

        // Function to stop auto-scrolling
        function stopAutoScroll() {
            clearInterval(autoScrollInterval);
        }

        // Event listener for the 'previous' button
        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            updateCarousel();
            stopAutoScroll(); // Optional: stop auto-scroll on manual navigation
            startAutoScroll(); // Optional: restart auto-scroll after manual navigation
        });

        // Event listener for the 'next' button
        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex + 1) % items.length;
            updateCarousel();
            stopAutoScroll(); // Optional: stop auto-scroll on manual navigation
            startAutoScroll(); // Optional: restart auto-scroll after manual navigation
        });

        // Update carousel on window resize
        window.addEventListener('resize', updateCarousel);

        // Initial call to set the carousel position and start auto-scrolling
        updateCarousel();
        startAutoScroll();
    }
});
