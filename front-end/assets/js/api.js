async function getRootMessage() {
    window.addEventListener("DOMContentLoaded", async () => {
        const response = await fetch("http://127.0.0.1:8000/");
        const data = await response.json();
        document.getElementById("root_message").textContent = data.message;
    })
}

getRootMessage();