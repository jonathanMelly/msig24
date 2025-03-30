# Étape 1: Importation des modules nécessaires
import tkinter as tk
from tkinter import messagebox

# Étape 2: Création de la classe principale pour notre calculatrice
class CalculatriceTk:
    def __init__(self, root):
        # Étape 3: Configuration de la fenêtre principale
        self.root = root
        self.root.title("Calculatrice Python")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#e6e6e6")
        
        # Étape 4: Variable pour stocker l'expression
        self.expression = ""
        
        # Étape 5: Création des widgets d'affichage
        # Écran d'affichage
        self.ecran_resultat = tk.Entry(root, width=16, font=("Arial", 24), bd=5, 
                                      justify="right", bg="#f0f0f0")
        self.ecran_resultat.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.ecran_resultat.insert(0, "0")
        self.ecran_resultat.configure(state='readonly')
        
        # Étape 6: Création des boutons
        # Définition des boutons et de leur disposition
        boutons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1), ('^', 5, 2), ('Exit', 5, 3)
        ]
        
        # Étape 7: Création des boutons sur la grille
        for (text, row, col) in boutons:
            self.creer_bouton(text, row, col)
    
    # Étape 8: Méthode pour créer les boutons avec style
    def creer_bouton(self, text, row, col):
        if text == '=':
            # Bouton spécial pour le calcul
            bouton = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.calculer)
        elif text == 'C':
            # Bouton pour effacer tout
            bouton = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.effacer_tout)
        elif text == 'CE':
            # Bouton pour effacer un caractère
            bouton = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.effacer_dernier)
        elif text == 'Exit':
            # Bouton pour quitter
            bouton = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.root.destroy)
        else:
            # Boutons standards (chiffres et opérateurs)
            if text in '0123456789.':
                # Boutons pour les chiffres
                bouton = tk.Button(self.root, text=text, width=5, height=2,
                                  font=("Arial", 12, "bold"), bd=3, bg="#e6e6e6",
                                  command=lambda t=text: self.ajouter_a_expression(t))
            else:
                # Boutons pour les opérateurs
                bouton = tk.Button(self.root, text=text, width=5, height=2,
                                  font=("Arial", 12, "bold"), bd=3, bg="#cccccc",
                                  command=lambda t=text: self.ajouter_a_expression(t))
                
        bouton.grid(row=row, column=col, padx=5, pady=5)
    
    # Étape 9: Méthodes pour gérer les interactions
    def ajouter_a_expression(self, valeur):
        # Mise à jour de l'expression et de l'affichage
        self.expression += valeur
        self.ecran_resultat.configure(state='normal')
        self.ecran_resultat.delete(0, tk.END)
        self.ecran_resultat.insert(0, self.expression)
        self.ecran_resultat.configure(state='readonly')
    
    def effacer_tout(self):
        # Réinitialisation complète
        self.expression = ""
        self.ecran_resultat.configure(state='normal')
        self.ecran_resultat.delete(0, tk.END)
        self.ecran_resultat.insert(0, "0")
        self.ecran_resultat.configure(state='readonly')
    
    def effacer_dernier(self):
        # Supprimer le dernier caractère
        self.expression = self.expression[:-1]
        self.ecran_resultat.configure(state='normal')
        self.ecran_resultat.delete(0, tk.END)
        if self.expression:
            self.ecran_resultat.insert(0, self.expression)
        else:
            self.ecran_resultat.insert(0, "0")
        self.ecran_resultat.configure(state='readonly')
    
    # Étape 10: Méthode pour effectuer le calcul
    def calculer(self):
        try:
            # Remplacer ^ par ** pour la puissance
            expression_modifiee = self.expression.replace("^", "**")
            
            # Évaluer l'expression
            resultat = eval(expression_modifiee)
            
            # Afficher le résultat
            self.ecran_resultat.configure(state='normal')
            self.ecran_resultat.delete(0, tk.END)
            
            # Afficher sans décimales si c'est un entier
            if resultat == int(resultat):
                self.ecran_resultat.insert(0, str(int(resultat)))
            else:
                self.ecran_resultat.insert(0, str(resultat))
                
            self.ecran_resultat.configure(state='readonly')
            
            # Mettre à jour l'expression avec le résultat
            self.expression = str(resultat)
            
        except Exception as e:
            # Gestion des erreurs
            messagebox.showerror("Erreur", f"Erreur de calcul: {str(e)}")
            self.effacer_tout()

# Étape 11: Point d'entrée du programme
if __name__ == "__main__":
    # Création de la fenêtre principale
    root = tk.Tk()
    
    # Création de l'instance de la calculatrice
    app = CalculatriceTk(root)
    
    # Lancement de la boucle principale
    root.mainloop()
