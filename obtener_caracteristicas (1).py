import io
import itertools
import os
import re
import time
import timeit
import warnings

import emoji
import es_core_news_sm
import nltk
import numpy as np
import pandas as pd
import pysentimiento
import spacy
import unidecode
from nltk import bigrams
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from pysentimiento import create_analyzer
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm

warnings.filterwarnings("ignore")
nltk.download('stopwords')
nltk.download('punkt')

# Cargar wordbatch negativa
df_wb_neg = pd.read_csv("./recursos/wordbatch_negativa_consolidada.csv", delimiter=";")
wb_negativa = df_wb_neg["Palabra"]
wb_negativa.dropna(inplace=True)

# Cargar wordbatch positiva
df_wb_pos = pd.read_csv("./recursos/wordbatch_positiva_adjetivos.csv", delimiter=";")
wb_positiva = df_wb_pos["Palabra"]

# Cargar bigram list
df_bigram = pd.read_csv("./recursos/bigram_list_final.csv")
wb_bigram = df_bigram["Bigram"]


# Separar texto de 2 en 2 palabras para comparar con bigram
def pairwise(iterable):
    iterable = iterable.split(",")
    a = iter(iterable)
    return zip(a, a)

def sentiment_categorizer(s):
    if 0 < s < 1 / 7:
        return 0
    if 1 / 7 < s < 2 / 7:
        return 1
    if 2 / 7 < s < 3 / 7:
        return 2
    if 3 / 7 < s < 4 / 7:
        return 3
    if 4 / 7 < s < 5 / 7:
        return 4
    if 5 / 7 < s < 6 / 7:
        return 5
    if 6 / 7 < s < 1:
        return 6

analyzer = create_analyzer(task="sentiment", lang="es")

def extract_features(texto, texto_completo):
    features = []
    wb_neg_count = 0
    wb_pos_count = 0
    wb_bigram_count = 0
    mentions_count = texto.count("@")

    sentiment_cat = sentiment_categorizer(analyzer.predict(texto).probas["NEG"])

    # Split de texto para buscar positivas y negativas
    texto_pos_neg = set(texto.split(","))

    # Positiva
    wb_pos_count = len(texto_pos_neg.intersection(wb_positiva))

    # Negativas
    wb_neg_count = len(texto_pos_neg.intersection(wb_negativa))

    # Bigrams
    texto_bigrams = list(bigrams(texto.split()))
    wb_bigram_count = sum(1 for bigram in texto_bigrams if bigram in wb_bigram)
    
    features = [
        wb_bigram_count,
        wb_pos_count,
        wb_neg_count,
        mentions_count,
        sentiment_cat,
        texto_completo,
    ]
    
    return features


# Eliminar emojis, url y menciones optimizada
def delete_emoji(df):
    rows_to_drop = []

    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticonos emoji
        u"\U0001F300-\U0001F5FF"  # símbolos y pictogramas emoji
        u"\U0001F680-\U0001F6FF"  # transporte emoji
        u"\U0001F700-\U0001F77F"  # alquimia emoji
        u"\U0001F780-\U0001F7FF"  # emoji Geométricos
        u"\U0001F800-\U0001F8FF"  # Suplemento de símbolos de flecha
        u"\U0001F900-\U0001F9FF"  # Suplemento de emoji-cara
        u"\U0001FA00-\U0001FA6F"  # Suplemento de emoji-personas
        u"\U0001FA70-\U0001FAFF"  # Suplemento de emoji-pelo
        u"\U0001FAF0-\U0001FAFF"  # Suplemento de emoji-auricular
        u"\U00002702-\U000027B0"  # símbolos diversos
        u"\U000024C2-\U0001F251" 
        u"\U0001F004-\U0001F0CF" 
        u"\U0001F170-\U0001F251"
        "]+", flags=re.UNICODE)
    
    for index, row in tqdm(df.iterrows(), total = df.shape[0]):
        text = row['CONTENIDO A ANALIZAR'].lower()

        # Eliminar emojis
        text = emoji_pattern.sub(r'', text)
        
        # Eliminar URLs
        if 'http:' in text or 'https:' in text:
            rows_to_drop.append(index)
        
        # Actualizar fila del DataFrame
        df.at[index, 'CONTENIDO A ANALIZAR'] = text
        
    # Eliminar filas
    df.drop(rows_to_drop, inplace=True)
    
    # Eliminar filas con elementos menores a longitud 2
    df.drop(df[df['CONTENIDO A ANALIZAR'].map(len) < 2].index, inplace=True)
    
    # Resetear los índices de pandas
    df.reset_index(drop=True, inplace=True)
    
    return df
    
def text_processing(df_dict):
    texto_completo = []
    content_df = []
    puntuacion = r'[,;.:¡!¿?#$%&[\](){}<>~=+\-*/|\\_^`"\']'
    stop_words = set(stopwords.words('spanish'))

    for i in tqdm(df_dict.index):
        # Convertir a minúsculas
        text = df_dict['CONTENIDO A ANALIZAR'][i].lower()
        
         # Eliminar signos de puntuación y caracteres especiales
        text = text.translate(str.maketrans('', '', puntuacion))
        
         # Eliminar números
        text = re.sub(r'\d', ' ', text)
        
         # Eliminar acentos
        text = unidecode.unidecode(text)

        # Tokenizar el texto
        tokens = word_tokenize(text)

        # Eliminar palabras con un solo carácter y stopwords
        tokens = [token for token in tokens if len(token) > 2 and token not in stop_words]

        # Lemmatización y eliminación de palabras con un solo carácter
        lemmas = [token for token in tokens if len(token) > 2]

        # Unir los lemas en una cadena
        clean_str = ','.join(lemmas)

        content_df.append(clean_str)
        texto_completo.append(df_dict['CONTENIDO A ANALIZAR'][i])

    return content_df, texto_completo

def main(df):
    df.dropna()
    
    # Eliminamos emojis
    df = delete_emoji(df)

    process_list = text_processing(df)
    process_text = process_list[0]
    full_text = process_list[1]

    features_df = pd.DataFrame([(extract_features(element_a, element_b)) for element_a, element_b in tqdm(zip(process_text, full_text))])
    features_df.rename(columns={
        0: 'A',
        1: 'B',
        2: 'C',
        3: 'D',
        4: 'E',
        5: 'TEXTO'
    }, inplace=True)
    
    # Ampliación de características
    scaler = StandardScaler()
    features_df[['A_t', 'B_t', 'C_t', 'D_t', 'E_t']] = scaler.fit_transform(features_df[['A', 'B', 'C', 'D', 'E']])

    dfs = []
    count = 1
    for index, row in tqdm(features_df.iterrows()):
        iterables = [row["A_t"], row["B_t"], row["C_t"], row["D_t"], row["E_t"]]
        combinations = itertools.combinations(iterables, 2)
        new_cols = {}

        for i in list(combinations):
            col_name = "Valor_" + str(count)
            value = i[0] * i[1]
            new_cols[col_name] = value
            count += 1

        dfs.append(new_cols)
        count = 1

    features_df.reset_index(drop=True, inplace=True)
    df_new = pd.DataFrame(dfs)
    features_df = pd.concat([features_df, df_new], axis=1)

    droped_columns = ['A', 'B', 'C', 'D', 'E', 'TEXTO']
    features_df = features_df.drop(columns=droped_columns)

    return features_df