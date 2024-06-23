# Algorithm-for-detection-of-hate-speech-in-Spanish
Algoritmo de detección de expresiones de odio en español. Este algoritmo fue desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/AEI /10.13039/501100011033, con la colaboración de Possible Inc.

Por favor lea el documento README IN SPANISH, en el que se expone todos los pasos a seguir para el uso del algoritmo desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/ AEI /10.13039/501100011033

La estructura de carpetas con la documentación de Github es la presentada a continuación:

        02 Documentación Github
         └── 00_Odio y no odio
             ├── DOCUMENTACIÓN GITHUB.docx
             ├── ejemplo (1).py
             ├── Modelo_binario_ (1) (1).ipynb
             ├── obtener_caracteristicas (1).py
             └── Recursos-20231027T110710Z-001 (1).zip

Se detalla a continuación el contenido de cada fichero:

- DOCUMENTACIÓN GITHUB.docx:
Informe en el que se presenta el uso de los scripts ejemplo (1).py y obtener_caracteristicas (1).py para emplear los modelos.

- ejemplo (1).py:
Script Python que muestra el uso de los modelos para realizar predicciones.

- Modelo_binario_(1) (1).ipnyb:
Notebook con el código utilizado para el entrenamiento de los distintos modelos.

- Obtener_caracteristicas (1).py:
Script Python con las funciones de preprocesado utilizadas previamente al uso de los modelos para predecir las entradas de un dataframe.

- Recursos-20231027T110710Z-001 (1).zip:
La carpeta recursos contiene 3 .csv utilizados en la extracción de características.

El dataset que se ha utilizado para el entrenamiento de los modelos: 
- Said-Hung, Elias; Montero-Diaz, julio; Blanco, Xiomara; Ruiz-Iniesta, Almudena; Pérez Palau, Daniel; De Gregorio Vicente, Oscar; et al. (2024). Dataset usado para entrenamientos de modelos de algoritmos de clasificación de odio, por tipos e intensidades (Dataset used to train hate classification algorithm models by types and intensities). figshare. Dataset. https://doi.org/10.6084/m9.figshare.26085700.v1

El Algoritmo se desarrolló, a partir de las pruebas de modelos aplicados que se muestran a continuación:

        MODELOS
         ├── 70-30
         │   ├── CART_binario_70-30.joblib
         │   ├── GB_binario_70-30.joblib
         │   ├── MLP_binario_70-30.joblib
         │   ├── NB_binario_70-30.joblib
         │   ├── RF_binario_70-30.joblib
         │   └── SVM_binario_70-30.joblib
         ├── 80-20
         │   ├── CART_binario_80-20.joblib
         │   ├── GB_binario_80-20.joblib
         │   ├── MLP_binario_80-20.joblib
         │   ├── NB_binario_80-20.joblib
         │   ├── RF_binario_80-20.joblib
         │   └── SVM_binario_80-20.joblib
         └── 90-10
             ├── CART_binario_90-10.joblib
             ├── GB_binario_90-10.joblib
             ├── MLP_binario_90-10.joblib
             ├── NB_binario_90-10.joblib
             ├── RF_binario_90-10.joblib
             └── SVM_binario_90-10.joblib

En las carpetas 70-30, 80-20 y 90-10 podemos encontrar los distintos modelos ya entrenados con los respectivos porcentajes de train y test.

Se comparte resultados y comparativas generados durante el proceso de entrenamiento y validación de modelo final usado para el desarrollo del algoritmo, en documento Comparativa_V2.xlsx; y Explicación variación resultados Odio_No odio V2.pdf (Por publicar)

El procedimiento seguido para realizar el entrenamiento de los modelos queda reflejado en el Informe final Fase 1 - Odio y no odio.docx (Por publicar).

Autores: 
- Elias Said-Hung
- Julio Montero-Díaz
- Oscar De Gregorio
- Almudena Ruiz
- Xiomara Blanco
- Juan José Cubillas
- Daniel Pérez Palau 

Financiado por: 
Agencia Estatal de Investigación – Ministerio de Ciencia e Innovación

Con el apoyo de:
- POSSIBLE S.L.

Como citar: Said-Hung, E., Montero-Diaz, J., De Gregorio Vicente, O., Ruiz-Iniesta, A., Blanco Valencia, X., José Cubillas, J., and Pérez Palau, D. (2023), “Algorithm for classifying hate expressions in Spanish”, figshare. https://doi.org/10.6084/m9.figshare.24574906.

Más información:
- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net

---
Algorithm for detection of hate expressions in Spanish. This algorithm was developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/ AEI /10.13039/501100011033, with the collaboration of Possible Inc.

Please read README IN SPANISH, which outlines all the steps to follow to use the algorithm developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/ AEI /10.13039/501100011033

The folder structure with the GitHub documentation is presented below:

        02 Documentación Github
         └── 00_Odio y no odio
             ├── DOCUMENTACIÓN GITHUB.docx
             ├── ejemplo (1).py
             ├── Modelo_binario_ (1) (1).ipynb
             ├── obtener_caracteristicas (1).py
             └── Recursos-20231027T110710Z-001 (1).zip

The content of each file is detailed below:

- DOCUMENTACIÓN GITHUB.docx:
Report that presents the example of the script (1).py and get_characteristics (1).py to use the models.

- ejemplo (1).py:
Python script showing the use of models to make predictions.

- Modelo_binario_(1) (1).ipnyb:
Notebook with the code used for training the different models.

- Obtener_caracteristicas (1).py:
Python script with the preprocessing functions used before using the models to predict the inputs of a data frame.

- Recursos-20231027T110710Z-001 (1).zip:
The resources folder contains 3 .csv used in feature extraction.

The dataset that has been used for training the models is dataset_completo_caracteristicas_ampliadas_todos_combinaciones_v1_textoProcesado.csv
(https://acortar.link/diSV7o)

The Algorithm was developed from the tests of applied models shown below:

        MODELS
         ├── 70-30
         │   ├── CART_binario_70-30.joblib
         │   ├── GB_binario_70-30.joblib
         │   ├── MLP_binario_70-30.joblib
         │   ├── NB_binario_70-30.joblib
         │   ├── RF_binario_70-30.joblib
         │   └── SVM_binario_70-30.joblib
         ├── 80-20
         │   ├── CART_binario_80-20.joblib
         │   ├── GB_binario_80-20.joblib
         │   ├── MLP_binario_80-20.joblib
         │   ├── NB_binario_80-20.joblib
         │   ├── RF_binario_80-20.joblib
         │   └── SVM_binario_80-20.joblib
         └── 90-10
             ├── CART_binario_90-10.joblib
             ├── GB_binario_90-10.joblib
             ├── MLP_binario_90-10.joblib
             ├── NB_binario_90-10.joblib
             ├── RF_binario_90-10.joblib
             └── SVM_binario_90-10.joblib

In folders 70-30, 80-20 and 90-10, we can find the different models already trained with the respective percentages of train and test.

Results and comparisons generated during the training and validation process of the final model used for the development of the algorithm are shared in the document Comparativa_V2.xlsx; y Explicación variación resultados Odio_No odio V2.pdf (Por publicar)

The procedure for training the models is reflected in Informe final Fase 1 - Odio y no odio.docx (Por publicar).
The dataset used for training is dataset_completo_caracteristicas_ampliadas_todas_combinaciones_v1_textoProcesado.csv (https://acortar.link/diSV7o)

As documentation, in the folder "02 Documentación Github/00_Odio y no odio", the report "DOCUMENTACIÓN GITHUB.docx" explains the use of the different training models for making predictions.

Authors:
- Elias Said-Hung
- Julio Montero-Díaz
- Oscar De Gregorio
- Almudena Ruiz
- Xiomara Blanco
- Juan José Cubillas
- Daniel Pérez Palau

Funded by:
State Research Agency – Ministry of Science and Innovation

With the support of:
- POSSIBLE S.L.

How to cites: Said-Hung, E., Montero-Diaz, J., De Gregorio Vicente, O., Ruiz-Iniesta, A., Blanco Valencia, X., José Cubillas, J., and Pérez Palau, D. (2023), “Algorithm for classifying hate expressions in Spanish”, figshare. https://doi.org/10.6084/m9.figshare.24574906.

More information:
- https://www.hatemedia.es/ or contact: elias.said@unir.net

