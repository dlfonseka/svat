function zoom(player){
    var dimension = 0;

    var zoomInButton = createButton('&#8853;');
    var zoomOutButton = createButton('&#8854;');

    zoomInButton.onclick = function(){
        dimension += 1;
        if (dimension == 7){
            dimension = 6;
        };
        player.zoomrotate( {zoom: dimension} );
    };

    zoomOutButton.onclick = function(){
        dimension -= 1;
        if (dimension == 0){
            dimension = 1;
        };
        player.zoomrotate( {zoom: dimension} );
    };

    var playbackRate = document.querySelector('.vjs-playback-rate');
    insertAfter(zoomInButton, playbackRate);
    insertAfter(zoomOutButton, zoomInButton);

    function createButton(icon){
        var button = document.createElement('button');
        button.classList.add('vjs-menu-button');
        button.innerHTML = icon;
        button.style.fontSize = '1.8em';
        return button;
    };
   
    function insertAfter(newEl, element){
        element.parentNode.insertBefore(newEl,element.nextSibling);
    };
};

videojs.registerPlugin('zoom', zoom);