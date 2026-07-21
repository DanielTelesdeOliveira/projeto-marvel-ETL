window.addEventListener("DOMContentLoaded", async () => {
    await getPersonInfo();
})

async function getPersonInfo() {
    const params = new URLSearchParams(window.location.search)
    const id = params.get("id");
    console.log(id);
    const response = await fetch(`http://127.0.0.1:8000/person/show/${id}`);

    if(!response.ok){
        throw new Error("Error while fetching the person");
    }

    const data = await response.json();
    document.getElementById("person-name").textContent = data.name;

    const created_characters_list = document.getElementById("person-characters-created");
    const collaborated_issues_list = document.getElementById("person-issues-collaborated");

    data.characters.forEach(character => {
        const li = document.createElement("li");
        const a = document.createElement("a");

        a.textContent = character.name;
        a.href = `/front-end/pages/characters/details.html?id=${character.id}`;

        li.appendChild(a);
        created_characters_list.appendChild(li);
    });

    data.credits.forEach(credit => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.textContent = `${credit.issue.name}  #${credit.issue.number} - ${credit.person_role}`;
        a.href = `/front-end/pages/issues/details.html?id=${credit.issue.id}`
        li.appendChild(a);
        collaborated_issues_list.appendChild(li);
    });
}