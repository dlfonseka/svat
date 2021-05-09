function timestamp(id){
    var myPlayer = videojs('my-video');
    document.getElementById(id).value = myPlayer.currentTime();
}

function tstamp(){
    var myPlayer = videojs('my-video')
    return myPlayer.currentTime()
}

function showhide(id) {
    var divid = document.getElementById(id);
    var showElement = true;
    if (divid.style.visibility === 'visible') {
        showElement = false;
    }
    divid.style.visibility = 'hidden';
    if (showElement) {
        divid.style.visibility = 'visible';
    }
    return false;
}

function pause(){
    var myPlayer = videojs('my-video');
    myPlayer.pause()
}

function play(){
    var myPlayer = videojs('my-video');
    myPlayer.play()
}

function playpause(){
    var myPlayer = videojs('my-video');
    if (myPlayer.paused()) {
      myPlayer.play();
    }
    else {
      myPlayer.pause();
    }
}