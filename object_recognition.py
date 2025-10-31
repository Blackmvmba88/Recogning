#!/usr/bin/env python3
"""
Sistema de Reconocimiento de Objetos con KNN
Captura, entrena y clasifica imágenes desde la webcam usando K-Nearest Neighbors
"""

import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
import pickle


class ObjectRecognitionSystem:
    """Sistema de reconocimiento de objetos usando KNN"""
    
    def __init__(self, dataset_path="dataset", model_path="model.pkl"):
        """
        Inicializa el sistema de reconocimiento
        
        Args:
            dataset_path: Ruta donde se guardan las imágenes de entrenamiento
            model_path: Ruta donde se guarda el modelo entrenado
        """
        self.dataset_path = dataset_path
        self.model_path = model_path
        self.knn = None
        self.class_names = []
        self.training_data = []
        self.training_labels = []
        
        # Crear directorio de dataset si no existe
        if not os.path.exists(self.dataset_path):
            os.makedirs(self.dataset_path)
        
        # Configuración de captura de video
        self.cap = None
        self.img_size = (64, 64)  # Tamaño de imagen para procesamiento
        
        # Variables de estado
        self.mode = "capture"  # Modos: capture, train, predict
        self.current_class = ""
        self.sample_count = 0
        
    def start_camera(self):
        """Inicia la captura de video desde la webcam"""
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise Exception("No se pudo abrir la webcam")
        print("Webcam iniciada correctamente")
        
    def stop_camera(self):
        """Detiene la captura de video"""
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        
    def preprocess_image(self, frame):
        """
        Preprocesa una imagen para el clasificador
        
        Args:
            frame: Frame capturado de la webcam
            
        Returns:
            Array numpy con la imagen procesada y aplanada
        """
        # Redimensionar
        img = cv2.resize(frame, self.img_size)
        # Convertir a escala de grises
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Normalizar
        img = img / 255.0
        # Aplanar
        return img.flatten()
        
    def capture_sample(self, frame, class_name):
        """
        Captura y guarda una muestra de entrenamiento
        
        Args:
            frame: Frame de la webcam
            class_name: Nombre de la clase del objeto
        """
        # Crear directorio para la clase si no existe
        class_path = os.path.join(self.dataset_path, class_name)
        if not os.path.exists(class_path):
            os.makedirs(class_path)
        
        # Contar muestras existentes
        existing_samples = len([f for f in os.listdir(class_path) if f.endswith('.jpg')])
        
        # Guardar imagen
        filename = f"{class_name}_{existing_samples + 1}.jpg"
        filepath = os.path.join(class_path, filename)
        cv2.imwrite(filepath, frame)
        
        self.sample_count += 1
        print(f"Muestra capturada: {filename} (Total: {self.sample_count})")
        
    def load_dataset(self):
        """Carga el dataset desde el directorio de imágenes"""
        self.training_data = []
        self.training_labels = []
        self.class_names = []
        
        if not os.path.exists(self.dataset_path):
            print("No se encontró el dataset")
            return False
        
        # Obtener clases (subdirectorios)
        classes = [d for d in os.listdir(self.dataset_path) 
                  if os.path.isdir(os.path.join(self.dataset_path, d))]
        
        if len(classes) == 0:
            print("No se encontraron clases en el dataset")
            return False
        
        self.class_names = sorted(classes)
        
        # Cargar imágenes de cada clase
        for class_idx, class_name in enumerate(self.class_names):
            class_path = os.path.join(self.dataset_path, class_name)
            images = [f for f in os.listdir(class_path) if f.endswith('.jpg') or f.endswith('.png')]
            
            for img_name in images:
                img_path = os.path.join(class_path, img_name)
                img = cv2.imread(img_path)
                if img is not None:
                    processed = self.preprocess_image(img)
                    self.training_data.append(processed)
                    self.training_labels.append(class_idx)
        
        print(f"Dataset cargado: {len(self.training_data)} muestras de {len(self.class_names)} clases")
        print(f"Clases: {', '.join(self.class_names)}")
        return True
        
    def train_model(self):
        """Entrena el modelo KNN con el dataset cargado"""
        if len(self.training_data) == 0:
            print("No hay datos de entrenamiento")
            return False
        
        # Crear y entrenar clasificador KNN
        n_neighbors = min(5, len(self.training_data))
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        
        X = np.array(self.training_data)
        y = np.array(self.training_labels)
        
        self.knn.fit(X, y)
        print(f"Modelo KNN entrenado con {len(X)} muestras")
        
        # Guardar modelo
        self.save_model()
        return True
        
    def save_model(self):
        """Guarda el modelo entrenado en disco"""
        model_data = {
            'knn': self.knn,
            'class_names': self.class_names
        }
        with open(self.model_path, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Modelo guardado en {self.model_path}")
        
    def load_model(self):
        """Carga el modelo entrenado desde disco"""
        if not os.path.exists(self.model_path):
            print("No se encontró el modelo guardado")
            return False
        
        with open(self.model_path, 'rb') as f:
            model_data = pickle.load(f)
            self.knn = model_data['knn']
            self.class_names = model_data['class_names']
        
        print(f"Modelo cargado: {len(self.class_names)} clases")
        return True
        
    def predict(self, frame):
        """
        Predice la clase de un objeto en el frame
        
        Args:
            frame: Frame de la webcam
            
        Returns:
            Tupla (clase_nombre, probabilidad)
        """
        if self.knn is None:
            return None, 0.0
        
        processed = self.preprocess_image(frame)
        processed = processed.reshape(1, -1)
        
        # Predicción
        prediction = self.knn.predict(processed)[0]
        
        # Obtener probabilidades (basadas en vecinos más cercanos)
        distances, indices = self.knn.kneighbors(processed)
        # Convertir distancia a confianza (inversa de la distancia promedio)
        avg_distance = np.mean(distances)
        confidence = 1.0 / (1.0 + avg_distance)
        
        class_name = self.class_names[prediction]
        return class_name, confidence
        
    def run(self):
        """Ejecuta el sistema de reconocimiento en modo interactivo"""
        self.start_camera()
        
        print("\n=== Sistema de Reconocimiento de Objetos ===")
        print("\nControles:")
        print("  'c' - Modo captura: capturar muestras para entrenamiento")
        print("  't' - Entrenar modelo con las muestras capturadas")
        print("  'p' - Modo predicción: reconocer objetos en tiempo real")
        print("  'l' - Cargar modelo guardado")
        print("  ESPACIO - Capturar muestra (en modo captura)")
        print("  'q' - Salir")
        print("\nModo actual: CAPTURA")
        
        self.mode = "capture"
        
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error al capturar frame")
                break
            
            # Voltear horizontalmente para efecto espejo
            frame = cv2.flip(frame, 1)
            display_frame = frame.copy()
            
            # Dibujar información en pantalla
            if self.mode == "capture":
                cv2.putText(display_frame, f"MODO: CAPTURA - Clase: {self.current_class}", 
                           (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                cv2.putText(display_frame, f"Muestras capturadas: {self.sample_count}", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                cv2.putText(display_frame, "Presiona ESPACIO para capturar", 
                           (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                
            elif self.mode == "predict":
                if self.knn is not None:
                    # Realizar predicción
                    class_name, confidence = self.predict(frame)
                    
                    # Mostrar resultado
                    text = f"Objeto: {class_name} ({confidence:.2%})"
                    cv2.putText(display_frame, text, 
                               (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
                else:
                    cv2.putText(display_frame, "MODELO NO ENTRENADO", 
                               (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                
                cv2.putText(display_frame, "MODO: PREDICCION", 
                           (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
            
            # Mostrar frame
            cv2.imshow('Reconocimiento de Objetos', display_frame)
            
            # Procesar teclas
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord('q'):
                print("\nSaliendo...")
                break
                
            elif key == ord('c'):
                self.mode = "capture"
                class_name = input("\nIngrese el nombre de la clase a capturar: ")
                self.current_class = class_name
                self.sample_count = 0
                print(f"Modo CAPTURA activado para clase: {class_name}")
                print("Presiona ESPACIO para capturar muestras")
                
            elif key == ord(' ') and self.mode == "capture":
                if self.current_class:
                    self.capture_sample(frame, self.current_class)
                else:
                    print("Por favor, ingrese un nombre de clase primero (presione 'c')")
                    
            elif key == ord('t'):
                print("\nEntrenando modelo...")
                if self.load_dataset():
                    if self.train_model():
                        print("¡Entrenamiento completado!")
                    else:
                        print("Error al entrenar el modelo")
                else:
                    print("No se pudo cargar el dataset")
                    
            elif key == ord('p'):
                print("\nCambiando a modo PREDICCIÓN")
                if self.knn is None:
                    print("Cargando modelo...")
                    if not self.load_model():
                        print("No hay modelo entrenado. Entrene primero el modelo (presione 't')")
                        continue
                self.mode = "predict"
                
            elif key == ord('l'):
                print("\nCargando modelo guardado...")
                if self.load_model():
                    print("Modelo cargado exitosamente")
                else:
                    print("No se pudo cargar el modelo")
        
        self.stop_camera()
        print("Sistema finalizado")


def main():
    """Función principal"""
    system = ObjectRecognitionSystem()
    system.run()


if __name__ == "__main__":
    main()
