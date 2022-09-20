# AmazonWebScraping

## Descripción:

El objetivo de este proyecto es, a partir de la técnica de **web scraping**, la obtención de un listado (en formato csv) de las 10 mejores opciones de tarjetas gráficas valoradas por los clientes y que entran en el rango de precio deseado. Para ello se usara la página web [https://www.amazon.es/](https://www.amazon.es/) y se aplicarán los siguientes filtros en la búsqueda:
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

```
pip install -r requirements.txt
```