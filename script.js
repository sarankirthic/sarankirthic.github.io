// Get the current page URL
const currentPage = window.location.pathname;
const pageNames = {
	'/': 'home',
	'/about/about.html': 'about',
};

// Function to generate breadcrumbs
function generateCoffee() {
	const coffeeContainer = document.querySelector('.coffeespill');
	const pathSegments = currentPage.split('/').filter(
			segment => segment !== '');  // Split the URL and remove empty segments

	let coffeeStain = '<a href="/">home</a>';
	

	coffeeContainer.innerHTML = coffeeStain;
}

// Call the function to generate coffee
generateCoffee();
