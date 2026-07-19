window.addEventListener("DOMContentLoaded", async () => {
    await getCharactersInfo();
});

async function getCharactersInfo(){
    const params = new URLSearchParams(window.location.search)
    const id = params.get("id")
    console.log(id);
    const response = await fetch(`http://127.0.0.1:8000/characters/show/${id}`);
    
    if(!response){
        throw new Error("Error while fetching the character");
    }

    const data = await response.json();
    document.getElementById("character-name").textContent = data.name;
    document.getElementById("character-description").textContent = data.description;

    const creators_list = document.getElementById("character-creators-list");
    const powers_list = document.getElementById("character-powers-list");
    const issues_list = document.getElementById("character-issues-list");

    data.creators.forEach(creator => {
         const li = document.createElement("li");
         li.textContent = creator.name;
         creators_list.appendChild(li);       
    });

    data.powers.forEach(power => {
         const li = document.createElement("li");
         li.textContent = power.name;
         powers_list.appendChild(li);       
    });

    data.issues.forEach(issue => {
         const li = document.createElement("li");
         li.textContent = issue.name;
         issues_list.appendChild(li);       
    });

}