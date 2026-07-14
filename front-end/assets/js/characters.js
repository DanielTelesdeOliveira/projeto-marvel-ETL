window.addEventListener("DOMContentLoaded", async () => {
    const response = await fetch("http://127.0.0.1:8000/characters/");
    const data = await response.json();
    document.getElementById("characters_message").textContent = data.message;
});    
