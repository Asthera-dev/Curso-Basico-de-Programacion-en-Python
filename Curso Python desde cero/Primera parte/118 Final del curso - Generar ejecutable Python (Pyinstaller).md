# Ejecutables Python

Un ejecutable Python es un archivo independiente que contiene todo lo necesario para ejecutar un programa escrito en Python sin requerir que el usuario tenga instalado el intérprete de Python en su sistema.

En otras palabras, es un archivo ejecutable que encapsula un Script de Python y las dependencias necesarias, permitiendo que el programa se ejecute de manera autónoma en un entorno que no tiene Python instalado.

Existen varias herramientas en Python que permiten crear ejecutables, y una de las más comunes es **PyInstaller**.

Cuando utilizas **PyInstaller** para crear un ejecutable, este archivo incluye el intérprete de Python, es script Python y todas las bibliotecas o módulos necesarios para que el programa funcione.

La creación de ejecutables Python es útil para distribuir programas a usuarios que no están familiarizados con Python o que no desean instalar Python en sus sistemas. 

Ya que facilita la entrega de aplicaciones Python como archivos ejecutables independientes.

Estos archivos pueden ejecutarse directamente en el sistema operativo del usuario sin preocuparse por la instalación y configuración del entorno de Python.

Es importante tener en cuenta que, aunque la creación de ejecutables facilita la distribución de programas Python, también puede aumentar el tamaño del archivo y puede haber limitaciones dependiendo del sistema operativo y la arquitectura del hardware.

___
# Distribución de Programas: Generar Ejecutables con PyInstaller

Hasta este momento del curso, todos los programas que hemos desarrollado requieren que el usuario tenga instalado Python y un editor de código (como VS Code) para poder ejecutarse mediante la terminal. 

Sin embargo, en el mundo real, cuando entregamos un software a un cliente, a un profesor o a un amigo, no podemos pedirles que instalen Python ni que abran la consola para correr nuestro código. Necesitamos entregarles un archivo autónomo que funcione con un simple "doble clic".

Para lograr esto contamos con **PyInstaller**, una herramienta externa que congela nuestro código `.py`, empaqueta el intérprete de Python y todas las librerías necesarias en un único archivo ejecutable listo para distribuirse.

> **Nota importante sobre Sistemas Operativos:** PyInstaller genera el ejecutable para el sistema operativo desde el cual lo estás corriendo. 
> * Si lo ejecutas en **Windows**, generará un archivo `.exe`.
> * Si lo ejecutas en **macOS**, generará una aplicación `.app` / binario de Unix.
> * Si lo ejecutas en **Linux**, generará un binario ejecutable para Linux.

---

## Paso 0: Preparar tu código antes de empaquetar (¡Muy Importante!)

Cuando ejecutamos un programa en VS Code, la terminal permanece abierta al finalizar. Pero cuando abrimos un ejecutable con doble clic, **el sistema operativo cierra la ventana automáticamente en el instante en que se ejecuta la última línea de código**, impidiendo que el usuario alcance a leer el resultado final.

Para evitar este problema en programas de consola, siempre debemos agregar un `input()` al final de nuestro código que obligue a la ventana a esperar antes de cerrarse:

```python
# Ejemplo de programa listo para empaquetar (calculadora_simple.py)

print("==================================")
print("Bienvenido a mi primer ejecutable")
print("==================================")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

print(f"\nEl resultado de la suma es: {num1 + num2}")

# LÍNEA OBLIGATORIA AL FINAL DEL ARCHIVO:
input("\nPresiona la tecla Enter para salir del programa...")
```

## Paso 1: Verificar e instalar `pip` (El gestor de paquetes)

Como PyInstaller no viene incluido por defecto con Python, debemos descargarlo usando **pip**, que es la herramienta oficial de Python para instalar paquetes y librerías de terceros.

Para verificar si ya tienes `pip` instalado, abre la terminal de tu sistema operativo (CMD/PowerShell en Windows, o Terminal en Mac/Linux) y ejecuta:

```bash
# En Windows:
pip --version
# (Si marca error en Windows, prueba con: py -m pip --version)

# En macOS / Linux:
pip3 --version
```

Si la terminal te responde con un número de versión (ej. `pip 24.0 from...`), puedes saltar directamente al **Paso 2**.

### ¿Qué hacer si NO tienes `pip` instalado?

Si la terminal indica que el comando no se reconoce, puedes forzar su instalación nativa ejecutando el siguiente comando según tu sistema operativo:

```bash
# Solución para Windows:
py -m ensurepip --upgrade

# Solución para macOS:
python3 -m ensurepip --upgrade

# Solución para Linux (Ubuntu / Debian):
sudo apt update
sudo apt install python3-pip
```

## Paso 2: Instalar PyInstaller

Una vez que confirmamos que `pip` funciona correctamente, instalaremos **PyInstaller** descargándolo desde internet a través de nuestra terminal:

```bash
# En Windows:
pip install pyinstaller
# (Alternativa si el comando anterior falla: py -m pip install pyinstaller)

# En macOS / Linux:
pip3 install pyinstaller
```

Verás barras de carga en la consola. Cuando aparezca el mensaje `Successfully installed pyinstaller...`, tu computadora estará lista para compilar.

## Paso 3: Convertir tu archivo `.py` en un ejecutable

Para empaquetar nuestro programa, debemos ubicar nuestra terminal exactamente en la carpeta donde está guardado nuestro archivo de Python.

1. Abre la terminal y navega hasta tu carpeta usando el comando `cd` (Change Directory):

```bash
# Ejemplo de navegación a tu carpeta de proyectos:
cd C:\Usuarios\TuNombre\Documentos\CursoPython
```

> **Truco en VS Code:** Si ya tienes abierta la carpeta de tu proyecto en Visual Studio Code, simplemente abre la terminal integrada (`Ctrl + Ñ` o `Ctrl + ~`) y ya estarás ubicado automáticamente en la ruta correcta.

2. Ejecuta PyInstaller con la bandera `--onefile` para empaquetar todo en un solo archivo limpio:

```bash
# Sintaxis general:
pyinstaller --onefile nombre_de_tu_archivo.py

# Ejemplo real:
pyinstaller --onefile calculadora_simple.py
```

**Si en Windows te aparece el error "pyinstaller no se reconoce como un comando":** Esto ocurre cuando las variables de entorno (PATH) no están configuradas. Puedes solucionarlo inmediatamente ejecutándolo a través del lanzador de Python:

```bash
py -m PyInstaller --onefile calculadora_simple.py
```

> _(Nota que en este comando alternativo, la **P** y la **I** de PyInstaller deben ir en mayúsculas)._

### Parámetros adicionales útiles de PyInstaller:

|**Parámetro**|**Función**|**Cuándo usarlo**|
|---|---|---|
|`--onefile` o `-F`|Empaqueta todo el proyecto dentro de un único archivo ejecutable.|**Siempre recomendado** para facilitar la entrega.|
|`--noconsole` o `-w`|Oculta la pantalla negra de la terminal al abrir el programa.|**Solo para interfaces gráficas** (Tkinter, PyQt). ¡Nunca lo uses si tu programa usa `print()` e `input()`!|
|`--icon=logo.ico`|Cambia el ícono por defecto por una imagen personalizada (formato `.ico` en Windows o `.icns` en Mac).|Cuando quieras darle una presentación profesional a tu entregable final.|

## Paso 4: ¿Dónde quedó mi archivo ejecutable?

Cuando PyInstaller termine de trabajar, notarás que dentro de tu carpeta original se crearon varios elementos nuevos. La estructura de tu carpeta se verá así:

```Plaintext
📁 Tu_Carpeta_De_Proyecto/
│
├── 📄 calculadora_simple.py       <-- Tu código fuente original
├── 📄 calculadora_simple.spec     <-- Archivo de configuración (puedes ignorarlo)
├── 📁 build/                      <-- Archivos temporales de construcción (puedes borrarla)
└── 📁 dist/                       <-- ¡AQUÍ ESTÁ TU PROGRAMA! (Distribution)
    └── 🚀 calculadora_simple.exe  <-- Tu ejecutable final listo para compartir
```

1. Entra a la carpeta llamada **`dist`**.
    
2. Ahí dentro encontrarás tu archivo ejecutable (`calculadora_simple.exe` en Windows o `calculadora_simple` en Mac/Linux).
    
3. Ese único archivo dentro de `dist` es el que puedes enviar por correo, subir a Google Classroom o pasar en una memoria USB a cualquier otra computadora que tenga tu mismo sistema operativo, sin necesidad de que tengan Python instalado.
    

> **Nota sobre los Antivirus (Falsos Positivos):** En ocasiones, Windows Defender o algunos navegadores muestran una alerta de seguridad al descargar o abrir un `.exe` recién creado con PyInstaller. Esto sucede porque el programa es nuevo y no cuenta con una firma digital comercial de Microsoft (que cuesta cientos de dólares al año). Es completamente seguro darle clic en **"Más información" -> "Ejecutar de todas formas"**.