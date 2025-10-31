# Recogning 🎯

**Inteligencia visual en vivo.** Un sistema que aprende a reconocer el mundo desde la cámara, etiquetando y recordando objetos como un aprendiz cuántico digital.

## 📋 Descripción

Sistema básico de reconocimiento de objetos en Python que permite capturar, entrenar y clasificar imágenes desde la webcam usando el algoritmo **K-Nearest Neighbors (KNN)**. El objetivo es enseñar al modelo nuevos objetos manualmente y obtener reconocimiento en tiempo real.

### Características Principales

- ✅ **Captura de imágenes** desde webcam en tiempo real
- ✅ **Entrenamiento manual** de nuevas clases de objetos
- ✅ **Clasificación en tiempo real** usando KNN
- ✅ **Dataset local** con almacenamiento organizado por clases
- ✅ **Persistencia del modelo** entrenado
- ✅ **Interfaz interactiva** con controles de teclado
- ✅ **Preprocesamiento automático** de imágenes

## 🛠️ Tecnologías

- **OpenCV**: Captura y procesamiento de video/imágenes
- **NumPy**: Operaciones numéricas y manipulación de arrays
- **scikit-learn**: Implementación del clasificador KNN
- **Python 3.x**: Lenguaje base del proyecto

## 📦 Instalación

### Requisitos Previos

- Python 3.7 o superior
- Webcam funcional
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/Blackmvmba88/Recogning.git
cd Recogning
```

2. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

## 🚀 Uso

### Iniciar el Sistema

```bash
python object_recognition.py
```

### Controles del Teclado

| Tecla | Función |
|-------|---------|
| `c` | Activar **modo captura** - capturar muestras para entrenamiento |
| `ESPACIO` | **Capturar muestra** de la clase actual (en modo captura) |
| `t` | **Entrenar modelo** con las muestras capturadas |
| `p` | Activar **modo predicción** - reconocer objetos en tiempo real |
| `l` | **Cargar modelo** previamente guardado |
| `q` | **Salir** del programa |

### Flujo de Trabajo Típico

#### 1. Capturar Muestras de Entrenamiento

```
1. Ejecutar: python object_recognition.py
2. Presionar 'c' para modo captura
3. Ingresar nombre de la clase (ej: "taza", "libro", "celular")
4. Posicionar el objeto frente a la cámara
5. Presionar ESPACIO para capturar múltiples muestras (10-20 recomendado)
6. Repetir pasos 2-5 para cada clase de objeto que desee reconocer
```

#### 2. Entrenar el Modelo

```
7. Presionar 't' para entrenar el modelo con todas las muestras capturadas
8. Esperar a que el entrenamiento complete
```

#### 3. Reconocimiento en Tiempo Real

```
9. Presionar 'p' para activar modo predicción
10. Mostrar objetos frente a la cámara
11. Observar las predicciones en pantalla con porcentaje de confianza
```

## 📁 Estructura del Proyecto

```
Recogning/
├── object_recognition.py    # Módulo principal del sistema
├── requirements.txt         # Dependencias del proyecto
├── README.md               # Documentación
├── dataset/                # Directorio de imágenes (se crea automáticamente)
│   ├── clase1/            # Carpeta por clase
│   │   ├── clase1_1.jpg
│   │   ├── clase1_2.jpg
│   │   └── ...
│   ├── clase2/
│   └── ...
└── model.pkl              # Modelo KNN entrenado (se crea al entrenar)
```

## 🔬 Cómo Funciona

### 1. Captura y Preprocesamiento

- Las imágenes se capturan desde la webcam
- Se redimensionan a 64x64 píxeles
- Se convierten a escala de grises
- Se normalizan (valores 0-1)
- Se aplanan en un vector unidimensional

### 2. Almacenamiento

- Cada clase se guarda en su propio subdirectorio dentro de `dataset/`
- Las imágenes se guardan en formato JPG
- Se mantiene un conteo automático de muestras

### 3. Entrenamiento

- El sistema carga todas las imágenes del dataset
- Preprocesa cada imagen siguiendo el mismo pipeline
- Entrena un clasificador KNN (K-Nearest Neighbors)
- Guarda el modelo entrenado en `model.pkl`

### 4. Predicción

- Captura frames en tiempo real
- Preprocesa cada frame
- Clasifica usando el modelo KNN
- Calcula confianza basada en distancias de vecinos
- Muestra resultado en pantalla

## 💡 Casos de Uso

- 🎓 **Educación**: Base para aprender IA visual y machine learning
- 🤖 **Asistentes inteligentes**: Reconocimiento de objetos cotidianos
- 🔍 **Clasificación personalizada**: Entrenar categorías específicas
- 🧪 **Prototipado rápido**: Validar ideas de visión por computadora
- 📚 **Proyectos académicos**: Implementación práctica de KNN

## ⚙️ Configuración Avanzada

El sistema puede personalizarse editando la clase `ObjectRecognitionSystem`:

```python
# Cambiar tamaño de imagen para procesamiento
self.img_size = (64, 64)  # Aumentar para más detalle

# Modificar número de vecinos en KNN
n_neighbors = 5  # En método train_model()
```

## 🐛 Solución de Problemas

### La webcam no se inicia
- Verificar que la webcam esté conectada y funcional
- Verificar permisos de acceso a la cámara
- Probar con otra aplicación de cámara

### Predicciones inexactas
- Capturar más muestras por clase (20-30 recomendado)
- Asegurar buena iluminación durante captura
- Capturar objetos desde diferentes ángulos
- Mantener condiciones similares entre entrenamiento y predicción

### Error al importar módulos
- Verificar instalación de dependencias: `pip install -r requirements.txt`
- Usar entorno virtual para evitar conflictos

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👤 Autor

**Blackmvmba88**

## 🙏 Agradecimientos

- Comunidad de OpenCV por las herramientas de visión por computadora
- scikit-learn por la implementación de KNN
- Comunidad de Python por el ecosistema de librerías

---

⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub!
