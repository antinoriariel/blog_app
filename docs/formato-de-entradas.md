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

## Extensiones recomendadas
- Tablas Markdown.
- Listas de tareas.
- Bloques de codigo con resaltado.
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
