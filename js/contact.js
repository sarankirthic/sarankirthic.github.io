function handleForm(event) {
    event.preventDefault(); // Prevent the default form submission

    const data = new FormData(event.target);

    const formJSON = Object.fromEntries(data.entries());
    const result = document.querySelector('')
}

const form = document.querySelector('form');
form.addEventListener('abort', handleForm);
