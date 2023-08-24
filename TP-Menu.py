# -*- coding: utf-8 -*-
import csv
from datetime import date
import os

import pkgAdherants.Adherant as membre
import pkgDocuments.Bibliotheque as biblio
import pkgEmprunt.Emprunts as emp

def informationAdherant(fichier_Membre="Adherants.txt"):
    membres = []  # Liste des membres
    with open(fichier_Membre, 'r') as fichiers:
        adherant = csv.reader(fichiers, delimiter=';')
        for line in adherant:
            membre_nom, membre_prenom = line
            membrex = membre.Adherant(membre_nom, membre_prenom)
            membres.append(membrex)
    return membres

def informationBiblio(fichier_Biblio="Biblio.txt"):
    livres = []  # Liste des livres
    with open(fichier_Biblio, 'r') as liste:
        fichier = csv.reader(liste, delimiter=';')
        for line in fichier:
            titre, auteur, annee_pub, disponible = line
            livreChoisit = biblio.Bibliotheque(titre, auteur, annee_pub, disponible)
            livres.append(livreChoisit)
    return livres

def informationEmprunt(fichierEmprunt="Empruntes.txt"):
    emprunts = []  # Liste des emprunts
    with open(fichierEmprunt, 'r') as liste:
        fichier = csv.reader(liste, delimiter=';')
        for line in fichier:
            membre_nom, membre_prenom, livre, date_emprunte = line
            emprunte = emp.Emprunts(membre_nom, membre_prenom, livre, date_emprunte)
            emprunts.append(emprunte)
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

def ajouter_adherant(membres): #option 1 - ajouter membre
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 1 - Ajouter Adhérant         \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Rentrer les informations en ordre:           \n"
          "======================================================= \n")
    membre_nom = input("Entrez le nom du nouveau membre: ")
    membre_prenom = input("Entrez le prenom du nouveau membre: ")
    with open("Adherants.txt", 'a', newline='') as fichier: # a pour ajouter sans effacer
        if fichier.tell() != 0:
            fichier.write("\n")
        new_Adherant = csv.writer(fichier, delimiter=';')
        new_Adherant.writerow([membre_nom, membre_prenom])
    membrex = membre.Adherant(membre_nom, membre_prenom)
    membres.append(membrex)
    print(membre_nom," ",membre_prenom," a été ajouté à la liste des membres!.")

    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return
def ajouter_document(livres):  # option 4 - ajouter un document.
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 4 - Ajouter Document         \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Rentrer les information en ordre:            \n"
          "======================================================= \n")
    titre = input("Entrez le titre du livre: ")
    auteur = input("Entrez le nom de l'auteur: ")
    annee_pub = input("Entrez l'année de publication: ")
    emprunte = input("Est-ce que le livre est emprunté? (Oui/Non): ")
    with open("Biblio.txt", 'a', newline='') as fichier:  # a --> pour ajouter et ne pas effacer ce qui a.
        if fichier.tell() != 0:
            fichier.write("\n")
        new_Doc = csv.writer(fichier, delimiter=';')
        new_Doc.writerow([titre, auteur, annee_pub, emprunte])
    livreAjoute = biblio.Bibliotheque(titre, auteur, annee_pub, emprunte)
    livres.append(livreAjoute)
    print(titre," ", auteur," ",annee_pub, " a été ajouté à la liste des membres!.")
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return
def ajouter_emprunt(livres, emprunts, membres, fichierLivres="Biblio.txt", fichierAdherants="Adherants.txt",
                    fichierEmprunts="Empruntes.txt"):   ## option 7 - Ajouter emprunt
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 7 - Emprunter un Document    \n"
          "******************************************************* \n"
          "======================================================= \n"
          "   Pour emprunter un document, rentrer les détails:     \n"
          "======================================================= \n")
    titre = input("Entrez le titre du livre à emprunter: ")
    livre_trouve = None
    for livre in livres:
        if livre.getTitre() == titre:
            livre_trouve = livre
            break
    if not livre_trouve:
        print("Le livre n'est pas trouvé dans la bibliothèque.")
        return
    print("Livre dans bibliotheque:", livre_trouve.getTitre(), livre_trouve.getAuteur(), livre_trouve.getAnnee_pub(),
          livre_trouve.getDisponible())
    emprunter = input("Confirmer l'emprunte du livre: (Oui/Non)")
    if emprunter.lower() == "oui":
        membre_nom = input("Entrez votre nom: ")
        membre_existe = None
        for membre in membres:
            if membre.getMembre_nom() == membre_nom:
                membre_existe = membre
                break
        if not membre_existe:
            print("Ce membre n'existe pas!")
            return
        # If member exists, update the availability of the book and add the rental to Empruntes.txt
        livre_trouve.setDisponible("Non")
        current_date = date.today().strftime("%d/%m/%Y") # to settle date
        with open(fichierEmprunts, 'a', newline='') as info_Emprunt:
            writer = csv.writer(info_Emprunt, delimiter=';')
            info_Emprunt.write('\n')
            writer.writerow([membre_existe.getMembre_nom(), membre_existe.getMembre_prenom(), titre, current_date])
        print("Vous avez emprunté", titre, "!")
    # Rewrite Biblio.txt with updated information
    with open(fichierLivres, 'w', newline='') as fichier:
        recrire = csv.writer(fichier, delimiter=';')
        for document in livres:
            recrire.writerow(
                [document.getTitre(), document.getAuteur(), document.getAnnee_pub(), document.getDisponible()])
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return


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
            return # option 3
def afficher_document(livres):  # option 6 - affiche de la liste d'information des clients
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 6 - Liste Bibliotheque       \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Liste des informations des documents         \n"
          "======================================================= \n")
    for livre in livres:  # lecture de chaque valeur/information
        print(livre.getTitre(), livre.getAuteur(), livre.getAnnee_pub(), livre.getDisponible())
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return  # option 6

def afficher_emprunts(emprunts):  # option 9 - affiche de la liste d'information des clients
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 9 - Liste Adhérant           \n"
          "******************************************************* \n"
          "======================================================= \n"
          "           Liste des informations des membre            \n"
          "======================================================= \n")
    for livre in emprunts:  # lecture de chaque valeur/information
        print(livre.getMembre_nom(), livre.getMembre_prenom(), livre.getLivre(), livre.getDate_emprunte())
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return # option 9




membres = informationAdherant(fichier_Membre="Adherants.txt")
livres = informationBiblio(fichier_Biblio="Biblio.txt")
emprunts = informationEmprunt(fichierEmprunt="Empruntes.txt")

#body programme
while True:
    menuPrincipal() #menu d'options
    choix_d_option = input(" >>> Saisir votre choix: \n")
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
            afficher_document(livres)
        elif choix_d_option == "7":
            ajouter_emprunt(livres, emprunts, membres)
        elif choix_d_option == "8":
            retour_emprunt(emprunts)
        elif choix_d_option == "9":
            afficher_emprunts(emprunts)
        elif choix_d_option == "Q":
            print("Merci d'avoir utilisé la bibliothèque!")
            break
    else:
        print("Choix erroné. SVP, saisir à nouveau votre choix.")