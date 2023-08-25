# -*- coding: utf-8 -*-
import csv
from datetime import date
import os
import pkgAdherants.Adherant as membre
import pkgDocuments.Bibliotheque as biblio
import pkgEmprunt.Emprunts as emp

def informationAdherent(fichier_Membre="Adherants.txt"):
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
def informationEmprunt(fichier_Emprunt="Empruntes.txt"):
    emprunts = []  # Liste des emprunts
    with open(fichier_Emprunt, 'r') as liste:
        fichier = csv.reader(liste, delimiter=';')
        for line in fichier:
            membre_nom, membre_prenom, titre, date_emprunte, date_retour = line
            emprunte = emp.Emprunts(membre_nom, membre_prenom, titre, date_emprunte, date_retour)
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

def ajouter_adherent(membres): #option 1 - ajouter membre
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
    emprunte = input("Est-ce que le livre est disponible pour l'emprunter? (Oui/Non): ")
    with open("Biblio.txt", 'a', newline='') as fichier:  # a --> pour ajouter et ne pas effacer ce qui a.
        if fichier.tell() != 0:
            fichier.write("\n")
        new_Doc = csv.writer(fichier, delimiter=';')
        new_Doc.writerow([titre, auteur, annee_pub, emprunte])
    livreAjoute = biblio.Bibliotheque(titre, auteur, annee_pub, emprunte)
    livres.append(livreAjoute)
    print(titre," ", auteur," ",annee_pub, " a été ajouté à la liste Bibliotheque!.")
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return
def ajouter_emprunt(livres, membres, fichier_Biblio="Biblio.txt",
                    fichier_Emprunts="Empruntes.txt"):   ## option 7 - Ajouter emprunt
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
        membre_nom = input("Entrez le nom de l'emprunteur: ")
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
        date_d_emprunt= date.today().strftime("%d/%m/%Y") # to settle date
        with open(fichier_Emprunts, 'a', newline='') as info_Emprunt:
            recrire = csv.writer(info_Emprunt, delimiter=';')
            info_Emprunt.write('\n')
            recrire.writerow([membre_existe.getMembre_nom(), membre_existe.getMembre_prenom(), titre, date_d_emprunt])
        print("Vous avez emprunté", titre, "!")
    # Rewrite Biblio.txt with updated information
    with open(fichier_Biblio, 'w', newline='') as fichier:
        recrire = csv.writer(fichier, delimiter=';')
        for document in livres:
            recrire.writerow([document.getTitre(), document.getAuteur(), document.getAnnee_pub(), document.getDisponible()])
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return


def supprimer_adherent(fichier_Membre="Adherants.txt"): #option 2
    print("******************************************************* \n"
          "   Vous avez choisi Opt. 2 - Supprimer un Adhérant    \n"
          "******************************************************* \n"
          "======================================================= \n"
          "  Pour supprimer un adhérant, rentrer les détails:     \n"
          "======================================================= \n")

    membre_nom_to_effacer = input("Entrez le nom de l'adhérant à supprimer: ")
    membre_prenom_to_effacer = input("Entrez le prénom de l'adhérant à supprimer: ")

    try:
        with open(fichier_Membre, 'r') as fichier:
            lecteure_fichier = csv.reader(fichier, delimiter=';')
            adherants = [membre for membre in lecteure_fichier if membre and membre[0] != membre_nom_to_effacer and membre[1] != membre_prenom_to_effacer]

            if len(adherants) == len(list(lecteure_fichier)):
                print("L'adhérant n'existe pas!")
                return

            confirmation = input(f"Confirmez-vous la suppression de {membre_nom_to_effacer} {membre_prenom_to_effacer}? (Oui/Non): ").strip().lower()
            if confirmation != 'oui':
                print("Suppression annulée.")
                return

        with open(fichier_Membre, 'w', newline='') as adh_membre:
            recrire = csv.writer(adh_membre, delimiter=';')
            recrire.writerows(adherants)

        print("L'adhérant a été supprimé avec succès!")

    except FileNotFoundError:
        print(f"File '{fichier_Membre}' not found.")

    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return
def supprimer_document(fichier_Biblio="Biblio.txt"): # option 5
    print("******************************************************* \n"
          "   Vous avez choisi Opt. 5 - Supprimer un Livre         \n"
          "******************************************************* \n"
          "======================================================= \n"
          "  Pour supprimer un livre, rentrer les détails:         \n"
          "======================================================= \n")

    titre_a_effacer = input("Entrez le titre du livre à supprimer: ")
    try:
        with open(fichier_Biblio, 'r') as fichier:
            lecteure_fichie = csv.reader(fichier, delimiter=';')

            # Filter and store books not matching the deletion criteria
            liste_livres = [livre for livre in lecteure_fichie if
                            livre and livre[0] != titre_a_effacer]
            if len(liste_livres) == len(list(lecteure_fichie)):
                print("Le livre n'existe pas!")
                return
            confirmation = input(
                f"Confirmez-vous la suppression de '{titre_a_effacer}'? (Oui/Non): ").strip().lower()
            if confirmation != 'oui':
                print("Suppression annulée.")
                return
        with open(fichier_Biblio, 'w', newline='') as update:
            lecture_fichier = csv.writer(update, delimiter=';')
            lecture_fichier.writerows(liste_livres)
        print("Le livre a été supprimé avec succès!")
    except FileNotFoundError:
        print(f"File '{fichier_Biblio}' not found.")

    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return


def retour_emprunt(livres, membres, fichier_Biblio="Biblio.txt", fichier_Emprunts="Empruntes.txt"):
    print("******************************************************* \n"
          "     Vous avez choisi Opt. 8 - Retourner un Document    \n"
          "******************************************************* \n"
          "======================================================= \n"
          "    Pour retourner un document, rentrer les détails:    \n"
          "======================================================= \n")

    titre = input("Entrez le titre du livre à retourner: ")
    livre_trouve = None
    for livre in livres:
        if livre.getTitre() == titre:
            livre_trouve = livre
            break
    if not livre_trouve:
        print("Le livre n'est pas trouvé dans la bibliothèque.")
        return

    membre_nom = input("Entrez le nom de l'emprunteur: ")
    membre_prenom = input("Entrez le prénom de l'emprunteur: ")

    membre_existe = None
    for membre in membres:
        if membre.getMembre_nom() == membre_nom and membre.getMembre_prenom() == membre_prenom:
            membre_existe = membre
            break
    if not membre_existe:
        print("Ce membre n'existe pas!")
        return

    lines = []
    with open(fichier_Emprunts, 'r') as fichier:
        lire_fichier = csv.reader(fichier, delimiter=';')
        for element in lire_fichier:
            if element and element[0] == membre_nom and element[1] == membre_prenom and element[2] == titre:
                continue
            lines.append(element)

    with open(fichier_Emprunts, 'w', newline='') as fichier:
        recrire = csv.writer(fichier, delimiter=';')
        recrire.writerows(lines)

    livre_trouve.setDisponible("Oui")

    with open(fichier_Biblio, 'w', newline='') as fichier:
        recrire = csv.writer(fichier, delimiter=';')
        for document in livres:
            recrire.writerow(
                [document.getTitre(), document.getAuteur(), document.getAnnee_pub(), document.getDisponible()])

    date_de_retour = date.today().strftime("%d/%m/%Y")
    print(f"Le livre '{titre}' a été retourné le {date_de_retour}!")

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
def afficher_documents(livres):  # option 6 - affiche de la liste d'information des clients
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
        print(livre.getMembre_nom(), livre.getMembre_prenom(), livre.getTitre(), livre.getDate_emprunte(), livre.getDate_retour())
    while True:
        print("======================================================= \n")
        retourner_au_menu = input("Vouillez appuyer sur 'ENTER' pour retourner au menu principal: ")
        if retourner_au_menu == '':
            return # option 9


membres = informationAdherent(fichier_Membre="Adherants.txt")
livres = informationBiblio(fichier_Biblio="Biblio.txt")
emprunts = informationEmprunt(fichier_Emprunt="Empruntes.txt")

#body programme
while True:
    menuPrincipal() #menu d'options
    choix_d_option = input(" >>> Saisir votre choix: \n").upper()
    if choix_d_option in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "Q"]:
        if choix_d_option == "1":
            ajouter_adherent(membres)
        elif choix_d_option == "2":
            supprimer_adherent()
        elif choix_d_option == "3":
            afficher_adherents(membres)
        elif choix_d_option == "4":
            ajouter_document(livres)
        elif choix_d_option == "5":
            supprimer_document()
        elif choix_d_option == "6":
            afficher_documents(livres)
        elif choix_d_option == "7":
            ajouter_emprunt(livres, membres, fichier_Biblio="Biblio.txt", fichier_Emprunts="Empruntes.txt")
        elif choix_d_option == "8":
            retour_emprunt(livres, membres, fichier_Biblio="Biblio.txt", fichier_Emprunts="Empruntes.txt")
        elif choix_d_option == "9":
            afficher_emprunts(emprunts)
        elif choix_d_option == "Q":
            print("Merci d'avoir utilisé la bibliothèque!")
            break
    else:
        print("Choix erroné. SVP, saisir à nouveau votre choix.")