window.addEventListener("DOMContentLoaded", async () => {
    await getCharactersList();
});

async function getCharactersList() {
    const response = await fetch(`http://127.0.0.1:8000/characters/show`);
    const data = await response.json();

    const list = document.getElementById("characters_list");
    
    data.forEach(character => {
            const li = document.createElement("li");
            const a = document.createElement("a");
            a.href = `/front-end/pages/characters/details.html?id=${character.id}`
            a.textContent = `${character.id} - ${character.name}`;     
            li.appendChild(a); 
            list.appendChild(li);
        });
}