const EMAILJS_PUBLIC_KEY = import.meta.env.VITE_EMAILJS_PUBLIC_KEY;
const EMAILJS_SERVICE_ID = import.meta.env.VITE_EMAILJS_SERVICE_ID;
const EMAILJS_TEMPLATE_ID = import.meta.env.VITE_EMAILJS_TEMPLATE_ID;

document.addEventListener('DOMContentLoaded', () => {
    console.log("Script loaded");
    emailjs.init(EMAILJS_PUBLIC_KEY);

    const form = document.getElementById('contact-me');
    const submitBtn = form.querySelector('.submit-btn');

    form.addEventListener('input', () => {
        submitBtn.disabled = !form.checkValidity();
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();
        console.log("Form submitted");

        let CONTACT_FORM = document.getElementById('contact-me');
        emailjs.sendForm(
            EMAILJS_SERVICE_ID,
            EMAILJS_TEMPLATE_ID,
            CONTACT_FORM,
        ).then(function() {
            alert('Email sent successfully!');
            form.reset();
            submitBtn.disabled = true;
        }, function(error) {
            alert('Failed to send email. Please try again later.');
            console.error('EmailJS error:', error);
        });
    });
});
