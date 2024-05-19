# Algorithm-for-classifying-hate-expressions-in-Spanish
Algorithm for classifying hate expressions in messages in Spanish. This algorithm was developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/ AEI /10.13039/501100011033, with the collaboration of Possible Inc.

Please read README IN SPANISH, which outlines all the steps to follow to use the algorithm developed within the framework of the Hatemedia project (PID2020-114584GB-I00), funded by MCIN/ AEI /10.13039/501100011033

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

---
Algoritmo de clasificación de expresiones de odio en mensajes en español. Este algoritmo fue desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/AEI /10.13039/501100011033, con la colaboración de Possible Inc.

Por favor lea el documento README IN SPANISH, en el que se expone todos los pasos a seguir para el uso del algoritmo desarrollado en el marco del proyecto Hatemedia (PID2020-114584GB-I00), financiado por MCIN/ AEI /10.13039/501100011033

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
- https://www.hatemedia.es/ o contactar con:  elias.said@unir.net

---
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

- obtener_caracteristicas (1).py:
Python script with the preprocessing functions used before using the models to predict the inputs of a data frame.

- Recursos-20231027T110710Z-001 (1).zip:
The resources folder contains 3 .csv used in feature extraction.

The dataset that has been used for training the models is dataset_completo_caracteristicas_ampliadas_todos_combinaciones_v1_textoProcesado.csv
(https://acortar.link/diSV7o)

---

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

El dataset que se ha utilizado para el entrenamiento de los modelos es dataset_completo_caracteristicas_ampliadas_todas_combinaciones_v1_textoProcesado.csv 
(https://acortar.link/diSV7o)
