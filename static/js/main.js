document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll(".glass-panel");

    cards.forEach((card) => {
        card.addEventListener("mouseenter", () => {
            card.style.transition = "0.3s";
        });
    });
});