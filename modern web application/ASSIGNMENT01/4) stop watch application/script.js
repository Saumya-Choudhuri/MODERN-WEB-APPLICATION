let sec = 0, min = 0, timer;

function updateTime() {
    sec = (sec + 1) % 60;
    if (sec === 0) min++;
    document.getElementById("time").textContent = 
        String(min).padStart(2, "0") + ":" + String(sec).padStart(2, "0");
}

document.getElementById("start").onclick = () => { 
    if (!timer) timer = setInterval(updateTime, 1000);
};

document.getElementById("stop").onclick = () => clearInterval(timer), timer = null;

document.getElementById("reset").onclick = () => { 
    clearInterval(timer);
    timer = sec = min = 0;
    document.getElementById("time").textContent = "00:00";
};
