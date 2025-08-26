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