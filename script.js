// Helper function to load pages dynamically
function loadPage(page) {
    fetch(`pages/${page}.html`)
        .then(response => {
            if (!response.ok) throw new Error('Page not found');
            return response.text();
        })
        .then(data => {
            document.getElementById('content').innerHTML = data;
            // Update browser history state
            history.pushState({ page }, '', `#${page}`);
        })
        .catch(error => {
            document.getElementById('content').innerHTML = `<h2>Error: ${error.message}</h2>`;
        });
}

// Handle navigation link clicks
document.querySelectorAll('header a').forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        const page = event.target.dataset.page;
        loadPage(page);
    });
});

// Handle back/forward navigation
window.addEventListener('popstate', () => {
    const page = window.location.hash.replace('#', '') || 'home';
    loadPage(page);
});

// Load the correct page on initial load
const initialPage = window.location.hash.replace('#', '') || 'home';
loadPage(initialPage);