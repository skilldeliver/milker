#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converts skilldeliver's JSON to a Kaggle-friendly CSV
Created on Fri Jun 12 21:37:13 2020

@author: nasko7
"""

import numpy as np
import pandas as pd
from transliterate import translit

def translit_bg(x):
    """Transliterates string, if in Bulgarian."""
    try:
        return translit(x, 'bg', reversed=True)
    except:
        return str(x)
    
payner = pd.read_json("tracks_payner.json")
data = pd.json_normalize(data=payner['tracks'])

# Simplify column names
shortcols = {
    'audio_features.danceability': 'danceability',
    'audio_features.energy': 'energy',
    'audio_features.key': 'key',
    'audio_features.loudness': 'loudness',
    'audio_features.mode': 'mode',
    'audio_features.speechiness': 'speechiness',
    'audio_features.acousticness': 'acousticness',
    'audio_features.instrumentalness': 'instrumentalness',
    'audio_features.liveness': 'liveness',
    'audio_features.valence': 'valence', 
    'audio_features.tempo': 'tempo',
    'audio_features.duration_ms': 'duration',
    'audio_features.time_signature': 'time_signature',
    'date': 'datetime'
}

data = data.rename(columns=shortcols)

# Split 'artists' array values to first, second and third artist
artists = pd.DataFrame(data.artists.values.tolist()).add_prefix('artist_')

data['artist_1'] = artists.artist_0.apply(translit_bg)
data['artist_2'] = artists.artist_1.apply(translit_bg)
data['artist_3'] = artists.artist_2.apply(translit_bg)

# Wrong transliteration, issues may arise
data = data.replace({
    'Iliyan':'Ilian',
    'Djena':'Dzhena',
    'Djulia': 'Dzhulia',
    'Adnan Biyts': 'Adnan Beats',
    'Djordan': 'Dzhordan',
    'Djamaikata': 'Dzhamaikata',
    'Silvar': 'Silver',
    'Geym Ouvar': 'Game Over',
    'Vanya i Damyan': 'Vanya', # Sorry, Damyan
    'Extra Nina': 'Ekstra Nina',
    'MALINA': 'Malina',
    'Tedi Aleksanrova':'Tedi Aleksandrova',
    'Tedi Aleksadrova':'Tedi Aleksandrova',
    'Alisiya':'Alisia',
    'Julia': 'Dzhulia',
    
    
})

# Fix one song (thanks, nasko)
data.loc[493,'artist_1'] = 'Maria & Magdalena'
data.loc[493,'artist_2'] = 'None'


data = data.drop(columns=['artists'])

# Reorder columns
new_cols = ['track_id',  'artist_1', 'artist_2', 'artist_3', 'track_name', 'popularity',
            'datetime', 'danceability', 'energy', 'key', 'loudness', 'mode', 'speechiness',
            'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration',
            'time_signature']
data = data[new_cols]

# Apply transliteration to track names
data['track_name'] = data['track_name'].apply(translit_bg)

# Out
data.to_csv("payner.csv",index=False)