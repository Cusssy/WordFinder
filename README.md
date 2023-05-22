# Word Finder

Un sencillo programa que usa la whisper la inteligencia artificia de OpenAI para transcribir todos tus videos/audios a texto el cual sera almacenado en una base de datos de mongoDB.

Podras acceder a el desde la pagina web que tu vas alojar, te dira en que parte se ha dicho esa palabra o frase y que video, si tiene acceso local a esos videos te saldra un boton para copiar la ubicacion del video y accerder a el desde el propio navegador


vas a neceistar instalar estas 3 librerias 

````
pip install flask, pymongo, openai-whisper
````

## Como usar:

Si quieres ejecutar la pagina web ve a ``src/app.py``.

Si quieres transcribir tus videos/audios ejecuta el archivo ``transcriptor.py`` y pon el directorio, ten en cuenta que cuantos mas videos tengas, mas va a tardar en terminar, pero en cualquier momento podras dejar el proceso a medias y el programa sera capaz de continuar por donde lo dejó

## Issues: 

Si encuentra un video corruo el progrma se va congelar y tendras que borrar el archivo de manera manual (en un futuro borra o saltara el video de manera automatica)

## Uso de recursos:

Al transcribir el proceso usara bastante CPU, ten en cuenta que se neceistas un CPU gama media o mas (mi CPU es un R7 5700x y no tiene problemas al usarlo y hacer tareas normales)

Se puede ejecutar en GPU pero yo no lo he probado

