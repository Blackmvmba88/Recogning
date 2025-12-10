#!/usr/bin/env python3
"""
Ejemplo de Uso del Sistema de Reconocimiento de Objetos

Este script demuestra cómo usar programáticamente el sistema
de reconocimiento de objetos sin la interfaz interactiva.
"""

from object_recognition import ObjectRecognitionSystem
import cv2


def example_capture_and_train():
    """
    Ejemplo 1: Captura de muestras y entrenamiento programático
    """
    print("=== Ejemplo 1: Captura y Entrenamiento ===\n")
    
    # Crear instancia del sistema
    system = ObjectRecognitionSystem()
    
    # Iniciar cámara
    system.start_camera()
    
    print("Este ejemplo capturará automáticamente 10 muestras")
    print("Posiciona el objeto frente a la cámara...\n")
    
    input("Presiona ENTER cuando estés listo para capturar 'laptop'...")
    
    # Capturar 10 muestras de "laptop"
    for i in range(10):
        ret, frame = system.cap.read()
        if ret:
            frame = cv2.flip(frame, 1)
            system.capture_sample(frame, "laptop")
            cv2.imshow("Captura", frame)
            cv2.waitKey(200)  # Pausa entre capturas
    
    print("\n¡Muestras capturadas!")
    
    # Entrenar modelo
    print("\nEntrenando modelo...")
    if system.load_dataset() and system.train_model():
        print("¡Modelo entrenado exitosamente!")
    
    system.stop_camera()


def example_load_and_predict():
    """
    Ejemplo 2: Cargar modelo existente y realizar predicciones
    """
    print("\n=== Ejemplo 2: Predicción con Modelo Existente ===\n")
    
    # Crear instancia del sistema
    system = ObjectRecognitionSystem()
    
    # Cargar modelo previamente entrenado
    if not system.load_model():
        print("Error: No hay modelo entrenado. Ejecute primero el ejemplo 1.")
        return
    
    # Iniciar cámara
    system.start_camera()
    
    print("Mostrando predicciones en tiempo real...")
    print("Presiona 'q' para salir\n")
    
    while True:
        ret, frame = system.cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        
        # Realizar predicción
        class_name, confidence = system.predict(frame)
        
        # Mostrar resultado en el frame
        text = f"Objeto: {class_name} ({confidence:.2%})"
        cv2.putText(frame, text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("Prediccion", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    system.stop_camera()


def example_custom_dataset():
    """
    Ejemplo 3: Trabajar con dataset personalizado
    """
    print("\n=== Ejemplo 3: Dataset Personalizado ===\n")
    
    # Crear sistema con rutas personalizadas
    system = ObjectRecognitionSystem(
        dataset_path="mi_dataset",
        model_path="mi_modelo.pkl"
    )
    
    print(f"Dataset: {system.dataset_path}")
    print(f"Modelo: {system.model_path}")
    
    # Cargar dataset y mostrar estadísticas
    if system.load_dataset():
        print(f"\nClases encontradas: {system.class_names}")
        print(f"Total de muestras: {len(system.training_data)}")
    else:
        print("\nNo se encontró dataset personalizado")


if __name__ == "__main__":
    print("Sistema de Reconocimiento de Objetos - Ejemplos de Uso\n")
    print("1. Captura y entrenamiento")
    print("2. Predicción con modelo existente")
    print("3. Dataset personalizado")
    print("4. Ejecutar sistema interactivo completo")
    
    choice = input("\nSeleccione un ejemplo (1-4) o 'q' para salir: ")
    
    if choice == '1':
        example_capture_and_train()
    elif choice == '2':
        example_load_and_predict()
    elif choice == '3':
        example_custom_dataset()
    elif choice == '4':
        print("\nEjecutando sistema interactivo completo...\n")
        system = ObjectRecognitionSystem()
        system.run()
    else:
        print("Saliendo...")
