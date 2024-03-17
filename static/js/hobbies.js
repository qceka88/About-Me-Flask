function setVideoSize() {
    const vidWidth = 1920;
    const vidHeight = 1080;
    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;
    const tempVidWidth = windowHeight * vidWidth / vidHeight;
    const tempVidHeight = windowWidth * vidHeight / vidWidth;
    const newVidWidth = tempVidWidth > windowWidth ? tempVidWidth : windowWidth;
    const newVidHeight = tempVidHeight > windowHeight ? tempVidHeight : windowHeight;
    const tmVideo = $('video-background');

    tmVideo.css('width', newVidWidth);
    tmVideo.css('height', newVidHeight);

}

$(document).ready(function () {

    setVideoSize();

    // Set video background size based on window size
    let timeout;
    window.onresize = function () {
        clearTimeout(timeout);
        timeout = setTimeout(setVideoSize, 100);
    };

    // Play/Pause button for video background
    const btn = $(".video-button");
    const btnSymbol = $(".video-button-symbol")
    btn.on("click", function (e) {
        const video = document.getElementById("video-background");
        const sound = document.getElementById("sound-wrapper");
        btnSymbol.removeClass();

        if (video.paused) {
            video.play();
            sound.play();
            btnSymbol.addClass("fas fa-pause");
        } else {
            video.pause();
            sound.pause();
            btnSymbol.addClass("fas fa-play");
        }
    });
});