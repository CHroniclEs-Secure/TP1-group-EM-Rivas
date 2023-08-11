# -*- coding: utf-8 -*-
import csv

def menuPrincipal():  # liste des options a avoir.
    choix_d_option = print("======================================================== \n"
                           "|           Bienvenue à votre bibliothèque             | \n"
                           "|            Vous pouvez faire les choix:              | \n"
                           "|======================================================| \n"
                           "|   1 - Ajouter Adhérent                               | \n" #adherant =? membre
                           "|   2 - Supprimer Adhérant                             | \n"
                           "|   3 - Afficher tous les Adhérant                     | \n" 
                           "|   4 - Ajouter Document                               | \n"
                           "|   5 - Supprimer Document                             | \n"
                           "|   6 - Afficher Liste de Document                     | \n"
                           "|   7 - Ajouter Emprunts                               | \n"
                           "|   8 - Retour d'un Emprunts                           | \n"
                           "|   9 - Afficher Liste d'Emprunts                      | \n"
                           "|   Q - Quitter                                        | \n"
                           "======================================================== \n")
    return choix_d_option