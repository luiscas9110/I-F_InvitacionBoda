PROYECTO INVITACIÓN DE BODA — IVONNE & FERNANDO

Incluye un carrusel elegante en la sección “Nuestros momentos”.

Fotos esperadas: foto1.jpg, foto2.jpg, foto3.jpg, foto4.jpg y foto5.jpg.
Colócalas junto a index.html, tal como aparecen en las rutas del HTML.

Estructura:
- index.html
- css/styles.css
- assets/ (si deseas guardar aquí tus archivos)

El carrusel tiene flechas, indicadores, reproducción automática y gesto de deslizamiento en celular.


AJUSTE DEL CARRUSEL:
El carrusel fue reducido de tamaño y las fotografías usan object-fit: contain para conservar su proporción original sin deformarlas ni recortarlas.


RSVP INTEGRADO CON GOOGLE FORMS:
El botón "Confirmar asistencia" abre el formulario de Google dentro de una ventana elegante, sin sacar al invitado de la invitación.
Formulario conectado: https://docs.google.com/forms/d/e/1FAIpQLSefK2MG07ljBWun1-mynbA1ylw7TNyUhMmGxyBxnBST-Z_G3w/viewform?usp=dialog
Las respuestas se registran directamente en tu Google Forms y podrás verlas en la pestaña "Respuestas" de Google Forms.


RSVP PERSONALIZADO:
Formulario visual integrado en la invitación, conectado al Google Apps Script:
https://script.google.com/macros/s/AKfycbxUhlXa7QkP_sPs433wRij0gCjvjt954oIujjFpgTJhFpDyO3PwEPistR9xvBXA-seJ/exec

Campos:
- Nombre completo
- Número de cédula (solo números)
- Número de acompañantes
- ¿Nos acompañarás?
- Restricciones o preferencias alimentarias
- Mensaje para los novios

Después de enviar, la invitación muestra un mensaje diferente según la respuesta Sí/No.
Las respuestas se envían al Google Sheet configurado en Apps Script.


CORRECCIÓN RSVP: Eliminada la duplicación de JavaScript que impedía que el botón respondiera. El botón 'Confirmar asistencia' ahora utiliza una sola instancia del código RSVP.


CORRECCIÓN FINAL: Se corrigió un error de sintaxis JavaScript que detenía todo el script, incluyendo el contador y el botón RSVP. También se hizo que el botón de confirmación del encabezado abra el mismo formulario RSVP.


CORRECCIÓN DEL ENVÍO: Se agregó la declaración de 'esNo' dentro del envío RSVP. Ese error impedía que el formulario procesara el clic en 'Enviar confirmación'.

PORTADA DE APERTURA:
La invitación comienza con una portada a pantalla completa con las iniciales I & F, los nombres, la fecha, Girardota y un botón "Abrir invitación".
Al pulsar el botón, la portada desaparece, la página vuelve al inicio y se intenta iniciar la música aprovechando la interacción del usuario.
Cada vez que se abre la página desde cero se muestra nuevamente la portada.
