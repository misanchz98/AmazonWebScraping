# AmazonWebScraping

## Descripción:

El objetivo de este proyecto es, a partir de la técnica de **web scraping**, la obtención de un listado (**en formato csv**) de las 10 mejores opciones de tarjetas gráficas valoradas por los clientes y que entran en el rango de precio deseado. En este caso, se usará la página web [https://www.amazon.es/](https://www.amazon.es/) y se aplicarán los siguientes filtros en la búsqueda:
- **Precio:** 50 - 100 EUR
- Valoración media de los clientes

Los datos recopilados sobre cada tarjeta gráfica son los que se exponen a continuación:
- Título (*title*)
- Valoración (*assessment*)
- Precio (*price*)
- Tamaño de RAM (*RAM_size*)
- Tipo de RAM (*RAM_type*)
- Tarjeta gráfica (*graphic_card*)
- Velocidad de memoria (*memory_speed*)

## Instrucciones de uso:

## 1. Instalación requisitos

Antes de ejecutar el *script* que realizará la tarea descrita en la sección anterior, es necesario instalar las librerías precisas para su correcto funcionamiento:
```
cd AmazonWebScraping
pip install -r requirements.txt
```

## 2. Ejecución del *script* (Windows)

- **Símbolo del Sistema (cmd):**
```
amazon_scraper.bat
```
- **PowerShell:**
```
./amazon_scraper.bat
```

Finalizada la ejecución, aparecerá en el directorio *amazon_scraper* el fichero **items.csv**. El fichero incluirá la información recopilada sobre las 10 tarjertas gráficas con mejor valoración y dentro del rango de 50 - 100 EUR.

**NOTA:** Si el fichero **items.csv** existe antes de ejecutar el *script*, al llevar a cabo su ejecución, este será eliminado y sustituido por un nuevo fichero del mismo nombre con los nuevos datos.

## A tener en cuenta:
- Este proyecto utiliza el driver **ChromeDriver 105.0.5195.52**, si esta versión no es compatible con su navegador de Google Chrome, puede descargar una versión que sí sea compatible en (https://chromedriver.chromium.org/downloads)[https://chromedriver.chromium.org/downloads]. Una vez terminada su descarga, debe situar el fichero chromedriver.exe dentro del directorio *amazon_scraper/driver*. 
- Si el fichero **items.csv** existe antes de ejecutar el *script* (amazon_scraper.bat), al llevar a cabo su ejecución, este será eliminado y sustituido por un nuevo fichero del mismo nombre con los nuevos datos.