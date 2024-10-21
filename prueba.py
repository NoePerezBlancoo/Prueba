 Crea un repositorio en GitHub
Inicia sesión en GitHub.
Haz clic en "New" (Nuevo) para crear un nuevo repositorio.
Dale un nombre al repositorio, por ejemplo mi-script-python.
Deja la opción "Inicializar con README" desmarcada si planeas agregar los archivos desde tu computadora.
Haz clic en "Create repository".
2. Clona el repositorio en tu máquina
Abre la terminal o consola.
Ejecuta el siguiente comando para clonar tu repositorio localmente:
bash
Copiar código
git clone https://github.com/usuario/mi-script-python.git
3. Copia tu archivo .py al repositorio local
Mueve tu archivo mi_script.py a la carpeta del repositorio que acabas de clonar.
4. Añade el archivo al repositorio
Ve a la carpeta del repositorio en la terminal:
bash
Copiar código
cd mi-script-python
Añade tu archivo .py al repositorio con este comando:
bash
Copiar código
git add mi_script.py
5. Confirma los cambios (commit)
Guarda los cambios en el repositorio local con el siguiente comando:
bash
Copiar código
git commit -m "Añadir script de Python"
6. Sube los cambios a GitHub (push)
Sube el archivo al repositorio en GitHub con este comando:
bash
Copiar código
git push origin main
7. Verifica en GitHub
Ve a tu repositorio en GitHub para comprobar que el archivo mi_script.py se ha subido correctamente.
¡Y eso es todo! Tu script de Python ya estará en GitHub.