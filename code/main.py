import sys 
import os

import pandas as pd 
import numpy as np
import sys

import pyAgrum as gum

import pyAgrum.skbn as skbn

sys.path.append('..')
from Lib import data_selection as ds 
from Lib import constraints as cons
from Lib import model_evidences as me
from Lib import evidence as ev
from Lib import evaluation_metrics as em

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.metrics import make_scorer, confusion_matrix, fbeta_score
from pyAgrum.lib.bn2roc import showROC_PR, showPR
from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTENC
from pyAgrum.lib.bn2graph import BN2dot 

# ----- Para ejecutar este fichero, hacerlo desde la 'cmd' especificando el cancer de interés --------
# ----- Ejemplo: 'python main.py cancer_endocrino'

if (__name__ == "__main__") and (len(sys.argv) >= 2):
    cancer_interes = sys.argv[1]
    checkpoint = 1
    

# ---------- Construcción de una Red Bayesiana para Clasificación ------------------------------------


# Utilizamos ahora las funciones que trae el módulo 'skbn' de la librería pyAgrum
# IMPORTANTE --- Estamos utilizando la versión 0.21.0 de pyAgrum por compatibilidad con Artemisa -----
# https://pyagrum.readthedocs.io/en/0.21.0/Classifier.html



    # ---- Leemos los datasets que tenemos guardados para la tarea -----------------------------------
    df = pd.read_csv("data/df_hackathon_tr.csv", index_col = None)
    df_val = pd.read_csv("data/df_hackathon_val.csv", index_col = None)



    # ---- Utilizamos la función "dataselection" para hacer la selección del cáncer de interés -------
    df_selec = ds.data_selection(df, cancer_interes, checkpoint)
    df_selec_val = ds.data_selection(df_val, cancer_interes, checkpoint)



    # ---- Definimos los arcos que queremos que tenga la red de forma obligatoria --------------------
    path = 'Resultados/'
    constraint_dict = cons.constraints(cancer_interes, checkpoint)




    # Realizamos un resampling de la clase minoritaria con el objetivo de que no haya tanto desequilibrio de clases:
    # ---- Solo tiene efecto en el dataset de entrenamiento.
    # ----
    # ---- Como tenemos atributos categóricos, tendremos que especificar donde están, dado que el algoritmo SMOTENC
    # ---- necesita diferencia entre variables contínuas y categoricas. 
    # ---- https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTENC.html 
    #
    smote_sampling = SMOTENC(categorical_features= [1,3,4,5,6,7,8,9,10,11,12,13,14,15,16], random_state = 42)



    # Definimos el clasificador en forma de red bayesiana 
    # ---- Para más info ver https://pyagrum.readthedocs.io/en/0.21.0/Classifier.html
    # ---- Un aspecto a destacar es que el propio algoritmo en este caso es capaz de discretizar los atributos continuos.
    BayesNetClassifier = skbn.BNClassifier(constraints= constraint_dict, discretizationNbBins=3)



    # ---- Metemos el proceso en un Pipeline para realizar luego cross validation sin contaminar el dataset de testeo 
    # ---- https://imbalanced-learn.org/stable/references/generated/imblearn.pipeline.Pipeline.html
    pipeline = Pipeline([('sampling', smote_sampling), ('classifier', BayesNetClassifier)])
    



    # ---- Hacemos una búsqueda de hiperparámetros.
    # ---- Hay parámetros que tiene el modelo que se tienen que ajustar de manera manual. Buscaremos la combinación de parámetros que mejores resultados ofrezca.
    grid = {'sampling__sampling_strategy': [0.1, 0.3], 
            'classifier__learningMethod': ['Tabu','GHC'], 
            'classifier__aPriori' : ['Smoothing'], 
            'classifier__scoringType': ['K2', 'BDeu'],
            'classifier__aPrioriWeight': [0.01], 
            'classifier__usePR': (True, False) 
            }


    
    # ---- Debemos definir la métrica a considerar para analizar el problema -------------------------------
    # ---- https://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter -----------------
    custom_scorer = 'recall'
    



    # ---- https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html -----
    grid_search = GridSearchCV(pipeline, grid, cv = StratifiedKFold(shuffle = True, random_state=42),
                                scoring = custom_scorer , n_jobs = -1)
    
    print(grid_search)




    # ---- Cogemos los datos a introducir en el modelo separando por clase y atributos ----------------------
    y = df_selec[cancer_interes]
    X = df_selec.drop(labels = cancer_interes, axis = 1)



    # ---- Realizamos la construcción de la red bayesiana óptima para la tarea de clasificación ------------
    grid_search.fit(X, y)


    # ---- Guardamos el mejor modelo ------------------------------------------------------------------------
    best_model = grid_search.best_estimator_['classifier']

    print(grid_search.best_estimator_)
    print(grid_search.best_score_)



    # ---- Guardamos la Red Bayesian en forma de imagen ----------------------------------------------------
    file_name = str(cancer_interes) + '_BN.png'
    file_path = os.path.join(path,file_name)

    g = BN2dot(best_model.bn, size = '20!')
    g.write(file_path, format = 'png')




    # ---- Evaluamos el modelo obtenido en el entrenamiento con otro conjunto de datos no vistos previamente por el modelo 
    y_val = df_selec_val[cancer_interes]
    X_val = df_selec_val.drop(labels = cancer_interes, axis = 1)

    y_pred = best_model.predict(X_val)

    cf = confusion_matrix(y_val, y_pred)

    TN = cf[0,0]
    FN = cf[1,0]
    TP = cf[1,1]
    FP = cf[0,1]

    em.evaluation_metrics(TN, FN, TP, FP, cancer_interes, path)




    # ---- Podemos además hacer inferencia en la red escogida ----------------------------------------
    evidences = ev.evidence(cancer_interes, checkpoint)

    evidence = me.model_evidences(best_model.bn, evidences, cancer_interes, path)

    print("Construcción automatizada de una red bayesiana para clasificación realizada con éxito!")


# ----------------------------------------------------------------------

else: 
    print("Debe introducir un tipo de cáncer")   
