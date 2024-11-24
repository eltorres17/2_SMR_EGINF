<!-- Con # se ponen los títulos -->
# Introducción a la criptografia

<!-- Así se pone una imagen -->
![Logo Alberties](assets/logo-crypto.png)

---

## ¿Qué es la criptografía? 

Es la disciplina que estudia las técnicas para transformar la información desde su formato original a otro que permita protegerla del acceso por parte de usuarios no autorizados de forma que se pueda prevenir cualquier adulteración y certificar su procedencia.

---

## ¿Qué objetivos buscamos con el uso de la criptografía?

* **Confidencialidad:** Asegurar que la información sea consultada y utilizada solo por aquellas
personas que deban poder hacerlo según la voluntad del propietario o creador de la misma.
* **Integridad:** Garantizar que la información no sea alterada sin autorización.
* **No repudio:** Comprobar que las partes que participan en una trasacción son efectivamente
aquellas que dicen serlo y al mismo tiempo evitar que puedan negarlo.

---

## Conceptos Básicos de Criptografía
* **Criptograma**: Mensaje cifrado que requiere una clave o método de descifrado.
* **Criptoanálisis**: Técnica utilizada para descifrar criptogramas sin conocer la clave, mediante métodos como la fuerza bruta y el análisis de frecuencias.
* **Clave**: Información o valor secreto que permite cifrar o descifrar un mensaje.

---

## Principales aplicaciones

* **Seguridad informática:** Proteger datos de usuarios almacenandándo de forma cifrada (encriptada) en
medios sistemas de archivos o bases de datos, proteger las comunicaciones en comunicaciones en línea,
como el tráfico de la web o los correo electrónicos, etc.
* **Comercio electrónico y finanzas en línea:** Protección de las transacciones en línea, en particular cuando
tienen que ver con dinero: compras, ventas, préstamos, cambio de divisas, etc. 
* **Firma digital:**  Verificación de la autenticidad de documentos electrónicos de manera digital.
* **Criptomonedas y cadenas de bloques:** Las monedas digitales que utilizan la criptografía para garantizar la seguridad y transparencia de las transacciones pero la tecnología subyacente de [cadena de bloques](https://es.wikipedia.org/wiki/Cadena_de_bloques?useskin=vector)
se utiliza justamente para asegurar la integridad e irrenunciabilidad de información legal, industrial y comercial


---

## ¿Cómo te impacta como desarrollador?

* Requiriendo que sepas implementar correctamente mecanismos de autenticación y autorización.
* Requiriendo que sepas como almacenar adecuadamente contraseñas y otros secretos en bases de datos.
* Requiriendo que sepas como inyectar secretos en tu código en tiempo de ejecución y durante el despliegue sin que los mismos sean parte de tu código fuente y mucho menos sean incluidos en repositorios bajo control de versiones.
* Requiriendo que puedas utilizar sumas de verificación y firmas digitales en tus procesos de IT para garantizar la integridad y no repudio de los datos.

---

## Tipos de criptografía que nos interesan

* **Criptografía de clave simétrica:** Se utiliza una única clave para cifrar y descifrar la información.
Es eficiente para comunicaciones donde las partes confían entre sí.

* **Criptografía de clave asimétrica:** Se utilizan dos claves diferentes, una pública y otra privada.
La clave pública se utiliza para cifrar la información, y la clave privada para descifrarla.
Es ideal para comunicaciones donde no hay confianza previa entre las partes.

* **Funciones hash:** Se utilizan para generar un resumen digital de la información.
Este resumen permite verificar la integridad de la información sin necesidad de descifrarla.

---

## Ejemplos de uso

* Cuando colocas una clave en un archivo comprimido con un programa como WinZip estas utilizando una clave simétrica
porque todos los que sepan esa clave podrán revertir el proceso de cifrado y obtener los archivos originales.
* Cuando utilizas PGP o GPG en tus correos o creas una billetera crypto estas utilizando una clave asimétrica.
De hecho, en el caso de las criptomonedas la dirección de la billetera se deriva de la llave pública.
* Cuando descargas paquetes de Linux desde un repositorio autorizado y conocido. Se utiliza en este caso una clave asimetrica, ya que primero hay que descargar y registrar una llave pública
que permite verificar que los paquetes provienen de una fuente oficial de la distribución o del proyecto opensource y no de una tercera parte que podría incluir en ellos código malicioso.
* Finalmente, un ejemplo muy conocido del uso de funciones de hashes para realizar sumas de verificación que te debería resultar familiar, consiste en descargar una imagen ISO que nos permite instalar un sistema operativo como Windows o alguna distribución de Linux empleando una memoria USB. Como el archivo es grande y puede tener varios
gigabytes el riesgo de que la información este corrupta por problemas en la descarga aumenta y antes de perder tiempo
intentando hacer la instalación con una imagen producto de una descarga fallida calculamos la suma de verificación y confirmamos la integridad del archivo descargado comprobando que tenemos la descarga correcta.

---

