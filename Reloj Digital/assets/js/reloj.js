// Asegurémonos de que el JS se ejecute cuando el DOM esté completamente cargado
window.onload = function() {
    function updateClock() {
        const clockElement = document.getElementById('clock');
        const now = new Date();

        let hours = now.getHours();
        let minutes = now.getMinutes();
        let seconds = now.getSeconds();

        // Formateamos la hora para que siempre tenga dos dígitos
        hours = (hours < 10) ? '0' + hours : hours;
        minutes = (minutes < 10) ? '0' + minutes : minutes;
        seconds = (seconds < 10) ? '0' + seconds : seconds;

        // Actualizamos el contenido del reloj
        clockElement.textContent = `${hours}:${minutes}:${seconds}`;
    }

    // Actualizamos el reloj cada segundo
    setInterval(updateClock, 1000);

    // Llamada inicial para mostrar el reloj sin esperar 1 segundo
    updateClock();
};
