# Despliegue

## Objetivo
Publicar el sitio como contenido estatica, sin servidor de aplicacion. La carpeta generada por el build debe poder alojarse en cualquier hosting para sitios estaticos.

## Salida esperada
- Carpeta de salida lista para servir, por ejemplo `dist/`.
- Archivos HTML finales.
- Assets copiados y referenciados con rutas correctas.
- Paginas auxiliares como `404.html` y sitemap, si se activan.

## Opciones de hosting
- GitHub Pages.
- Netlify.
- Cloudflare Pages.
- Servidor web simple o almacenamiento estatico propio.

## Flujo recomendado
1. Ejecutar el build local.
2. Revisar la carpeta generada.
3. Verificar rutas, imagenes y estilos.
4. Publicar la carpeta de salida en el proveedor elegido.

## Reglas para hosting estatica
- Las rutas deben funcionar desde la raiz o desde una base URL configurable.
- Los enlaces internos no deben depender de rutas absolutas fragiles.
- Los recursos pesados deben estar optimizados antes del despliegue.
- El sitio debe incluir un `404.html` util si el hosting lo soporta.

## Consideraciones SEO y compartido
- Generar `title` y `meta description` por pagina.
- Incluir `canonical` cuando corresponda.
- Preparar metadatos Open Graph y Twitter Card si se decide activarlos.
- Generar `sitemap.xml` y `robots.txt` cuando el proyecto entre en fase de publicacion.

## Validacion previa
- Abrir el sitio generado en un servidor local estatica.
- Comprobar enlaces, imagenes y tipografia.
- Revisar que no existan recursos externos caidos.
- Probar en desktop y mobile antes de publicar.
