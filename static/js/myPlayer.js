var myPlayer = videojs('my-video', {
    muted: true,
    autoplay: true,
    controls: true,
    preload: true,
    width="640",
    height="264",
    playbackRates: [0.25,0.5,0.75,1.0,1.5,2.0,2.5,3],
});

//myPlayer.currentTime(parseFloat("{{available_video.video_timestamp}}"));

//myPlayer.rotate(myPlayer);
//myPlayer.zoom(myPlayer);