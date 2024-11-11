Las recetas de la abuela

The dataset contains the main elements of a recipee (title, description, ingredients and
steps to prepare). 10 more attributes were added so now the dataset has more than 280k
(20k x 14) elements (6M words and 40M characters).

Attributes:
1. Id: Numerical identifier.
2. Nombre: Recipee name.
3. URL: Website.
4. Ingredientes: Used food.
5. Pasos: Steps for preparation.
6. País: ISO_A3 country code, where the recipee comes from.
7. Duracion (HH:MM): Estimated time of preparation.
8. Categoria: Recipee type (for example vegetarian, pasta, sauce, dessert, pork, chicken, etc).
9. Contexto: Recipee context or use environment. 
10. Valoracion y Votos: Value 1-5 and amount of votes. 
11. Comensales: Amount of portion.
12. Tiempo: Moment of the dish (for example: breakfast, appetizer, main, company, etc.) 
13. Dificultad: Degree of dificulty (high/medium/low)
14. Valor nutricional: Nutritional value: 1) Calories/sodium level (high/medium/low), 2) Absence
of fat/trans fat/colesterol/sugar and 3) Fiber level.

Assignment 2: Creating a UI for visualizing food recipes

In the FastAPI assignment, you were asked to create an API to retrieve a single random
recipe containing a given ingredient. Here we propose you to create a UI where you can
specify the ingredient and how many recipes containing this ingredient you want to
retrieve. The UI should also include a button that, once pressed, it will retrieve the recipes
and show them in table, including the ingredients in one column and the recipes in the
other column.
Remember you can use the dataset available at:
https://huggingface.co/datasets/somosnlp/RecetasDeLaAbuela
