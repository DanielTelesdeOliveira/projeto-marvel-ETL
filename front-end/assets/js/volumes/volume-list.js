document.addEventListener("DOMContentLoaded", async() => {
    await getVolumeList();
})

async function getVolumeList(){
    const response = await fetch("http://127.0.0.1:8000/volume/show");

    if(!response.ok){
        throw new Error("Error while fetching volume");
    }

    const data = await response.json();
    const list = document.getElementById("volume-list");
    
    data.forEach(volume => {
        const li = document.createElement("li");
        const a = document.createElement("a");
        
        a.textContent = `${volume.id} - ${volume.name}`;
        a.href=`/front-end/pages/volumes/details.html?id=${volume.id}`;

        li.appendChild(a);
        list.appendChild(li);
    });

}