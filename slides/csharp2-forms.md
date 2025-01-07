---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  Présentation des bases de Windows Forms en C#
drawings:
  persist: false
transition: slide-left
title: Windows Forms C# - Les Bases
---

# Windows Forms C#
## Les éléments fondamentaux

---

# Qu'est-ce que Windows Forms ?

- Framework graphique pour créer des applications Windows
- Fait partie du framework .NET
- Idéal pour les applications d'entreprise
- Interface graphique rapide à développer

---

# Création d'un projet Windows Forms

```csharp
// Dans Visual Studio :
// 1. File -> New Project
// 2. Windows Forms App (.NET Core)
// 3. Choisir un nom et un emplacement
```

Le fichier Program.cs est créé automatiquement :

```csharp
static class Program
{
    [STAThread]
    static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Application.Run(new Form1());
    }
}
```

---

# La classe Form

- Base de toute fenêtre Windows Forms
- Hérite de la classe `System.Windows.Forms.Form`

```csharp
public class MainWindow : Form
{
    public MainWindow()
    {
        Text = "Ma première application";
        Size = new Size(800, 600);
        StartPosition = FormStartPosition.CenterScreen;
    }
}
```

---

# Les contrôles de base

## Button
```csharp
Button submitButton = new Button();
submitButton.Text = "Valider";
submitButton.Location = new Point(100, 100);
submitButton.Click += SubmitButton_Click;

private void SubmitButton_Click(object sender, EventArgs e)
{
    MessageBox.Show("Bouton cliqué !");
}
```

## TextBox
```csharp
TextBox userInput = new TextBox();
userInput.Location = new Point(100, 50);
userInput.Size = new Size(200, 20);
userInput.TextChanged += UserInput_TextChanged;
```

---

# Les contrôles avancés

## ListBox
```csharp
ListBox itemList = new ListBox();
itemList.Items.Add("Élément 1");
itemList.Items.Add("Élément 2");
itemList.Location = new Point(50, 50);
itemList.Size = new Size(200, 100);
```

## ComboBox
```csharp
ComboBox optionSelect = new ComboBox();
optionSelect.Items.AddRange(new string[] { 
    "Option 1", 
    "Option 2", 
    "Option 3" 
});
optionSelect.SelectedIndexChanged += OptionSelect_SelectedIndexChanged;
```

---

# Gestion de la disposition (Layout)

## TableLayoutPanel
```csharp
TableLayoutPanel layout = new TableLayoutPanel();
layout.RowCount = 2;
layout.ColumnCount = 2;
layout.Dock = DockStyle.Fill;

layout.Controls.Add(new Button { Text = "1" }, 0, 0);
layout.Controls.Add(new Button { Text = "2" }, 1, 0);
```

## FlowLayoutPanel
```csharp
FlowLayoutPanel flow = new FlowLayoutPanel();
flow.Dock = DockStyle.Top;
flow.AutoSize = true;

flow.Controls.Add(new Button { Text = "Bouton 1" });
flow.Controls.Add(new Button { Text = "Bouton 2" });
```

---

# Gestion des événements

## Structure de base
```csharp
public class MainForm : Form
{
    private TextBox inputBox;
    private Button saveButton;

    public MainForm()
    {
        InitializeComponents();
        AttachEvents();
    }

    private void AttachEvents()
    {
        saveButton.Click += SaveButton_Click;
        inputBox.TextChanged += InputBox_TextChanged;
    }
}
```

---

# Boîtes de dialogue

## MessageBox
```csharp
// Simple message
MessageBox.Show("Opération réussie !");

// Message avec titre
MessageBox.Show(
    "Voulez-vous sauvegarder ?",
    "Confirmation",
    MessageBoxButtons.YesNo,
    MessageBoxIcon.Question
);
```

## OpenFileDialog
```csharp
OpenFileDialog openFile = new OpenFileDialog();
openFile.Filter = "Fichiers texte (*.txt)|*.txt|Tous les fichiers (*.*)|*.*";

if (openFile.ShowDialog() == DialogResult.OK)
{
    string filePath = openFile.FileName;
    // Traitement du fichier
}
```

---

# Bonnes pratiques

1. **Structure du code**
   - Séparer la logique métier de l'interface
   - Utiliser des régions pour organiser le code
   - Nommer clairement les contrôles

2. **Performance**
   - Utiliser `SuspendLayout()` pendant les modifications massives
   - Libérer les ressources avec `Dispose()`
   - Éviter les boucles dans les gestionnaires d'événements

3. **Interface utilisateur**
   - Respecter les guidelines Microsoft
   - Prévoir les cas d'erreur
   - Rendre l'interface responsive

---

# Débogage

## Outils disponibles
- Points d'arrêt
- Fenêtre Watch
- Vue des propriétés live
- Inspecteur de contrôles

```csharp
// Exemple de débogage basique
private void DebugButton_Click(object sender, EventArgs e)
{
    Debug.WriteLine("Valeur actuelle : " + textBox1.Text);
    if (string.IsNullOrEmpty(textBox1.Text))
    {
        Debug.Assert(false, "TextBox vide !");
    }
}
```

---

# Resources et documentation

- Documentation officielle Microsoft
- Windows Forms GitHub repository
- Communauté Stack Overflow
- Forums MSDN

Pour aller plus loin :
- Data binding
- MDI Forms
- Custom controls
- Internationalisation

