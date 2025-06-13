// This script fetches the user's public IP address and displays it on the page.
document.addEventListener('DOMContentLoaded', () => {
fetch("https://api.ipify.org?format=json")
    .then(response => response.json())
    .then(data => {
        document.getElementById('ip-address').textContent = `IP address: ${data.ip}`;
    })
    .catch(error => {
        console.error("Error fetching IP address:", error);
        document.getElementById('ip-address').textContent = "IP address: Unable to fetch";
    });
});
