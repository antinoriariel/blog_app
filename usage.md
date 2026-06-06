# Guía de uso

Referencia completa para escribir entradas, ejecutar el generador y mantener el sitio.

## Flujo de trabajo habitual

```bash
# Crear una entrada nueva
cp templates/new-post.md content/posts/2026-06-10-mi-entrada.md

# Editar el archivo y escribir el contenido
# ...

# Compilar
python scripts/build.py

# Revisar localmente
cd dist && python -m http.server 8000
```

## Frontmatter — referencia completa

Cada archivo `.md` debe comenzar con un bloque YAML entre `---`:

```yaml
---
title: "Título visible de la entrada"
slug: "titulo-visible-de-la-entrada"
date: "2026-06-10"
summary: "Resumen breve. Aparece en tarjetas, listados y como meta description."
tags:
  - python
  - tutorial
category: "técnico"
author: "Nombre del Autor"
cover: "assets/img/posts/mi-slug/cover.jpg"
featured: false
published: true
---
```

### Campos

| Campo       | Tipo      | Obligatorio | Descripción                                                  |
|-------------|-----------|-------------|--------------------------------------------------------------|
| `title`     | texto     | **sí**      | Título de la entrada. Aparece como `<h1>` y en `<title>`.    |
| `slug`      | texto     | **sí**      | URL amigable. Solo minúsculas, números y guiones.            |
| `date`      | ISO 8601  | **sí**      | Fecha de publicación: `YYYY-MM-DD`.                          |
| `summary`   | texto     | **sí**      | Resumen de 1-2 oraciones para tarjetas y SEO.                |
| `tags`      | lista     | no          | Etiquetas temáticas. Generan páginas `/etiquetas/<tag>/`.    |
| `category`  | texto     | no          | Categoría principal visible en la tarjeta.                   |
| `author`    | texto     | no          | Nombre del autor. Visible en la cabecera del post.           |
| `cover`     | ruta      | no          | Imagen de portada. Ruta relativa a la raíz del proyecto.     |
| `featured`  | booleano  | no          | `true` para destacar la entrada en la portada.               |
| `published` | booleano  | no          | `false` para excluir del build. Por defecto `true`.          |

## Convenciones de nombre de archivo

```
YYYY-MM-DD-slug.md
```

Ejemplo: `2026-06-10-como-usar-jinja2.md`

- El slug del nombre de archivo y el `slug` del frontmatter deben coincidir.
- No uses espacios ni caracteres especiales en el nombre.
- Los borradores pueden nombrarse `_draft-titulo.md` (el guión bajo los excluye del glob por convención, pero es más seguro usar `published: false`).

## Cuerpo del artículo

El cuerpo puede usar Markdown completo. Extensiones habilitadas:

- **Tablas** — sintaxis GFM estándar.
- **Bloques de código** — con triple backtick y nombre de lenguaje:
  ````
  ```python
  print("hola")
  ```
  ````
- **Tabla de contenidos** — insertar `[TOC]` donde querés que aparezca.
- **Notas al pie** — `Texto[^1]` y `[^1]: Nota.` al final.
- **Saltos de línea** — una línea en blanco es un párrafo nuevo.

## Imágenes

Guardar las imágenes en `assets/img/posts/<slug>/` y referenciarlas así:

```markdown
![Descripción](../../assets/img/posts/mi-slug/imagen.jpg)
```

En el frontmatter, la ruta de `cover` es relativa a la raíz:

```yaml
cover: "assets/img/posts/mi-slug/cover.jpg"
```

## Páginas estáticas

Las páginas (sobre, contacto, etc.) van en `content/pages/`. Tienen el mismo formato de frontmatter. No aparecen en listados de entradas pero sí en el navbar.

Ejemplo mínimo:

```markdown
---
title: "Sobre"
slug: "sobre"
summary: "Quién escribe este blog."
published: true
---

Contenido de la página.
```

## Ejecutar el build

```bash
python scripts/build.py
```

Salida esperada:

```
Limpiando salida anterior en dist/ ...
✓ Build completado
  2 entrada(s) · 2 página(s)
  Salida: dist/
```

Si hay errores de validación, aparecen antes del resumen con `✗`.

## Lista de verificación antes de publicar

- [ ] Todos los campos obligatorios están completos.
- [ ] El slug es único y no tiene caracteres inválidos.
- [ ] La fecha está en formato `YYYY-MM-DD`.
- [ ] El resumen tiene entre 80 y 160 caracteres.
- [ ] Las rutas de imágenes existen en `assets/`.
- [ ] `published: true` está activo.
- [ ] El build local no reporta errores.
- [ ] El sitio se ve bien en desktop y mobile.
