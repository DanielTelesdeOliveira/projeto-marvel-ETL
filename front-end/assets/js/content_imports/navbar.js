async function loadNavBar(){
    if(!document.querySelector(`link[href="/front-end/assets/css/navbar.css"]`)){
        link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = "/front-end/assets/css/navbar.css";
        document.head.appendChild(link);
    }

    const response = await fetch('/front-end/components/navbar.html');
    const html = await response.text();

    document.getElementById("navbar").innerHTML = html;
}

document.addEventListener("DOMContentLoaded", () => {
    loadNavBar().catch(error => console.log(error));
});

