# Sistema visual

## Dirección de diseño
El blog debe sentirse editorial, moderno y limpio. La composición debe priorizar una jerarquía clara, mucho aire, tarjetas bien definidas y una navegación intuitiva.

## Stack visual
- **Bootstrap** para layout, rejillas, espaciado y componentes.
- **animate.css** para transiciones de entrada en carga de página.
- **AOS (Animate On Scroll)** para animaciones de entrada y salida basadas en scroll en posts.
- **Font Awesome** para iconos funcionales y decorativos.
- **Google Fonts** para tipografía principal y secundaria.

## Tipografía
- Elegir una fuente con personalidad para títulos.
- Usar una fuente muy legible para el cuerpo.
- Mantener contraste claro entre encabezados, subtítulos y texto.
- Evitar exceso de variantes tipográficas.

## Color y composición
- Base neutra con un color de acento bien definido.
- Fondo con profundidad visual sin perder legibilidad.
- Tarjetas, separadores y botones con bordes y sombras moderadas.
- Estados hover visibles pero discretos.

## Componentes visuales
- Portada con hero principal y llamada a la acción.
- Tarjetas para listado de entradas.
- Encabezado de post con fecha, tags y autor.
- Navegación simple con iconos cuando aporten claridad.
- Footer con enlaces útiles y metadatos del sitio.

## Animaciones

El sistema usa **animate.css** junto con `IntersectionObserver` para dos tipos de animaciones de scroll, sin bloquear el render ni depender de librerías adicionales.

### Entrada progresiva (scroll hacia abajo)

Las tarjetas de post (`.post-card`), los grupos de archivo (`.archive-month`) y los ítems del índice de etiquetas (`.tag-index-item`) aparecen con `fadeInUp` cuando entran al viewport por primera vez. Una vez animados, el observer deja de observarlos (`unobserve`).

### Salida con desvanecimiento (scroll en posts largos)

En las páginas de entrada individual se usa **AOS** (`mirror: true`, `once: false`) para animar los elementos de bloque del cuerpo del post (`p`, `h2`–`h6`, `blockquote`, `pre`, `ul`, `ol`, `figure`, `table`, `div`, `hr`).

El JS asigna `data-aos="fade-left"` a cada uno de esos elementos antes de que AOS se inicialice. Con esa configuración:

- **Al entrar al viewport**: el elemento aparece con un deslizamiento desde la izquierda (fade-left).
- **Al salir del viewport** (arriba o abajo): AOS invierte la animación, produciendo un desvanecimiento hacia la izquierda.
- El umbral superior se alinea con la altura del navbar vía el parámetro `offset` de `AOS.init()`.

El `overflow-x: hidden` en `body` previene la barra de scroll horizontal durante el deslizamiento lateral.

## Accesibilidad
- Contraste suficiente entre texto y fondo.
- Estados de foco visibles.
- Navegación legible en teclado.
- Jerarquía semántica correcta en títulos y regiones.
