window.addEventListener("DOMContentLoaded", async () => {
    await getPersonList();
});

async function getPersonList() {
    const response = await fetch(`http://127.0.0.1:8000/person/show`);
    const data = await response.json();

    const list = document.getElementById("person_list");

    data.forEach(person => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        a.href = `/front-end/pages/person/details.html?id=${person.id}`;
        a.textContent = `${person.id} - ${person.name}`;
        li.appendChild(a);
        list.appendChild(li);
    });
}