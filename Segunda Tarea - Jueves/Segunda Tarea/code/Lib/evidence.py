def evidence(cancer_interes, checkpoint):

    c = {"evidences": [
        
        ("imc", ["condicion_socioeconomica_media"]),

        ("diabetes1", ["edad"]),
        ("diabetes1", ["imc"]),

        ('hipertension1', ['fumador']),
        ('consumo_alcohol', ['fumador']),

        ('hipertension1', ['fumador', 'consumo_alcohol']),

        ('calidad_sueño', ['consumo_alcohol']),
        ('calidad_sueño', ['fumador']),

        ('calidad_sueño', ['fumador','consumo_alcohol']),

        (cancer_interes, ['edad']),
        (cancer_interes, ["imc"]),
        (cancer_interes, ["condicion_socioeconomica_media"]),
        (cancer_interes, ["tasa_de_paro"]),
        (cancer_interes, ["consumo_alcohol"]),
        (cancer_interes, ["fumador"]),
    ]   
    }
    

    return c