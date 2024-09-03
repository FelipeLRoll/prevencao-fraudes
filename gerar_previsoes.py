def gerar_previsoes():
    
    import pandas as pd
    import joblib
    from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder, RobustScaler

    
    print("Carregando as bibliotecas...")
    
    clf = joblib.load("modelo/modelo.pk")
    
    print("Gerando Previsões...")
    
    df = pd.read_csv(r"dataset/novos_dados.csv")
    
    print("Tratando os dados...")
    
    colunas_categoricas = ["Sexo", "Estado_Civil", "Escolaridade", "Possui_Patrimonio", "Possivel_Fraude"]

    for coluna in colunas_categoricas:
        df[coluna] = df[coluna].astype("category")

    escolaridade = ["Nenhum", "Ensino Médio", "Ensino Superior", "Ensino Fundamental", "Pós Graduação / Mestrado / Doutorado"]
    df["Escolaridade"] = df["Escolaridade"].cat.set_categories(escolaridade, ordered = True)
    
    colunas_float = df.select_dtypes(include="float64").columns
    colunas_int = df.select_dtypes(include="int64").columns

    df[colunas_float] = df[colunas_float].apply(pd.to_numeric, downcast="float")
    df[colunas_int] = df[colunas_int].apply(pd.to_numeric, downcast="integer")
    
    df = df.drop_duplicates()
    
    df["Estado_Civil"] = df["Estado_Civil"].replace(["NENHUM"], "OUTRO")
    df["Estado_Civil"] = df["Estado_Civil"].replace(["UNIÃO ESTAVEL" , "CASADO (A)"], "CASADO(A)")
    df["Estado_Civil"] = df["Estado_Civil"].replace(["SEPARADO JUDICIALMENTE"], "DIVORCIADO")
    
    faixas = [0, 20, 30, 40, 50, 60, 70, 110]
    categorias = ["0-20 Anos", "21-30 Anos", "31-40 Anos", "41-50 Anos", "51-60 Anos", "61-70 Anos", "71-110 Anos"]
    df["Faixa_Etaria"] = pd.cut(df["Idade"], bins=faixas, labels=categorias)
    df["Faixa_Etaria"] = df["Faixa_Etaria"].cat.set_categories(categorias, ordered = True)
    
    faixas = [-1, 1000, 3000, 5000, 10000, 20000, 50000, 100000, 500000, 1000000, 5000000, 999000000]
    categorias = ["Até 1000", "1k - 3k", "3k - 5k", "5k - 10k", "10k - 20k", "20k - 50k", "50k - 100k", "100k - 500k", "500k - 1kk", "1kk - 5kk", "Mais de 5kk"]
    df["Faixa_Salarial"] = pd.cut(df["Valor_Renda"], bins=faixas, labels=categorias)
    df["Faixa_Salarial"] = df["Faixa_Salarial"].cat.set_categories(categorias, ordered = True)
    
    df["QT_Dias_Atraso"] = df["QT_Dias_Atraso"].fillna((df["QT_Dias_Atraso"].median()))
    
    faixas = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 366, 9999]
    categorias = ["Até 30 dias", "De 30 - 60 dias", "De 60 - 90 dias", "De 90 - 120 dias", "De 120 - 150 dias", "De 150 - 180 dias", "De 180 - 210 dias", "De 210 - 240 dias", "De 240 - 270 dias", "De 270 -  300 dias", "De 300 - 330 dias", "De 330 - 1 ano", "Mais de 1 ano"]
    df["Faixa_Dias_Atraso"] = pd.cut(df["QT_Dias_Atraso"], bins=faixas, labels=categorias)
    df["Faixa_Dias_Atraso"] = df["Faixa_Dias_Atraso"].cat.set_categories(categorias, ordered = True)
    
    faixas = [-1, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 250000, 400000, 999999]
    categorias = ["Até 1k", "De 1k - 2k", "De 2k - 5k", "De 5k - 10k", "De 10k - 20k", "De 20k - 50k", "De 50k - 100k", "De 100k - 250k", "De 250k - 400k",  "Mais de 400k"]
    df["Faixa_Total_Pago"] = pd.cut(df["Total_Pago"], bins=faixas, labels=categorias)
    df["Faixa_Total_Pago"] = df["Faixa_Total_Pago"].cat.set_categories(categorias, ordered = True)
    
    faixas = [-1, 1000, 2000, 5000, 10000, 20000, 50000, 100000, 250000, 500000, 999999]
    categorias = ["Até 1k", "De 1k - 2k", "De 2k - 5k", "De 5k - 10k", "De 10k - 20k", "De 20k - 50k", "De 50k - 100k", "De 100k - 250k", "De 250k - 500k",  "Mais de 500k"]
    df["Faixa_Saldo_Devedor"] = pd.cut(df["Saldo_Devedor"], bins=faixas, labels=categorias)
    df["Faixa_Saldo_Devedor"] = df["Faixa_Saldo_Devedor"].cat.set_categories(categorias, ordered = True)
    
    faixas = [-1, 60, 120, 200, 720]
    categorias = ["Até 60 Meses", "De 61 até 120 Meses", "De 121 até 200 Meses", "Acima de 200 Meses"]
    df["Faixa_Prazo_Emprestimo"] = pd.cut(df["Prazo_Emprestimo"], bins=faixas, labels=categorias)
    df["Faixa_Prazo_Emprestimo"] = df["Faixa_Prazo_Emprestimo"].cat.set_categories(categorias, ordered = True)
    
    faixas = [-20, 60, 120, 200, 500]
    categorias = ["Até 60 Meses", "De 61 até 120 Meses", "De 121 até 200 Meses", "Acima de 200 Meses"]
    df["Faixa_Prazo_Restante"] = pd.cut(df["Prazo_Restante"], bins=faixas, labels=categorias)
    df["Faixa_Prazo_Restante"] = df["Faixa_Prazo_Restante"].cat.set_categories(categorias, ordered = True)
    
    norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
    nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
    sudeste = ["ES", "MG", "RJ", "SP"]
    sul = ["PR", "RS", "SC"]
    centro_oeste = ["DF", "GO", "MT", "MS"]

    regiao_estados = {}

    for estado in norte:
        regiao_estados[estado] = "Norte"
    
    for estado in nordeste:
        regiao_estados[estado] = "Nordeste"    
    
    for estado in sudeste:
        regiao_estados[estado] = "Sudeste"   
    
    for estado in sul:
        regiao_estados[estado] = "Sul"  
    
    for estado in centro_oeste:
        regiao_estados[estado] = "Centro_Oeste"         
    
    def get_region(estado):
        return regiao_estados.get(estado, "Nenhum")

    df["Regiao_UF_Cliente"] = df["UF_Cliente"].apply(get_region)
    
    colunas = ["Sexo", "Regiao_UF_Cliente", "Perc_Juros", "VL_Emprestimo", "VL_Emprestimo_ComJuros", "QT_Total_Parcelas_Pagas", "QT_Total_Parcelas_Pagas_EmDia", 
            "QT_Total_Parcelas_Pagas_EmAtraso", "Qt_Renegociacao", "Estado_Civil", "QT_Parcelas_Atraso", "Faixa_Etaria", 
            "Faixa_Salarial", "Faixa_Dias_Atraso", "Faixa_Total_Pago", "Faixa_Saldo_Devedor", "Faixa_Prazo_Emprestimo", "Faixa_Prazo_Restante", "Possivel_Fraude"]

    df_tratado = pd.DataFrame(df, columns=colunas)
    
    df_numerico = df_tratado.select_dtypes(include=['number'])
    
    colunas_numericas = df_tratado.select_dtypes(include=['number']).columns
    coluna_alvo = df_tratado[["Possivel_Fraude"]]

    df_categorica = df_tratado.drop(columns=colunas_numericas).drop(columns=coluna_alvo)
    
    print("Fazendo o OneHotEnconding e OrdinalEnconding...")
    ore = OrdinalEncoder()
    ohe = OneHotEncoder(sparse_output=False)

    colunas_ordinal_encoding = ["Faixa_Etaria", "Faixa_Salarial", "Faixa_Dias_Atraso", "Faixa_Total_Pago", "Faixa_Saldo_Devedor", "Faixa_Prazo_Emprestimo", "Faixa_Prazo_Restante"]
    colunas_onehot_encoding = ["Sexo", "Regiao_UF_Cliente", "Estado_Civil"]

    ore_ft = ore.fit_transform(df_categorica[colunas_ordinal_encoding])
    ore_df = pd.DataFrame(ore_ft, columns=colunas_ordinal_encoding)

    ohe_ft = ohe.fit_transform(df_categorica[colunas_onehot_encoding])
    ohe_df = pd.DataFrame(ohe_ft, columns=ohe.get_feature_names_out(colunas_onehot_encoding))

    df_categorico_encoded = pd.concat([ore_df, ohe_df], axis=1)

    df_transformado = pd.concat([df_categorico_encoded, df_numerico, df_tratado[["Possivel_Fraude"]]], axis=1)
    
    colunas_float = df_transformado.select_dtypes(include="float64").columns

    df_transformado[colunas_float] = df_transformado[colunas_float].apply(pd.to_numeric, downcast="float")
    
    var_preditoras = df_transformado.drop("Possivel_Fraude", axis = 1)
    
    print("Usando o RobustScaler...")
    robusto = RobustScaler()
    dados_robusto = robusto.fit_transform(var_preditoras)
    
    print("Fazendo a previsão...")
    previsoes = clf.predict(dados_robusto)
    probabilidades = clf.predict_proba(dados_robusto)
    df["Previsoes"] = previsoes
    df["Probabilidades em %"] = probabilidades[:, 1] * 100
    
    df.to_excel("previsao/previsoes.xlsx")
    print("Previsoes Geradas com Sucesso!")      
    
def main():
    gerar_previsoes()    


if __name__ == "__main__":
    main()    
