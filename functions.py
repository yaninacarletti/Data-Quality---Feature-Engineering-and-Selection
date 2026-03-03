import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def data_quality_analysis(df):
    # Se crea un nuevo dataframe para almacenar los resultados
    result_df = pd.DataFrame(columns=['Columna', 'Tipo de dato', 'Valores únicos', 'Valores faltantes'])

    # Se obtiene información general del dataframe
    columns = df.columns
    data_types = df.dtypes.to_list()
    unique_values = [df[column].nunique() for column in columns]
    missing_values = [df[column].isnull().mean() for column in columns]

    # Se llena el nuevo dataframe con los resultados
    result_df['Columna'] = columns
    result_df['Tipo de dato'] = data_types
    result_df['Valores únicos'] = unique_values
    result_df['Valores faltantes'] = missing_values

    return result_df




def plot_distributions(data, analysis_result, columns_review=None):
    plt.rcParams.update({'font.size': 25})

    if columns_review:
        columns_distributions = columns_review
    else:
        columns_distributions = data.columns
    plt.figure(figsize=(30, 30))
    number_rows = len(columns_distributions)//2 + len(columns_distributions)%2
    for n, i in enumerate(columns_distributions):
        plt.subplot(5, 2, n + 1)
        if analysis_result.loc[i, 'Tipo de dato']=='object':
            col = data[i].astype(str)
            sns.countplot(y= col, order=col.value_counts().iloc[:7].index)
            plt.title('Frecuencias para {}'.format(i))
        else:
            sns.distplot(data[i])
            plt.title('Distribución para {}'.format(i))
        plt.tight_layout()




def initial_transform(data):
    data2 = data.copy()
    data2['User Rating'] = data2['User Rating'].astype(str).str.replace('User Rating', 'NaN').str.replace(',', '').astype(float)
    data2['Number of Votes'] = data2['Number of Votes'].astype(str).str.replace(',', '').str.replace('Number of Votes', 'NaN').astype(float)
    data2['Runtime'] = data2['Runtime'].str.replace(' min', '').str.replace('Runtime', 'NaN').str.replace(',', '').astype(float)
    data2['Year'] = data2['Year'].str.extract('(\d+)', expand=True).astype(float)
    data2['Gross'] = data2['Gross'].astype(str).str.replace('Gross', 'NaN').str.replace(',', '').astype(float)
    data2['Episode'] = data2['Episode'].astype(str).str.replace('Episode', 'NaN').astype(float)
    data2 = data2.drop(['Summary'], axis=1)
    return data2




def detect_outliers_iqr(data, columns, factor=1.5):
    outliers = {}
    idx_outs = set()
    for column_name in columns:
        # Se calculan los estadísticos clave
        Q1 = data[column_name].quantile(0.25)
        Q3 = data[column_name].quantile(0.75)
        IQR = Q3 - Q1

        # Se calculan los límites para los valores atípicos
        lower_bound = Q1 - factor * IQR
        upper_bound = Q3 + factor * IQR

        d_outs = data.loc[(lower_bound>data[column_name])|(data[column_name]>upper_bound)]
        q_outliers = d_outs.shape[0]
        idx_outs.update(set(d_outs.index))  
        outliers[column_name] = {'lower_bound': lower_bound, 'upper_bound': upper_bound, 'q': q_outliers}
    outliers = pd.concat([pd.DataFrame(outliers), data[columns].describe()]).T
    return outliers, idx_outs




def tranform_final(data):
    data2 = data.copy()
    data2['Genre_n'] = data2['Genre'].str.split(', ').str.len()
    data2['Number of Votes Log'] = np.log(data2['Number of Votes'])
    data2['Gross Log'] = np.log(data2['Gross'])

    data_categories = data2['Genre'].str.split(', ').str.join('|').str.get_dummies()
    data2 = data2.drop(['Genre', 'Certificate', 'Number of Votes', 'Gross'], axis=1)
    data2 = data2.merge(data_categories, left_index=True, right_index=True)
    data2.dropna(inplace=True)
    data2 = data2.reset_index(drop=True)
    return data2




