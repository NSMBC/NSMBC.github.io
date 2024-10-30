document.addEventListener("DOMContentLoaded", function() {
    fetch('/nav.html')
        .then(response => response.text())
        .then(html => {
            document.getElementById("navbar").innerHTML = html;
        });
});