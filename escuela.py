#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%

# Cargar los datos
df = pd.read_excel('/Users/paola/OneDrive/Desktop/Python_practicum/Escuela/Aceptados_clean.xlsx ')
df.columns = ['name','institution', 'citizenship','gender','economic_support','background_gr','programming_skills','academic_level','email','field','money']
df['academic_level'] = df['academic_level'].str.upper()
df['background_gr']=df['background_gr'].str.upper()
df['conocimientos_programacion']=df['conocimientos_programacion'].str.upper()

print(df['field'].value_counts())
reemplazo = {'Astronomia-Matematicas': 'Astronomia', 'Astro': 'Astronomia','Fisico': 'Fisica'}
df['field'] = df['field'].replace(reemplazo)
print(df['field'].value_counts())

print(df['field'].tail(10))
print(df.loc[28])

df.at[28, 'field']='Astronomia'
print(df.loc[28])

df.info()
print(df.head())

grouped_data = df.groupby('gender')
print(grouped_data.head(2))

grouped_data['gender'].count()
df['count']= 1
print(df['background_gr'].head(20))
print(df.loc[17])
df.at[17, 'background_gr']='SI'
print(df.loc[17])






#data_pivot = df.pivot_table(index=['background_gr'], columns='nivel_academico',values='conteo', aggfunc='sum')
table1 = pd.pivot_table(df, values='count', index=[ 'gender','background_gr'],columns=['academic_level'], aggfunc="sum", fill_value=0)
print(table1)

table2 = pd.pivot_table(df, values='count', index=[ 'gender','programming_skills'],columns=['academic_level'], aggfunc="sum", fill_value=0)
print(table2)

table3=pd.pivot_table(df, values='count', index=[ 'field'],columns=['academic_level'], aggfunc="sum", fill_value=0)
print(table3)

# Crear una figura de Matplotlib para la tabla dinámica

fig, ax = plt.subplots()

# Crear una tabla para mostrar los datos
#table = ax.table(cellText=table1.values, colLabels=table1.columns, rowLabels=table1.index, loc='center')
#table.auto_set_font_size(False)
#table.set_fontsize(12)

# Eliminar ejes de la figura
#ax.axis('off')

# Guardar la tabla dinámica como una imagen PNG
#plt.savefig('tabla1.png', bbox_inches='tight')




# %%
