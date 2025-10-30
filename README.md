#### **Descripción**



Este proyecto es un conversor de divisas escrito en Python que obtiene las tasas de cambio actualizadas desde una API pública

Permite ingresar un monto y una divisa de origen, y muestra su equivalente en varias monedas de destino.



#### **Tecnologías utilizadas**



***-Python 3.10+***

***-Requests*** (Obtener datos de la API)

***-JSON*** (manejar respuestas de la API)



#### **Como ejecutar el programa**

1. Clona este repositorio:

 

   git clone https://github.com/ThomasAlfaro/currency-converter.git

   cd currency-converter



2\. Instala dependencias:



   pip install -r requirements.txt



3\. Ejecuta el código:

 

   python converter.py





#### **Ejemplos de uso**



Ingrese el monto: 100

Ingrese divisa: usd





Conversión de 100.00000000 usd

(tasas actualizadas diariamente desde Github)

---

Moneda           Tasa            Monto

---

EUR             0.9254           92.54

ARS           1043.2500      104,325.00

...

---





#### **Funcionalidades**



* Validación de monto ingresado (solo números mayores a 0).



* Validación de código de divisa (3 letras y dentro de una lista permitida).



* Llamada a una API externa para obtener las tasas actualizadas.



* Presentación clara de los resultados en formato tabular.





#### 

#### **Aprendizajes**



###### *Este proyecto fue desarrollado como práctica para aprender:*



* Manejo de excepciones (try / except).



* Uso de APIs y formato JSON.



* Buenas prácticas de organización de código y documentación.





#### **Autor**



Thomas Alfaro

Fecha: 29/10/2025

Repositorio: https://github.com/ThomasAlfaro/currency-converter

