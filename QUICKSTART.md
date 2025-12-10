# Guía de Inicio Rápido - Recogning

**[Español](#español) | [English](QUICKSTART_EN.md)**

Esta guía te ayudará a poner en marcha el sistema de reconocimiento de objetos en 5 minutos.

## 📋 Pre-requisitos

- Python 3.7+
- Webcam
- 5 minutos de tu tiempo

## 🚀 Instalación Rápida

```bash
# Clonar el repositorio
git clone https://github.com/Blackmvmba88/Recogning.git
cd Recogning

# Instalar dependencias
pip install -r requirements.txt
```

## 🎯 Tutorial Básico

### Opción 0: ¡Prueba Instantánea! (Modelo Demo)

¿Quieres probar el sistema **sin capturar imágenes**?

```bash
# Crear modelo de demostración (solo una vez)
python crear_modelo_demo.py

# Usar el modelo demo
python ejemplo_modelo_demo.py
```

¡Listo! El sistema ya reconoce 5 objetos básicos (círculo, cuadrado, triángulo, estrella, línea).

### Opción 1: Versión Simple (Recomendada)

```bash
python reconocimiento_simple.py
```

**Sigue el menú:**
1. Selecciona opción **1** para enseñar un objeto nuevo
2. Ingresa el nombre del objeto (ej: "taza")
3. Posiciona el objeto frente a la cámara
4. Se capturarán 30 muestras automáticamente
5. Repite para 2-3 objetos diferentes
6. Selecciona opción **2** para entrenar el modelo
7. Selecciona opción **3** para ver reconocimiento en tiempo real!

### Opción 2: Versión Avanzada

```bash
python object_recognition.py
```

### Paso 2: Capturar Muestras (2 minutos)

1. **Presiona `c`** para entrar en modo captura
2. **Escribe** el nombre de un objeto (ej: "taza")
3. **Posiciona** el objeto frente a la cámara
4. **Presiona ESPACIO** 10-15 veces para capturar muestras desde diferentes ángulos

Repite para 2-3 objetos diferentes (ej: "libro", "celular")

### Paso 3: Entrenar el Modelo (30 segundos)

**Presiona `t`** para entrenar el modelo con las muestras capturadas

### Paso 4: ¡Reconocer Objetos! (tiempo real)

**Presiona `p`** para entrar en modo predicción y muestra objetos frente a la cámara

## 💡 Consejos para Mejores Resultados

### Durante la Captura:
- ✅ Captura 15-20 muestras por objeto
- ✅ Varía el ángulo y la distancia
- ✅ Mantén buena iluminación
- ✅ Usa fondos simples y consistentes

### Para Mejor Precisión:
- ✅ Objetos visualmente distintos
- ✅ Más muestras = mejor precisión
- ✅ Condiciones similares entre entrenamiento y predicción

## 🔧 Comandos Rápidos

### Menú Versión Simple
| Opción | Acción |
|--------|--------|
| `1` | Enseñar Nuevo Objeto |
| `2` | Entrenar Modelo |
| `3` | Reconocer en Tiempo Real |
| `4` | Ver Objetos Aprendidos |
| `5` | Salir |

### Teclas Versión Avanzada
| Tecla | Acción |
|-------|--------|
| `c` | Modo Captura |
| `ESPACIO` | Capturar Muestra |
| `t` | Entrenar Modelo |
| `p` | Modo Predicción |
| `l` | Cargar Modelo |
| `q` | Salir |

## 📊 Ejemplo Completo

### Usando Versión Simple:
```bash
# 1. Iniciar
python reconocimiento_simple.py

# 2. En el programa:
# - Selecciona 1, ingresa "taza", espera 30 capturas
# - Selecciona 1, ingresa "libro", espera 30 capturas
# - Selecciona 1, ingresa "celular", espera 30 capturas
# - Selecciona 2 para entrenar
# - Selecciona 3 para ver reconocimiento en tiempo real
# - Selecciona 5 para salir
```

### Usando Versión Avanzada:
```bash
# 1. Iniciar
python object_recognition.py

# 2. En el programa:
# - Presiona 'c', escribe "taza", captura 15 muestras con ESPACIO
# - Presiona 'c', escribe "libro", captura 15 muestras con ESPACIO
# - Presiona 'c', escribe "celular", captura 15 muestras con ESPACIO
# - Presiona 't' para entrenar
# - Presiona 'p' para ver reconocimiento en tiempo real
# - Presiona 'q' para salir
```

## 🎓 Próximos Pasos

1. **Lee el README completo** para funcionalidades avanzadas
2. **Prueba example_usage.py** para uso programático
3. **Experimenta** con diferentes objetos y configuraciones
4. **Comparte** tus resultados

## ❓ Problemas Comunes

**La cámara no funciona:**
- Verifica que está conectada
- Cierra otras aplicaciones que usen la cámara
- Verifica permisos de acceso

**Las predicciones son incorrectas:**
- Captura más muestras (20-30 por objeto)
- Mejora la iluminación
- Usa objetos más distintos visualmente

**Error al importar módulos:**
- Ejecuta: `pip install -r requirements.txt`

## 🎉 ¡Listo!

Ahora tienes un sistema funcional de reconocimiento de objetos. ¡Diviértete enseñándole a reconocer el mundo!

---

**¿Necesitas más ayuda?** Consulta el [README completo](README.md)
