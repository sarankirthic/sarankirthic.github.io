function loadPage(page) {
  fetch(`/pages/${page}.html`)
    .then(response => {
      if (!response.ok) throw new Error('Page not found');
      return response.text();
    })
    .then(data => {
		console.log(data)
		document.getElementById('content').innerHTML = data;
    })
    .catch(error => {
      document.getElementById('content').innerHTML = `<h2>Error: ${error.message}</h2>`;
    });
}

document.querySelectorAll('header a').forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const page = event.target.dataset.page;
    loadPage(page);
  });
});

// loadPage('home');