#!/usr/bin/env python3
"""
Sistema Simple de Reconocimiento de Objetos
Versión simplificada con menú interactivo en español
"""

import cv2
import os
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# --- Configuración inicial ---
DATA_DIR = "dataset_mamba"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# --- Inicializar webcam ---
cap = cv2.VideoCapture(0)
model = None
labels = []
features = []

def capture_object(name):
    """Captura ejemplos de un objeto para entrenamiento"""
    path = os.path.join(DATA_DIR, name)
    os.makedirs(path, exist_ok=True)
    print(f"Grabando ejemplos para '{name}'...")
    print("Presiona 'q' para detener la captura antes de tiempo")
    count = 0
    while count < 30:
        ret, frame = cap.read()
        if not ret:
            break
        # Voltear para efecto espejo
        frame = cv2.flip(frame, 1)
        # Mostrar contador
        cv2.putText(frame, f"Capturando: {count + 1}/30", 
                   (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Entrenando...", frame)
        cv2.imwrite(os.path.join(path, f"{count}.jpg"), frame)
        count += 1
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    cv2.destroyWindow("Entrenando...")
    print(f"✓ {count} ejemplos capturados para '{name}'")

def train_model():
    """Entrena el modelo KNN con los ejemplos capturados"""
    global model, labels, features
    labels, features = [], []
    
    if not os.path.exists(DATA_DIR) or len(os.listdir(DATA_DIR)) == 0:
        print("❌ No hay objetos para entrenar. Primero enseña algunos objetos (Opción 1)")
        return
    
    print("\nEntrenando modelo...")
    for label in os.listdir(DATA_DIR):
        label_path = os.path.join(DATA_DIR, label)
        if not os.path.isdir(label_path):
            continue
        img_files = [f for f in os.listdir(label_path) if f.endswith('.jpg')]
        for img_name in img_files:
            img_path = os.path.join(label_path, img_name)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is not None:
                img = cv2.resize(img, (64, 64)).flatten()
                features.append(img)
                labels.append(label)
    
    if len(features) == 0:
        print("❌ No se encontraron imágenes válidas")
        return
    
    n_neighbors = min(3, len(features))
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(features, labels)
    
    # Mostrar resumen
    unique_labels = set(labels)
    print(f"✓ Modelo entrenado con éxito")
    print(f"  - {len(features)} ejemplos")
    print(f"  - {len(unique_labels)} objetos: {', '.join(sorted(unique_labels))}")

def recognize():
    """Reconoce objetos en tiempo real"""
    if model is None:
        print("❌ Primero entrena el modelo (Opción 2)")
        return
    
    print("\nReconociendo objetos en tiempo real...")
    print("Presiona 'q' para salir")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Voltear para efecto espejo
        frame = cv2.flip(frame, 1)
        
        # Preparar imagen para predicción
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = cv2.resize(gray, (64, 64)).flatten().reshape(1, -1)
        
        # Predecir
        pred = model.predict(img)[0]
        
        # Calcular confianza (distancia a vecinos más cercanos)
        distances, _ = model.kneighbors(img)
        confidence = 1.0 / (1.0 + np.mean(distances))
        
        # Mostrar resultado
        cv2.putText(frame, f"Objeto: {pred}", 
                   (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(frame, f"Confianza: {confidence:.2%}", 
                   (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        
        cv2.imshow("Reconocimiento", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.destroyWindow("Reconocimiento")

def show_menu():
    """Muestra el menú principal"""
    print("\n" + "="*50)
    print("  SISTEMA DE RECONOCIMIENTO DE OBJETOS")
    print("="*50)
    print("\nOpciones:")
    print("  1. Enseñar nuevo objeto")
    print("  2. Entrenar modelo")
    print("  3. Reconocer en tiempo real")
    print("  4. Ver objetos aprendidos")
    print("  5. Salir")
    print("-"*50)

# --- Flujo principal ---
def main():
    """Función principal del programa"""
    print("\n¡Bienvenido al Sistema de Reconocimiento de Objetos!")
    
    while True:
        show_menu()
        opt = input("Selecciona una opción (1-5): ").strip()
        
        if opt == "1":
            name = input("\nNombre del objeto: ").strip()
            if name:
                capture_object(name)
            else:
                print("❌ Nombre inválido")
                
        elif opt == "2":
            train_model()
            
        elif opt == "3":
            recognize()
            
        elif opt == "4":
            if os.path.exists(DATA_DIR):
                objects = [d for d in os.listdir(DATA_DIR) 
                          if os.path.isdir(os.path.join(DATA_DIR, d))]
                if objects:
                    print("\n📚 Objetos aprendidos:")
                    for obj in sorted(objects):
                        obj_path = os.path.join(DATA_DIR, obj)
                        count = len([f for f in os.listdir(obj_path) if f.endswith('.jpg')])
                        print(f"  - {obj}: {count} ejemplos")
                else:
                    print("\n❌ No hay objetos aprendidos aún")
            else:
                print("\n❌ No hay objetos aprendidos aún")
                
        elif opt == "5":
            print("\n¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción inválida. Por favor selecciona 1-5")
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
