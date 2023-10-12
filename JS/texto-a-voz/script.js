function speakMessage(textToSpeak) {
    const message = new SpeechSynthesisUtterance(textToSpeak);
    speechSynthesis.speak(message);
};


const readme = document.querySelector(".readme");
readme.addEventListener("click", () => {
    const text = document.querySelector("#to-read");
    speakMessage(text.value);
});