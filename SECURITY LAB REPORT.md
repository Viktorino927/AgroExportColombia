SECURITY LAB REPORT

Implementación Práctica de Snyk CLI y Snyk Code

Información General

Proyecto

AgroExportColombia



Repositorio

https://github.com/Viktorino927/AgroExportColombia



Herramientas utilizadas

Snyk Open Source (SCA)

Snyk Code (SAST)

Cursor IDE

GitHub

Python

Django

Git

Auditor

Victor Mauricio Correa García



Fecha

Noviembre 2026



1\. Introducción

La seguridad del software se ha convertido en un componente fundamental dentro del proceso de desarrollo, especialmente en aplicaciones que gestionan información de usuarios y procesos de negocio. En este contexto, las prácticas DevSecOps promueven la integración de actividades de seguridad desde las primeras etapas del ciclo de vida del software, permitiendo identificar y corregir vulnerabilidades antes de que lleguen a entornos de producción. Herramientas como Snyk facilitan este proceso mediante capacidades de análisis de dependencias (SCA) y análisis estático de código (SAST), ayudando a detectar riesgos asociados tanto a componentes de terceros como al código desarrollado internamente.



En la presente práctica se realizó una evaluación de seguridad sobre el proyecto AgroExportColombia utilizando Snyk CLI y Snyk Code para identificar, analizar y priorizar vulnerabilidades presentes en la aplicación. Durante el ejercicio se seleccionaron vulnerabilidades representativas de tipo SAST y SCA, se analizó su impacto sobre la confidencialidad, integridad y disponibilidad de la información, se determinaron sus causas raíz y se aplicaron acciones de remediación. Finalmente, se efectuaron reescaneos de validación para verificar la efectividad de las correcciones implementadas y se propusieron controles preventivos orientados a fortalecer la seguridad del proceso de desarrollo mediante un enfoque Shift-Left.



2\. Objetivos

2.1 Objetivo General

Evaluar la seguridad del proyecto AgroExportColombia mediante la implementación práctica de Snyk CLI, aplicando análisis SCA y SAST para identificar, analizar, remediar y verificar vulnerabilidades presentes tanto en dependencias de terceros como en el código fuente de la aplicación.



2.2 Objetivos Específicos

Identificar vulnerabilidades de seguridad en dependencias y componentes de software mediante las capacidades SCA y SAST de Snyk, determinando su severidad, impacto y riesgo potencial.



Analizar técnicamente los hallazgos encontrados, estableciendo su causa raíz, impacto sobre la confidencialidad, integridad y disponibilidad de la información y su relación con OWASP, CVE y CWE.



Implementar acciones de remediación y validar su efectividad mediante reescaneos de seguridad, evidenciando la reducción de vulnerabilidades y fortaleciendo la postura de seguridad del proyecto.



3\. Resumen Ejecutivo

Se realizó una evaluación de seguridad sobre el proyecto AgroExportColombia utilizando Snyk Open Source para el análisis de dependencias (SCA) y Snyk Code para el análisis estático de código (SAST). El objetivo fue identificar vulnerabilidades presentes tanto en componentes de terceros como en el código fuente desarrollado para la aplicación.



Como resultado se identificaron vulnerabilidades de alta y crítica severidad, entre las que destacan Open Redirect, SQL Injection y HTTP Request Smuggling. Posteriormente se ejecutaron acciones de remediación mediante actualización de dependencias y correcciones en el código fuente. Finalmente se realizaron reescaneos con Snyk para validar que las vulnerabilidades seleccionadas fueron eliminadas satisfactoriamente.



4\. Metodología y Alcance

Instalación de Node.js, npm y Snyk CLI.

Autenticación mediante Snyk.

Verificación del entorno de análisis.

Ejecución de análisis SCA:

snyk test

snyk test --severity-threshold=high

snyk monitor

Ejecución de análisis SAST:

npx snyk code test

Selección de vulnerabilidades.

Interpretación del riesgo.

Identificación de causa raíz.

Remediación.

Reescaneo y validación.

Definición de controles preventivos y prácticas Shift-Left.



5\. Matriz Obligatoria de Vulnerabilidades

\#	Hallazgo	SAST/SCA	CVE/CWE	Severidad	CVSS	Riesgo real	Estado

1	Open Redirect	SAST	CWE-601	High	No reportado	Redirección de usuarios hacia sitios maliciosos y riesgo de phishing.	Corregido

2	SQL Injection (Django 5.2.8)	SCA	SNYK-PYTHON-DJANGO-15198931 / 15198932	Critical	Critical	Compromiso de la base de datos, lectura y modificación de información.	Corregido

3	HTTP Request Smuggling (h11 0.14.0)	SCA	SNYK-PYTHON-H11-10293728	Critical	Critical	Manipulación de solicitudes HTTP y evasión de controles de seguridad.	Corregido

6\. Vulnerabilidad 1 – Open Redirect (SAST)

Hallazgo Inicial

Figura: Hallazgo Open Redirect identificado por Snyk Code.





Ficha Técnica

Campo	Valor

Tipo	SAST

Vulnerabilidad	Open Redirect

Severidad	High

CWE	CWE-601

Archivo	agro\_export/views.py

Línea	121

CVE	No aplica

Estado	Corregida

Interpretación del Riesgo

La vulnerabilidad permite la redirección de usuarios hacia sitios externos no autorizados mediante el uso de parámetros manipulados. Un atacante podría utilizar esta condición para ejecutar campañas de phishing o engañar a usuarios legítimos.



Impacto CIA

Principio	Impacto

Confidencialidad	Alto

Integridad	Medio

Disponibilidad	Bajo

Causa Raíz

El parámetro HTTP recibido por la aplicación era utilizado directamente en la función redirect() sin una validación adecuada.



Código vulnerable

next\_page = request.GET.get('next', 'home')

return redirect(next\_page)

Corrección Aplicada

next\_page = request.GET.get('next')



allowed\_pages = \['home', 'dashboard', 'perfil']



if next\_page not in allowed\_pages:

&#x20;   next\_page = 'home'



return redirect(next\_page)

Evidencia Antes / Después

Insertar:



Captura del hallazgo original.

Captura del código corregido.

Verificación

Comando ejecutado:



npx snyk code test

Resultado:



CWE-601 -> No results

7\. Vulnerabilidad 2 – SQL Injection (SCA)

Hallazgo Inicial

Figura: Vulnerabilidad SQL Injection identificada en Django 5.2.8.



Ficha Técnica

Campo	Valor

Tipo	SCA

Dependencia	Django

Versión vulnerable	5.2.8

Vulnerabilidad	SQL Injection

Severidad	Critical

Referencia	SNYK-PYTHON-DJANGO-15198931

Referencia	SNYK-PYTHON-DJANGO-15198932

Versión segura	5.2.17 / 5.2.18

Interpretación del Riesgo

Una explotación exitosa podría permitir acceso, modificación o eliminación de información de la base de datos.



Impacto CIA

Principio	Impacto

Confidencialidad	Crítico

Integridad	Crítico

Disponibilidad	Alto

Causa Raíz

Uso de una versión vulnerable del framework Django.



Remediación

Antes

Django==5.2.8

Después

Django==5.2.18

Evidencia Antes / Después

Insertar:



Captura de Django vulnerable.

Captura del requirements.txt actualizado.

Captura de pip show django.

Verificación

Comando ejecutado:



snyk test --severity-threshold=high

Resultado:



Los identificadores asociados a Django ya no se encuentran presentes.



8\. Vulnerabilidad 3 – HTTP Request Smuggling (SCA)

Hallazgo Inicial

Figura: Vulnerabilidad HTTP Request Smuggling identificada en h11 0.14.0.



Ficha Técnica

Campo	Valor

Tipo	SCA

Dependencia	h11

Versión vulnerable	0.14.0

Vulnerabilidad	HTTP Request Smuggling

Severidad	Critical

Referencia	SNYK-PYTHON-H11-10293728

Versión segura	0.16.0

Interpretación del Riesgo

Un atacante podría manipular solicitudes HTTP especialmente construidas para alterar el procesamiento de peticiones entre servidores y componentes de infraestructura.



Impacto CIA

Principio	Impacto

Confidencialidad	Alto

Integridad	Alto

Disponibilidad	Alto

Causa Raíz

Uso de una versión vulnerable de la dependencia h11.



Remediación

Antes

h11==0.14.0

Después

h11==0.16.0

Evidencia Antes / Después

Insertar:



Captura del hallazgo original.

Captura de actualización de h11.

Captura de instalación satisfactoria.

Verificación

Comando ejecutado:



snyk test

Resultado:



El identificador asociado a h11 ya no aparece en el reescaneo posterior.



9\. Comparación Antes / Después

Vulnerabilidad	Antes	Después

Open Redirect	Presente	Corregida

SQL Injection (Django)	Presente	Corregida

HTTP Request Smuggling (h11)	Presente	Corregida

Métricas de análisis

Métrica	Resultado

Dependencias analizadas	57

Issues iniciales	120

Issues High/Critical iniciales	69

Vulnerabilidades remediadas	3

10\. Evidencias de Reescaneo

Agregar:



Resultado de npx snyk code test.

Resultado de snyk test.

Resultado de snyk test --severity-threshold=high.

Evidencias "No results" para cada hallazgo corregido.

11\. Prevención y Shift-Left

Reglas de desarrollo seguro

Implementar políticas de validación de entradas y prohibir redirecciones basadas en parámetros no validados.



Semgrep

semgrep scan .

Permite identificar patrones inseguros antes del despliegue.



Hooks Pre-Commit

Implementar verificaciones automáticas usando:



Bandit

Semgrep

Black

Flake8

Secret Scanning

Utilizar:



GitGuardian

Gitleaks

TruffleHog

para detectar credenciales expuestas.



Quality Gate CI/CD

Commit

↓

Tests

↓

Snyk Test

↓

Semgrep

↓

Deploy

Bloqueo de Pull Request

Impedir despliegues con vulnerabilidades High o Critical.



Gestión continua de dependencias

Ejecutar periódicamente:



snyk test

snyk monitor

12\. Integración con Cursor + MCP

Durante la práctica se utilizó Cursor como entorno de desarrollo para revisar y corregir el código fuente del proyecto. No se configuró una integración MCP activa con Snyk. Los análisis fueron ejecutados mediante Snyk CLI y los resultados fueron revisados manualmente.



Cursor fue utilizado para:



Revisar vulnerabilidades.

Localizar código afectado.

Aplicar remediaciones.

Validar cambios antes del reescaneo.

La validación final siempre fue realizada mediante reescaneo de seguridad y revisión humana.



13\. Conclusiones

Snyk permitió identificar vulnerabilidades presentes tanto en dependencias externas como en componentes desarrollados dentro de la aplicación.



Las vulnerabilidades críticas identificadas fueron corregidas mediante actualización de dependencias y ajustes en el código fuente.



Los reescaneos confirmaron la efectividad de las acciones de remediación implementadas y evidenciaron la eliminación de los hallazgos seleccionados.



La incorporación de prácticas Shift-Left fortalece la seguridad del ciclo de desarrollo al permitir la detección y corrección temprana de vulnerabilidades.



14\. Anexos

Agregar en orden:



Instalación de Snyk.

Autenticación.

snyk whoami.

snyk test.

snyk test --severity-threshold=high.

snyk monitor.

npx snyk code test.

Evidencias de Open Redirect.

Evidencias de SQL Injection.

Evidencias de HTTP Request Smuggling.

Evidencias de remediación.

Evidencias de reescaneo.

