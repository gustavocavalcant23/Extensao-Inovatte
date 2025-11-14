

let seconds = 10;
const countdownElement = document.getElementById('countdown');
        
const countdown = setInterval(() => {
    seconds--;
    countdownElement.textContent = seconds;
            
    if (seconds <= 0) {
        clearInterval(countdown);
        window.location.href = "/";
    }
}, 1000);
        
