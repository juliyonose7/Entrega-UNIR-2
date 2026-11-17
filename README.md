# Laboratorio: Tecnologías JavaScript y AJAX

## Descripción del Proyecto
Este proyecto contiene la solución interactiva para la actividad **"Laboratorio: Tecnologías JavaScript y AJAX"**, implementada con **React 18 y CSS3 puro** en el frontend, y complementada con una memoria técnica formal en formato Word (`.docx`) y PDF (`.pdf`).

---

## 📋 Estructura de la Solución y Módulos Desarrollados

| Ítem | Módulo | Descripción Técnica de la Implementación |
| :---: | :--- | :--- |
| **1** | Detección de Palíndromos | Algoritmo de normalización Unicode NFD, supresión de tildes ortográficas y caracteres no alfanuméricos con verificación simétrica. |
| **2** | Mayor de Dos Números | Parseo numérico con `parseFloat`, validación contra `isNaN` y bifurcación condicional de mayor, menor o igualdad. |
| **3** | Vocales Presentes | Extracción y filtrado del subconjunto de vocales existentes en el texto ingresado. |
| **4** | Frecuencia de Vocales | Conteo exacto de apariciones mediante acumulador tipo hash y barras porcentuales dinámicas. |
| **5** | URL por Defecto en AJAX | Inicialización automática del campo de texto con la propiedad `window.location.href` durante el montaje. |
| **6** | Contenidos del Archivo | Descarga asíncrona mediante `XMLHttpRequest` y renderizado del cuerpo de datos en la zona designada. |
| **7** | Estados de la Petición | Monitorización continua de las cinco fases de `readyState` (del cero al cuatro) con registro cronológico en tiempo real. |
| **8** | Cabeceras HTTP | Extracción y desglose estructurado de metadatos mediante `getAllResponseHeaders()`. |
| **9** | Código y Texto de Estado | Captura visual del código numérico `status` y del texto oficial `statusText` devueltos por el servidor. |
| **10** | Memoria Técnica | Documento académico formal en Word (`.docx`) y PDF (`.pdf`) con código fuente explicado y batería de pruebas. |

---

## 🚀 Cómo Ejecutar la Aplicación

### Opción A (Recomendada - Con Servidor Local HTTP):
1. Haz doble clic en el archivo **`iniciar_servidor.bat`** (o ejecuta en consola `python servidor.py`).
2. Se abrirá automáticamente tu navegador en `http://localhost:8000/index.html`.
3. Todas las peticiones AJAX a archivos locales (`data/ejemplo.txt`, `data/datos.json`, etc.) funcionarán con total compatibilidad CORS.

### Opción B (Directa en el Navegador):
1. Abre directamente el archivo **`index.html`** con Google Chrome, Mozilla Firefox o Microsoft Edge.
2. Nota: los navegadores bloquean peticiones XMLHttpRequest locales bajo `file://` por políticas de seguridad; para las pruebas AJAX locales, utiliza la Opción A o las URLs públicas preparadas en la interfaz.

---

## 📁 Archivos Entregables

1. **`Solucion_Laboratorio_JavaScript_AJAX.docx`**: Memoria técnica formal para entrega en formato Microsoft Word (estilo sobrio en negro, sin mención a calificaciones ni paréntesis excesivos).
2. **`Solucion_Laboratorio_JavaScript_AJAX.pdf`**: Documento generado en formato PDF para envío en la plataforma educativa (7 páginas, conforme al límite de 10 páginas).
3. **`index.html`**: Aplicación web completa en React + CSS.
4. **`styles.css`**: Hoja de estilos moderna y responsive.
5. **`servidor.py` / `iniciar_servidor.bat`**: Servidor local HTTP para pruebas de AJAX.
6. **`laboratorio_clasico.html`**: Versión clásica HTML+JS puro del laboratorio.
7. **`data/`**: Archivos de prueba (`ejemplo.txt`, `datos.json`, `fragmento.html`).
