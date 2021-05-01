function timestamp(){
    var myPlayer = videojs('my-video');
    document.getElementById('id_annotation_timestamp').value = myPlayer.currentTime();
}