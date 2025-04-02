let text = document.getElementById("textInput"), count = document.getElementById("charCount");
text.addEventListener("input", () => {
    let len = text.value.length;
    count.textContent = `${len} / 150`;
    count.classList.toggle("red", len > 150);
});
