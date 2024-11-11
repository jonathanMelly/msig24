# Calculateur de Paiement Mensuel et Simulation d'Intérêts**

Vous travaillez pour une banque qui propose des prêts personnels. Vous devez créer un programme pour aider les clients à
estimer leur paiement mensuel et le montant total des intérêts payés pour différents montants de prêt et taux d'intérêt.

## Objectifs

1. Calculer le paiement mensuel en fonction d'un montant de prêt, d'un taux d'intérêt annuel et d'une durée de
   remboursement (en années).
2. Calculer le montant total des intérêts payés sur la durée du prêt.
3. Limiter le paiement minimum et maximum mensuel avec les valeurs données par la banque.
4. Arrondir les résultats de manière adéquate pour les afficher aux clients.

## Formules

Le calcul du paiement mensuel d'un prêt est basé sur la formule de l'annuité :

$\text{Paiement Mensuel} = \frac{P \times rate \times (1 + rate)^n}{(1 + rate)^n - 1}$

où :

- \( P \) est le montant du prêt,
- \( rate \) est le taux d'intérêt mensuel (taux d'intérêt annuel divisé par 12),
- \( n \) est le nombre total de paiements (nombre d'années multiplié par 12).

## Instructions

1. Demandez à l'utilisateur de saisir :
    - Le montant du prêt (exemple : 10 000 CHF).
    - Le taux d'intérêt annuel en pourcentage (exemple : 5 %).
    - La durée du prêt en années (exemple : 5 ans).
    - Le paiement minimum mensuel accepté par la banque (exemple : 100 CHF).
    - Le paiement maximum mensuel accepté par la banque (exemple : 1 000 CHF).

2. **Calculs** :
    - Calculez le paiement mensuel brut en utilisant la formule ci-dessus avec `Math.Pow`.
    - Limitez le paiement mensuel brut entre les valeurs minimum et maximum fournies par la banque en utilisant
      `Math.Min` et `Math.Max`.
    - Calculez le montant total des intérêts payés sur la durée du prêt, qui est :
      $\text{Total des Intérêts} = (\text{Paiement Mensuel} \times n) - P$
    - Arrondissez les résultats à deux décimales en utilisant `Math.Round`.

3. Affichez les résultats arrondis.

## Exemple de calcul

Imaginons un prêt de 10 000 CHF, remboursé sur 5 ans (60 mois) avec un taux d'intérêt de 5 % par an.

1. Supposons que le **paiement mensuel** calculé soit de 188,71 CHF.
2. Sur 60 mois, le **montant total des paiements** sera donc $188,71 \times 60 = 11 322,60$ CHF.
3. En soustrayant le montant initial du prêt, soit 10 000 CHF, on obtient :
   $\text{Total des Intérêts} = 11 322,60 - 10 000 = 1 322,60 \, CHF$

Le montant des intérêts est donc de 1 322,60 CHF, et c’est ce que l’on obtient en appliquant la formule $(\text{Paiement
Mensuel} \times n) - P$.

Cela montre la différence entre le montant que l’emprunteur rembourse et le montant qu’il a initialement emprunté, qui
représente donc uniquement les frais d’intérêt.

## Exemple de solution (pour comparer)

<details>
<summary>J’ai déjà codé une solution et souhaite comparer</summary>

```csharp
using System;

class LoanCalculator
{
    static void Main()
    {
        // Saisie des données par l'utilisateur
        Console.Write("Entrez le montant du prêt (CHF) : ");
        double principal = Convert.ToDouble(Console.ReadLine());

        Console.Write("Entrez le taux d'intérêt annuel (%) : ");
        double annualInterestRate = Convert.ToDouble(Console.ReadLine());

        Console.Write("Entrez la durée du prêt en années : ");
        int loanDurationYears = Convert.ToInt32(Console.ReadLine());

        Console.Write("Entrez le paiement minimum mensuel accepté (CHF) : ");
        double minMonthlyPayment = Convert.ToDouble(Console.ReadLine());

        Console.Write("Entrez le paiement maximum mensuel accepté (CHF) : ");
        double maxMonthlyPayment = Convert.ToDouble(Console.ReadLine());

        // Calcul du taux d'intérêt mensuel et du nombre total de paiements
        double monthlyInterestRate = annualInterestRate / 100 / 12;
        int totalPayments = loanDurationYears * 12;

        // Calcul du paiement mensuel brut
        double rawMonthlyPayment = principal * monthlyInterestRate * Math.Pow(1 + monthlyInterestRate, totalPayments) /
                                   (Math.Pow(1 + monthlyInterestRate, totalPayments) - 1);

        // Limite entre le paiement minimum et maximum
        double monthlyPayment = Math.Max(minMonthlyPayment, Math.Min(rawMonthlyPayment, maxMonthlyPayment));

        // Calcul du total des intérêts payés
        double totalInterest = (monthlyPayment * totalPayments) - principal;

        // Arrondi des valeurs
        monthlyPayment = Math.Round(monthlyPayment, 2);
        totalInterest = Math.Round(totalInterest, 2);

        // Affichage des résultats
        Console.WriteLine("\n--- Résultats ---");
        Console.WriteLine($"Paiement Mensuel : {monthlyPayment} CHF");
        Console.WriteLine($"Total des Intérêts Payés : {totalInterest} CHF");
    }
}
```

</details>

