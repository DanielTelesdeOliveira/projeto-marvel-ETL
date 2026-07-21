window.addEventListener("DOMContentLoaded", async () => {
    await getIssuesList();
});

async function getIssuesList(){
    const response = await fetch("http://127.0.0.1:8000/issue/show");

    if(!response.ok){
        throw new Error("Error while fetching issue");
    }

    const data = await response.json();
    const list = document.getElementById("issues-list");
    
    data.forEach(issue => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        
        a.textContent = `${issue.id} - ${issue.name}`;
        a.href=`/front-end/pages/issues/details.html?id=${issue.id}`;

        li.appendChild(a);
        list.appendChild(li);
    });
}