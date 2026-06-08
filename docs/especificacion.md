# Especificacion del proyecto

## Resumen
El proyecto consiste en un blog estatica generado a partir de archivos Markdown con un esquema fijo. El contenido se escribe en local, un proceso Python lo valida y lo convierte en paginas HTML, y el resultado se publica como sitio estatica.

## Objetivo funcional
- Convertir entradas `.md` en paginas HTML completas.
- Mantener una separacion clara entre contenido, plantillas, estilos y salida generada.
- Publicar un sitio navegable sin necesidad de servidor dinamico.

## Requisitos funcionales
1. El sistema debe detectar automaticamente los archivos Markdown dentro de la carpeta de contenido.
2. El sistema debe validar el frontmatter antes de renderizar.
3. El sistema debe generar una pagina individual para cada entrada publicada.
4. El sistema debe generar una portada con listado o tarjetas de articulos.
5. El sistema debe poder generar paginas de archivo, etiquetas o categorias.
6. El sistema debe copiar assets estaticos al directorio de salida.
7. El sistema debe generar metadatos basicos para SEO y redes sociales.
8. El sistema debe poder ejecutarse en local sin dependencias de infraestructura externa.

## Requisitos no funcionales
- El sitio debe ser responsive en desktop y mobile.
- El contenido debe ser accesible y tener contraste adecuado.
- La generacion debe ser predecible y reproducible.
- La estructura del proyecto debe ser facil de mantener.
- La salida debe poder desplegarse en hosting estatico comun.

## Modelo de contenido
### Tipos de contenido
- Entradas de blog.
- Paginas estaticas como sobre, contacto o archivo.
- Assets asociados como imagenes, fuentes y estilos.

### Metadatos base
- `title`
- `slug`
- `date`
- `summary`
- `tags`
- `category`
- `author`
- `cover`
- `published`
- `featured`

### Metadatos exclusivos de páginas estáticas
- `icon` — clases CSS de Font Awesome para el ícono que aparece junto al título en el navbar (p.ej. `fa-solid fa-user me-1`). Opcional; si se omite, el menú móvil usa `fa-solid fa-file-lines` y el menú de escritorio no muestra ícono.

## Salidas esperadas
- `index.html` como portada.
- Paginas individuales para cada entrada.
- Paginas de categoria o etiqueta, si se activan.
- `404.html` para hosting estatica.
- Carpeta de assets lista para servir.

## Criterios de aceptacion
- Una entrada valida compila sin intervencion manual.
- Una entrada invalida produce un error comprensible.
- La navegacion entre portada y articulos funciona sin enlaces rotos.
- El sitio conserva la identidad visual definida en la guia de diseno.

## Ambito futuro opcional
- RSS o Atom.
- Sitemap automatico.
- Busqueda estatia en cliente.
- Traducciones o multiidioma.
