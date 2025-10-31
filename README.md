# Recogning 🎯

**[Español](#español) | [English](#english)**

---

## Español

**Inteligencia visual en vivo.** Un sistema que aprende a reconocer el mundo desde la cámara, etiquetando y recordando objetos como un aprendiz cuántico digital.

## 📋 Descripción

Sistema básico de reconocimiento de objetos en Python que permite capturar, entrenar y clasificar imágenes desde la webcam usando el algoritmo **K-Nearest Neighbors (KNN)**. El objetivo es enseñar al modelo nuevos objetos manualmente y obtener reconocimiento en tiempo real.

### 🎯 Dos Versiones Disponibles

1. **`reconocimiento_simple.py`** - Versión simplificada con menú interactivo
   - Ideal para principiantes
   - Interfaz de menú fácil de usar
   - Flujo guiado paso a paso

2. **`object_recognition.py`** - Versión avanzada con clase completa
   - Para usuarios avanzados
   - API programática completa
   - Controles de teclado interactivos

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

### Opción 1: Versión Simple (Recomendado para principiantes)

```bash
python reconocimiento_simple.py
```

**Menú interactivo:**
1. Enseñar nuevo objeto (captura 30 ejemplos automáticamente)
2. Entrenar modelo
3. Reconocer en tiempo real
4. Ver objetos aprendidos
5. Salir

### Opción 2: Versión Avanzada

```bash
python object_recognition.py
```

**Controles del Teclado:**

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

---
---

## English

**Live visual intelligence.** A system that learns to recognize the world through the camera, labeling and remembering objects like a digital quantum learner.

## 📋 Description

Basic object recognition system in Python that allows capturing, training, and classifying images from the webcam using the **K-Nearest Neighbors (KNN)** algorithm. The goal is to manually teach the model new objects and obtain real-time recognition.

### 🎯 Two Available Versions

1. **`reconocimiento_simple.py`** - Simplified version with interactive menu
   - Ideal for beginners
   - Easy-to-use menu interface
   - Step-by-step guided workflow

2. **`object_recognition.py`** - Advanced version with complete class
   - For advanced users
   - Complete programmatic API
   - Interactive keyboard controls

### Main Features

- ✅ **Image capture** from webcam in real-time
- ✅ **Manual training** of new object classes
- ✅ **Real-time classification** using KNN
- ✅ **Local dataset** with organized storage by classes
- ✅ **Trained model persistence**
- ✅ **Interactive interface** with keyboard controls
- ✅ **Automatic image preprocessing**

## 🛠️ Technologies

- **OpenCV**: Video/image capture and processing
- **NumPy**: Numerical operations and array manipulation
- **scikit-learn**: KNN classifier implementation
- **Python 3.x**: Base project language

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- Functional webcam
- pip (Python package manager)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/Blackmvmba88/Recogning.git
cd Recogning
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Option 1: Simple Version (Recommended for beginners)

```bash
python reconocimiento_simple.py
```

**Interactive menu:**
1. Teach new object (captures 30 examples automatically)
2. Train model
3. Recognize in real-time
4. View learned objects
5. Exit

### Option 2: Advanced Version

```bash
python object_recognition.py
```

**Keyboard Controls:**

| Key | Function |
|-----|----------|
| `c` | Activate **capture mode** - capture training samples |
| `SPACE` | **Capture sample** from current class (in capture mode) |
| `t` | **Train model** with captured samples |
| `p` | Activate **prediction mode** - recognize objects in real-time |
| `l` | **Load model** previously saved |
| `q` | **Exit** program |

### Typical Workflow (Simple Version)

```
1. Run: python reconocimiento_simple.py
2. Select option 1, enter object name (e.g., "cup")
3. Position object in front of camera, 30 samples captured automatically
4. Repeat for different objects
5. Select option 2 to train model
6. Select option 3 to see real-time recognition
```

### Typical Workflow (Advanced Version)

```
1. Run: python object_recognition.py
2. Press 'c', enter class name (e.g., "cup")
3. Press SPACE 10-20 times to capture samples
4. Repeat for different objects
5. Press 't' to train model
6. Press 'p' to see real-time recognition
```

## 📁 Project Structure

```
Recogning/
├── reconocimiento_simple.py # Simple version with menu
├── object_recognition.py    # Advanced version with class
├── requirements.txt         # Project dependencies
├── README.md               # Documentation (Spanish/English)
├── QUICKSTART.md           # Quick start guide (Spanish)
├── example_usage.py        # Code examples
├── test_system.py          # Test suite
├── dataset/                # Images directory (auto-created)
│   ├── class1/
│   └── class2/
├── dataset_mamba/          # Images for simple version (auto-created)
│   ├── object1/
│   └── object2/
└── model.pkl              # Trained KNN model (created when training)
```

## 🔬 How It Works

### 1. Capture and Preprocessing

- Images captured from webcam
- Resized to 64x64 pixels
- Converted to grayscale
- Normalized (values 0-1)
- Flattened into one-dimensional vector

### 2. Storage

- Each class saved in its own subdirectory
- Images saved in JPG format
- Automatic sample counting

### 3. Training

- System loads all images from dataset
- Preprocesses each image following same pipeline
- Trains KNN classifier
- Saves trained model

### 4. Prediction

- Captures frames in real-time
- Preprocesses each frame
- Classifies using KNN model
- Calculates confidence based on neighbor distances
- Displays result on screen

## 💡 Use Cases

- 🎓 **Education**: Base for learning visual AI and machine learning
- 🤖 **Smart assistants**: Everyday object recognition
- 🔍 **Custom classification**: Train specific categories
- 🧪 **Rapid prototyping**: Validate computer vision ideas
- 📚 **Academic projects**: Practical KNN implementation

## ⚙️ Advanced Configuration

The system can be customized by editing the `ObjectRecognitionSystem` class:

```python
# Change image size for processing
self.img_size = (64, 64)  # Increase for more detail

# Modify number of neighbors in KNN
n_neighbors = 5  # In train_model() method
```

## 🐛 Troubleshooting

### Webcam doesn't start
- Verify webcam is connected and functional
- Check camera access permissions
- Test with another camera application

### Inaccurate predictions
- Capture more samples per class (20-30 recommended)
- Ensure good lighting during capture
- Capture objects from different angles
- Maintain similar conditions between training and prediction

### Module import error
- Verify dependency installation: `pip install -r requirements.txt`
- Use virtual environment to avoid conflicts

## 🤝 Contributions

Contributions are welcome. Please:

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the MIT license.

## 👤 Author

**Blackmvmba88**

## 🙏 Acknowledgments

- OpenCV community for computer vision tools
- scikit-learn for KNN implementation
- Python community for the library ecosystem

---

⭐ If you found this project useful, consider giving it a star on GitHub!
