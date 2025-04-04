<p align="center">
  <img src="imagenes/Logo_bicimad.png" alt="Bicimad" />
</p>

----------


# 🚲 Análisis Exploratorio de Datos (EDA) de BiciMAD
Este proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre el sistema de bicicletas públicas BiciMAD en Madrid, con el objetivo de validar hipótesis relacionadas con el uso y comportamiento del sistema.

## 📌 Objetivo
Validar, mediante análisis de datos, hipótesis sobre el uso de bicicletas, su localización y su relación con patrones de movilidad urbana en Madrid.Ademas este proyecto es evaluar la utilidad y eficiencia del sistema de bicicletas públicas BiciMAD como alternativa de movilidad sostenible en la ciudad de Madrid.

## 🧪 Hipótesis
📍 Las estaciones están ubicadas en sitios clave con alto aforo de personas.

⏰ Existe buena disponibilidad de bicicletas en horas pico.

🧳 Las bicicletas se usan para hacer turismo.

📆 Las bicicletas se usan más los fines de semana que entre semana.

## 📊 Dataset
Se utilizan datos históricos de BiciMAD, incluyendo:

### 📦 Enlaces Fuentes de Datos

<p><strong>- Alta de usuarios y usos por día del servicio público de bicicleta eléctrica</strong><br>
<a href="https://datos.madrid.es/sites/v/index.jsp?vgnextoid=6d8bdae2be63c410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD" target="_blank">
  Ver datos
</a></p>

<p><strong>- BiciMAD. Datos de la situación de estaciones bicimad por día y hora</strong><br>
<a href="https://datos.madrid.es/sites/v/index.jsp?vgnextoid=f4b07e0543815610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD" target="_blank">
  Ver datos
</a></p>

<p><strong>- BiciMAD. Datos de los itinerarios de las bicicletas eléctricas</strong><br>
<a href="https://datos.madrid.es/sites/v/index.jsp?vgnextoid=d67921bb86e64610VgnVCM2000001f4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD" target="_blank">
  Ver datos
</a></p>

<p><strong>- BiciMAD. Bases del servicio público de bicicleta eléctrica de la ciudad de Madrid</strong><br>
<a href="https://datos.madrid.es/sites/v/index.jsp?vgnextoid=e9b2a4059b4b7410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD" target="_blank">
  Ver datos
</a></p>

<p><strong>- BiciMAD. Disponibilidad de unidades (bicicletas) del servicio público de bicicleta eléctrica</strong><br>
<a href="https://datos.madrid.es/sites/v/index.jsp?vgnextoid=7547ff52e4a4f410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD" target="_blank">
  Ver datos
</a></p>

<p><strong>- Aforos de peatones y bicicletas</strong><br>
<a href="https://datos.madrid.es/sites/v/index.jsp?vgnextoid=695cd64d6f9b9610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD" target="_blank">
  Ver datos
</a></p>

<p><strong>- Afluencia Turistas del 2022 en Madrid</strong><br>
<a href="https://www.ine.es/jaxiT3/Tabla.htm?t=10823" target="_blank">
  Ver datos
</a></p>

## Conclusiones

Es BiciMAD eficiente? En grandes razgos si:
- Hay estaciones suficientes, pero no siempre suficientes bicicletas.
- Hay cierta desconexion entre la infraestructura y la demanda real.
- El sistema puede cubrir incluso un uso peatonal masivo, pero con ajustes.
- El turismo influye, pero no es el factor principal.


## 📦 Requisitos e instalación

Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes librerías de Python. Puedes instalarlas con `pip`.

### 🔧 Instalación
```python
pip install pandas
pip install numpy
pip install json
pip install xlrd
pip install datetime 
pip install os
pip isntall geopandas
pip isntall shapely
pip isntall pyproj
pip install pyogrio
pip install shapely
pip install seaborn
pip install matplotlib
pip install folium
pip install plotly
```
### 📥 Lectura de Repositiorio
```python
git clone https://github.com/Krvelez92/EDA-BICIMAD.git
cd EDA-BICIMAD
```
## 📂 Estructura del proyecto

```python
eda-bicimad/
│
├── src/data/          # Datos originales y preprocesados
├── src/notebooks/     # Jupyter Notebooks de prueba y utils
├── imagenes           # Gráficos exportados y logos
├── src/               # codigo 
├── src/memoria.ipynb  # Notebook de EDA
└── README.md
```


