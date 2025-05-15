document.addEventListener('DOMContentLoaded', () => {
  const opciones = document.querySelectorAll('.opcion');
  const anuncio = document.getElementById('anuncio');

  opciones.forEach(opcion => {
    opcion.addEventListener('mouseenter', () => {
      // Muestra el anuncio cuando el ratón entra sobre una opción
      anuncio.textContent = `¡Has seleccionado: ${opcion.textContent}!`; // Personaliza el mensaje
      anuncio.style.display = 'block'; // Muestra el anuncio
    });

    opcion.addEventListener('mouseleave', () => {
      // Oculta el anuncio cuando el ratón sale de la opción
      anuncio.style.display = 'none';
    });
  });
});
