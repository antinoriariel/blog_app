# Plan del proyecto

## Objetivo

Blog estático que convierte archivos `.md` con frontmatter YAML en páginas HTML completas usando un generador Python + plantillas Jinja2. La salida es una carpeta `dist/` servible en cualquier hosting estático.

## Estado actual

**Estable.** Todos los bloqueantes y correcciones de robustez están resueltos. El sitio compila, navega y cumple los criterios de cierre.

## Decisiones tomadas

- Resaltado de código: **highlight.js** (auto-detección de lenguaje, tema atom-one-dark).
- Sitio en **`/`** (`base_url: "/"`).
- Categorías: **solo metadato**, sin páginas navegables por categoría.
- RSS/Atom: **backlog**, no entra en este ciclo.

## Criterios de cierre — verificados

- [x] Build exitoso.
- [x] Ningún enlace interno hardcodeado a `/` (sobre.md usa ruta relativa).
- [x] Un solo sistema de resaltado de código documentado y cargado (highlight.js).
- [x] Sitemap alineado con las rutas reales (portada, posts, páginas, archivo, etiquetas).
- [x] Parser y slugs resistentes a casos límite (regex, BOM, CRLF, no-ASCII).

## Fases completadas

### Fase 1: definición editorial
- Formato canónico de entradas definido en `docs/formato-de-entradas.md`.
- Campos de frontmatter requeridos y opcionales documentados en `usage.md`.
- Estructura de carpetas implementada.

### Fase 2: generación base
- Scanner de archivos Markdown (`scripts/utils.py → scan_posts`).
- Parser de frontmatter YAML robusto con regex, manejo de BOM y CRLF (`scripts/utils.py → parse_entry`).
- Validador de esquema con mensajes de error claros (`scripts/utils.py → validate_frontmatter`).
- Conversión de Markdown a HTML con extensiones (`python-markdown`).
- Renderizado por entrada usando Jinja2.
- `slugify` con normalización NFKD: convierte á→a, ñ→n, etc. antes de generar la URL.

### Fase 3: experiencia del sitio
- Portada con hero, entrada destacada y listado de tarjetas (la destacada se excluye de "Últimas entradas").
- Páginas individuales de entrada con prev/next y sidebar.
- Páginas de archivo cronológico por mes.
- Páginas de etiqueta e índice de etiquetas.
- Páginas estáticas (sobre, contacto).
- Navbar con links activos (`.nav-link.active`) y efecto scroll (`.navbar-scrolled`).
- Integración de Bootstrap 5, Font Awesome, Google Fonts (Fraunces + DM Sans), animate.css y highlight.js.
- CSS editorial completo con variables CSS y diseño responsive.
- Footer con enlaces sociales (GitHub, YouTube, X) configurables en `config.yaml`.
- Templates divididos en partials: `partials/navbar.html` y `partials/footer.html`.

### Fase 4: calidad y publicación
- Build reproducible desde cero con `python scripts/build.py` (limpia y reconstruye todo).
- Sitemap completo: portada, posts, páginas, `/archivo/`, `/etiquetas/` y cada tag.
- Documentación técnica completa en `docs/`.
- Plantilla para nuevas entradas en `templates/new-post.md`.
- JS hardening: `initSmoothScroll` ignora anclas vacías y maneja selectores inválidos.

## Próximos pasos opcionales

- RSS/Atom feed.
- Búsqueda estática en cliente (lunr.js o similar).
- Soporte de imágenes optimizadas (resize automático en build).
- Paginación en la portada si el número de entradas crece.
- Navegación por categoría si se decide exponer categorías como páginas.
- CI/CD con GitHub Actions para build y deploy automático.

## Criterios de aceptación — verificados

- [x] Un archivo Markdown válido genera una entrada HTML sin pasos manuales.
- [x] El sitio se puede abrir y navegar localmente.
- [x] El diseño es consistente en desktop y mobile.
- [x] El build falla con mensaje claro cuando falta un dato obligatorio.
- [x] Las páginas estáticas (sobre, contacto) se generan y aparecen en el navbar.
- [x] El archivo cronológico y las páginas de etiqueta funcionan.
- [x] Se genera `sitemap.xml`, `robots.txt` y `404.html`.
- [x] El sitemap incluye todas las rutas públicas activas.
- [x] No hay enlaces internos hardcodeados a rutas absolutas en el contenido.
- [x] Los slugs con caracteres no ASCII se normalizan correctamente.
