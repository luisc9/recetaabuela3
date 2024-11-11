import pandas as pd
import random

class Recipee():
    """
    This class encapsulates the search of recipees that contain a particular ingredient
    """
    def __init__(self, ingredient:str):
        """Initialization of the class"""
        self.ingredient = ingredient

    def search(self):
        """
        Search ingredient and return all recipees with that ingredient, and the amount of recipees.
        """
        # Read the csv file
        recipee_df = pd.read_csv("recetasdelaabuela.csv")
        # Filter by the search term
        mask = recipee_df.Ingredientes.str.contains(self.ingredient, case=False, na=False)
        amount_of_recipees = recipee_df[mask].shape[0]
        recipees_chosen = pd.DataFrame()
        recipees_chosen = recipee_df[mask][["Nombre", "Ingredientes", "Pasos"]]

        return recipees_chosen, amount_of_recipees