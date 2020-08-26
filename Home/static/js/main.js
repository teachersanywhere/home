window.setTimeout(function(){
    var loader = document.getElementById('preLoader');
    var body = document.getElementById('postLoader');
    loader.style.display = 'none';
    body.style.display = 'block';
}, 2000);

function animateValue(id, start, end, duration) {
    // assumes integer values for start and end
    
    var obj = document.getElementById(id);
    var range = end - start;
    // no timer shorter than 50ms (not really visible any way)
    var minTimer = 50;
    // calc step time to show all interediate values
    var stepTime = Math.abs(Math.floor(duration / range));
    
    // never go below minTimer
    stepTime = Math.max(stepTime, minTimer);
    
    // get current time and calculate desired end time
    var startTime = new Date().getTime();
    var endTime = startTime + duration;
    var timer;
  
    function run() {
        var now = new Date().getTime();
        var remaining = Math.max((endTime - now) / duration, 0);
        var value = Math.round(end - (remaining * range));
        obj.innerHTML = value;
        if (value == end) {
            clearInterval(timer);
        }
    }
    
    timer = setInterval(run, stepTime);
    run();
}

window.onload = function () {
    animateValue('count1', 0, 50, 6000);
    animateValue('count2', 0, 1000, 6000);
    animateValue('count3', 0, 5000, 6000);
};