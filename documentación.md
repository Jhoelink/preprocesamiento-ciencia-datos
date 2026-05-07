# Informe de Proyecto: Control de Versiones y Preprocesamiento de Datos

**Institución:** Universidad Nacional de Chimborazo  
**Facultad:** Ingeniería  
**Carrera:** Ciencia de Datos  
**Asignatura:** Cultura Digital y Sociedad  
**Estudiante:** [William Joel Macias Muñoz]  
**Repositorio:** [(https://github.com/Jhoelink/preprocesamiento-ciencia-datos.git)]

---

## 1. Introducción
Este proyecto tiene como objetivo aplicar de manera práctica el uso de **Git y GitHub** para la gestión de versiones y la colaboración en proyectos de Ciencia de Datos. 

Las funcionalidades implementadas incluyen:
* **Control de versiones:** Uso de ramas (`features`) para el desarrollo de código de manera aislada.
* **Preprocesamiento de datos:** Implementación de un script en Python utilizando la librería **Pandas** para la limpieza y preparación de datasets.
* **Automatización:** Configuración de flujos de trabajo automáticos para validar la integridad del código.

## 2. Comandos Git Utilizados
Para el desarrollo del proyecto se emplearon los siguientes comandos fundamentales:

* `git clone`: Utilizado para clonar el repositorio remoto en el entorno de trabajo local.
  
  <img width="1327" height="255" alt="image" src="https://github.com/user-attachments/assets/0629e727-4074-4600-a58e-1c761c87f9a2" />

  
* `git config`: Empleado para configurar el nombre de usuario y correo electrónico del autor.
  
  <img width="1327" height="78" alt="image" src="https://github.com/user-attachments/assets/676bba02-b07a-4acf-8507-37bbbfcc39e6" />

* `git checkout -b [nombre-rama]`: Comando para crear una nueva rama y cambiarse a ella inmediatamente.
  
  <img width="703" height="82" alt="image" src="https://github.com/user-attachments/assets/b1b00f51-e73b-46f4-a64c-d320415a37ba" />

* `git add`: Permite añadir archivos al área de preparación (staging area) para incluirlos en el próximo commit.

  <img width="768" height="85" alt="image" src="https://github.com/user-attachments/assets/1919e570-4018-4e31-aa3c-bd36a618aa6b" />

* `git commit -m "[mensaje]"`: Crea un registro en el historial con un mensaje descriptivo de los cambios realizados.

  <img width="690" height="117" alt="image" src="https://github.com/user-attachments/assets/c0688854-e659-4c56-a5fe-df5e95ec7302" />

* `git push origin [nombre-rama]`: Sube los cambios locales al repositorio remoto en GitHub.

<img width="754" height="269" alt="image" src="https://github.com/user-attachments/assets/111447ff-9317-40ef-bd82-4b5a4735fdd5" />

  
* `git merge`: Utilizado para fusionar la rama de características con la rama principal (`main`) tras la revisión de la Pull Request.

  <img width="912" height="369" alt="image" src="https://github.com/user-attachments/assets/5a68a1b8-9503-4bd3-beac-5b2a6f9edb61" />


## 3. Automatización: GitHub Actions

Se ha implementado un flujo de trabajo (workflow) en **GitHub Actions** que se activa automáticamente con cada evento de `push` o `pull request` en la rama principal. 

Este workflow realiza las siguientes tareas:
1.  Configura un entorno virtual con **Python 3.x**.
2.  Instala las dependencias necesarias (como `pandas` y `scikit-learn`).
3.  Ejecuta el script `preprocesamiento.py` para verificar que el código no contenga errores lógicos o de sintaxis antes de la integración fina.

## 4. Evidencias de Implementación

### A. Comandos ejecutados en la terminal
<img width="758" height="558" alt="image" src="https://github.com/user-attachments/assets/56c9cc4d-40bf-4597-a4c5-c0b1538149d3" />


### B. Pull Request y Fusión en GitHub
<img width="765" height="266" alt="image" src="https://github.com/user-attachments/assets/c0bd552b-5174-47ab-afbb-6ae8228832ca" />


### C. Ejecución de GitHub Actions

<img width="728" height="322" alt="image" src="https://github.com/user-attachments/assets/2e8d53eb-e050-4a3d-9f3d-5b64ae1a3e8a" />

---

