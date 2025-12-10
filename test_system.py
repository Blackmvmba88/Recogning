#!/usr/bin/env python3
"""
Test script para validar el sistema de reconocimiento de objetos
"""

import numpy as np
import cv2
import os
import shutil
from object_recognition import ObjectRecognitionSystem


def create_test_dataset():
    """Crea un dataset sintético para pruebas"""
    print("Creando dataset de prueba...")
    
    test_dataset = "test_dataset"
    
    # Limpiar dataset anterior si existe
    if os.path.exists(test_dataset):
        shutil.rmtree(test_dataset)
    
    os.makedirs(test_dataset)
    
    # Crear 3 clases con patrones diferentes
    classes = {
        "circulo": lambda: create_circle_image(),
        "cuadrado": lambda: create_square_image(),
        "triangulo": lambda: create_triangle_image()
    }
    
    # Generar 15 muestras por clase
    for class_name, generator in classes.items():
        class_path = os.path.join(test_dataset, class_name)
        os.makedirs(class_path)
        
        for i in range(15):
            img = generator()
            filepath = os.path.join(class_path, f"{class_name}_{i+1}.jpg")
            cv2.imwrite(filepath, img)
        
        print(f"  ✓ Clase '{class_name}': 15 muestras creadas")
    
    return test_dataset


def create_circle_image():
    """Crea imagen con círculo"""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    center = (50, 50)
    radius = 30 + np.random.randint(-5, 5)
    color = (255, 255, 255)
    cv2.circle(img, center, radius, color, -1)
    # Agregar ruido
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    img = cv2.add(img, noise)
    return img


def create_square_image():
    """Crea imagen con cuadrado"""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    size = 40 + np.random.randint(-5, 5)
    pt1 = (50 - size//2, 50 - size//2)
    pt2 = (50 + size//2, 50 + size//2)
    color = (255, 255, 255)
    cv2.rectangle(img, pt1, pt2, color, -1)
    # Agregar ruido
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    img = cv2.add(img, noise)
    return img


def create_triangle_image():
    """Crea imagen con triángulo"""
    img = np.zeros((100, 100, 3), dtype=np.uint8)
    pts = np.array([
        [50, 20 + np.random.randint(-3, 3)],
        [30 + np.random.randint(-3, 3), 70],
        [70 + np.random.randint(-3, 3), 70]
    ], np.int32)
    pts = pts.reshape((-1, 1, 2))
    color = (255, 255, 255)
    cv2.fillPoly(img, [pts], color)
    # Agregar ruido
    noise = np.random.randint(0, 50, img.shape, dtype=np.uint8)
    img = cv2.add(img, noise)
    return img


def test_training_and_prediction():
    """Prueba el ciclo completo de entrenamiento y predicción"""
    print("\n=== Prueba de Entrenamiento y Predicción ===\n")
    
    # Crear dataset de prueba
    test_dataset = create_test_dataset()
    
    # Crear sistema con dataset de prueba
    system = ObjectRecognitionSystem(
        dataset_path=test_dataset,
        model_path="test_model.pkl"
    )
    
    # Cargar dataset
    print("\nCargando dataset...")
    success = system.load_dataset()
    assert success, "Error al cargar dataset"
    print(f"  ✓ Dataset cargado: {len(system.training_data)} muestras")
    print(f"  ✓ Clases: {system.class_names}")
    
    # Entrenar modelo
    print("\nEntrenando modelo...")
    success = system.train_model()
    assert success, "Error al entrenar modelo"
    print("  ✓ Modelo entrenado exitosamente")
    
    # Verificar que el modelo se guardó
    assert os.path.exists("test_model.pkl"), "Modelo no se guardó"
    print("  ✓ Modelo guardado en disco")
    
    # Probar predicciones
    print("\nProbando predicciones...")
    test_images = {
        "circulo": create_circle_image(),
        "cuadrado": create_square_image(),
        "triangulo": create_triangle_image()
    }
    
    correct = 0
    total = len(test_images)
    
    for expected_class, test_img in test_images.items():
        predicted_class, confidence = system.predict(test_img)
        
        is_correct = predicted_class == expected_class
        if is_correct:
            correct += 1
        
        status = "✓" if is_correct else "✗"
        print(f"  {status} Esperado: {expected_class}, Predicho: {predicted_class} ({confidence:.2%})")
    
    accuracy = correct / total * 100
    print(f"\n  Precisión: {accuracy:.1f}% ({correct}/{total})")
    
    # Probar carga del modelo
    print("\nProbando carga del modelo...")
    new_system = ObjectRecognitionSystem(
        dataset_path=test_dataset,
        model_path="test_model.pkl"
    )
    success = new_system.load_model()
    assert success, "Error al cargar modelo"
    print("  ✓ Modelo cargado exitosamente")
    
    # Verificar que el modelo cargado funciona
    test_img = create_circle_image()
    predicted_class, confidence = new_system.predict(test_img)
    print(f"  ✓ Predicción con modelo cargado: {predicted_class} ({confidence:.2%})")
    
    # Limpiar archivos de prueba
    print("\nLimpiando archivos de prueba...")
    shutil.rmtree(test_dataset)
    os.remove("test_model.pkl")
    print("  ✓ Archivos de prueba eliminados")
    
    print("\n✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
    return True


def test_edge_cases():
    """Prueba casos límite"""
    print("\n=== Prueba de Casos Límite ===\n")
    
    system = ObjectRecognitionSystem(
        dataset_path="nonexistent_dataset",
        model_path="nonexistent_model.pkl"
    )
    
    # Intentar cargar dataset inexistente
    print("Probando carga de dataset inexistente...")
    result = system.load_dataset()
    assert result is False, "Debería retornar False para dataset inexistente"
    print("  ✓ Manejo correcto de dataset inexistente")
    
    # Intentar cargar modelo inexistente
    print("\nProbando carga de modelo inexistente...")
    result = system.load_model()
    assert result is False, "Debería retornar False para modelo inexistente"
    print("  ✓ Manejo correcto de modelo inexistente")
    
    # Intentar entrenar sin datos
    print("\nProbando entrenamiento sin datos...")
    result = system.train_model()
    assert result is False, "Debería retornar False sin datos de entrenamiento"
    print("  ✓ Manejo correcto de entrenamiento sin datos")
    
    # Intentar predicción sin modelo
    print("\nProbando predicción sin modelo...")
    test_img = np.zeros((100, 100, 3), dtype=np.uint8)
    predicted_class, confidence = system.predict(test_img)
    assert predicted_class is None, "Debería retornar None sin modelo"
    print("  ✓ Manejo correcto de predicción sin modelo")
    
    print("\n✅ TODOS LOS CASOS LÍMITE MANEJADOS CORRECTAMENTE")
    return True


if __name__ == "__main__":
    print("=" * 60)
    print("SISTEMA DE RECONOCIMIENTO DE OBJETOS - SUITE DE PRUEBAS")
    print("=" * 60)
    
    try:
        # Ejecutar pruebas
        test_training_and_prediction()
        test_edge_cases()
        
        print("\n" + "=" * 60)
        print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR EN LAS PRUEBAS: {e}")
        import traceback
        traceback.print_exc()
        exit(1)
