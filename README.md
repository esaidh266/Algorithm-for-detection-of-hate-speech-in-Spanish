# Modelo de detección de discursos de odio
Este código implementa un sistema de clasificación de discurso de odio utilizando el modelo RoBERTuito (una versión en español de RoBERTa) para detectar discurso de odio en tuits.


## Arquitectura del Modelo

El modelo se basa en `pysentimiento/robertuito-base-uncased` con las siguientes modificaciones:
- Se añadió una capa de clasificación densa sobre el modelo base.
- Utiliza IDs de entrada y máscaras de atención como entradas.
- Genera una clasificación binaria (odio vs. no odio).

## Datasets

1. **Conjunto de Datos de Preentrenamiento**: Conjunto de datos multilingüe de sentimiento de tuits de Cardiff NLP (parte en español).
- Convertido a clasificación binaria:
- Tweets negativos (etiqueta original 0) → Odio (1).
- Tweets positivos (etiqueta original 2) → No odio (0).
- Tweets neutrales (etiqueta original 1) → No odio (0).


2. **Conjunto de Datos HATEMEDIA**: Conjunto de datos personalizado de discurso de odio.
- Clasificación binaria:
- Odio (1).
- No odio (0).

## Training Process

### Pre-entrenamiento
- Batch size: 16
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2

### Fine-tuning
- Batch size: 128
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2
- Métricas personalizadas:
  - Recall for non-hate class
  - Precision for hate class
  - F1-score (weighted)
  - AUC-PR
  - Recall at precision=0.9 (non-hate)
  - Precision at recall=0.9 (hate)

## Métricas de Evaluación

El modelo se evalúa utilizando:
- Macro recall, precision, and F1-score
- One-vs-Rest AUC
- Accuracy
- Métricas por clase
- Matriz de confusión

## Requerimientos

Se requiere los siguientes paquetes de Python (consulte requirements.txt para ver la lista completa):
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn

## Uso
El modelo espera datos de entrada con las siguientes especificaciones:

1. **Formato de datos**:
- Archivo CSV o DataFrame de Pandas
- Nombre de columna obligatorio: `text` (tipo cadena)
- Nombre de columna opcional: `label` (tipo entero, 0 o 1) si está disponible para la evaluación

2. **Preprocesamiento de texto**:
- El texto se convertirá automáticamente a minúsculas durante el procesamiento
- Longitud máxima: 128 tokens (los textos más largos se truncarán)
- Los caracteres especiales, las URL y los emojis deben permanecer en el texto (el tokenizador los gestiona)

3. **Codificación de etiquetas**:
- `0` = Sin contenido de odio (incluido contenido neutral/positivo)

- `1` = Incitación al odio

------------
# Hate Speech Detection Model
This code implements a hate speech classification system using the RoBERTuito model (a Spanish version of RoBERTa) to detect hate speech in tweets.

## Model Architecture

The model is based on `pysentimiento/robertuito-base-uncased` with the following modifications:
- A dense classification layer has been added over the base model.
- It uses input IDs and attention masks as inputs.
- It generates a binary classification (hate vs. non-hate).

## Datasets

1. **Pre-training Dataset**: Cardiff NLP multilingual tweet sentiment dataset (Spanish part).
- Converted to binary classification:
- Negative tweets (original label 0) → Hate (1).
- Positive tweets (original label 2) → Non-hate (0).
- Neutral tweets (original label 1) → No hate (0).

2. **HATEMEDIA Dataset**: Custom hate speech dataset.
- Binary classification:
- Hate (1).
- No hate (0).

## Training Process

### Pre-workout
- Batch size: 16
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2

### Fine-tuning
- Batch size: 128
- Epochs: 5
- Learning rate: 2e-5 with 10% warmup steps
- Early stopping with patience=2
- Custom metrics: 
- Recall for non-hate class 
- Precision for hate class 
- F1-score (weighted) 
- AUC-PR 
- Recall at precision=0.9 (non-hate) 
- Precision at recall=0.9 (hate)

## Evaluation Metrics

The model is evaluated using:
- Macro recall, precision, and F1-score
- One-vs-Rest AUC
- Accuracy
- Metrics by class
- Confusion matrix

## Requirements

The following Python packages are required (see requirements.txt for the full list):
- TensorFlow
- Transformers
- scikit-learn
- pandas
- datasets
- matplotlib
- seaborn

## Usage
The model expects input data with the following specifications:

1. **Data Format**:
- CSV file or Pandas DataFrame
- Mandatory column name: `text` (type string)
- Optional column name: `label` (type integer, 0 or 1) if available for evaluation

2. **Text Preprocessing**:
- Text will be automatically converted to lowercase during processing
- Maximum length: 128 tokens (longer texts will be truncated)
- Special characters, URLs, and emojis must remain in the text (the tokenizer handles these)

3. **Label Encoding**:
- `0` = No hateful content (including neutral/positive content)

- 1 = Hate speech
