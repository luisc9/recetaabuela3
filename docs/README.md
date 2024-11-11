---
license: openrail
task_categories:
- question-answering
- summarization
language:
- es
pretty_name: RecetasDeLaAbuel@
size_categories:
- 10K<n<100K
tags:
- recipes
- cooking
- recetas
- cocina
configs:
- config_name: version_inicial
  data_files: "recetasdelaabuela.csv"
- config_name: version_1
  data_files: "main.csv"
---
# Motivación inicial

<!-- Motivation for the creation of this dataset. -->
Este corpus ha sido creado durante el Hackathon SomosNLP Marzo 2024: #Somos600M (https://somosnlp.org/hackathon).
Responde a una de las propuestas somosnlp sobre 'Recetas típicas por país/zona geográfica'.

# Nombre del Proyecto

<!-- Provide a quick summary of the dataset. -->
Este corpus o dataset se llama 'RecetasDeLaAbuel@' y es un homenaje a todas nuestr@s abuel@s que nos han enseñado a cocinar. Se trata de la mayor y más completa colección de recetas open-source en español de países hispanoamericanos.


<p align="left">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/6456c6184095c967f9ace04d/h5GG5ht9r9HJCvJbuetRO.png" alt="Mi abuela cocinando" width="323">
</p>


## Corpus
## Descripción

<!-- Provide a longer summary of what this dataset is. -->
Este corpus contiene los principales elementos de una receta de cocina (título, descripción, ingredientes y preparación). Se ha completado con otros 10 atributos 
hasta completar un impresionante dataset con más de 280k (20k x 14) elementos (6M palabras y 40M caracteres).

- **Curated by:** iXrst
- **Funded by:** rovi27, sbenel, GaboTuco, iXrst
- **Language(s) (NLP):** Python
- **License:** openrail

### Estructura

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->
Este dataset 'RecetasDeLaAbuel@' tiene formato tabular (20k x 14). Cada fila de datos tiene los siguientes atributos:
1. Id: Identificador numérico.
2. Nombre: Nombre de la receta.
3. URL: Origen web.
4. Ingredientes: Alimentos usados.
5. Pasos: Pasos de preparación.
6. País: Código ISO_A3/país originario de la receta.
7. Duracion (HH:MM): Tiempo estimado de preparación.
8. Categoria: Tipo de receta (ej. vegetarianos, pastas, salsas, postres, cerdo, pollo etc).
9. Contexto: Entorno de uso/consumo o contexto de la receta. 
10. Valoracion y Votos: Valoración 1-5 y número de votos. 
11. Comensales: Número de raciones.
12. Tiempo: Tiempo del plato (ej: Desayuno, entrante, principal, acompañamiento, etc.) 
13. Dificultad: Grado de dificultad (alto/medio/bajo)
14. Valor nutricional: Características básicas: 1) Nivel calorías/sodio (alto/medio/bajo), 2) Ausencia de grasas/grasas trans/colesterol/azúcar y 3) Nivel de fibra.

### Fuentes de datos
<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->
La información básica se ha recolectado y procesado mediante las técnicas conocidas como 'web scrapping'.
La información original se ha recopilado de diferentes páginas web:
- Recetas gratis de cocina
- Cocina peruana
- Cocina mexicana
- Cocina colombiana

Ponganse en contacto con nosotros para incluir recetas de su país, por favor!

Para más información sobre recetas de cocina dirijanse a la fuente original. Expresamos nuestro reconocimiento y agradecimiento a sus autores.

### Procesamiento de datos

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->
Se utilizó scripts de Python para hacer el procesamiento del corpus, y las funciones de limpieza y curación del dataset.
** https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela/blob/main/stats.pdf

### Estadísticas

Son 20447 registros de recetas.
** https://github.com/recetasdelaabuela/somosnlp/blob/main/Docs/Stats.pdf

## Política de Uso

<!-- Address questions around how the dataset is intended to be used. -->

### Uso directo

<!-- This section describes suitable use cases for the dataset. -->
Nuestra Misión es la creación del mejor asistente de cocina inteligente específico del idioma español (corpus Recetas de la Abuel@) que agrupe recetas de países hispanoamericanos 
y permita mejorar nuestra relación con la preparación y el cocinado de los alimentos.

Nuestra IA responderá a cuestiones de los sigientes tipos:
'Dime la receta del ceviche, frijoles, tortilla de patata, paella, etc'
'Qué puedo cocinar con 3 ingredientes?', 
'Dime una comida de temporada para este mes de Marzo?' , 
'Propón un menú mensual para una familia'

### Fuera de alcance

<!-- This section addresses misuse, malicious use, and uses that the dataset will not work well for. -->
Queda excluido cualquier uso no contemplado por la UE AI Policity (https://www.consilium.europa.eu/es/policies/artificial-intelligence/)

## Entrenamiento del modelo LLM

Consultese el informe adjunto wandb: 
https://github.com/recetasdelaabuela/somosnlp/blob/e7f9796dc2c293ce923f31814de78c49c5b4e3f8/Docs/RecetasDeLaAbuel%40%20Report%20_%20Recetas19kTest20_gemma-2b-it-bnb-4bit%20%E2%80%93%20Weights%20%26%20Biases%20(3).pdf
https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela/blob/main/RecetasDeLaAbuel%40%20Report%20_%20Recetas19kTest20_gemma-2b-it-bnb-4bit%20%E2%80%93%20Weights%20%26%20Biases.pdf

Los experimentos se realizaron utilizando HuggingFace (AWS) en la región sa-east-1, que tiene una eficiencia de carbono de 0.2 kg CO2 eq/kWh. 
Se realizó un acumulado de 50 horas de cómputo en HW tipo T4 (TDP 189 de 70W). Las emisiones totales estimadas son 0.7 kg eq. CO2., obtenidas a través de la web ML CO2
Impact (https://mlco2.github.io/impact/).

# Links del proyecto

<!-- Provide the basic links for the dataset. -->

- **Repository:** https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela
- **GitHub:** https://github.com/recetasdelaabuela/somosnlp
- **Paper:** https://github.com/recetasdelaabuela/somosnlp/blob/main/Paper/LatinX_NAACL_2024-3-1.pdf
- **Corpus con formato tabular:** https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela
- **Corpus de Instrucciones Original:** https://huggingface.co/datasets/somosnlp/recetasdelaabuela_genstruct_it
- **Corpus de Instrucciones Curado:** https://huggingface.co/datasets/somosnlp/recetasdelaabuela_it

- **Modelo LLM Gemma 7b 20k RecetasDeLaAbuel@:** https://huggingface.co/somosnlp/recetasdelaabuela-0.03
- **Modelo LLM Gemma 2b 20k RecetasDeLaAbuel@:** https://huggingface.co/somosnlp/RecetasDeLaAbuela_gemma-2b-it-bnb-4bit
- **Modelo LLM Tiny Llama 1.1B RecetasDeLaAbuel@:** https://huggingface.co/somosnlp/recetasdelaabuela-0.03
- **Modelo LLM 5k RecetasDeLaAbuel@:** https://huggingface.co/somosnlp/RecetasDeLaAbuela5k_gemma-2b-bnb-4bit

- **Demo RecetasDeLaAbuel@:** https://huggingface.co/spaces/somosnlp/RecetasDeLaAbuela_Demo
  
- **Modelo LLM ComeBien:** https://huggingface.co/somosnlp/ComeBien_gemma-2b-it-bnb-4bit
- **Demo ComeBien:** https://huggingface.co/spaces/somosnlp/ComeBien_Demo

## Uso del modelo LLM

Los modelos LLM Gemma RecetasDeLaAbuel@ se deben usar siguiendo el formato sistema/usuario/modelo (SOT='<'start_of_turn'>'',EOT='<'end_of_turn'>')"": 
<bos>SOT system\n {instruction} EOT SOT user\n {nombre} EOT SOT model\n {receta} EOT EOS_TOKEN.
Más info en https://unsloth.ai/blog/gemma-bugs

## Impacto medioambiental
Los experimentos se realizaron utilizando HuggingFace (AWS) en la región sa-east-1, que tiene una eficiencia de carbono de 0,2 kg CO2 eq/kWh. Se realizó un acumulado de 50 horas de cómputo en HW tipo T4 (TDP de 70W). Se estima que las emisiones totales son 0,7 kg eq. CO2. Las estimaciones se realizaron utilizando la web ML CO2 Impact https://mlco2.github.io/impact/#compute.


# Citaciones

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->
Este trabajo se ha basado y es continuación del trabajo desarrollado en el siguiente corpus durante el Hackhaton somosnlp 2023:
https://huggingface.co/datasets/somosnlp/recetas-cocina

Debemos reconocer y agradecer públicamente la labor de su creador Fredy pues gracias a su orientación inicial hemos llegado tan lejos!
https://huggingface.co/Frorozcol

Más información del magnífico proyecto inicial 'Creación de Dataset de Recetas de Comidas' de Fredy se puede encontrar en su github:
https://github.com/Frorozcoloa/ChatCocina/tree/main

Asismismo debemos reconocer y agradecer la labor de Tiago en la recopilación de diversas fuentes de recetas:
- 37 comidas saludables para cuidarse durante todo el mes
- 101 recetas sanas para tener un menú saludable de lunes a domingo 
- 50 recetas Fáciles, Sanas, Rápidas y Económicas - Antojo en tu cocina
- 54 recetas saludables para niños, comidas sanas y fáciles de hacer

# Autores

https://huggingface.co/rovi27 <br>
https://huggingface.co/sbenel <br>
https://huggingface.co/GabTuco <br>
https://huggingface.co/iXrst <br>


# Asesoría Académica 

Modelización de temática mediante BERTopic
https://huggingface.co/andreamorgar

# Cita Académica 
@software{recetasdelaabuela2024,
  author = {Morales-Garzón, Andrea and Rocha, Oscar A. and Benel Ramirez, Sara and Tuco Casquino, Gabriel and Medina, Alberto},
  title = {RecetasDeLaAbuel@},
  month = March,
  year = 2024,
  url = {https://huggingface.co/datasets/somosnlp/recetasdelaabuela}
}

Presentado y aceptado como poster en LatinX in Natural Language Processing Research Workshop at NAACL 2024 (https://www.latinxinai.org/naacl-2024):<br>
https://github.com/recetasdelaabuela/somosnlp/blob/main/Paper%20NAACL/HealthyCooking_NAACL_LatinXAI_Paper.pdf <br>
<p><img src="https://cdn-uploads.huggingface.co/production/uploads/6456c6184095c967f9ace04d/aI5Njprr35eLGrbAi0lML.jpeg" alt="Paper" style="display:inline-block;">
<img src="https://cdn-uploads.huggingface.co/production/uploads/6456c6184095c967f9ace04d/eApqOE-Etw6-mPVvCmrWP.jpeg" alt="Paper" style="display:inline-block;">
<img src="https://cdn-uploads.huggingface.co/production/uploads/6456c6184095c967f9ace04d/o6sJ_Ixh9cwYHP5YfT3Vn.jpeg" alt="Paper" style="display:inline-block;">
<! -- img src="https://cdn-uploads.huggingface.co/production/uploads/6456c6184095c967f9ace04d/fMxdOxjOPYBitSz4-5ikg.jpeg" alt="Paper" style="display:inline-block;" ––>
</p>
https://github.com/recetasdelaabuela/somosnlp/blob/main/Paper%20NAACL/HealthyCooking_NAACL_LatinXAI_Poster.pdf
<p align="left">
<img src="https://cdn-uploads.huggingface.co/production/uploads/6456c6184095c967f9ace04d/jD17u4pTDjUK2KdS1G4Zp.jpeg" alt="HealthyCooking_NAACL_LatinXAI_Poster" width="323">
</p>

# Contacto
mailto: recetasdelaabuela.comebien@gmail.com