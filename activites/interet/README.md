# Calculateur de Paiement Mensuel et Simulation d'Intérêts**

Vous travaillez pour une banque qui propose des prêts personnels. Vous devez créer un programme pour aider les clients à
estimer leur paiement mensuel et le montant total des intérêts payés pour différents montants de prêt et taux d'intérêt.

## Objectifs

1. Calculer le paiement mensuel en fonction d'un montant de prêt, d'un taux d'intérêt annuel et d'une durée de
   remboursement (en années).
2. Calculer le montant total des intérêts payés sur la durée du prêt.
3. Arrondir les résultats de manière adéquate pour les afficher aux clients.

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

2. **Calculs** :
    - Calculez le paiement mensuel brut en utilisant la formule ci-dessus avec `Math.Pow`.
    - Calculez le montant total des intérêts payés sur la durée du prêt, qui est :
      $\text{Total des Intérêts} = (\text{Paiement Mensuel} \times n) - P$
    - Détailler la part d’intérêt et de remboursement
    - Arrondissez les résultats à deux décimales en utilisant `Math.Round`.

3. Affichez les résultats arrondis.

## Exemples de calcul
V1 (attention l’arnaque)
```text
Entrez le montant du prêt (CHF) : 10000
Entrez le taux d'intérêt annuel (%) : 55
Entrez la durée du prêt en années : 5

--- Résultats ---
Frais mensuels       : 491.75 CHF
-->Dont  intérêts    : 325.09 CHF
Montant total versé  : 29505.16 CHF
Part la plus élevée des frais: 325.09 CHF
```

V2
```text
Entrez le montant du prêt (CHF) : 10000
Entrez le taux d'intérêt annuel (%) : 5
Entrez la durée du prêt en années : 5

--- Résultats ---
Frais mensuels       : 188.71 CHF
-->Dont  intérêts    : 22.05 CHF
Montant total versé  : 11322.74 CHF
Part la plus élevée des frais: 166.66 CHF
```

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

        // Calcul du taux d'intérêt mensuel et du nombre total de paiements
        double monthlyInterestRate = annualInterestRate / 100 / 12;
        int totalPayments = loanDurationYears * 12;

        // Calcul du paiement mensuel brut
        double rawMonthlyPayment = principal * monthlyInterestRate * Math.Pow(1 + monthlyInterestRate, totalPayments) /
                                   (Math.Pow(1 + monthlyInterestRate, totalPayments) - 1);


        double totalPaid = rawMonthlyPayment * totalPayments;
        // Calcul du total des intérêts payés
        double totalInterest = totalPaid - principal ;

        // Arrondi des valeurs
        totalInterest = Math.Round(totalInterest,2);
        rawMonthlyPayment = Math.Round(rawMonthlyPayment,2);
        totalPaid = Math.Round(totalPaid, 2);
        double rawInterestPayment = Math.Round(totalInterest / totalPayments, 2);

        // Affichage des résultats
        Console.WriteLine("\n--- Résultats ---");
        Console.WriteLine($"Frais mensuels       : {rawMonthlyPayment} CHF");
        Console.WriteLine($"-->Dont  intérêts    : {rawInterestPayment} CHF");
        Console.WriteLine($"Montant total versé  : {totalPaid} CHF");

        Console.WriteLine($"Part la plus élevée des frais: {Math.Max(rawMonthlyPayment-rawInterestPayment,rawInterestPayment)} CHF");

    }
}
```

</details>

