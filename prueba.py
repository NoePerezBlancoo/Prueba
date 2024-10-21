 Crear el repositorio en GitHub:
Iniciaste sesión en GitHub.
Creaste un nuevo repositorio haciendo clic en "New".
Le diste un nombre (por ejemplo, Prueba) y lo creaste sin ningún archivo inicial.
2. Clonar el repositorio en tu máquina local:
Abriste la terminal y clonaste el repositorio con el siguiente comando:
bash
Copiar código
git clone https://github.com/NoePerezBlancoo/Prueba.git
3. Mover el archivo .py al repositorio clonado:
Muiste el archivo prueba.py desde su ubicación original (C:\Users\M.GONZALEZ\Documents\Trapallada\Prueba.py) a la carpeta del repositorio clonado (C:\Users\M.GONZALEZ\Prueba).
4. Configurar tu identidad en Git (si no lo habías hecho antes):
Configuraste tu nombre y correo electrónico para que Git pueda registrar quién realiza los cambios:
bash
Copiar código
git config --global user.email "noeperezblanco1992@gmail.com"
git config --global user.name "NoePerezBlancoo"
5. Añadir el archivo al área de preparación:
Añadiste el archivo prueba.py al área de preparación de Git con este comando:
bash
Copiar código
git add prueba.py
6. Hacer un commit:
Confirmaste los cambios en el repositorio local, con un mensaje explicativo:
bash
Copiar código
git commit -m "Añadir prueba.py"
7. Subir los cambios a GitHub:
Subiste los cambios al repositorio remoto en GitHub (en la rama main):
bash
Copiar código
git push origin main
Resultado final:
Tu archivo prueba.py ya está en tu repositorio de GitHub.

Resumen de los comandos clave:
bash
Copiar código
# 1. Clonar el repositorio
git clone https://github.com/NoePerezBlancoo/Prueba.git

# 2. Mover el archivo al repositorio clonado

# 3. Configurar la identidad (si no estaba configurada)
git config --global user.email "your.email@example.com"
git config --global user.name "Your Name"

# 4. Añadir el archivo al área de preparación
git add prueba.py

# 5. Hacer commit de los cambios
git commit -m "Añadir prueba.py"

# 6. Subir los cambios a GitHub
git push origin main


Pasos para actualizar un archivo en Git:
Verifica que estés en el directorio del repositorio: Asegúrate de estar en la carpeta del repositorio que clonaste. Usa este comando para navegar al directorio:

bash
Copiar código
cd C:\Users\M.GONZALEZ\Prueba
Verifica el estado de Git: Puedes usar este comando para ver qué archivos han sido modificados:

bash
Copiar código
git status
Esto te mostrará los archivos que han cambiado. Verás tu archivo .py como modificado (aparecerá en rojo).

Añade el archivo modificado al área de preparación: Añade el archivo modificado para que esté listo para ser "commiteado":

bash
Copiar código
git add prueba.py
Haz un commit de los cambios: Haz un commit para guardar los cambios localmente con un mensaje explicativo:

bash
Copiar código
git commit -m "Actualizar prueba.py con los nuevos cambios"
Sube los cambios a GitHub (push): Finalmente, sube los cambios al repositorio remoto en GitHub con el siguiente comando:

bash
Copiar código
git push origin main
Resumen de comandos:
bash
Copiar código
cd C:\Users\M.GONZALEZ\Prueba   # Ve al directorio del repositorio
git status                      # Verifica los cambios
git add prueba.py                # Añadir el archivo modificado
git commit -m "Actualizar prueba.py con los nuevos cambios"   # Haz commit de los cambios
git push origin main             # Sube los cambios a GitHub