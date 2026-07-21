Taller 3 — Lógica difusa
========================

.. rst-class:: workshop-label

   RAZONAMIENTO BAJO INCERTIDUMBRE

Descripción
-----------

En este taller el estudiante diseñará un sistema de inferencia difusa capaz
de tomar decisiones utilizando variables lingüísticas y reglas aproximadas.

La actividad permitirá representar expresiones como ``temperatura alta``,
``velocidad media`` o ``riesgo bajo`` mediante grados de pertenencia entre
cero y uno.

Objetivos de aprendizaje
------------------------

Al finalizar el taller, el estudiante estará en capacidad de:

* Diferenciar conjuntos clásicos y conjuntos difusos.
* Definir variables lingüísticas.
* Construir funciones de pertenencia.
* Diseñar reglas difusas.
* Ejecutar procesos de fuzzificación e inferencia.
* Obtener una salida mediante defuzzificación.
* Implementar una solución con SciKit-Fuzzy.

Conceptos previos
-----------------

* Incertidumbre y vaguedad.
* Conjuntos difusos.
* Grados de pertenencia.
* Variables lingüísticas.
* Funciones de pertenencia.
* Reglas difusas.
* Fuzzificación.
* Inferencia.
* Defuzzificación.

Flujo del sistema
-----------------

.. container:: fuzzy-flow

   **Entradas numéricas**

   ↓

   **Fuzzificación**

   ↓

   **Evaluación de reglas lingüísticas**

   ↓

   **Agregación de resultados**

   ↓

   **Defuzzificación**

   ↓

   **Salida numérica o decisión**

Desarrollo del taller
---------------------

.. container:: workshop-steps

   **1. Definición del problema**

   Seleccionar un proceso en el que existan decisiones aproximadas.

   **2. Identificación de variables**

   Definir variables de entrada y salida.

   **3. Funciones de pertenencia**

   Construir las categorías lingüísticas de cada variable.

   **4. Base de reglas**

   Formular las reglas que representan el conocimiento del experto.

   **5. Implementación**

   Construir el sistema utilizando Python y SciKit-Fuzzy.

   **6. Experimentación**

   Evaluar diferentes combinaciones de entrada y analizar la salida obtenida.

Entregables
-----------

* Definición del problema.
* Variables de entrada y salida.
* Gráficas de funciones de pertenencia.
* Base de reglas.
* Código fuente.
* Pruebas de funcionamiento.
* Análisis de resultados.

.. important::

   No basta con que el programa produzca una salida. El estudiante deberá
   explicar cómo las funciones de pertenencia y las reglas influyen en la
   decisión final.