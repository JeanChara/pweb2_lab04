<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">GUÍA DE LABORATORIO</span><br />
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2023 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA DE PRESENTACION:</td><td>05/06/2023</td><td>HORA DE PRESENTACION:</td><td></td>
</tr>
<tr><td colspan="6">INTEGRANTE(S):
    <ul>
        <li>Chara Condori Jean Carlo</li>
    </ul>
</td>
</<tr>
<tr><td colspan="6">DOCENTE(s):
<ul>
<li>Mg. Anibal Sardon Paniagua</li>
</ul>
</td>
</<tr>
</tdbody>
</table>

# Python

## EJERCICIOS PROPUESTOS

- Para resolver los siguientes ejercicios sólo está permitido usar ciclos, condicionales, definición de listas por
comprensión, sublistas, map, join, (+), lambda, zip, append, pop, range.
• Implemente los metodos de la clase Picture.
Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en
las siguientes preguntas.
• Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a
draw):

- REPOSITORIO GITHUB: https://github.com/JeanChara/pweb2_lab04

- Código clase picture: 
    ![img](./img/img1.png)
    ![img](./img/img2.png)
    ![img](./img/img3.png)
    
    - Ejercicio2a (1): 

    ![img](./img/img4.png)

    - Utilizamos la función negative para hallar el color inverso de nuestra pieza, la función up para colocar
        nuestra pieza arriba de la otra, y la función join para unir estas piezas.
        Colocamos al caballo blanco encima de nuestro caballo negro, una vez realizado esto, la unimos con
        la otra columna(caballo negro sobre caballo blanco). 

    **- Ejecucion:**

    ![img](./img/img5.png)

    - Ejercicio2b (2): 

    ![img](./img/img6.png)

    - En este ejercicio añadimos la función horizontalMirror(), la cual cambiara de dirección a nuestra
        pieza, haciendo que mire hacia el otro lado. Al igual que el ejercicio2a (1), creamos nuestros
        caballos, los colocamos en columnas y los unimos. 


    **- Ejecucion:**

    ![img](./img/img7.png)
    

    - Ejercicio2c (3): 

    ![img](./img/img8.png)

    - En este ejercicio creamos la función horizontalRepeat, la cual repetirá nuestra pieza un numero
        determinado de veces, esta función concatena a las piezas, haciendo que se coloquen una al
        costado de otra (izquierda a derecha).

    **- Ejecucion:**

    ![img](./img/img9.png)

        - Ejercicio2d (4): 

    ![img](./img/img10.png)

    - En este ejercicio se nos pide crear una fila de un tablero de ajedrez, por lo que creamos los 2
        primeros cuadrados (blanco y negro) y los repetimos 4 veces, para crear una fila con 8 elementos.  

    **- Ejecucion:**

    ![img](./img/img11.png)

        - Ejercicio2e (5): 

    ![img](./img/img12.png)

    - Al igual que el anterior (Ejercicio2d), se nos pide crear una fila de cuadrados, solo que el orden de los
        cuadrados es diferente (negro y blanco).  

    **- Ejecucion:**

    ![img](./img/img13.png)

        - Ejercicio2f (6): 

    ![img](./img/img14.png)

    - Se crea la función verticalRepeat, la cual al igual que horizontalRepeat, creara varias veces un
        elemento o pieza, pero en columna, es decir, repetirá n veces el elemento hacia abajo.
        En este ejercicio se nos pide crear 4 filas intercaladas de cuadrados, por lo que creamos la variable
        fila, la cual almacenara una fila intercalada de cuadrados (iniciando con el blanco), luego, lo
        colocamos encima de nuestra fila con color negativo, utilizando la función verticalRepeat, lo
        haremos 2 veces para asi crear 4 filas, puesto que repite 2 veces la creación de 2 filas. 
 
    **- Ejecucion:**

    ![img](./img/img15.png)

        - Ejercicio2g (7): 

    ![img](./img/img16.png)

    - En este ejercicio se nos pide crear un tablero de ajedrez.
        Creamos la variable torres, la cual concatenara con join a todas las piezas en orden de juego, estas
        piezas se encuentran superpuestas a los cuadros respectivos, intercalando de color.
        Seguidamente creamos la variable peones, la cual creara con horizontalRepeat la fila de peones.
        Creamos la variable fila, la cual almacenara una fila de cuadros, repitiéndose 4 veces para llegar a 8
        elementos, luego en la variable espacio, la repetimos verticalmente 2 veces.
        Creamos las variables fichas y fichasN, las cuales almacenaran el orden de piezas para las fichas
        negras y blancas respectivamente, se utiliza la funcion up y negative para el orden y color.
        Finalmente, unimos las variables en la variable tablero, la cual colocara primero las fichas negras,
        luego el espacio y finalmente las fichas blancas. 


    **- Ejecucion:**

    ![img](./img/img17.png)



## SOLUCIÓN DEL CUESTIONARIO
- Explique: ¿Para qué sirve el directorio pycache? 
    
    Almacena el código utilizado por Python para almacenar caché, se utiliza con el propósito de
    aumentar el rendimiento de los scripts.
    Cuando se ejecuta un modulo mas de una vez, en lugar de compilar de nuevo, se busca el caché, en
    caso de encontrarse, se utiliza este mismo para ejecutarse de forma rápida. 



**III. CONCLUSIONES**

- Se utilizo módulos o “librerías” de Python (pygame) para la correcta realización de la práctica. Se ha practicado los temas en Python relacionados a objetos, métodos, funciones, arreglos (listas), ciclos, condicionales, entre otros aspectos básicos con el fin de reforzar nuestro conocimiento del mismo


**RETROALIMENTACIÓN GENERAL**

- REPOSITORIO GITHUB: https://github.com/JeanChara/pweb2_lab04

**REFERENCIAS Y BIBLIOGRAFÍA**
- [https://docs.python.org/3/library/array.html?highlight=pop#array.array.pop](https://docs.python.org/3/library/array.html?highlight=pop#array.array.pop)
- [https://docs.python.org/3/tutorial/introduction.html#lists](https://docs.python.org/3/tutorial/introduction.html#lists)
- [https://docs.python.org/3/glossary.html#term-function](https://docs.python.org/3/glossary.html#term-function)
- [https://docs.python.org/es/3/tutorial/classes.html](https://docs.python.org/es/3/tutorial/classes.html)
#

