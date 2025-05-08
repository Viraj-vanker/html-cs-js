document.getElementById('downloadBtn').addEventListener('click', function() {
    let progress = document.getElementById('progress');
    let width = 0;

    progress.style.width = '0%';

    let interval = setInterval(function() {
        if (width >= 100) {
            clearInterval(interval);
        } else {
            width++;
            progress.style.width = width + '%';
        }
    }, 50);
});