# Blog estático en Markdown

Generador de sitio estático escrito en Python. Convierte archivos `.md` con frontmatter YAML en páginas HTML completas usando plantillas Jinja2. La salida es una carpeta `dist/` lista para subir a cualquier hosting estático.

## Inicio rápido

```bash
# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Configurar el sitio (título, URL, autor…)
# Editar config.yaml

# 3. Compilar
python scripts/build.py

# 4. Verificar localmente
cd dist && python -m http.server 8000
```

Abrir [http://localhost:8000](http://localhost:8000).

## Agregar una entrada nueva

1. Copiar `templates/new-post.md` a `content/posts/YYYY-MM-DD-mi-slug.md`.
2. Completar el frontmatter (título, slug, fecha, resumen).
3. Escribir el cuerpo en Markdown.
4. Cambiar `published: false` a `published: true`.
5. Ejecutar `python scripts/build.py`.

Consultar [usage.md](usage.md) para la referencia completa del formato.

## Estructura del proyecto

```
blog_app/
├── content/
│   ├── posts/          ← entradas del blog (.md)
│   └── pages/          ← páginas estáticas (sobre, contacto…)
├── templates/
│   ├── base.html       ← layout base con nav y footer
│   ├── index.html      ← portada
│   ├── post.html       ← entrada individual
│   ├── page.html       ← página estática
│   ├── tag.html        ← listado por etiqueta
│   ├── archive.html    ← archivo cronológico
│   ├── 404.html        ← página de error
│   └── new-post.md     ← plantilla para nuevas entradas
├── assets/
│   ├── css/main.css    ← estilos personalizados
│   └── js/main.js      ← comportamiento del sitio
├── scripts/
│   ├── build.py        ← punto de entrada del generador
│   ├── render.py       ← funciones de renderizado
│   ├── utils.py        ← scanner, parser, validador
│   └── config.py       ← carga de config.yaml
├── docs/               ← documentación técnica
├── dist/               ← salida compilada (no editar)
├── config.yaml         ← configuración del sitio
└── requirements.txt    ← dependencias Python
```

## Stack

| Componente     | Tecnología                              |
|---------------|------------------------------------------|
| Generador     | Python 3.10+                             |
| Plantillas    | Jinja2                                   |
| Markdown      | python-markdown + extensiones            |
| Metadatos     | PyYAML (frontmatter)                     |
| Layout        | Bootstrap 5                              |
| Tipografía    | Google Fonts (Playfair Display + Inter)  |
| Iconos        | Font Awesome 6                           |
| Animaciones   | animate.css                              |
| Código        | Prism.js (resaltado de sintaxis)         |

## Configuración

Editar `config.yaml`:

```yaml
site:
  title: "Mi Blog"
  description: "Descripción del sitio."
  author: "Nombre del Autor"
  url: "https://mi-blog.com"
  language: "es"

build:
  base_url: "/"          # cambiar si el sitio vive en una subcarpeta

features:
  tags: true
  archive: true
  sitemap: true
  404: true
```

## Documentación

- [Guía de uso](usage.md) — formato de entradas y flujo de trabajo
- [Especificación](docs/especificacion.md) — requisitos funcionales
- [Arquitectura](docs/arquitectura.md) — pipeline del generador
- [Sistema visual](docs/sistema-visual.md) — guía de diseño
- [Despliegue](docs/despliegue.md) — opciones de publicación
- [Estructura del proyecto](docs/estructura-del-proyecto.md) — árbol de carpetas
- [Calidad](docs/calidad.md) — criterios de aceptación
- [Formato de entradas](docs/formato-de-entradas.md) — referencia del frontmatter
