# -*- coding: utf-8 -*-
import csv

import pkgAdherants.Adherant as membre
import pkgDocuments.Bibliotheque as biblio
import pkgEmprunt.Emprunts as emp

def informationAdherant(fichier_Membre="Adhérants.csv"):
    membres = []  # Liste des membres
    with open(fichier_Membre, 'r') as fichiers:
        adherant = csv.reader(fichiers, delimiter=';')
        for line in adherant:
            membre_nom, membre_prenom = line
            membrex = membre.Adherant(membre_nom, membre_prenom)
            membres.append(membrex)
    return membres

def informationBiblio(fichier_Biblio="Biblio.csv"):
    livres = []  # Liste des livres
    with open(fichier_Biblio, 'r') as liste:
        fichier = csv.reader(liste, delimiter=';')
        for line in fichier:
            titre, auteur, annee_pub, emprunte = line
            livreChoisit = biblio.Bibliotheque(titre, auteur, annee_pub, emprunte)
            livres.append(livreChoisit)
    return livres

def informationEmprunt(fichierEmprunt="Empruntes.csv"):
    emprunts = []  # Liste des emprunts
    with open(fichierEmprunt, 'r') as liste:
        fichier = csv.reader(liste, delimiter=';')
        for line in fichier:
            membre_nom, membre_prenom, livre = line
            livreChoisit = emp.Emprunts(membre_nom, membre_prenom, livre)
            emprunts.append(livreChoisit)
    return emprunts

def menuPrincipal():  # liste des options a avoir.
    choix_d_option = print("======================================================== \n"
                           "|           Bienvenue à votre bibliothèque             | \n"
                           "|            Vous pouvez faire les choix:              | \n"
                           "|======================================================| \n"
                           "|   1 - Ajouter Adhérant                               | \n" # a
                           "|   2 - Supprimer Adhérant                             | \n" #w 
                           "|   3 - Afficher tous les Adhérant                     | \n" #
                           "|   4 - Ajouter Document                               | \n" #
                           "|   5 - Supprimer Document                             | \n"
                           "|   6 - Afficher Liste de Document                     | \n" #
                           "|   7 - Ajouter Emprunts                               | \n" #
                           "|   8 - Retour d'un Emprunts                           | \n" 
                           "|   9 - Afficher Liste d'Emprunts                      | \n" #
                           "|   Q - Quitter                                        | \n"
                           "======================================================== \n")
    return choix_d_option


def afficher_adherents(membres):  # option 3 - affiche de la liste d'information des clients
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 3 - Liste Adhérant           \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Liste des informations des membre            \n"
          "======================================================= \n")
    for membre in membres:  # lecture de chaque valeur/information
        print(membre.getMembre_nom(), membre.getMembre_prenom())
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return

def afficher_documement(livres):  # option 6 - affiche de la liste d'information des clients
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 6 - Liste Bibliotheque       \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Liste des informations des documents         \n"
          "======================================================= \n")
    for livre in livres:  # lecture de chaque valeur/information
        print(livre.getTitre(), livre.getAuteur(), livre.getAnnee_pub(), livre.getEmprunter())
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return

def afficher_emprunts(emprunts):  # option 9 - affiche de la liste d'information des clients
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 9 - Liste Adhérant           \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Liste des informations des membre            \n"
          "======================================================= \n")
    for livre in emprunts:  # lecture de chaque valeur/information
        print(livre.getMembre_nom(), livre.getMembre_prenom(), livre.getLivre())
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return




membres = informationAdherant(fichier_Membre="Adhérants.csv")
livres = informationBiblio(fichier_Biblio="Biblio.csv")
empruntes = informationEmprunt(fichierEmprunt="Empruntes.csv")

#body programme
while True:
    menuPrincipal() #menu d'options
    choix_d_option = input(" >>> Saisir votre choix:\n")
    if choix_d_option in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Q"]:
        if choix_d_option == "1":
            ajouter_adherent(membres)
        elif choix_d_option == "2":
            supprimer_adherent(membres)
        elif choix_d_option == "3":
            afficher_adherents(membres)
        elif choix_d_option == "4":
            ajouter_document(livres)
        elif choix_d_option == "5":
            supprimer_document(livres)
        elif choix_d_option == "6":
            afficher_documement(livres)
        elif choix_d_option == "7":
            ajouter_emprunt(empruntes)
        elif choix_d_option == "8":
            retour_emprunt(empruntes)
        elif choix_d_option == "9":
            afficher_emprunts(empruntes)
        elif choix_d_option == "Q":
            print("Merci d'avoir utilisé la bibliothèque!")
            break
    else:
        print("Choix erroné. SVP, saisir à nouveau votre choix.")