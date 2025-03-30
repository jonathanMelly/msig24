# Étape 1: Définition de la fonction principale
def calculatrice():
    print("=== Calculatrice Python ===")
    print("Opérations disponibles: +, -, *, /, ^")
    print("Tapez 'q' pour quitter")
    
    # Étape 2: Création de la boucle principale
    while True:
        # Étape 3: Lecture de l'entrée utilisateur
        expression = input("\nEntrez une expression (ex: 5 + 3): ")
        
        # Étape 4: Vérification si l'utilisateur veut quitter
        if expression.lower() == 'q':
            print("Au revoir!")
            break
        
        # Étape 5: Traitement de l'expression avec gestion d'erreurs
        try:
            # Étape 6: Découpage de l'expression
            parties = expression.split()
            if len(parties) != 3:
                print("Format incorrect. Utilisez: nombre opérateur nombre")
                continue
            
            # Étape 7: Extraction et conversion des opérandes
            nombre1 = float(parties[0])
            operateur = parties[1]
            nombre2 = float(parties[2])
            
            # Étape 8: Exécution de l'opération selon l'opérateur
            resultat = 0
            if operateur == '+':
                resultat = nombre1 + nombre2
            elif operateur == '-':
                resultat = nombre1 - nombre2
            elif operateur == '*':
                resultat = nombre1 * nombre2
            elif operateur == '/':
                if nombre2 == 0:
                    print("Erreur: Division par zéro")
                    continue
                resultat = nombre1 / nombre2
            elif operateur == '^':
                resultat = nombre1 ** nombre2
            else:
                print(f"Opérateur '{operateur}' non reconnu")
                continue
            
            # Étape 9: Affichage du résultat
            # Pour les entiers, afficher sans décimale
            if resultat == int(resultat):
                print(f"Résultat: {int(resultat)}")
            else:
                print(f"Résultat: {resultat}")
            
        # Étape 10: Gestion des erreurs
        except ValueError:
            print("Erreur: Veuillez entrer des nombres valides")
        except Exception as e:
            print(f"Erreur: {e}")

# Étape 11: Point d'entrée du programme
if __name__ == "__main__":
    calculatrice()