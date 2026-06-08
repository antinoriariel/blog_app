# Formato de entradas

Este documento define el formato canonico de los archivos Markdown que alimentan el blog.

## Estructura obligatoria
Cada archivo debe tener:
- Un bloque inicial de frontmatter en YAML, entre lineas `---`.
- El cuerpo del articulo escrito en Markdown.

## Esquema del frontmatter
```yaml
---
title: "Titulo de la entrada"
slug: "titulo-de-la-entrada"
date: "2026-06-05"
summary: "Resumen corto para listado y SEO."
tags:
  - blog
  - python
category: "proyecto"
author: "Nombre del autor"
cover: "assets/posts/slug/cover.jpg"
featured: false
published: true
---
```

## Reglas por campo
- `title`: obligatorio, texto corto y claro.
- `slug`: obligatorio, en minusculas, con guiones, sin espacios.
- `date`: obligatorio, formato ISO `YYYY-MM-DD`.
- `summary`: obligatorio, idealmente entre 120 y 160 caracteres.
- `tags`: opcional, lista corta de temas.
- `category`: opcional, una sola categoria principal.
- `author`: opcional, nombre visible del autor.
- `cover`: opcional, ruta relativa a una imagen existente.
- `featured`: opcional, controla el destacado en portada.
- `published`: opcional, por defecto `true`.

## Reglas de validacion
- El frontmatter debe ser valido y parseable.
- No se permiten slugs vacios o duplicados.
- No se deben aceptar fechas fuera de formato.
- Si `published` es `false`, la entrada no debe salir en la web publica.
- Si se define `cover`, la ruta debe existir durante el build.

## Reglas del cuerpo
- El contenido se escribe en Markdown comun.
- Los encabezados siguen una jerarquia coherente.
- El primer `h1` puede ser generado por la plantilla; si ocurre, el cuerpo no necesita repetirlo.
- Los fragmentos de codigo deben ir en fences y, si aplica, indicar el lenguaje.
- Las tablas, listas y citas deben renderizarse sin estilos inline.

## Campos exclusivos de páginas estáticas

Las páginas en `content/pages/` aceptan un campo adicional no disponible en entradas de blog:

| Campo  | Tipo  | Descripción                                                                                       |
|--------|-------|---------------------------------------------------------------------------------------------------|
| `icon` | texto | Clases CSS del `<i>` de Font Awesome que aparece junto al título en el navbar. Ej: `fa-solid fa-user me-1`. Si se omite, el menú móvil usa `fa-solid fa-file-lines`; el menú de escritorio no muestra ícono. |

Ejemplo de frontmatter de página con ícono:

```yaml
---
title: "Sobre"
slug: "sobre"
icon: "fa-solid fa-user me-1"
summary: "Quién escribe este blog."
published: true
---
```

## Matemáticas con LaTeX

El generador detecta expresiones LaTeX automáticamente y las renderiza con **KaTeX** en el navegador. No se necesita ningún campo especial en el frontmatter.

### Sintaxis

| Tipo | Delimitadores | Resultado |
|------|--------------|-----------|
| Inline | `$...$` | Fórmula dentro del párrafo |
| Display | `$$...$$` | Fórmula centrada en su propio bloque |

### Ejemplos

Inline: escribí `$f(x) = x^2$` y se renderiza como fórmula dentro del texto.

Display (en su propio párrafo, con líneas en blanco antes y después):

```
$$
\lim_{x \to 0} \frac{\sin x}{x} = 1
$$
```

### Cómo funciona

Antes de procesar el Markdown, el generador extrae todos los bloques `$...$` y `$$...$$` y los reemplaza por marcadores opacos. Esto evita que el parser de Markdown corrompa caracteres como `_`, `*`, `<` o `>` dentro de las expresiones. Una vez generado el HTML, los marcadores se reemplazan por elementos `<span class="math-inline">` y `<div class="math-display">` con los delimitadores `\(...\)` y `\[...\]` que KaTeX auto-render interpreta en el navegador.

KaTeX se carga únicamente en las páginas que contienen al menos una expresión matemática (detección automática en tiempo de build).

### Consideraciones

- El `$` que representa dinero puede disparar el parser si hay otro `$` en la misma línea. Escapalo con `\$` para prevenirlo.
- Las expresiones inline no pueden contener saltos de línea.
- KaTeX requiere conexión a la CDN de jsDelivr en la primera visita; las visitas siguientes usan la caché del navegador.

## Extensiones recomendadas
- Tablas Markdown.
- Listas de tareas.
- Bloques de codigo con resaltado.
- Expresiones matemáticas con LaTeX (`$...$` y `$$...$$`).
- Enlaces e imagenes relativas.

## Ejemplo de archivo valido
```md
---
title: "Publicar una entrada"
slug: "publicar-una-entrada"
date: "2026-06-05"
summary: "Paso a paso para crear una entrada de blog desde Markdown."
tags:
  - guia
  - contenido
published: true
---

## Introduccion

Aqui empieza el contenido de la entrada.
```
