document.addEventListener('DOMContentLoaded', function () {
    function checkBackgroundMode() {
        const backgroundMode = document.querySelector("#backgroundMode");
        if (backgroundMode.checked == false) {
            console.log('off')
            document.body.style.backgroundColor = "#24303d";
            let all = document.getElementsByTagName("*");
            for (let i = 0, max = all.length; i < max; i++) {
                all[i].style.color = "#f0f8ff";
            }
            let unchangedElements = document.querySelectorAll(".carousel-caption");
            for (let g = 0; g < unchangedElements.length; g++) {
                const elemet = unchangedElements[g];
                elemet.style.backgroundColor = "#24303d86"
            }
        } else {
            document.body.style.backgroundColor = "#f5f5f5";

            let all = document.getElementsByTagName("*");
            for (let i = 0, max = all.length; i < max; i++) {
                all[i].style.color = "black";
            }

            let unchangedElements = document.querySelectorAll(".carousel-caption");
            for (let g = 0; g < unchangedElements.length; g++) {
                const elemet = unchangedElements[g];
                elemet.style.backgroundColor = "#f5f5f588"
            }
        }
    }
    setInterval(checkBackgroundMode, 500);
});