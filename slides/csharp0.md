---
theme: default
title: C#1
class: text-center
drawings:
  persist: true
transition: slide-left
mdc: true
lineNumbers: true
---

# Anatomie d’un programme C#

---

## Exemple de code

```csharp {1|3-4,49|5-6,48|7-8,47|9-13|9|10|11|12|13|23-24|all}{maxHeight:'100px'}

using System;

namespace RobotBarista
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variables
            string client = "Jean-Michel";   // Nom du client
            int age = 42;                    // Âge du client
            bool aFaim = true;               // Indicateur de faim
            int nombreDeCafes = 3;           // Nombre de cafés qu'il souhaite boire

            // Introduction
            Console.WriteLine($"Bonjour, {client}! Bienvenue au Café du Robot 🤖☕️");

            // Condition : vérifier si le client a faim
            if (aFaim)
            {
                Console.WriteLine($"{client} est affamé ! On va lui préparer un petit snack.");
            }
            else
            {
                Console.WriteLine($"{client} n'a pas faim, mais il veut son café ! ☕️");
            }

            // Boucle : Servir les cafés demandés
            for (int i = 1; i <= nombreDeCafes; i++)
            {
                Console.WriteLine($"Préparation du café n°{i} pour {client}...");
                Console.WriteLine("Café prêt ! ☕️ Voici un café bien chaud pour vous !");
            }

            // Condition : vérifier l'âge pour offrir un dessert
            if (age > 40)
            {
                Console.WriteLine("On offre un dessert à Jean-Michel pour être un client fidèle (et un peu plus vieux) ! 🍰");
            }
            else
            {
                Console.WriteLine($"{client} est trop jeune pour le dessert offert, mais il reviendra sûrement !");
            }

            // Fin
            Console.WriteLine("Merci d'avoir commandé au Café du Robot, revenez quand vous voulez ! Au revoir !");
        }
    }
}
```
