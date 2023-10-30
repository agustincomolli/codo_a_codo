class CustomAlert {
    constructor(title = "¡Alerta!", message = "Escribe tu mensaje aquí") {
        this.title = title;
        this.message = message;
        this.createAlert();
        this.attachEvents();
    };

    createAlert() {
        this.alertDiv = document.createElement("div");
        this.alertDiv.id = "custom-alert";
        this.alertDiv.className = "custom-alert hidden-alert";
        this.alertContent = `
            <div class="alert-box">
                <span class="close-alert" id="close-alert">&times;</span>
                <h2 class="alert-title">${this.title}</h2>
                <p class="alert-message">${this.message}</p>
                <button class="alert-button-ok send-btn" id="alert-button-ok">Aceptar</button>
            </div>
        `;
        this.alertDiv.innerHTML = this.alertContent;
        document.body.appendChild(this.alertDiv);
    };


    attachEvents() {
        const closeAlert = document.querySelector("#close-alert");
        closeAlert.onclick = () => { this.closeAlert() };

        const btnOK = document.querySelector("#alert-button-ok");
        btnOK.onclick = () => { this.closeAlert() };
    };


    showAlert() {
        this.alertDiv.classList.toggle("hidden-alert");
        this.alertDiv.classList.toggle("overlay-alert");
    };


    closeAlert() {
        this.showAlert();
    };
};


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
    alert.classList.toggle('hidden-middle-alert');
    alert.classList.toggle('overlay-middle-alert');
}

function closeMiddleAlert() {
    const alert = document.querySelector(".middle-alert");
    alert.classList.toggle('hidden-middle-alert');
    alert.classList.toggle('overlay-middle-alert');
}



function showAlerts() {
    // showTopAlert();
    showMiddleAlert();
    // const myAlert = new CustomAlert();
    // myAlert.showAlert()
};

const showAlertsButton = document.querySelector(".show-alerts");
showAlertsButton.addEventListener("click", () => { showAlerts() });

