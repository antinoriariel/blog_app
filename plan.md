# Plan del proyecto

## Objetivo
Construir un blog estatica que convierta archivos `.md` con una estructura definida en entradas HTML listas para publicar. El proceso de generacion se ejecuta en local con Python y produce una salida completamente estatica, apta para hosting simple.

## Alcance inicial
- Convertir entradas Markdown con metadatos en HTML.
- Generar una portada, paginas de entrada, archivos por fecha o categoria, y paginas de soporte.
- Aplicar una capa visual moderna con Bootstrap, animate.css, Font Awesome y Google Fonts.
- Mantener un flujo de trabajo simple: escribir contenido, ejecutar el generador y publicar la carpeta de salida.

## Fuera de alcance por ahora
- Login, panel de administracion o CMS dinamico.
- Comentarios en tiempo real o funciones de backend.
- Edicion colaborativa desde el navegador.
- Buscador indexado en servidor.

## Fases de trabajo
### Fase 1: definicion editorial
- Cerrar el formato canonico de los archivos `.md`.
- Definir los campos de metadatos requeridos y opcionales.
- Establecer la estructura de carpetas de contenido, plantillas y salida.

### Fase 2: generacion base
- Implementar el descubrimiento de archivos Markdown.
- Validar y parsear frontmatter.
- Convertir el cuerpo Markdown a HTML.
- Renderizar una pagina por entrada.

### Fase 3: experiencia del sitio
- Construir la portada con entradas destacadas y listado principal.
- Generar paginas de archivo, etiquetas y secciones.
- Integrar estilos, iconografia y animaciones.

### Fase 4: calidad y publicacion
- Verificar accesibilidad, responsive y metadatos SEO.
- Preparar el flujo de build local.
- Validar la carpeta generada con un hosting estatica.

## Criterios de aceptacion
- Un archivo Markdown valido genera una entrada HTML sin pasos manuales.
- El sitio se puede abrir y navegar localmente con los recursos resueltos.
- El diseno mantiene consistencia visual en desktop y mobile.
- El build falla de forma clara cuando falta un dato obligatorio o el archivo es invalido.

## Riesgos conocidos
- Ambiguedad en el formato de entrada si el esquema no se documenta bien.
- Ruptura de estilos si cada entrada admite estructuras demasiado libres.
- Enlaces rotos a imagenes o recursos no copiados al build.

## Resultado esperado
Una base documental y tecnica suficiente para implementar el generador Python y el sitio estatico sin rehacer decisiones mas adelante.
