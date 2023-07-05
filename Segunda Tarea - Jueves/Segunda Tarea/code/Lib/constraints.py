def constraints(cancer_interes, checkpoint):
    c = {
        "MandatoryArcs": [
                
                # Known risk factors (obtained from ChatGPT)
                ('consumo_alcohol', cancer_interes),
                ("fumador", cancer_interes),
                ("obesidad", cancer_interes),

                ("diabetes1", cancer_interes),
                
                # Other relations (obtained using experts opinions)
                
                ('imc', 'diabetes1'),
                ('imc', 'hipertension1'),
                ('imc', 'hipercolesterolemia1'),
                ('imc', 'medicacion'),

                ('consumo_alcohol', 'medicacion'),

                ('fumador', 'hipertension1'),
                ('fumador', 'medicacion'),

                ('af', 'imc'),
                ('af', 'diabetes1'),
                ('af', 'hipertension1'),
                ('af', 'hipercolesterolemia1'),
                ('af', 'medicacion'),
                ('af', 'inicio_sueño'),
                ('af', 'calidad_sueño'),
                ('af', 'impresion_sueño'),
                ('af', 'duracion_sueño'),
                ('af', cancer_interes),

                ('sexo', 'depresion'),
                ('sexo', 'ansiedad'),

                ('edad', 'diabetes1'),
                ('edad', 'hipertension1'),

                ('condicion_socioeconomica_media', 'af')
                
            ], 
            
        "ForbiddenArcs": [
                ('imc', 'sexo'),
                ('obesidad', 'sexo'),
                ('af', 'sexo'),
                ('consumo_alcohol', 'sexo'),
                ('fumador', 'sexo'),
                ('calidad_sueño', 'sexo'),
                ('duracion_sueño', 'sexo'),
                ('inicio_sueño', 'sexo'),
                ('impresion_sueño', 'sexo'),
                ('medicacion', 'sexo'),
                ('diabetes1', 'sexo'),
                ('hipertension1', 'sexo'),
                ('hipercolesterolemia1', 'sexo'),
                ('depresion', 'sexo'),
                ('ansiedad', 'sexo'),
                (cancer_interes, 'sexo'),
                ('tasa_de_paro', 'sexo'),
                ('condicion_socioeconomica_media', 'sexo'),
                ('nivel_medio_de_estudios_ge_30_39', 'sexo'),


                ('imc', 'edad'),
                ('obesidad', 'edad'),
                ('af', 'edad'),
                ('consumo_alcohol', 'edad'),
                ('fumador', 'edad'),
                ('calidad_sueño', 'edad'),
                ('duracion_sueño', 'edad'),
                ('inicio_sueño', 'edad'),
                ('impresion_sueño', 'edad'),
                ('medicacion', 'edad'),
                ('diabetes1', 'edad'),
                ('hipertension1', 'edad'),
                ('hipercolesterolemia1', 'edad'),
                ('depresion', 'edad'),
                ('ansiedad', 'edad'),
                (cancer_interes, 'edad'),
                ('tasa_de_paro', 'edad'),
                ('condicion_socioeconomica_media', 'edad'),
                ('nivel_medio_de_estudios_ge_30_39', 'edad'),
        ]
        
    }


    return c