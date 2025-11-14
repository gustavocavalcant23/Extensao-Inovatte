

let seconds = 30;
const countdownElement = document.getElementById('countdown');
let countdownTimer;

function startCountdown() {
    countdownTimer = setInterval(() => {
        seconds--;
        countdownElement.textContent = seconds;
        
        if (seconds <= 0) {
            clearInterval(countdownTimer);
            window.location.href = "/";
        }
    }, 1000);
}

startCountdown();

// Botão de voltar
document.querySelector('.btn').addEventListener('click', function(e) {
    e.preventDefault();
    clearInterval(countdownTimer);
    window.location.href = "/";
});