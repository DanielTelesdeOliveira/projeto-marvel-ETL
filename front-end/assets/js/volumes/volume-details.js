window.addEventListener("DOMContentLoaded", async () => {
    await getVolumeInfo();
});

characters_ids = new Set();
collaborators_ids = new Set();

async function getVolumeInfo() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    const response = await fetch(`http://127.0.0.1:8000/volume/show/${id}`);

    if(!response.ok){
        throw new Error("Error while fetching the volume");
    }

    const data = await response.json();
    document.getElementById("volume-name").textContent = data.name;
    document.getElementById("volume-issues-quantity").textContent = `This volume has ${data.issues_quantity} issues`
    
    const characters_feat_list = document.getElementById("volume-characters-list");
    const issues_list = document.getElementById("volume-issues-list");
    const collaborators_list = document.getElementById("volume-collaborators-list");
    
    data.issues.forEach(issue => {
        let li = document.createElement("li");
        let a = document.createElement("a");
        a.textContent = `${issue.name} #${issue.number}`;
        a.href = `/front-end/pages/issues/details.html?id=${issue.id}`   
        li.appendChild(a);
        issues_list.appendChild(li);
    });

    data.issues.forEach(issue => {
        issue.characters.forEach(character => {
             let li = document.createElement("li");
             let a = document.createElement("a");
             if(!isRepeated(characters_ids, character.id)){
                a.textContent = `${character.name}`;
                a.href = `/front-end/pages/characters/details.html?id=${character.id}`   
                li.appendChild(a);
                characters_feat_list.appendChild(li);
            }
        })
    });

    data.issues.forEach(issue => {
        issue.credits.forEach(credit => {
             let li = document.createElement("li");
             let a = document.createElement("a");
             if(!isRepeated(collaborators_ids, credit.person.id)){
                a.textContent = `${credit.person.name}`;
                a.href = `/front-end/pages/person/details.html?id=${credit.person.id}`   
                li.appendChild(a);
                collaborators_list.appendChild(li);
            }
        })
    });
}

function isRepeated(set, id){
    if(set.has(id)){
        return true;
    }
    set.add(id);
    return false;
}