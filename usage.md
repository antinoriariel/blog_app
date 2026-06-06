# Guia de uso

Esta guia define como escribir entradas para el blog y como preparar el contenido para que el generador Python lo transforme en HTML.

## Flujo de trabajo
1. Crear un archivo Markdown nuevo dentro de la carpeta de contenido.
2. Escribir el frontmatter con los metadatos requeridos.
3. Redactar el cuerpo de la entrada en Markdown.
4. Ejecutar el generador local.
5. Revisar la salida estatica antes de publicar.

## Formato general de una entrada
Cada entrada debe tener dos partes:
- Un bloque de metadatos al inicio, rodeado por lineas `---`.
- El contenido del articulo en Markdown.

Ejemplo minimo:

```md
---
title: "Mi primera entrada"
slug: "mi-primera-entrada"
date: "2026-06-05"
summary: "Resumen breve de la publicacion."
tags:
  - blog
  - python
  - static
published: true
---

# Mi primera entrada

Texto del articulo.
```

## Campos recomendados
| Campo | Tipo | Requerido | Uso |
| --- | --- | --- | --- |
| `title` | texto | si | Titulo visible de la entrada y etiqueta principal de la pagina. |
| `slug` | texto | si | Nombre amigable para la URL. |
| `date` | fecha ISO | si | Orden cronologico y metadatos. |
| `summary` | texto | si | Resumen para tarjetas, SEO y listados. |
| `tags` | lista | no | Agrupacion tematica. |
| `category` | texto | no | Seccion principal de la entrada. |
| `author` | texto | no | Nombre del autor. |
| `cover` | ruta | no | Imagen principal de la entrada. |
| `published` | booleano | no | Control de publicacion. |
| `featured` | booleano | no | Marca para destacar la entrada en la portada. |

## Reglas de contenido
- El titulo principal de la pagina se toma desde `title`; evita duplicarlo como primer encabezado si el generador ya lo inserta.
- Usa un solo `h1` por entrada si el renderizador no lo crea automaticamente.
- Mantiene los enlaces relativos y las imagenes dentro de rutas que el build pueda copiar.
- Usa bloques de codigo con triple acento invertido y especifica el lenguaje cuando sea posible.
- No mezcles estilos inline con el Markdown; el estilo debe vivir en las plantillas o en CSS.

## Convenciones de archivo
- Recomendado: `YYYY-MM-DD-slug.md`.
- El `slug` debe ser estable y no cambiar sin necesidad.
- Los borradores deben quedarse fuera de la carpeta publicada o marcarse con `published: false`.

## Ejemplo completo
```md
---
title: "Construyendo un blog estatica con Python"
slug: "construyendo-un-blog-estatica-con-python"
date: "2026-06-05"
summary: "Base documental y tecnica para generar un blog a partir de Markdown."
tags:
  - python
  - markdown
  - blog
category: "proyecto"
author: "Equipo del blog"
cover: "assets/posts/construyendo-un-blog-estatica-con-python/cover.jpg"
featured: true
published: true
---

# Construyendo un blog estatica con Python

Este articulo explica como el generador toma el contenido Markdown y lo convierte en una pagina HTML con estilo, navegacion y metadatos.
```

## Lista de verificacion antes de publicar
- El frontmatter contiene todos los campos obligatorios.
- La ruta de portada y demas imagenes existe en la carpeta de assets.
- El resumen es breve y util para tarjetas y SEO.
- El articulo se ve bien en desktop y mobile.
- El build local no reporta errores de formato.
