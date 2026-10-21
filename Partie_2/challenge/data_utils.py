"""Module de fonctions mathématiques et statistiques de base."""

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
