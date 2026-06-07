---
title: "Cómo funciona el generador estático"
slug: "como-funciona-el-generador-estatico"
date: "2026-06-05"
summary: "Recorrido por el código Python que convierte archivos Markdown en páginas HTML: scanner, parser de frontmatter, validador, renderizador y ensamblador."
tags:
  - python
  - markdown
  - tutorial
category: "técnico"
author: "Nombre del Autor"
published: true
---

## Visión general

El generador sigue un pipeline de cinco pasos que se ejecutan en orden cada vez que corrés `python scripts/build.py`:

1. **Scan** — encuentra todos los `.md` en `content/posts/` y `content/pages/`.
2. **Parse** — separa el frontmatter YAML del cuerpo Markdown.
3. **Validate** — comprueba que existan los campos obligatorios y que el slug sea válido.
4. **Render** — convierte el Markdown a HTML y lo inserta en las plantillas Jinja2.
5. **Assemble** — escribe los archivos de salida, genera índices y copia los assets.

## El scanner

```python
def scan_posts(directory):
    directory = Path(directory)
    if not directory.exists():
        return []
    return sorted(directory.glob("*.md"))
```

Simple: busca todos los archivos `.md` en el directorio dado. Ordenarlos garantiza que el build sea reproducible independientemente del sistema de archivos.

## El parser de frontmatter

Cada entrada tiene esta estructura:

```
---
title: "Título"
slug: "titulo"
date: "2026-06-05"
...
---

Cuerpo del artículo en Markdown.
```

El parser separa esas dos partes usando `split('---', 2)` y procesa el bloque YAML con `PyYAML`:

```python
parts = text.split("---", 2)
meta  = yaml.safe_load(parts[1])
body  = parts[2].strip()
```

## El validador

Los campos obligatorios son `title`, `slug`, `date` y `summary`. Si falta alguno, el build se detiene con un error descriptivo:

```
✗ Campo obligatorio 'summary' faltante o vacío en mi-entrada.md
```

El slug también se valida contra la expresión regular `^[a-z0-9]+(?:-[a-z0-9]+)*$` para asegurar URLs limpias.

## El renderizador

El cuerpo Markdown se convierte a HTML usando la librería `markdown` de Python con extensiones habilitadas:

| Extensión    | Qué agrega                             |
|-------------|----------------------------------------|
| `tables`    | Tablas tipo GFM                        |
| `fenced_code` | Bloques de código con triple backtick |
| `toc`       | Tabla de contenidos automática         |
| `footnotes` | Notas al pie                           |
| `nl2br`     | Saltos de línea como `<br>`            |

El HTML resultante se inserta en una plantilla Jinja2 con `{{ post.body_html | safe }}`. El resaltado de sintaxis lo maneja **highlight.js** en el cliente: detecta automáticamente el lenguaje si no se especifica en el bloque, y aplica el tema `atom-one-dark`.

## El ensamblador

Para cada entrada publicada se genera:

```
dist/posts/<slug>/index.html
```

Usar carpetas con `index.html` en lugar de archivos directos (`<slug>.html`) permite URLs limpias sin extensión:

```
https://mi-blog.com/posts/mi-entrada/   ✓
https://mi-blog.com/posts/mi-entrada.html   ✗
```

Además del contenido, el ensamblador genera:

- `dist/index.html` — portada
- `dist/etiquetas/<tag>/index.html` — páginas de etiqueta
- `dist/archivo/index.html` — archivo cronológico
- `dist/404.html` — página de error
- `dist/sitemap.xml` y `dist/robots.txt`

## Manejo de errores

Si una entrada tiene el frontmatter mal formado o le falta un campo obligatorio, el generador reporta el error pero sigue procesando el resto. Al final, si hubo errores, termina con código de salida 1:

```
✗ 2026-06-04-entrada-rota.md: Campo obligatorio 'date' faltante o vacío
✓ Build completado
  3 entrada(s) · 2 página(s)
⚠ 1 error(es) encontrado(s). Revisar arriba.
```

Esto permite ver el estado del sitio completo antes de corregir los archivos con problemas.
