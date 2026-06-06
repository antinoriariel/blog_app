# Plan del proyecto

## Objetivo

Blog estático que convierte archivos `.md` con frontmatter YAML en páginas HTML completas usando un generador Python + plantillas Jinja2. La salida es una carpeta `dist/` servible en cualquier hosting estático.

## Estado actual

**Implementación completa.** Todas las fases están terminadas.

## Fases completadas

### Fase 1: definición editorial
- Formato canónico de entradas definido en `docs/formato-de-entradas.md`.
- Campos de frontmatter requeridos y opcionales documentados en `usage.md`.
- Estructura de carpetas implementada.

### Fase 2: generación base
- Scanner de archivos Markdown (`scripts/utils.py → scan_posts`).
- Parser de frontmatter YAML (`scripts/utils.py → parse_entry`).
- Validador de esquema con mensajes de error claros (`scripts/utils.py → validate_frontmatter`).
- Conversión de Markdown a HTML con extensiones (`python-markdown`).
- Renderizado por entrada usando Jinja2.

### Fase 3: experiencia del sitio
- Portada con hero, entrada destacada y listado de tarjetas.
- Páginas individuales de entrada con prev/next y sidebar.
- Páginas de archivo cronológico por mes.
- Páginas de etiqueta e índice de etiquetas.
- Páginas estáticas (sobre, contacto).
- Integración de Bootstrap 5, Font Awesome, Google Fonts, animate.css, Prism.js.
- CSS editorial completo con variables CSS y diseño responsive.

### Fase 4: calidad y publicación
- Build reproducible desde cero con `python scripts/build.py`.
- Salida validada: 2 entradas, 2 páginas, 13 archivos HTML, sitemap.xml, robots.txt, 404.html.
- Documentación técnica completa en `docs/`.
- Plantilla para nuevas entradas en `templates/new-post.md`.

## Próximos pasos opcionales

- RSS/Atom feed.
- Búsqueda estática en cliente (lunr.js o similar).
- Soporte de imágenes optimizadas (resize automático en build).
- Paginación en la portada si el número de entradas crece.
- CI/CD con GitHub Actions para build y deploy automático.

## Criterios de aceptación — verificados

- [x] Un archivo Markdown válido genera una entrada HTML sin pasos manuales.
- [x] El sitio se puede abrir y navegar localmente.
- [x] El diseño es consistente en desktop y mobile.
- [x] El build falla con mensaje claro cuando falta un dato obligatorio.
- [x] Las páginas estáticas (sobre, contacto) se generan y aparecen en el navbar.
- [x] El archivo cronológico y las páginas de etiqueta funcionan.
- [x] Se genera `sitemap.xml`, `robots.txt` y `404.html`.
