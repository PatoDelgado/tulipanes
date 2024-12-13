// Función para mostrar el poema al hacer clic en una imagen
function showPoem(element) {
    // Si la imagen ya tiene la clase "show", la eliminamos
    if (element.classList.contains('show')) {
        element.classList.remove('show');
    } else {
        // Si no tiene la clase, la agregamos
        element.classList.add('show');
    }
}
