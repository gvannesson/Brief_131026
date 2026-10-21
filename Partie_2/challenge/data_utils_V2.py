"""Module de fonctions mathématiques et statistiques (version 2)."""

import math

PI = math.pi
E = math.e


def carre(x):
    return x * x


def cube(x):
    return x * x * x


def factorielle(n):
    if n < 0:
        raise ValueError("La factorielle n'existe pas pour un nombre négatif.")
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat


def valeur_absolue(x):
    if x < 0:
        return -x
    return x


def maximum(liste):
    plus_grand = liste[0]
    for valeur in liste:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand


def minimum(liste):
    plus_petit = liste[0]
    for valeur in liste:
        if valeur < plus_petit:
            plus_petit = valeur
    return plus_petit


def moyenne(liste):
    total = 0
    for valeur in liste:
        total += valeur
    return total / len(liste)


def ecart_type(liste):
    m = moyenne(liste)
    ecarts_au_carre = []
    for valeur in liste:
        ecarts_au_carre.append(carre(valeur - m))
    return math.sqrt(moyenne(ecarts_au_carre))


def mediane(liste):
    triee = sorted(liste)
    n = len(triee)
    milieu = n // 2
    if n % 2 == 1:
        return triee[milieu]
    return (triee[milieu - 1] + triee[milieu]) / 2


def somme_cumulee(liste):
    """Calcule la somme cumulée d'une liste.

    Chaque élément du résultat est la somme de tous les éléments
    jusqu'à cette position incluse.

    Paramètre : liste (liste de nombres)
    Retour : liste, par exemple [1, 2, 3, 4] donne [1, 3, 6, 10]
    """
    resultat = []
    total = 0
    for valeur in liste:
        total += valeur
        resultat.append(total)
    return resultat


def compter_occurrences(liste):
    """Compte le nombre d'apparitions de chaque élément d'une liste.

    Paramètre : liste (liste d'éléments quelconques)
    Retour : dictionnaire {élément: nombre d'apparitions}
    """
    compteur = {}
    for element in liste:
        if element in compteur:
            compteur[element] += 1
        else:
            compteur[element] = 1
    return compteur


def inverser_dict(dictionnaire):
    """Inverse les clés et les valeurs d'un dictionnaire.

    Si plusieurs clés ont la même valeur, seule la dernière est gardée.

    Paramètre : dictionnaire (dict dont les valeurs peuvent servir de clés)
    Retour : nouveau dictionnaire {valeur: clé}
    """
    inverse = {}
    for cle, valeur in dictionnaire.items():
        inverse[valeur] = cle
    return inverse


def filtrer_pairs(liste):
    """Garde uniquement les nombres pairs d'une liste.

    Paramètre : liste (liste d'entiers)
    Retour : nouvelle liste contenant les nombres pairs, dans le même ordre
    """
    pairs = []
    for nombre in liste:
        if nombre % 2 == 0:
            pairs.append(nombre)
    return pairs


def celsius_to_fahrenheit(celsius):
    """Convertit une température de degrés Celsius en degrés Fahrenheit.

    Formule : F = (C * 9/5) + 32

    Paramètre : celsius (int ou float)
    Retour : float, la température en Fahrenheit
    """
    return (celsius * 9 / 5) + 32


def trouver_doublons(liste):
    """Trouve les éléments qui apparaissent plus d'une fois dans une liste.

    Paramètre : liste (liste d'éléments quelconques)
    Retour : liste des éléments en double, chacun présent une seule fois,
    dans l'ordre de leur première apparition
    """
    doublons = []
    for element, nombre in compter_occurrences(liste).items():
        if nombre > 1:
            doublons.append(element)
    return doublons


def calculer_moyenne_ponderee(valeurs, poids):
    """Calcule la moyenne pondérée d'une liste de valeurs.

    Chaque valeur est multipliée par son poids, puis la somme obtenue
    est divisée par la somme des poids.

    Paramètres :
        valeurs (liste de nombres)
        poids (liste de nombres de même longueur que valeurs)
    Retour : float
    Lève une ValueError si les deux listes n'ont pas la même longueur.
    """
    if len(valeurs) != len(poids):
        raise ValueError("Les listes valeurs et poids doivent avoir la même longueur.")
    total = 0
    total_poids = 0
    for i in range(len(valeurs)):
        total += valeurs[i] * poids[i]
        total_poids += poids[i]
    return total / total_poids
