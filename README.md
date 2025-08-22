# Proyecto Ciffer

> **Nota:** El manejo de errores y reintentos automáticos en la conexión a la base de datos se realiza con la librería `tenacity` en el archivo `python/connection.py`.

## Estructura del Proyecto

- **frontend (React):**
  - Carpeta `src/`: Contiene la aplicación React, incluyendo el formulario de login (`App.js`).
- **backend (Python):**
  - Carpeta `python/`: Incluye los archivos para la API Flask (`api.py`), la lógica de login (`loggin.py`), y la conexión a MongoDB Atlas (`connection.py`).
- **Base de datos:**
  - MongoDB Atlas, donde se almacenan los usuarios registrados.

## Descripción General

Este proyecto es un cifrador de archivos que permite el acceso únicamente a usuarios registrados en la base de datos.  
Está pensado como una **aplicación de escritorio** para brindar mayor seguridad y facilidad de uso a los usuarios finales.  
Los usuarios deben iniciar sesión mediante el formulario de login. La autenticación se realiza contra la base de datos MongoDB Atlas usando una API desarrollada en Flask.  
Una vez autenticados, los usuarios podrán acceder a las funcionalidades de cifrado de archivos.

El manejo de errores en la conexión a la base de datos utiliza la librería `tenacity`, lo que permite reintentar la conexión automáticamente en caso de fallos temporales.

---

Para más detalles sobre cómo iniciar y usar el proyecto, consulta la documentación específica de cada parte:

- **Frontend (React):** [Documentación de Create React App](https://facebook.github.io/create-react-app/docs/getting-started)
- **Backend (Python):** Revisa los comentarios en el código de los archivos en la carpeta `python/`.
- **Base de datos (MongoDB Atlas):** [Documentación de MongoDB Atlas](https://docs.atlas.mongodb.com/)

## Instrucciones Específicas

### 1. Configuración del Entorno

- Asegúrate de tener instaladas las dependencias necesarias tanto para el frontend como para el backend.
- Crea un archivo `.env` en la carpeta `python/` con la configuración adecuada para la conexión a tu base de datos MongoDB Atlas. Usa el archivo `.env.example` como referencia.

### 2. Ejecución del Proyecto

#### Frontend (React)

```bash
cd frontend
npm install
npm start
```

#### Backend (Python)

```bash
cd backend
pip install -r requirements.txt
python api.py
```

### 3. Acceso a la Aplicación

- Una vez que el frontend y el backend estén en funcionamiento, abre tu navegador y ve a `http://localhost:3000` para acceder a la aplicación.
- Usa las credenciales de un usuario registrado para iniciar sesión.

### 4. Cifrado de Archivos

- Después de iniciar sesión, podrás acceder a la funcionalidad de cifrado de archivos.
- Selecciona un archivo desde el frontend y el sistema lo cifrará usando la clave pública del usuario.

### 5. Descifrado de Archivos

- Para descifrar un archivo, súbelo a la sección de descifrado en el frontend.
- El archivo será procesado y se descargará automáticamente una vez descifrado.

---

## Notas Adicionales

- El proyecto utiliza `React Router` para la navegación entre el formulario de login y las funcionalidades de cifrado/descifrado.
- Se recomienda usar un navegador moderno y actualizado para evitar problemas de compatibilidad.
- Para cualquier duda o problema, revisa los issues abiertos en el repositorio o crea uno nuevo describiendo tu situación.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
