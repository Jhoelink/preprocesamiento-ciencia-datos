# Informe de Proyecto: Control de Versiones y Preprocesamiento de Datos

**Institución:** Universidad Nacional de Chimborazo  
**Facultad:** Ingeniería  
**Carrera:** Ciencia de Datos  
**Asignatura:** Cultura Digital y Sociedad  
**Estudiante:** [William Joel Macias Muñoz]  
**Repositorio:** [[Pega aquí el enlace a tu repositorio de GitHub](https://github.com/Jhoelink/preprocesamiento-ciencia-datos.git)]

---

## 1. Introducción
[cite_start]Este proyecto tiene como objetivo aplicar de manera práctica el uso de **Git y GitHub** para la gestión de versiones y la colaboración en proyectos de Ciencia de Datos[cite: 23]. 

Las funcionalidades implementadas incluyen:
* [cite_start]**Control de versiones:** Uso de ramas (`features`) para el desarrollo de código de manera aislada[cite: 66].
* [cite_start]**Preprocesamiento de datos:** Implementación de un script en Python utilizando la librería **Pandas** para la limpieza y preparación de datasets[cite: 24, 67].
* [cite_start]**Automatización:** Configuración de flujos de trabajo automáticos para validar la integridad del código[cite: 82].

## 2. Comandos Git Utilizados
Para el desarrollo del proyecto se emplearon los siguientes comandos fundamentales:

* [cite_start]`git clone`: Utilizado para clonar el repositorio remoto en el entorno de trabajo local[cite: 59, 61].
* [cite_start]`git config`: Empleado para configurar el nombre de usuario y correo electrónico del autor[cite: 62, 63, 64].
* [cite_start]`git checkout -b [nombre-rama]`: Comando para crear una nueva rama y cambiarse a ella inmediatamente[cite: 66].
* [cite_start]`git add`: Permite añadir archivos al área de preparación (staging area) para incluirlos en el próximo commit[cite: 68].
* [cite_start]`git commit -m "[mensaje]"`: Crea un registro en el historial con un mensaje descriptivo de los cambios realizados[cite: 69].
* [cite_start]`git push origin [nombre-rama]`: Sube los cambios locales al repositorio remoto en GitHub[cite: 69].
* [cite_start]`git merge`: Utilizado para fusionar la rama de características con la rama principal (`main`) tras la revisión de la Pull Request[cite: 72].

## 3. Automatización: GitHub Actions
[cite_start]Se ha implementado un flujo de trabajo (workflow) en **GitHub Actions** que se activa automáticamente con cada evento de `push` o `pull request` en la rama principal[cite: 82]. 

Este workflow realiza las siguientes tareas:
1.  Configura un entorno virtual con **Python 3.x**.
2.  Instala las dependencias necesarias (como `pandas` y `scikit-learn`).
3.  [cite_start]Ejecuta el script `preprocesamiento.py` para verificar que el código no contenga errores lógicos o de sintaxis antes de la integración final[cite: 92].

## 4. Evidencias de Implementación
[cite_start]*(A continuación, se presentan las capturas de pantalla que validan la ejecución de las tareas solicitadas)*[cite: 83].

### A. Comandos ejecutados en la terminal
> [cite_start]**[Insertar captura de pantalla de la terminal aquí]** > *(Se deben visualizar los comandos git add, commit y push)*[cite: 90].

### B. Pull Request y Fusión en GitHub
> [cite_start]**[Insertar captura de pantalla de la Pull Request aquí]** > *(Se debe ver el historial de la PR aceptada y la fusión con la rama main)*[cite: 91].

### C. Ejecución de GitHub Actions
> [cite_start]**[Insertar captura de pantalla de la pestaña 'Actions' aquí]** > *(Se debe mostrar el check verde indicando que el flujo de trabajo terminó con éxito)*[cite: 92].

---

## 5. Bibliografía
* Chacon, S., & Straub, B. (2014). *Pro Git*. [cite_start]Apress[cite: 97].
* McKinney, W. (2018). *Python for Data Analysis*. [cite_start]O'Reilly Media[cite: 98].