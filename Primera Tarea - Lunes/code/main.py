
import sys 
import os

import pandas as pd
import sys

import pyAgrum as gum

import pyAgrum.skbn as skbn
import pyAgrum.lib.notebook as gnb

sys.path.append('..')
from Lib import data_selection as ds 
from Lib import data_discretization as dd
from Lib import constraints as cons
from Lib import model_evidences as me
from Lib import learning_BN as learn_bn
from Lib import evidence as ev

import pyAgrum.lib.image as gumimage
from pyAgrum.lib.bn2graph import BN2dot 


# ---------- Para ejecutar el 'main.py' es necesario hacerlo introduciendo el cáncer de interés ----------
#       Ejemplo: 'python main.py cancer_piel' desde la terminal

if (__name__ == "__main__") and (len(sys.argv) >= 2):
    cancer_interes = sys.argv[1]
    checkpoint = 0

# ---------- Construcción de una Red Bayesiana para Inferencia ----------


    # --- Lee los '.csv' necesarios para la tarea ---
    df = ""
    # -----------------------------------------------



    # -- Utiliza la función 'data_selection' para filtrar por las columnas de interés ---
    df_selec = ds.data_selection(df, cancer_interes, checkpoint)



    # -- Para poder hacer inferencia en una Red Bayesiana necesitamos datos discretos ---
    path = 'inferencia/'
    df_tr_discrete = dd.data_discretization(df_selec, cancer_interes)




    # --- ¿Qué restricciones / conocimiento previo le queremos poner a la red? ----------
    constraints = cons.constraints(cancer_interes, checkpoint)




    # --- Utiliza la función 'learning_BN' para hacer el aprendizaje de la estructura de la red ---
    model = learn_bn.learning_BN(df_tr_discrete, constraints, path)

    file_name = str(cancer_interes) + '_BN.png'
    file_path = os.path.join(path,file_name)
    gumimage.export(model, file_path, size = "20!")
    g = BN2dot(model, size = '20!')
    g.write(file_path, format = 'png')




    # --- ¿Cuáles son las evidencias que queremos introducir? ---
    # --- ¿Cómo son las tablas de probabilidad condicionada en base a esas evidencias? ---
    evidences = ev.evidence(cancer_interes,checkpoint)
    evidence = me.model_evidences(model, evidences, cancer_interes, path)

    print("Inferencia realizada con éxito!")

# ----------------------------------------------------------------------

else: 
    print("Debe introducir un tipo de cáncer")   
