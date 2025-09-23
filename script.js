function loadPage(page) {
    fetch(`pages/${page}.html`)
        .then(response => {
            if (!response.ok) throw new Error('Page not found');
            return response.text();
        })
        .then(data => {
            document.getElementById('content').innerHTML = data;
            history.pushState({ page }, '', `#${page}`);
        })
        .catch(error => {
            document.getElementById('content').innerHTML = `<h2>Error: ${error.message}</h2>`;
        });
}

document.addEventListener('click', event => {
    const link = event.target.closest('[data-page]');
    if(!link) return;
    event.preventDefault();
    const page = event.target.dataset.page;
    loadPage(page);
});

window.addEventListener('popstate', () => {
    const page = window.location.hash.replace('#', '') || 'home';
    loadPage(page);
});

const initialPage = window.location.hash.replace('#', '') || 'home';
loadPage(initialPage);
