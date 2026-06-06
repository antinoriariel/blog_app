# Estructura del proyecto

## Estructura propuesta
```text
blog_app/
  content/
    posts/
    pages/
  templates/
    base.html
    post.html
    index.html
    page.html
  assets/
    css/
    js/
    img/
    fonts/
  scripts/
    build.py
    render.py
    utils.py
  dist/
  docs/
  plan.md
  readme.md
  usage.md
```

## Responsabilidad de cada carpeta
- `content/`: fuente editable por autores.
- `templates/`: esqueletos HTML reutilizables.
- `assets/`: estilos, scripts, imagenes y tipografia.
- `scripts/`: logica de build y conversion.
- `dist/`: salida generada que se publica.
- `docs/`: documentacion tecnica y editorial.

## Reglas de organizacion
- El contenido no debe mezclar HTML de presentacion salvo casos justificados.
- Los assets del sitio deben tener nombres estables.
- Las plantillas deben ser modulares para evitar duplicacion.
- La salida generada no debe editarse a mano.

## Resultado esperado
La estructura debe permitir crecer sin reordenar todo el proyecto cuando se agreguen mas paginas, taxonomias o estilos.
