function onClickHandler() {
    console.log("TODO");
}

function addHoverEffect() {
    document.getElementById("404").classList.add("gradient-text-hover-404");
}

function removeHoverEffect(event) {
    document.getElementById("404").classList.remove("gradient-text-hover-404");
}

document.getElementById("404").addEventListener("click", onClickHandler)
document.getElementById("404").addEventListener("mouseover", addHoverEffect)
document.getElementById("404").addEventListener("mouseout", removeHoverEffect)

document.addEventListener('DOMContentLoaded', function() {
    const luigi = document.querySelector('.luigi');
    const frames = [
        '/assets/images/404/Luigi-1.png',
        '/assets/images/404/Luigi-2.png',
        '/assets/images/404/Luigi-3.png',
        '/assets/images/404/Luigi-2.png',
    ];
    let currentFrame = 0;

    // Frame update interval
    setInterval(function() {
        currentFrame = (currentFrame + 1) % frames.length;
        luigi.style.backgroundImage = 'url(' + frames[currentFrame] + ')';
    }, 200); // Change frame every 200ms
});