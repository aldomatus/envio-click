<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://i.imgur.com/19coMSB.png" alt="Header" >
  </a>
   <div align="center">
   <a href="https://www.facebook.com/aldo.matusmartinez" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/facebook.svg" title="Facebook" width="60"  margin="30px"/></a><a href="https://github.com/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/github.svg" title="Github" width="60"/></a><a href="https://www.instagram.com/aldomatus1/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/instagram.svg" title="Instagram" width="60"  /></a><a href="https://www.linkedin.com/in/aldomatus/" ><img src="https://github.com/edent/SuperTinyIcons/blob/master/images/svg/linkedin.svg" title="Linkedin" width="60"  /></a>

  </div>
  <h1 align="center">THIS PROJECT WAS MADE FOR Envioclick® 🚚📦</h1>
  <h3 align="center">Learn REST API with Flask, Mysql and Docker</h3>

  <p align="center">
    A project to work with flask REST api with docker and the mysql database manager!
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project 🚀
### Sección A.
#### A1
Sin hacer uso de librerías o funciones nativas. Hacer un programa que tomando una
palabra o párrafo:
* Contar cuántas vocales hay.
* Reemplazar las vocales por la vocal consecutiva (ejemplo: “hacer” se cambia a
“hecir”).
#### A2
Sin hacer uso de librerías o funciones nativas. Escribe un programa el cual tomando un
conjunto de datos con sus atributos (Figura A):
* Ordenar los datos de acuerdo al nivel de prioridad (padre, hijo).
* Utilizar un método llamado show() que permita visualizar los datos ordenados.
* Utilizar un método llamado addData() que permita ingresar un nuevo dato (o
conjunto de datos) y ajustar necesario para colocar el dato en la posición adecuada.
#### A3
De los ejercicios anteriores:
* Escribe las pruebas unitarias necesarias.
##### Input example
```json
{
    "DataA": {
                "name": "One name",
                "Level": "One",
                "Priority": "Highest",
                "SubdataA": {
                            "name": "One nameSubdataA",
                            "Level": "One",
                            "Priority": "Highest",
                            },
                "SubdataA2": {
                            "name": "One nameSubdataA2",
                            "Level": "Two",
                            "Priority": "High",
                            "SubdataAA": {
                                        "name": "One nameSubdataAA",
                                        "Level": "One",
                                        "Priority": "Highest",
                                        }
                            }
    },

    "DataB": {
            "name": "One nameB",
            "Level": "Two",
            "Priority": "Highest",
            "SubdataB":
                    {
                        "name": "One nameSubdataB",
                        "Level": "One",
                        "Priority": "Highest",
                    }
        }
}
```
##### Options:
"Priority": "Highest, High, Medium, Low, Lowest"
"Level": "One, two....",

##### Insert data (example input):
```json
"DataC": {
"name":"One nameC"
"Level": "One",
"Priority": "High",
}
```
 <img src="https://i.imgur.com/qqKeA0x.png" alt="Header" width="400" >
 
### Sección B.
#### B2
Realiza el esquema DB y normaliza como creas conveniente para lo siguiente:
* Aplicación para gestionar una flota de vehículos, en donde una persona puede tener n vehículos asignados pero solo puede manejar uno. Cada asignación de vehículo tiene una fecha de expiración.
#### B3
Haciendo uso del ejercicio anterior, utiliza un ORM (de tu preferencia) para realizar el
modelado y migraciones correspondientes.
* Al realizar el modelado contempla los diversos escenarios del ejercicio anterior (es decir, anexar nuevos vehículos a una persona, las fechas de expiración, etc).
* Desde tu perspectiva, qué mejoras implementarías?

### Sección C.
#### C1
Basado en la siguiente HU (Historia de usuario), define las pruebas a realizar:
* Como Cliente, quiero suscribirme a un canal Premium por períodos flexibles de
tiempo por medio del sitio web.

#### C2
De los ejercicios de la sección A y B:
* ¿Que powerup(mejora) desarrollarias y por que?.
* Ejecuta un analizador de sintaxis Flake8 y el analizador de complejidad, del
resultado obtenido:
  * Explica que mejoras harías a tu código?.
  * Qué estándar utilizaste para la evaluación del sintaxis?.

### Built With

This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Mysql](https://www.mysql.com/)
* [Docker](https://www.docker.com/)

### Libraries

#### SQLAlchemy (Offers an ORM along with a Core)
The Python SQL Toolkit and Object Relational Mapper
SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.

#### Flask-SQLAlchemy 
Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application. It aims to simplify using SQLAlchemy with Flask by providing useful defaults and extra helpers that make it easier to accomplish common tasks.

#### Flask JWT
JSON Web Tokens (or JWTs) provide a means of transmitting information from the client to the server in a stateless, secure way.
On the server, JWTs are generated by signing user information via a secret key, which are then securely stored on the client. This form of auth works well with modern, single page applications. 

<!-- GETTING STARTED -->
## Getting Started
### To check your rest api
#### Insomnia

With their streamlined API client, you can quickly and easily send REST, SOAP, GraphQL, and GRPC requests directly within Insomnia.
Link to visit insomnia website: - [Link](https://insomnia.rest/download)
<div align="center">
 <img src=https://seeklogo.com/images/I/insomnia-logo-A35E09EB19-seeklogo.com.png width="150" alt="Header" >
  </div>


#### Postman
Postman is a collaboration platform for API development. Postman's features simplify each step of building an API and streamline collaboration so you can create better APIs—faster.
Link to visit postman website: - [Link](https://www.postman.com/downloads/)
<div align="center">
 <img src=https://seeklogo.com/images/P/postman-logo-F43375A2EB-seeklogo.com.png width="150" alt="Header" >
</div>


### Prerequisites
For this project you need to have Docker and Docker installed

<ol>
<li>Link to install Docker engine:</li>
<a href="https://docs.docker.com/engine/install/ubuntu/">Linux</a>
<a href="https://docs.docker.com/engine/install/">  -  Windows or Mac</a>

<li>After installing docker engine install docker compose</li>
<a href="https://docs.docker.com/compose/install/">Linux Windows Mac</a>
</li>


### Aplicación para gestionar una flota de vehículos 🚚📦
<div align="center">
 <img src=https://blog.llerandi.com/hubfs/flota%20de%20vehiculos.jpg width=500 alt="Header" >
</div>

#### Entity relationship model

<div align="center">
 <img src=https://i.imgur.com/FmXAdqu.png width="800" alt="Header" >
  </div>

For the construction of the database, the relationship entity model was made with which the relationships between each table were deduced. 
<div align="center">
 <img src=https://i.imgur.com/63jXTbK.png width=1000 alt="Header" >
</div>


Para la construccion de la base de datos se tomaron en cuenta los siguientes aspectos:
* Las principales entidades a guardar seran: vehiculos, conductores y asignaciones
* Se elaborá una tabla para cada entidad
* La tabla que hará las relaciones entre conductores y vehiculos será la tabla de asignaciones por lo que contendrá las llaves foraneas de cada entidad
* Un conductor puede tener asignado varios autos pero un auto puede estar asignado a un solo conductor

##### Tabla drivers
<div align="center">
 <img src=https://i.imgur.com/UovtKxz.png width=400 alt="Header" >
</div>

Descripción:
* La llave primaria será un objeto de tipo UUIDType que será la llave con la que relacionaremos con los vehiculos a cada conductor
* El email empresarial del conductor será una llave unica que lo identificará junto a su id (Elegiremos el email por su facilidad de memorizar y manejar) 
* Tendremos un valor único que es el Número de Identificación Vehicular VIN (Vehicle Identification Number) consta de 17 caracteres alfanuméricos 
* La tabla contendrá otros datos del conductor como nombre, fecha de nacimiento (dob), tipo de crdencial con la que cuenta, telefono etc.


##### Tabla vehicles
<div align="center">
 <img src=https://i.imgur.com/Bwy81FS.png width=400 alt="Header" >
</div>

Descripción:
* La llave primaria será un objeto de tipo UUIDType que será la llave con la que relacionaremos con los conductores a cada vehiculo
* Tendremos un valor único que es el Número de Identificación Vehicular VIN (Vehicle Identification Number) consta de 17 caracteres alfanuméricos 
* La tabla contendrá otros datos del vehiculo como: marca, modelo, maxima carga permitida, tipo de vehiculo y otras


##### Tabla assignments
<div align="center">
 <img src=https://i.imgur.com/1pRaSu1.png width=400 alt="Header" >
</div>

Descripción:
* La llave primaria será un objeto de tipo UUIDType 
* Relacionaremos dos llaves foraneas (llave foranea de vehicle y driver)
* Las asignaciones son unicas es decir no se puede repetir una asignacion con mismo id de vehiculo y driver
* La tabla contendrá otros datos de la asignacion como: fecha, si ya ha expirado, notas, área etc.

### Installation 🖥

1. To obtain my repository you must create a folder in a desired directory and within this folder open a terminal or use cmd in the case of windows.
2. Clone the repo
   ```
   git clone git@github.com:aldomatus/envio-click.git
   
   ```
3. Move to envio_click directory
   ```
   cd envio_click/A/A2
   
   ```
4. Build Docker container
   ```
   docker build -t fleet_local:local_latest . ;
   ```
   
4. Build Docker container
   ```
   docker build -t fleet_local:local_latest . ;
   ```
   
5. Run Docker container
   ```
   docker run --rm -d -it --env-file=.env -v ${PWD}:/usr/src/app -p 5022:5000 --name fleet_local fleet_local:local_latest;
   ```
6. To see the logs at runtime
   ```
   docker logs -f fleet_local;
   ```



