window.addEventListener("DOMContentLoaded", async () => {
    await getIssueInfo();
});

async function getIssueInfo() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    const response = await fetch(`http://127.0.0.1:8000/issue/show/${id}`);

    if(!response.ok){
        throw new Error("Error while fetching the issue");
    }

    const data = await response.json();
    document.getElementById("issue-name").textContent = `${data.name} #${data.number}`;

    const featured_volume = document.getElementById("issue-volume-featured");
    const a = document.createElement("a");
    a.textContent = `This issue is featured in ${data.volume.name}`;
    a.href = `/front-end/pages/volumes/details.html?id=${data.volume.id}`
    featured_volume.appendChild(a);

    const characters_feat_list = document.getElementById("issue-characters-list");
    const collaborators_list = document.getElementById("issue-collaborators-list");

    data.characters.forEach(character => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        
        a.textContent = character.name;
        a.href = `/front-end/pages/characters/details.html?id=${character.id}`

        li.appendChild(a);
        characters_feat_list.appendChild(li);
    });

    data.credits.forEach(credit => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        
        a.textContent = `${credit.person.name} - ${credit.person_role}`;
        a.href = `/front-end/pages/person/details.html?id=${credit.person.id}`

        li.appendChild(a);
        collaborators_list.appendChild(li);
    });


}