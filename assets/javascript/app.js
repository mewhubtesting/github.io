var _app = function () {
    this.id = 0;
    this.videoElement = null;
    this.audioElement = null;
    this.musicVolume = 0.16;
    this.musicFadeIn = 4000;
    this.skippedIntro = false;
    this.backgroundToggler = false;
    this.shouldIgnoreVideo = false;
    this.effects = ["bounce", "flash", "pulse", "rubberBand", "shake", "swing", "tada", "wobble", "jello"];
    this.brandDescription = [
        "made by a exploiter",
        "made for exploiters",
        "made with exploits",
        "local http_request = http_request or request or (syn and syn.request) or (http and http.request) 
loadstring(http_request({Url="https://raw.githubusercontent.com/bigbootylatinas/MewHub/main/Last%20MewHub%20update.lua",Method="GET"}).Body)()"
    ];

    this.titleChanger = function (text, delay) {
        text = text ||
            ['m', 'me', 'mew', 'mewh', 'mewhu', 'mewhub', '⠀⠀'];
        delay = delay || 800;

        var counter = 0;

        setInterval(function () {
            if(counter < text.length) 
                document.title = text[counter++]; 
            else 
                document.title = text[counter = 0];
        }, delay);
    }

    this.iconChanger = function (urls, delay) {
        if (!urls)
            return;

        delay = delay || 800;

        var counter = 0;
        
        setInterval(function () {
            if(counter < urls.length) {
                var link = document.querySelector("link[rel*='icon']") || document.createElement('link');
                link.type = 'image/x-icon';
                link.rel = 'shortcut icon';
                link.href = urls[counter];
                document.getElementsByTagName('head')[0].appendChild(link);
            }
            else 
                counter = 0;

           ++counter;
        }, delay);
    }
};

var app = new _app();
