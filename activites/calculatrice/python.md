# Calculatrice Python (Console)

## Étape 1: Définition de la fonction principale
```python
def calculator():
    print("=== Python Calculator ===")
    print("Available operations: +, -, *, /, ^")
    print("Type 'q' to quit")
```
Nous définissons la fonction principale `calculator()` et affichons un message d'accueil avec les instructions pour l'utilisateur.

## Étape 2: Création de la boucle principale
```python
    while True:
        # Code à venir...
```
Cette boucle infinie permet à la calculatrice de continuer à fonctionner jusqu'à ce que l'utilisateur décide de quitter.

## Étape 3: Lecture de l'entrée utilisateur
```python
        expression = input("\nEnter an expression (ex: 5 + 3): ")
```
La fonction `input()` permet de lire ce que l'utilisateur tape au clavier et le stocke dans la variable `expression`.

## Étape 4: Vérification si l'utilisateur veut quitter
```python
        if expression.lower() == 'q':
            print("Goodbye!")
            break
```
Si l'utilisateur tape 'q', nous affichons un message d'au revoir et utilisons `break` pour sortir de la boucle `while`.

## Étape 5: Traitement de l'expression avec gestion d'erreurs
```python
        try:
            # Code à venir...
```
Le bloc `try` nous permet de gérer les erreurs qui pourraient survenir lors du traitement de l'expression.

## Étape 6: Découpage de l'expression
```python
            parts = expression.split()
            if len(parts) != 3:
                print("Incorrect format. Use: number operator number")
                continue
```
La méthode `split()` divise la chaîne en une liste de sous-chaînes en utilisant l'espace comme séparateur. Ensuite, nous vérifions que l'expression contient exactement 3 parties (nombre1, opérateur, nombre2).

## Étape 7: Extraction et conversion des opérandes
```python
            number1 = float(parts[0])
            operator = parts[1]
            number2 = float(parts[2])
```
Nous extrayons les deux nombres et l'opérateur de la liste `parts`. La fonction `float()` convertit les chaînes en nombres décimaux.

## Étape 8: Exécution de l'opération selon l'opérateur
```python
            result = 0
            if operator == '+':
                result = number1 + number2
            elif operator == '-':
                result = number1 - number2
            # etc.
```
Cette structure conditionnelle vérifie l'opérateur et effectue l'opération correspondante. Notez la gestion spéciale pour la division par zéro.

## Étape 9: Affichage du résultat
```python
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
```
Nous vérifions si le résultat est un nombre entier pour l'afficher sans décimale si possible, ce qui rend l'affichage plus propre.

## Étape 10: Gestion des erreurs
```python
        except ValueError:
            print("Error: Please enter valid numbers")
        except Exception as e:
            print(f"Error: {e}")
```
Le bloc `except ValueError` gère les erreurs lors de la conversion des chaînes en nombres. Le second bloc `except` attrape toutes les autres erreurs possibles.

## Étape 11: Point d'entrée du programme
```python
if __name__ == "__main__":
    calculator()
```
Cette ligne permet d'exécuter la fonction `calculator()` uniquement lorsque le script est exécuté directement (et non importé comme module).

# Calculatrice Python (GUI)

## Étape 1: Importation des modules nécessaires
```python
import tkinter as tk
from tkinter import messagebox
```
Nous importons le module `tkinter` pour l'interface graphique et le sous-module `messagebox` pour afficher des messages d'erreur.

## Étape 2: Création de la classe principale
```python
class TkCalculator:
    def __init__(self, root):
        # Code à venir...
```
Nous créons une classe pour organiser notre code. Le constructeur prend un paramètre `root` qui est la fenêtre principale de l'application.

## Étape 3: Configuration de la fenêtre principale
```python
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400") //TODO corriger le problème constaté lors du test
        self.root.resizable(False, False)
        self.root.configure(bg="#e6e6e6")
```
Nous configurons les propriétés de base de la fenêtre: titre, dimensions, empêcher le redimensionnement et définir une couleur de fond.

## Étape 4: Variable pour stocker l'expression
```python
        self.expression = ""
```
Cette variable stockera l'expression mathématique que l'utilisateur est en train de construire.

## Étape 5: Création des widgets d'affichage
```python
        self.result_display = tk.Entry(root, width=16, font=("Arial", 24), bd=5, 
                                      justify="right", bg="#f0f0f0")
        self.result_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.result_display.insert(0, "0")
        self.result_display.configure(state='readonly')
```
Nous créons un champ de saisie `Entry` qui servira d'écran pour afficher l'expression et le résultat. Nous le configurons en mode lecture seule après y avoir inséré "0".

## Étape 6: Définition des boutons
```python
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            # ajouter les autres boutons en suivant la même logique
        ]
```
Nous définissons une liste de tuples pour chaque bouton, contenant le texte du bouton et sa position (ligne, colonne) dans la grille.

## Étape 7: Création des boutons sur la grille
```python
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
```
Nous parcourons la liste des boutons et appelons la méthode `create_button` pour chacun d'eux.

## Étape 8: Méthode pour créer les boutons avec style
```python
    def create_button(self, text, row, col):
        if text == '=':
            # Special button for calculation
            button = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.calculate)
        elif text == 'C':
            # Button to clear all
            button = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.clear_all)
        elif text == 'CE':
            # Button to clear last character
            button = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.clear_last)
        elif text == 'Exit':
            # Button to quit
            button = tk.Button(self.root, text=text, width=5, height=2,
                              font=("Arial", 12, "bold"), bd=3, bg="#ff9980",
                              command=self.root.destroy)
        else:
            # Standard buttons (digits and operators)
            if text in '0123456789.':
                # Buttons for digits
                button = tk.Button(self.root, text=text, width=5, height=2,
                                  font=("Arial", 12, "bold"), bd=3, bg="#e6e6e6",
                                  command=lambda t=text: self.add_to_expression(t))
            else:
                # Buttons for operators
                button = tk.Button(self.root, text=text, width=5, height=2,
                                  font=("Arial", 12, "bold"), bd=3, bg="#cccccc",
                                  command=lambda t=text: self.add_to_expression(t))
                
        button.grid(row=row, column=col, padx=5, pady=5)
```
Cette méthode crée un bouton avec un style différent selon son type (égal, effacer, chiffre, opérateur) et lui associe la fonction appropriée.

## Étape 9: Méthodes pour gérer les interactions
```python
    def add_to_expression(self, value):
        # Mise à jour de l'expression et de l'affichage
        self.expression += value
        self.result_display.configure(state='normal')
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, self.expression)
        self.result_display.configure(state='readonly')
    
    def clear_all(self):
        # Réinitialisation complète
        self.expression = ""
        self.result_display.configure(state='normal')
        self.result_display.delete(0, tk.END)
        self.result_display.insert(0, "0")
        self.result_display.configure(state='readonly')
    
    def clear_last(self):
        # Supprimer le dernier caractère
        self.expression = self.expression[:-1]
        self.result_display.configure(state='normal')
        self.result_display.delete(0, tk.END)
        if self.expression:
            self.result_display.insert(0, self.expression)
        else:
            self.result_display.insert(0, "0")
        self.result_display.configure(state='readonly')
```
Ces méthodes gèrent les interactions avec les boutons de la calculatrice: ajouter à l'expression, effacer tout, effacer le dernier caractère.

## Étape 10: Méthode pour effectuer le calcul
```python
    def calculate(self):
        try:
            # Replace ^ with ** for power
            modified_expression = self.expression.replace("^", "**")
            
            # Evaluate expression
            result = eval(modified_expression)
            
            # Display result
            self.result_display.configure(state='normal')
            self.result_display.delete(0, tk.END)
            
            # Display without decimals if it's an integer
            if result == int(result):
                self.result_display.insert(0, str(int(result)))
            else:
                self.result_display.insert(0, str(result))
                
            self.result_display.configure(state='readonly')
            
            # Update expression with result
            self.expression = str(result)
            
        except Exception as e:
            # Error handling
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
            self.clear_all()
```
Cette méthode évalue l'expression mathématique et gère les erreurs. Elle utilise la fonction `eval()` pour calculer le résultat de l'expression.

## Étape 11: Point d'entrée du programme
```python
if __name__ == "__main__":
    # Création de la fenêtre principale
    root = tk.Tk()
    
    # Création de l'instance de la calculatrice
    app = TkCalculator(root)
    
    # Lancement de la boucle principale
    root.mainloop()
```
Ce bloc crée la fenêtre principale, initialise notre calculatrice et lance la boucle principale de Tkinter qui gère les événements de l'interface graphique.

# Principales différences entre les versions

### Version Console:
- Utilise une approche procédurale
- Lit l'entrée utilisateur via le terminal
- Traite manuellement chaque opérateur
- Affiche les messages d'erreur dans la console

### Version Tkinter:
- Utilise une approche orientée objet avec une classe
- Fournit une interface graphique avec des boutons
- Utilise `eval()` pour calculer l'expression
- Affiche les erreurs dans des boîtes de dialogue
- Offre des fonctionnalités supplémentaires (effacer le dernier caractère, bouton quitter)

# Aide : code complets
<details>
<summary>Console</summary>

[console](./calculatrice-python.py)
</details>

<details>
<summary>GUI</summary>

[GUI](./calculatrice-tkinter.py)
</details>
