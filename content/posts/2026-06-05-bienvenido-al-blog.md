---
title: "Bienvenido al blog"
slug: "bienvenido"
date: "2026-06-05"
summary: "Primera entrada del blog. Por qué lo armé, qué vas a encontrar aquí y cómo está construido desde cero con Python y Markdown."
tags:
  - blog
  - meta
category: "personal"
author: "Ariel Antinori"
featured: true
published: true
---

## Por qué existe este blog

Durante años guardé notas, apuntes y experimentos en carpetas locales que nadie más leía. Este blog es el intento de organizar eso en un lugar público, searchable y con forma.

No hay una audiencia definida. Si te sirve algo de lo que escribo, perfecto. Si no, igual seguiré escribiendo.

## Qué vas a encontrar

La idea es mezclar tres tipos de contenido:

- **Proyectos técnicos**: cómo armé algo, qué decisiones tomé y qué salió mal antes de que saliera bien.
- **Notas cortas**: ideas sueltas, aprendizajes de la semana, cosas que quiero recordar.
- **Tutoriales**: guías paso a paso cuando encuentro que la documentación existente es confusa o está desactualizada.

## Cómo está construido

El blog en sí es un generador estático escrito en Python. Funciona así:

1. Escribo una entrada como este archivo `.md` con un bloque de metadatos al principio.
2. Ejecuto `python scripts/build.py` desde la raíz del proyecto.
3. El generador valida el frontmatter, convierte el Markdown a HTML y lo mete dentro de plantillas Jinja2.
4. La salida es una carpeta `dist/` con HTML puro, lista para subir a cualquier hosting estático.

El diseño usa Bootstrap 5, Font Awesome, Google Fonts (Fraunces + DM Sans), animate.css para las transiciones y highlight.js para el resaltado de sintaxis con detección automática de lenguaje.

### Dependencias Python

```
Markdown==3.6
PyYAML==6.0.1
Jinja2==3.1.4
```

### Estructura de carpetas

```
blog_app/
  content/posts/      ← entradas en Markdown
  content/pages/      ← páginas estáticas (sobre, contacto…)
  templates/          ← plantillas HTML con Jinja2
  assets/             ← CSS, JS e imágenes
  scripts/            ← generador Python
  dist/               ← salida compilada (no editar a mano)
```

## Cómo agregar una entrada nueva

Copio la plantilla `templates/new-post.md`, la guardo en `content/posts/` con el nombre `YYYY-MM-DD-slug.md`, relleno el frontmatter y escribo el cuerpo. Cuando termino, ejecuto el build y listo.

---

Si encontrás un error o algo que se podría mejorar, podés abrir un issue en el repositorio.
