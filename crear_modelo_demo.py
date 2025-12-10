#!/usr/bin/env python3
"""
Script para crear un modelo de demostración con objetos básicos
Útil para no empezar desde cero

Creates a demo model with basic objects
Useful for not starting from scratch
"""

import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
import joblib

def create_synthetic_object_samples(object_name, samples=20, output_dir="dataset_demo"):
    """
    Crea muestras sintéticas de un objeto para demostración
    Creates synthetic samples of an object for demonstration
    """
    path = os.path.join(output_dir, object_name)
    os.makedirs(path, exist_ok=True)
    
    print(f"Creando {samples} muestras sintéticas de '{object_name}'...")
    print(f"Creating {samples} synthetic samples of '{object_name}'...")
    
    for i in range(samples):
        # Crear imagen base 640x480 (tamaño webcam típico)
        img = np.random.randint(180, 220, (480, 640, 3), dtype=np.uint8)
        
        # Añadir patrón único según el objeto
        if object_name == "circulo":
            # Dibujar círculo
            center = (320 + np.random.randint(-50, 50), 240 + np.random.randint(-50, 50))
            radius = 80 + np.random.randint(-20, 20)
            color = (np.random.randint(50, 100), np.random.randint(100, 200), np.random.randint(100, 200))
            cv2.circle(img, center, radius, color, -1)
            
        elif object_name == "cuadrado":
            # Dibujar cuadrado
            size = 120 + np.random.randint(-30, 30)
            x = 320 - size//2 + np.random.randint(-40, 40)
            y = 240 - size//2 + np.random.randint(-40, 40)
            color = (np.random.randint(100, 200), np.random.randint(50, 100), np.random.randint(100, 200))
            cv2.rectangle(img, (x, y), (x+size, y+size), color, -1)
            
        elif object_name == "triangulo":
            # Dibujar triángulo
            pts = np.array([
                [320 + np.random.randint(-30, 30), 160 + np.random.randint(-20, 20)],
                [240 + np.random.randint(-30, 30), 320 + np.random.randint(-20, 20)],
                [400 + np.random.randint(-30, 30), 320 + np.random.randint(-20, 20)]
            ], np.int32)
            color = (np.random.randint(100, 200), np.random.randint(100, 200), np.random.randint(50, 100))
            cv2.fillPoly(img, [pts], color)
            
        elif object_name == "estrella":
            # Dibujar estrella (pentágono con puntas)
            center = (320, 240)
            radius = 100
            points = []
            for j in range(10):
                angle = j * np.pi / 5 - np.pi / 2
                r = radius if j % 2 == 0 else radius // 2
                x = int(center[0] + r * np.cos(angle))
                y = int(center[1] + r * np.sin(angle))
                points.append([x, y])
            pts = np.array(points, np.int32)
            color = (np.random.randint(150, 255), np.random.randint(150, 255), np.random.randint(50, 150))
            cv2.fillPoly(img, [pts], color)
            
        elif object_name == "linea":
            # Dibujar líneas
            for _ in range(3):
                x1 = np.random.randint(100, 500)
                y1 = np.random.randint(100, 400)
                x2 = np.random.randint(100, 500)
                y2 = np.random.randint(100, 400)
                color = (np.random.randint(50, 150), np.random.randint(50, 150), np.random.randint(100, 200))
                cv2.line(img, (x1, y1), (x2, y2), color, np.random.randint(5, 15))
        
        # Añadir ruido para variación
        noise = np.random.randint(-20, 20, img.shape, dtype=np.int16)
        img = np.clip(img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
        
        # Guardar imagen
        filename = os.path.join(path, f"{object_name}_{i}.jpg")
        cv2.imwrite(filename, img)
    
    print(f"  ✓ {samples} muestras guardadas en {path}")
    print(f"  ✓ {samples} samples saved in {path}")

def create_demo_dataset():
    """
    Crea un dataset de demostración completo con varios objetos
    Creates a complete demo dataset with various objects
    """
    print("\n" + "="*60)
    print("CREANDO DATASET DE DEMOSTRACIÓN")
    print("CREATING DEMO DATASET")
    print("="*60 + "\n")
    
    # Limpiar dataset anterior si existe
    output_dir = "dataset_demo"
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # Crear objetos de demostración
    demo_objects = ["circulo", "cuadrado", "triangulo", "estrella", "linea"]
    
    for obj in demo_objects:
        create_synthetic_object_samples(obj, samples=25, output_dir=output_dir)
    
    print(f"\n✅ Dataset de demostración creado en '{output_dir}/'")
    print(f"✅ Demo dataset created in '{output_dir}/'")
    print(f"   Total: {len(demo_objects)} objetos, 125 muestras")
    print(f"   Total: {len(demo_objects)} objects, 125 samples")
    
    return output_dir

def train_demo_model(dataset_dir="dataset_demo"):
    """
    Entrena un modelo KNN con el dataset de demostración
    Trains a KNN model with the demo dataset
    """
    print("\n" + "="*60)
    print("ENTRENANDO MODELO DE DEMOSTRACIÓN")
    print("TRAINING DEMO MODEL")
    print("="*60 + "\n")
    
    if not os.path.exists(dataset_dir):
        print(f"❌ Error: Dataset '{dataset_dir}' no existe")
        print(f"❌ Error: Dataset '{dataset_dir}' doesn't exist")
        return None
    
    labels = []
    features = []
    
    # Cargar todas las imágenes
    print("Cargando imágenes... / Loading images...")
    for label in os.listdir(dataset_dir):
        label_path = os.path.join(dataset_dir, label)
        if not os.path.isdir(label_path):
            continue
        
        img_files = [f for f in os.listdir(label_path) if f.endswith('.jpg')]
        print(f"  - {label}: {len(img_files)} muestras")
        
        for img_name in img_files:
            img_path = os.path.join(label_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (64, 64))
                img = img.flatten() / 255.0  # Normalizar
                features.append(img)
                labels.append(label)
    
    # Entrenar modelo
    print(f"\nEntrenando KNN con {len(features)} muestras...")
    print(f"Training KNN with {len(features)} samples...")
    
    n_neighbors = min(5, len(features))
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(features, labels)
    
    # Guardar modelo
    model_data = {
        'knn': model,
        'class_names': sorted(list(set(labels)))
    }
    
    model_path = "modelo_demo.pkl"
    joblib.dump(model_data, model_path)
    
    print(f"\n✅ Modelo guardado en '{model_path}'")
    print(f"✅ Model saved in '{model_path}'")
    print(f"   Clases: {', '.join(model_data['class_names'])}")
    print(f"   Classes: {', '.join(model_data['class_names'])}")
    
    return model_path

def create_usage_example():
    """
    Crea un script de ejemplo para usar el modelo demo
    Creates an example script to use the demo model
    """
    example_code = '''#!/usr/bin/env python3
"""
Ejemplo de uso del modelo de demostración
Example using the demo model
"""

from object_recognition import ObjectRecognitionSystem

# Crear sistema con modelo demo
system = ObjectRecognitionSystem(
    dataset_path="dataset_demo",
    model_path="modelo_demo.pkl"
)

# Cargar modelo pre-entrenado
if system.load_model():
    print("✓ Modelo demo cargado / Demo model loaded")
    print(f"✓ Objetos reconocidos: {', '.join(system.class_names)}")
    
    # Ahora puedes usar el sistema directamente
    system.run()  # Inicia interfaz interactiva
else:
    print("❌ Error cargando modelo demo")
    print("   Ejecuta: python crear_modelo_demo.py")
'''
    
    with open("ejemplo_modelo_demo.py", "w", encoding="utf-8") as f:
        f.write(example_code)
    
    print(f"\n✅ Ejemplo creado en 'ejemplo_modelo_demo.py'")
    print(f"✅ Example created in 'ejemplo_modelo_demo.py'")

def main():
    """Función principal"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║  CREADOR DE MODELO DE DEMOSTRACIÓN                      ║")
    print("║  DEMO MODEL CREATOR                                      ║")
    print("╚" + "="*58 + "╝\n")
    
    print("Este script crea un modelo pre-entrenado con objetos básicos")
    print("para que no tengas que empezar desde cero.")
    print("\nThis script creates a pre-trained model with basic objects")
    print("so you don't have to start from scratch.\n")
    
    # Crear dataset demo
    dataset_dir = create_demo_dataset()
    
    # Entrenar modelo demo
    model_path = train_demo_model(dataset_dir)
    
    if model_path:
        # Crear ejemplo de uso
        create_usage_example()
        
        print("\n" + "="*60)
        print("✅ ¡LISTO! / READY!")
        print("="*60)
        print("\n📦 Archivos creados / Files created:")
        print("   • dataset_demo/      - Dataset con 5 objetos")
        print("   • modelo_demo.pkl    - Modelo KNN pre-entrenado")
        print("   • ejemplo_modelo_demo.py - Script de ejemplo")
        
        print("\n🚀 Para usar el modelo demo / To use the demo model:")
        print("   python ejemplo_modelo_demo.py")
        
        print("\n💡 O puedes cargar el modelo en cualquier script:")
        print("   Or you can load the model in any script:")
        print("   from object_recognition import ObjectRecognitionSystem")
        print("   system = ObjectRecognitionSystem(")
        print("       dataset_path='dataset_demo',")
        print("       model_path='modelo_demo.pkl'")
        print("   )")
        print("   system.load_model()")
        print("   system.run()")
        
        print("\n" + "="*60)

if __name__ == "__main__":
    main()
