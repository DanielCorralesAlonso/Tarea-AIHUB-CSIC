

def data_selection(df, cancer_interes, checkpoint):
    try:
        df.drop(columns=["tipo_reco",  'año_reco', 'mes_reco', 'estacion_nac',"edad5","imc4", "tas", "tad","colesterol", "glucosa", "farmacos", "colesterol_hdl", "colesterol_ldl", "fecha_reco", "juicio_clinico", "por_estudios_pre_obligatorios", "por_estudios_post_obligatorios"], inplace= True)
        
        df.dropna(inplace = True)

        cancer_drop_list = ["cancer_cabeza_y_cuello", "cancer_cerebral", "cancer_piel", "cancer_endocrino",
                            'cancer_digestivo']

        cancer_drop_list.remove(cancer_interes)

        conditions = [None]*4
        for i in range(len(cancer_drop_list)):
            conditions[i] = df[cancer_drop_list[i]] == False

        df_clean = df[(df[cancer_interes] == True) | (conditions[0] & conditions[1] & conditions[2] & conditions[3])].copy().reset_index(drop = True)
        
        df_clean.drop(columns= cancer_drop_list, inplace=True)

        df_clean = df_clean[df_clean["duracion_sueño"] != '>9h'].reset_index(drop=True).copy()


        return df_clean
    
    except:
        return df