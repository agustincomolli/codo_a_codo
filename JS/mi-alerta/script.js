function closeTopAlert() {
    const topAlert = document.querySelector(".top-alert");
    topAlert.style.display = "none";
}


function showTopAlert() {
    const topAlert = document.querySelector(".top-alert");
    const closeAlert = document.querySelector("#close-top-alert");
    closeAlert.setAttribute("onclick", "closeTopAlert()");
    topAlert.style.display = "block";
}


function showMiddleAlert() {
    const alert = document.querySelector(".middle-alert");
    const btnOk = document.querySelector(".btn-alert-ok");
    const closeAlert = document.querySelector("#close-middle-alert");
    closeAlert.setAttribute("onclick", "closeMiddleAlert()");
    btnOk.setAttribute("onclick", "closeMiddleAlert()");
    alert.classList.toggle('hidden');
    alert.classList.toggle('overlay');
}

function closeMiddleAlert() {
    const alert = document.querySelector(".middle-alert");
    alert.classList.toggle('hidden');
    alert.classList.toggle('overlay');
}



function showAlerts() {
    // showTopAlert();
    showMiddleAlert();
};

const showAlertsButton = document.querySelector(".show-alerts");
showAlertsButton.addEventListener("click", () => { showAlerts() });