# 🤝 Guía de Contribución - Recogning

¡Gracias por tu interés en contribuir a **Recogning**! Este proyecto es una iniciativa colaborativa para crear un estándar latinoamericano de percepción visual viva.

## 📋 Tabla de Contenidos

- [Código de Conducta](#-código-de-conducta)
- [Cómo Puedo Contribuir](#-cómo-puedo-contribuir)
- [Estándares de Desarrollo](#-estándares-de-desarrollo)
- [Proceso de Pull Request](#-proceso-de-pull-request)
- [Estándares de Branches](#-estándares-de-branches)
- [Guía de Estilo](#-guía-de-estilo)

---

## 🌟 Código de Conducta

Este proyecto se adhiere a un código de conducta inclusivo y respetuoso. Esperamos que todos los participantes:

- Sean respetuosos y constructivos
- Acepten críticas constructivas
- Se enfoquen en lo mejor para la comunidad
- Muestren empatía hacia otros miembros

---

## 🚀 Cómo Puedo Contribuir

### Reportar Bugs

Los bugs se rastrean como [GitHub issues](https://github.com/Blackmvmba88/Recogning/issues). Antes de crear un issue:

1. **Verifica** que el bug no haya sido reportado ya
2. **Usa** la plantilla de issue correspondiente
3. **Incluye** detalles específicos:
   - Descripción clara del problema
   - Pasos para reproducir
   - Comportamiento esperado vs. actual
   - Capturas de pantalla (si aplica)
   - Versión de Python y sistema operativo

### Sugerir Mejoras

Las sugerencias de mejoras también se rastrean como issues:

1. **Usa** la plantilla de feature request
2. **Explica** el problema que resuelve
3. **Describe** la solución propuesta
4. **Menciona** alternativas consideradas

### Contribuir Código

#### Primera Contribución

¿Primera vez contribuyendo? Busca issues etiquetados como:
- `good first issue` - Problemas ideales para principiantes
- `help wanted` - Issues donde necesitamos ayuda

#### Proceso de Desarrollo

1. **Fork** el repositorio
2. **Clona** tu fork localmente:
   ```bash
   git clone https://github.com/TU_USUARIO/Recogning.git
   cd Recogning
   ```

3. **Crea** una rama desde `main`:
   ```bash
   git checkout -b feature/nombre-descriptivo
   ```

4. **Instala** dependencias de desarrollo:
   ```bash
   pip install -r requirements-dev.txt
   ```

5. **Desarrolla** tu feature/fix

6. **Prueba** tus cambios:
   ```bash
   pytest tests/
   ```

7. **Commit** tus cambios (ver [Guía de Commits](#commits))

8. **Push** a tu fork:
   ```bash
   git push origin feature/nombre-descriptivo
   ```

9. **Abre** un Pull Request

---

## 🛠️ Estándares de Desarrollo

### Estructura del Proyecto

```
Recogning/
├── recogning/           # Código fuente principal
│   ├── core/           # Lógica central
│   ├── perception/     # Módulos de visión
│   ├── memory/         # Sistema de memoria
│   └── utils/          # Utilidades
├── tests/              # Tests
├── docs/               # Documentación
├── examples/           # Ejemplos de uso
└── scripts/            # Scripts de utilidad
```

### Tecnologías Principales

- **Python 3.8+**: Lenguaje principal
- **PyTorch**: Deep learning
- **OpenCV**: Visión por computadora
- **YOLO/MobileNet**: Detección de objetos
- **CLIP**: Embeddings visuales

### Testing

- Escribe tests para nuevas funcionalidades
- Mantén cobertura de tests > 80%
- Usa `pytest` para ejecutar tests
- Tests unitarios en `tests/unit/`
- Tests de integración en `tests/integration/`

### Documentación

- Documenta funciones públicas con docstrings
- Usa formato Google/NumPy para docstrings
- Actualiza README si añades features mayores
- Añade ejemplos en `examples/` si es relevante

---

## 🔄 Proceso de Pull Request

### Checklist del PR

Antes de abrir un PR, asegúrate de:

- [ ] El código sigue la guía de estilo del proyecto
- [ ] Los tests pasan (`pytest tests/`)
- [ ] Añadiste tests para nueva funcionalidad
- [ ] Actualizaste documentación relevante
- [ ] El commit message sigue las convenciones
- [ ] No hay conflictos con `main`

### Descripción del PR

Usa esta plantilla:

```markdown
## Descripción
[Descripción breve de los cambios]

## Tipo de Cambio
- [ ] Bug fix
- [ ] Nueva feature
- [ ] Breaking change
- [ ] Documentación

## ¿Cómo se ha probado?
[Describe las pruebas realizadas]

## Checklist
- [ ] Mi código sigue el estilo del proyecto
- [ ] He revisado mi propio código
- [ ] He comentado código complejo
- [ ] He actualizado la documentación
- [ ] Mis cambios no generan warnings
- [ ] He añadido tests
- [ ] Tests nuevos y existentes pasan
```

### Revisión de Código

- Sé paciente - las revisiones pueden tomar tiempo
- Responde a comentarios constructivamente
- Realiza cambios solicitados
- Mantén el PR enfocado en un solo objetivo

---

## 🌿 Estándares de Branches

### Nomenclatura de Branches

Usa prefijos descriptivos:

```
feature/nombre-descriptivo    # Nueva funcionalidad
bugfix/nombre-del-bug         # Corrección de bug
hotfix/issue-critico          # Fix urgente
docs/actualizacion            # Solo documentación
refactor/mejora-codigo        # Refactoring
test/nuevos-tests             # Añadir tests
```

**Ejemplos:**
- `feature/yolo-integration`
- `bugfix/camera-initialization`
- `docs/update-readme`
- `refactor/memory-module`

### Branch Principal

- `main`: Branch principal, siempre estable
- Solo se actualiza vía Pull Requests
- Debe pasar todos los tests antes de merge

### Desarrollo

1. Crea branches desde `main`
2. Mantén branches enfocadas (un feature/fix por branch)
3. Actualiza regularmente desde `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout tu-branch
   git rebase main
   ```

---

## 📝 Guía de Estilo

### Commits

Usa **Conventional Commits**:

```
<tipo>: <descripción corta>

[cuerpo opcional]

[footer opcional]
```

**Tipos:**
- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Solo documentación
- `style`: Formato, sin cambios de código
- `refactor`: Refactoring de código
- `test`: Añadir tests
- `chore`: Mantenimiento

**Ejemplos:**
```
feat: add YOLOv8 integration for object detection

fix: resolve camera initialization error on startup

docs: update installation instructions

refactor: improve memory module performance
```

### Código Python

Seguimos **PEP 8** con algunas adaptaciones:

```python
# Imports
import os
import sys
from typing import List, Dict, Optional

# Constantes en MAYÚSCULAS
MAX_OBJECTS = 100
DEFAULT_CONFIDENCE = 0.5

# Clases en PascalCase
class ObjectDetector:
    """Detector de objetos usando YOLOv8.
    
    Args:
        model_path: Ruta al modelo YOLO
        confidence: Umbral de confianza mínimo
        
    Example:
        >>> detector = ObjectDetector("yolov8n.pt")
        >>> results = detector.detect(image)
    """
    
    def __init__(self, model_path: str, confidence: float = 0.5):
        self.model_path = model_path
        self.confidence = confidence
    
    def detect(self, image: np.ndarray) -> List[Dict]:
        """Detecta objetos en una imagen.
        
        Args:
            image: Imagen en formato numpy array
            
        Returns:
            Lista de detecciones con bbox y clase
        """
        pass

# Funciones en snake_case
def process_detections(detections: List[Dict]) -> List[Dict]:
    """Procesa lista de detecciones.
    
    Args:
        detections: Lista de detecciones raw
        
    Returns:
        Detecciones procesadas y filtradas
    """
    return [d for d in detections if d['confidence'] > 0.5]
```

### Docstrings

Usa formato Google:

```python
def function_with_types_in_docstring(param1, param2):
    """Descripción breve de la función.
    
    Descripción más detallada si es necesario.
    Puede tener múltiples líneas.
    
    Args:
        param1 (int): Descripción del primer parámetro.
        param2 (str): Descripción del segundo parámetro.
        
    Returns:
        bool: Descripción del valor de retorno.
        
    Raises:
        ValueError: Si param1 es negativo.
        
    Example:
        >>> result = function_with_types_in_docstring(5, "test")
        >>> print(result)
        True
    """
    pass
```

---

## 🎯 Áreas de Contribución

### Por Fase del Proyecto

#### PHASE 0 - Fundación (Actual)
- Documentación
- Issue templates
- Estructura del proyecto
- Tests iniciales

#### PHASE 1 - Percepción
- Integración de cámara
- Detección con YOLO/MobileNet
- Visualización en tiempo real

#### PHASE 2+ - Features Avanzadas
- Sistema de memoria
- Embeddings vectoriales
- SLAM y mapeo
- Integración con LLMs

### Por Expertise

- **🐍 Python/Backend:** Core del sistema, detección, memoria
- **🎨 Frontend/UI:** Visualizadores, dashboards
- **🤖 Hardware:** ESP32-CAM, Jetson, RPi
- **📚 Docs:** Tutoriales, guías, traducciones
- **🧪 Testing:** Unit tests, integration tests
- **🎓 Educación:** Cursos, labs, ejemplos

---

## 📚 Recursos

### Documentación
- [Wiki del Proyecto](https://github.com/Blackmvmba88/Recogning/wiki)
- [Roadmap Completo](README.md#-roadmap)
- [Issues](https://github.com/Blackmvmba88/Recogning/issues)

### Guías de Referencia
- [PEP 8 - Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/)

---

## ❓ Preguntas

¿Tienes preguntas? Puedes:

1. Abrir un [Discussion](https://github.com/Blackmvmba88/Recogning/discussions)
2. Crear un [Issue](https://github.com/Blackmvmba88/Recogning/issues)
3. Revisar la [Wiki](https://github.com/Blackmvmba88/Recogning/wiki)

---

## 🙏 Agradecimientos

Gracias por contribuir a **Recogning**. Cada contribución, por pequeña que sea, nos acerca más a crear un estándar latinoamericano de percepción visual viva.

**¡Juntos estamos criando un ser digital que aprende a ver el mundo!** 🌱🧠📷

---

<div align="center">

**Happy Coding!** 💻✨

[Volver al README](README.md) | [Ver Issues](https://github.com/Blackmvmba88/Recogning/issues)

</div>
