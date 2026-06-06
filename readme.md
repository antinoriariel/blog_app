# Blog estatica en Markdown

Repositorio base para un blog estatica que transforma archivos `.md` con una estructura definida en entradas HTML listas para publicar. El generador se ejecuta en Python en local y el resultado es un sitio estatica que puede desplegarse en hosting simple.

## Que pretende resolver
- Convertir contenido Markdown en paginas de blog con una estructura uniforme.
- Mantener una experiencia de escritura simple para crear nuevas entradas.
- Separar contenido, plantillas, estilos y salida generada.
- Ofrecer un diseno visual cuidado con Bootstrap, animate.css, Font Awesome y Google Fonts.

## Stack previsto
- Python para el algoritmo de conversion y build.
- Markdown como formato de entrada.
- Bootstrap para la base de layout y componentes.
- animate.css para animaciones de entrada y microinteracciones puntuales.
- Font Awesome para iconos.
- Google Fonts para tipografia expresiva.

## Documentacion principal
- [Plan del proyecto](plan.md)
- [Guia de uso](usage.md)
- [Especificacion del proyecto](docs/especificacion.md)
- [Formato de entradas](docs/formato-de-entradas.md)
- [Arquitectura](docs/arquitectura.md)
- [Diseno visual](docs/diseno-ui.md)
- [Despliegue](docs/despliegue.md)
- [Estructura del proyecto](docs/estructura-del-proyecto.md)

## Estructura propuesta
- `content/` para las entradas Markdown y paginas estaticas.
- `templates/` para las plantillas HTML.
- `assets/` para CSS, JS, imagenes e iconos.
- `scripts/` para el generador Python.
- `dist/` para la salida compilada.

## Estado actual
La documentacion base esta definida. La implementacion del generador y de la UI queda lista para seguir sobre estas especificaciones.
