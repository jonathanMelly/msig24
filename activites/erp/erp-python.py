import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import mysql.connector
from mysql.connector import Error
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os
import datetime
from tkinter import filedialog



class ERP:
    def __init__(self, root):
        self.root = root
        self.root.title("ERP Client - Gestion des Commandes et Produits")
        self.root.geometry("1200x700")
        
        # Variables de connexion à la base de données
        self.host = "localhost"
        self.database = "erp"
        self.user = "root"
        self.password = "123"
        
        # Initialisation de la connexion à la DB
        self.connection = None
        self.create_database()
        self.connect_database()
        
        # Création de l'interface utilisateur
        self.create_ui()
        
    def create_database(self):
        """Crée la base de données et les tables si elles n'existent pas"""
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
            cursor = conn.cursor()
            
            # Création de la base de données
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            
            # Connexion à la nouvelle base de données
            cursor.execute(f"USE {self.database}")
            
            # Création de la table clients
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clients (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(100) NOT NULL,
                    prenom VARCHAR(100) NOT NULL,
                    email VARCHAR(100),
                    telephone VARCHAR(20),
                    adresse TEXT
                )
            """)
            
            # Création de la table produits
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produits (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nom VARCHAR(100) NOT NULL,
                    description TEXT,
                    prix DECIMAL(10, 2) NOT NULL,
                    stock INT NOT NULL
                )
            """)
            
            # Création de la table commandes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS commandes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    client_id INT NOT NULL,
                    date_commande DATETIME NOT NULL,
                    statut VARCHAR(50) NOT NULL,
                    FOREIGN KEY (client_id) REFERENCES clients(id)
                )
            """)
            
            # Création de la table details_commande
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS details_commande (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    commande_id INT NOT NULL,
                    produit_id INT NOT NULL,
                    quantite INT NOT NULL,
                    prix_unitaire DECIMAL(10, 2) NOT NULL,
                    FOREIGN KEY (commande_id) REFERENCES commandes(id),
                    FOREIGN KEY (produit_id) REFERENCES produits(id)
                )
            """)
            
            conn.commit()
            conn.close()
            print("Base de données et tables créées avec succès")
            
        except Error as e:
            print(f"Erreur lors de la création de la base de données: {e}")

    def connect_database(self):
        """Établit la connexion à la base de données"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connexion à la base de données établie")
        except Error as e:
            print(f"Erreur de connexion à la base de données: {e}")
            messagebox.showerror("Erreur de connexion", f"Impossible de se connecter à la base de données: {e}")

    def create_ui(self):
        """Crée l'interface utilisateur principale"""
        # Création du notebook (onglets)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Création des onglets
        self.tab_clients = ttk.Frame(self.notebook)
        self.tab_produits = ttk.Frame(self.notebook)
        self.tab_commandes = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_clients, text="Clients")
        self.notebook.add(self.tab_produits, text="Produits")
        self.notebook.add(self.tab_commandes, text="Commandes")
        
        # Initialisation des interfaces pour chaque onglet
        self.init_clients_tab()
        self.init_produits_tab()
        self.init_commandes_tab()
        
        # Barre de menu
        self.create_menu()

    def create_menu(self):
        """Crée la barre de menu"""
        menubar = tk.Menu(self.root)
        
        # Menu Fichier
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Exporter les clients (PDF)", command=self.export_clients_pdf)
        file_menu.add_command(label="Exporter les produits (PDF)", command=self.export_produits_pdf)
        file_menu.add_command(label="Exporter les commandes (PDF)", command=self.export_commandes_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Quitter", command=self.root.quit)
        
        menubar.add_cascade(label="Fichier", menu=file_menu)
        
        # Menu Aide
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="À propos", command=self.show_about)
        
        menubar.add_cascade(label="Aide", menu=help_menu)
        
        self.root.config(menu=menubar)

    def init_clients_tab(self):
        """Initialise l'onglet des clients"""
        # Frame pour les contrôles
        control_frame = ttk.LabelFrame(self.tab_clients, text="Gestion des clients")
        control_frame.pack(fill="x", padx=10, pady=10)
        
        # Formulaire d'ajout/modification de client
        ttk.Label(control_frame, text="Nom:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.client_nom = ttk.Entry(control_frame, width=30)
        self.client_nom.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Prénom:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.client_prenom = ttk.Entry(control_frame, width=30)
        self.client_prenom.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.client_email = ttk.Entry(control_frame, width=30)
        self.client_email.grid(row=1, column=1, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Téléphone:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
        self.client_telephone = ttk.Entry(control_frame, width=30)
        self.client_telephone.grid(row=1, column=3, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Adresse:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.client_adresse = ttk.Entry(control_frame, width=80)
        self.client_adresse.grid(row=2, column=1, columnspan=3, padx=5, pady=5)
        
        # Boutons d'action
        btn_frame = ttk.Frame(control_frame)
        btn_frame.grid(row=3, column=0, columnspan=4, pady=10)
        
        ttk.Button(btn_frame, text="Ajouter", command=self.add_client).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Modifier", command=self.update_client).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Supprimer", command=self.delete_client).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Rafraîchir", command=self.load_clients).pack(side="left", padx=5)
        
        # Tableau des clients
        columns = ("id", "nom", "prenom", "email", "telephone", "adresse")
        self.clients_tree = ttk.Treeview(self.tab_clients, columns=columns, show="headings")
        
        # Définition des en-têtes
        self.clients_tree.heading("id", text="ID")
        self.clients_tree.heading("nom", text="Nom")
        self.clients_tree.heading("prenom", text="Prénom")
        self.clients_tree.heading("email", text="Email")
        self.clients_tree.heading("telephone", text="Téléphone")
        self.clients_tree.heading("adresse", text="Adresse")
        
        # Définition des largeurs de colonnes
        self.clients_tree.column("id", width=50)
        self.clients_tree.column("nom", width=150)
        self.clients_tree.column("prenom", width=150)
        self.clients_tree.column("email", width=200)
        self.clients_tree.column("telephone", width=150)
        self.clients_tree.column("adresse", width=300)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tab_clients, orient="vertical", command=self.clients_tree.yview)
        self.clients_tree.configure(yscrollcommand=scrollbar.set)
        
        # Placement du tableau et de la scrollbar
        self.clients_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)
        
        # Événement de sélection
        self.clients_tree.bind("<<TreeviewSelect>>", self.on_client_select)
        
        # Chargement initial des clients
        self.load_clients()

    def init_produits_tab(self):
        """Initialise l'onglet des produits"""
        # Frame pour les contrôles
        control_frame = ttk.LabelFrame(self.tab_produits, text="Gestion des produits")
        control_frame.pack(fill="x", padx=10, pady=10)
        
        # Formulaire d'ajout/modification de produit
        ttk.Label(control_frame, text="Nom:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.produit_nom = ttk.Entry(control_frame, width=40)
        self.produit_nom.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Prix:").grid(row=0, column=2, padx=5, pady=5, sticky="e")
        self.produit_prix = ttk.Entry(control_frame, width=15)
        self.produit_prix.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Stock:").grid(row=0, column=4, padx=5, pady=5, sticky="e")
        self.produit_stock = ttk.Entry(control_frame, width=10)
        self.produit_stock.grid(row=0, column=5, padx=5, pady=5)
        
        ttk.Label(control_frame, text="Description:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.produit_description = ttk.Entry(control_frame, width=80)
        self.produit_description.grid(row=1, column=1, columnspan=5, padx=5, pady=5)
        
        # Boutons d'action
        btn_frame = ttk.Frame(control_frame)
        btn_frame.grid(row=2, column=0, columnspan=6, pady=10)
        
        ttk.Button(btn_frame, text="Ajouter", command=self.add_produit).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Modifier", command=self.update_produit).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Supprimer", command=self.delete_produit).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Rafraîchir", command=self.load_produits).pack(side="left", padx=5)
        
        # Tableau des produits
        columns = ("id", "nom", "description", "prix", "stock")
        self.produits_tree = ttk.Treeview(self.tab_produits, columns=columns, show="headings")
        
        # Définition des en-têtes
        self.produits_tree.heading("id", text="ID")
        self.produits_tree.heading("nom", text="Nom")
        self.produits_tree.heading("description", text="Description")
        self.produits_tree.heading("prix", text="Prix (CHF)")
        self.produits_tree.heading("stock", text="Stock")
        
        # Définition des largeurs de colonnes
        self.produits_tree.column("id", width=50)
        self.produits_tree.column("nom", width=200)
        self.produits_tree.column("description", width=400)
        self.produits_tree.column("prix", width=100)
        self.produits_tree.column("stock", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(self.tab_produits, orient="vertical", command=self.produits_tree.yview)
        self.produits_tree.configure(yscrollcommand=scrollbar.set)
        
        # Placement du tableau et de la scrollbar
        self.produits_tree.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y", pady=10)
        
        # Événement de sélection
        self.produits_tree.bind("<<TreeviewSelect>>", self.on_produit_select)
        
        # Chargement initial des produits
        self.load_produits()

    def init_commandes_tab(self):
        """Initialise l'onglet des commandes"""
        # Diviser l'onglet en deux parties
        paned_window = ttk.PanedWindow(self.tab_commandes, orient=tk.VERTICAL)
        paned_window.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Frame pour les commandes
        commandes_frame = ttk.LabelFrame(paned_window, text="Liste des commandes")
        paned_window.add(commandes_frame, weight=1)
        
        # Frame pour les détails de commande
        details_frame = ttk.LabelFrame(paned_window, text="Détails de la commande")
        paned_window.add(details_frame, weight=1)
        
        # Tableau des commandes
        columns = ("id", "client", "date", "statut", "total")
        self.commandes_tree = ttk.Treeview(commandes_frame, columns=columns, show="headings")
        
        # Définition des en-têtes
        self.commandes_tree.heading("id", text="ID")
        self.commandes_tree.heading("client", text="Client")
        self.commandes_tree.heading("date", text="Date")
        self.commandes_tree.heading("statut", text="Statut")
        self.commandes_tree.heading("total", text="Total (CHF)")
        
        # Définition des largeurs de colonnes
        self.commandes_tree.column("id", width=50)
        self.commandes_tree.column("client", width=200)
        self.commandes_tree.column("date", width=150)
        self.commandes_tree.column("statut", width=100)
        self.commandes_tree.column("total", width=100)
        
        # Scrollbar pour les commandes
        scrollbar1 = ttk.Scrollbar(commandes_frame, orient="vertical", command=self.commandes_tree.yview)
        self.commandes_tree.configure(yscrollcommand=scrollbar1.set)
        
        # Placement du tableau des commandes et de sa scrollbar
        self.commandes_tree.pack(side="left", fill="both", expand=True)
        scrollbar1.pack(side="right", fill="y")
        
        # Boutons pour les commandes
        btn_frame = ttk.Frame(commandes_frame)
        btn_frame.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame, text="Nouvelle commande", command=self.new_commande).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Modifier statut", command=self.update_commande_statut).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Supprimer", command=self.delete_commande).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Rafraîchir", command=self.load_commandes).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Exporter PDF", command=self.export_commande_pdf).pack(side="left", padx=5)
        
        # Tableau des détails de commande
        columns = ("id", "produit", "quantite", "prix_unitaire", "total")
        self.details_tree = ttk.Treeview(details_frame, columns=columns, show="headings")
        
        # Définition des en-têtes
        self.details_tree.heading("id", text="ID")
        self.details_tree.heading("produit", text="Produit")
        self.details_tree.heading("quantite", text="Quantité")
        self.details_tree.heading("prix_unitaire", text="Prix unitaire (CHF)")
        self.details_tree.heading("total", text="Total (CHF)")
        
        # Définition des largeurs de colonnes
        self.details_tree.column("id", width=50)
        self.details_tree.column("produit", width=300)
        self.details_tree.column("quantite", width=100)
        self.details_tree.column("prix_unitaire", width=100)
        self.details_tree.column("total", width=100)
        
        # Scrollbar pour les détails
        scrollbar2 = ttk.Scrollbar(details_frame, orient="vertical", command=self.details_tree.yview)
        self.details_tree.configure(yscrollcommand=scrollbar2.set)
        
        # Placement du tableau des détails et de sa scrollbar
        self.details_tree.pack(side="left", fill="both", expand=True)
        scrollbar2.pack(side="right", fill="y")
        
        # Boutons pour les détails
        btn_frame2 = ttk.Frame(details_frame)
        btn_frame2.pack(fill="x", pady=5)
        
        ttk.Button(btn_frame2, text="Ajouter produit", command=self.add_produit_to_commande).pack(side="left", padx=5)
        ttk.Button(btn_frame2, text="Modifier quantité", command=self.update_detail_quantite).pack(side="left", padx=5)
        ttk.Button(btn_frame2, text="Supprimer produit", command=self.delete_detail).pack(side="left", padx=5)
        
        # Événement de sélection pour les commandes
        self.commandes_tree.bind("<<TreeviewSelect>>", self.on_commande_select)
        
        # Chargement initial des commandes
        self.load_commandes()
        
        # Variable pour stocker l'ID de la commande sélectionnée
        self.selected_commande_id = None

    # ====================== FONCTIONS POUR LES CLIENTS ======================

    def load_clients(self):
        """Charge les clients depuis la base de données"""
        # Effacer les données actuelles
        for item in self.clients_tree.get_children():
            self.clients_tree.delete(item)
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM clients")
                rows = cursor.fetchall()
                
                for row in rows:
                    self.clients_tree.insert("", "end", values=row)
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement des clients: {e}")

    def add_client(self):
        """Ajoute un nouveau client"""
        nom = self.client_nom.get().strip()
        prenom = self.client_prenom.get().strip()
        email = self.client_email.get().strip()
        telephone = self.client_telephone.get().strip()
        adresse = self.client_adresse.get().strip()
        
        if not nom or not prenom:
            messagebox.showwarning("Attention", "Les champs Nom et Prénom sont obligatoires")
            return
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    INSERT INTO clients (nom, prenom, email, telephone, adresse)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values = (nom, prenom, email, telephone, adresse)
                cursor.execute(query, values)
                self.connection.commit()
                
                cursor.close()
                messagebox.showinfo("Succès", "Client ajouté avec succès")

                # Réinitialiser les champs
                self.client_nom.delete(0, tk.END)
                self.client_prenom.delete(0, tk.END)
                self.client_email.delete(0, tk.END)
                self.client_telephone.delete(0, tk.END)
                self.client_adresse.delete(0, tk.END)
                
                # Rafraîchir la liste
                self.load_clients()
                
                
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout du client: {e}")

    def update_produit(self):
        """Modifie un produit existant"""
        selected = self.produits_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un produit à modifier")
            return
        
        produit_id = self.produits_tree.item(selected[0], "values")[0]
        nom = self.produit_nom.get().strip()
        description = self.produit_description.get().strip()
        prix_str = self.produit_prix.get().strip()
        stock_str = self.produit_stock.get().strip()
        
        if not nom:
            messagebox.showwarning("Attention", "Le champ Nom est obligatoire")
            return
        
        try:
            prix = float(prix_str)
            stock = int(stock_str)
            
            if prix < 0:
                messagebox.showwarning("Attention", "Le prix doit être positif")
                return
                
            if stock < 0:
                messagebox.showwarning("Attention", "Le stock doit être positif")
                return
                
        except ValueError:
            messagebox.showwarning("Attention", "Prix et Stock doivent être des nombres valides")
            return
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    UPDATE produits
                    SET nom = %s, description = %s, prix = %s, stock = %s
                    WHERE id = %s
                """
                values = (nom, description, prix, stock, produit_id)
                cursor.execute(query, values)
                self.connection.commit()
                
                cursor.close()
                messagebox.showinfo("Succès", "Produit modifié avec succès")
                
                # Réinitialiser les champs
                self.produit_nom.delete(0, tk.END)
                self.produit_description.delete(0, tk.END)
                self.produit_prix.delete(0, tk.END)
                self.produit_stock.delete(0, tk.END)
                
                # Rafraîchir la liste
                self.load_produits()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la modification du produit: {e}")

    def delete_produit(self):
        """Supprime un produit"""
        selected = self.produits_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un produit à supprimer")
            return
        
        produit_id = self.produits_tree.item(selected[0], "values")[0]
        
        # Vérifier si le produit est utilisé dans des commandes
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM details_commande WHERE produit_id = %s", (produit_id,))
                count = cursor.fetchone()[0]
                
                if count > 0:
                    messagebox.showwarning("Attention", "Ce produit est utilisé dans des commandes et ne peut pas être supprimé")
                    cursor.close()
                    return
                
                # Demander confirmation
                if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce produit ?"):
                    cursor.execute("DELETE FROM produits WHERE id = %s", (produit_id,))
                    self.connection.commit()
                    messagebox.showinfo("Succès", "Produit supprimé avec succès")
                    
                    # Réinitialiser les champs
                    self.produit_nom.delete(0, tk.END)
                    self.produit_description.delete(0, tk.END)
                    self.produit_prix.delete(0, tk.END)
                    self.produit_stock.delete(0, tk.END)
                    
                    # Rafraîchir la liste
                    self.load_produits()
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression du produit: {e}")

    def on_produit_select(self, event):
        """Gère l'événement de sélection d'un produit"""
        selected = self.produits_tree.selection()
        if selected:
            # Récupérer les valeurs du produit sélectionné
            values = self.produits_tree.item(selected[0], "values")
            
            # Effacer les champs
            self.produit_nom.delete(0, tk.END)
            self.produit_description.delete(0, tk.END)
            self.produit_prix.delete(0, tk.END)
            self.produit_stock.delete(0, tk.END)
            
            # Remplir les champs avec les valeurs du produit
            self.produit_nom.insert(0, values[1])
            self.produit_description.insert(0, values[2] if values[2] else "")
            self.produit_prix.insert(0, values[3])
            self.produit_stock.insert(0, values[4])

    # ====================== FONCTIONS POUR LES COMMANDES ======================

    def load_commandes(self):
        """Charge les commandes depuis la base de données"""
        # Effacer les données actuelles
        for item in self.commandes_tree.get_children():
            self.commandes_tree.delete(item)
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    SELECT c.id, CONCAT(cl.nom, ' ', cl.prenom) as client, 
                        c.date_commande, c.statut,
                        COALESCE(SUM(d.quantite * d.prix_unitaire), 0) as total
                    FROM commandes c
                    JOIN clients cl ON c.client_id = cl.id
                    LEFT JOIN details_commande d ON c.id = d.commande_id
                    GROUP BY c.id
                    ORDER BY c.date_commande DESC
                """
                cursor.execute(query)
                rows = cursor.fetchall()
                
                for row in rows:
                    # Formater la date et le total
                    formatted_row = list(row)
                    formatted_row[2] = row[2].strftime("%d/%m/%Y %H:%M")
                    formatted_row[4] = f"{row[4]:.2f}"
                    
                    self.commandes_tree.insert("", "end", values=formatted_row)
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement des commandes: {e}")

    def load_details_commande(self, commande_id):
        """Charge les détails d'une commande"""
        # Effacer les données actuelles
        for item in self.details_tree.get_children():
            self.details_tree.delete(item)
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    SELECT d.id, p.nom, d.quantite, d.prix_unitaire, 
                        (d.quantite * d.prix_unitaire) as total
                    FROM details_commande d
                    JOIN produits p ON d.produit_id = p.id
                    WHERE d.commande_id = %s
                """
                cursor.execute(query, (commande_id,))
                rows = cursor.fetchall()
                
                for row in rows:
                    # Formater les prix
                    formatted_row = list(row)
                    formatted_row[3] = f"{row[3]:.2f}"
                    formatted_row[4] = f"{row[4]:.2f}"
                    
                    self.details_tree.insert("", "end", values=formatted_row)
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement des détails de commande: {e}")

    def on_commande_select(self, event):
        """Gère l'événement de sélection d'une commande"""
        selected = self.commandes_tree.selection()
        if selected:
            # Récupérer l'ID de la commande sélectionnée
            commande_id = self.commandes_tree.item(selected[0], "values")[0]
            self.selected_commande_id = commande_id
            
            # Charger les détails de la commande
            self.load_details_commande(commande_id)

    def new_commande(self):
        """Crée une nouvelle commande"""
        # Créer une fenêtre de dialogue pour sélectionner le client
        client_window = tk.Toplevel(self.root)
        client_window.title("Nouvelle commande - Sélection du client")
        client_window.geometry("500x400")
        client_window.grab_set()  # Rendre la fenêtre modale
        
        # Liste des clients
        ttk.Label(client_window, text="Sélectionnez un client:").pack(pady=10)
        
        # Tableau des clients
        columns = ("id", "nom", "prenom", "email")
        client_tree = ttk.Treeview(client_window, columns=columns, show="headings")
        
        # Définition des en-têtes
        client_tree.heading("id", text="ID")
        client_tree.heading("nom", text="Nom")
        client_tree.heading("prenom", text="Prénom")
        client_tree.heading("email", text="Email")
        
        # Définition des largeurs de colonnes
        client_tree.column("id", width=50)
        client_tree.column("nom", width=150)
        client_tree.column("prenom", width=150)
        client_tree.column("email", width=200)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(client_window, orient="vertical", command=client_tree.yview)
        client_tree.configure(yscrollcommand=scrollbar.set)
        
        # Placement du tableau et de la scrollbar
        client_tree.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        # Charger les clients
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT id, nom, prenom, email FROM clients")
                rows = cursor.fetchall()
                
                for row in rows:
                    client_tree.insert("", "end", values=row)
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement des clients: {e}")
            client_window.destroy()
            return
        
        # Fonction pour créer la commande
        def create_commande():
            selected = client_tree.selection()
            if not selected:
                messagebox.showwarning("Attention", "Veuillez sélectionner un client", parent=client_window)
                return
            
            client_id = client_tree.item(selected[0], "values")[0]
            
            try:
                if self.connection.is_connected():
                    cursor = self.connection.cursor()
                    query = """
                        INSERT INTO commandes (client_id, date_commande, statut)
                        VALUES (%s, %s, %s)
                    """
                    values = (client_id, datetime.datetime.now(), "En attente")
                    cursor.execute(query, values)
                    self.connection.commit()
                    
                    # Récupérer l'ID de la commande créée
                    commande_id = cursor.lastrowid
                    
                    cursor.close()
                    messagebox.showinfo("Succès", "Commande créée avec succès", parent=client_window)
                    
                    # Fermer la fenêtre et rafraîchir la liste des commandes
                    client_window.destroy()
                    self.load_commandes()
                    
                    # Sélectionner la commande créée
                    for item in self.commandes_tree.get_children():
                        if self.commandes_tree.item(item, "values")[0] == str(commande_id):
                            self.commandes_tree.selection_set(item)
                            self.commandes_tree.focus(item)
                            self.on_commande_select(None)
                            break
                    
                    # Ouvrir la fenêtre d'ajout de produit
                    self.add_produit_to_commande()
            except Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la création de la commande: {e}", parent=client_window)
        
        # Boutons
        btn_frame = ttk.Frame(client_window)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Créer commande", command=create_commande).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Annuler", command=client_window.destroy).pack(side="left", padx=5)

    def update_commande_statut(self):
        """Modifie le statut d'une commande"""
        selected = self.commandes_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner une commande")
            return
        
        commande_id = self.commandes_tree.item(selected[0], "values")[0]
        current_statut = self.commandes_tree.item(selected[0], "values")[3]
        
        # Liste des statuts possibles
        statuts = ["En attente", "En cours", "Expédiée", "Livrée", "Annulée"]
        
        # Demander le nouveau statut
        new_statut = simpledialog.askstring(
            "Modifier le statut",
            "Nouveau statut:",
            initialvalue=current_statut
        )
        
        if new_statut and new_statut in statuts:
            try:
                if self.connection.is_connected():
                    cursor = self.connection.cursor()
                    query = "UPDATE commandes SET statut = %s WHERE id = %s"
                    cursor.execute(query, (new_statut, commande_id))
                    self.connection.commit()
                    
                    cursor.close()
                    messagebox.showinfo("Succès", "Statut modifié avec succès")
                    
                    # Rafraîchir la liste des commandes
                    self.load_commandes()
            except Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la modification du statut: {e}")
        elif new_statut:
            messagebox.showwarning("Attention", f"Statut invalide. Choisissez parmi: {', '.join(statuts)}")

    def delete_commande(self):
        """Supprime une commande et ses détails"""
        selected = self.commandes_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner une commande à supprimer")
            return
        
        commande_id = self.commandes_tree.item(selected[0], "values")[0]
        
        # Demander confirmation
        if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cette commande et tous ses détails ?"):
            try:
                if self.connection.is_connected():
                    cursor = self.connection.cursor()
                    
                    # Supprimer d'abord les détails de la commande (contrainte de clé étrangère)
                    cursor.execute("DELETE FROM details_commande WHERE commande_id = %s", (commande_id,))
                    
                    # Puis supprimer la commande
                    cursor.execute("DELETE FROM commandes WHERE id = %s", (commande_id,))
                    
                    self.connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Succès", "Commande supprimée avec succès")
                    
                    # Effacer les détails affichés
                    for item in self.details_tree.get_children():
                        self.details_tree.delete(item)
                    
                    # Rafraîchir la liste des commandes
                    self.load_commandes()
            except Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la suppression de la commande: {e}")

    def add_produit_to_commande(self):
        """Ajoute un produit à la commande sélectionnée"""
        if not self.selected_commande_id:
            messagebox.showwarning("Attention", "Veuillez d'abord sélectionner une commande")
            return
        
        # Créer une fenêtre de dialogue pour sélectionner le produit
        produit_window = tk.Toplevel(self.root)
        produit_window.title("Ajout de produit à la commande")
        produit_window.geometry("700x500")
        produit_window.grab_set()  # Rendre la fenêtre modale
        
        # Liste des produits
        ttk.Label(produit_window, text="Sélectionnez un produit:").pack(pady=10)
        
        # Tableau des produits
        columns = ("id", "nom", "description", "prix", "stock")
        produit_tree = ttk.Treeview(produit_window, columns=columns, show="headings")
        
        # Définition des en-têtes
        produit_tree.heading("id", text="ID")
        produit_tree.heading("nom", text="Nom")
        produit_tree.heading("description", text="Description")
        produit_tree.heading("prix", text="Prix (CHF)")
        produit_tree.heading("stock", text="Stock")
        
        # Définition des largeurs de colonnes
        produit_tree.column("id", width=50)
        produit_tree.column("nom", width=200)
        produit_tree.column("description", width=300)
        produit_tree.column("prix", width=100)
        produit_tree.column("stock", width=100)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(produit_window, orient="vertical", command=produit_tree.yview)
        produit_tree.configure(yscrollcommand=scrollbar.set)
        
        # Placement du tableau et de la scrollbar
        produit_tree.pack(fill="both", expand=True, padx=10, pady=10)
        scrollbar.pack(side="right", fill="y")
        
        # Zone pour entrer la quantité
        quantite_frame = ttk.Frame(produit_window)
        quantite_frame.pack(pady=10)
        
        ttk.Label(quantite_frame, text="Quantité:").pack(side="left")
        quantite_entry = ttk.Entry(quantite_frame, width=10)
        quantite_entry.pack(side="left", padx=5)
        quantite_entry.insert(0, "1")  # Valeur par défaut
        
        # Charger les produits
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT id, nom, description, prix, stock FROM produits WHERE stock > 0")
                rows = cursor.fetchall()
                
                for row in rows:
                    # Formater le prix
                    formatted_row = list(row)
                    formatted_row[3] = f"{row[3]:.2f}"
                    
                    produit_tree.insert("", "end", values=formatted_row)
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement des produits: {e}", parent=produit_window)
            produit_window.destroy()
            return
        
        # Fonction pour ajouter le produit à la commande
        def add_to_commande():
            selected = produit_tree.selection()
            if not selected:
                messagebox.showwarning("Attention", "Veuillez sélectionner un produit", parent=produit_window)
                return
            
            produit_id = produit_tree.item(selected[0], "values")[0]
            prix = float(produit_tree.item(selected[0], "values")[3].replace(",", "."))
            stock_disponible = int(produit_tree.item(selected[0], "values")[4])
            
            try:
                quantite = int(quantite_entry.get())
                if quantite <= 0:
                    messagebox.showwarning("Attention", "La quantité doit être positive", parent=produit_window)
                    return
                
                if quantite > stock_disponible:
                    messagebox.showwarning("Attention", f"Stock insuffisant. Disponible: {stock_disponible}", parent=produit_window)
                    return
                
            except ValueError:
                messagebox.showwarning("Attention", "Quantité invalide", parent=produit_window)
                return
            
            try:
                if self.connection.is_connected():
                    cursor = self.connection.cursor()
                    
                    # Vérifier si le produit est déjà dans la commande
                    cursor.execute(
                        "SELECT id, quantite FROM details_commande WHERE commande_id = %s AND produit_id = %s",
                        (self.selected_commande_id, produit_id)
                    )
                    existing = cursor.fetchone()
                    
                    if existing:
                        # Le produit existe déjà, mettre à jour la quantité
                        detail_id, current_quantite = existing
                        new_quantite = current_quantite + quantite
                        
                        if new_quantite > stock_disponible:
                            messagebox.showwarning(
                                "Attention", 
                                f"Stock insuffisant. Vous avez déjà {current_quantite} unités dans la commande. Stock disponible: {stock_disponible}", 
                                parent=produit_window
                            )
                            cursor.close()
                            return
                        
                        cursor.execute(
                            "UPDATE details_commande SET quantite = %s WHERE id = %s",
                            (new_quantite, detail_id)
                        )
                        
                    else:
                        # Ajouter un nouveau détail de commande
                        query = """
                            INSERT INTO details_commande (commande_id, produit_id, quantite, prix_unitaire)
                            VALUES (%s, %s, %s, %s)
                        """
                        values = (self.selected_commande_id, produit_id, quantite, prix)
                        cursor.execute(query, values)
                    
                    # Mettre à jour le stock du produit
                    cursor.execute(
                        "UPDATE produits SET stock = stock - %s WHERE id = %s",
                        (quantite, produit_id)
                    )
                    
                    self.connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Succès", "Produit ajouté à la commande", parent=produit_window)
                    
                    # Fermer la fenêtre et rafraîchir les listes
                    produit_window.destroy()
                    self.load_details_commande(self.selected_commande_id)
                    self.load_commandes()  # Pour mettre à jour le total
                    self.load_produits()   # Pour mettre à jour le stock
            except Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'ajout du produit: {e}", parent=produit_window)
        
        # Boutons
        btn_frame = ttk.Frame(produit_window)
        btn_frame.pack(pady=10)
        
        ttk.Button(btn_frame, text="Ajouter à la commande", command=add_to_commande).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Annuler", command=produit_window.destroy).pack(side="left", padx=5)

    def update_detail_quantite(self):
        """Modifie la quantité d'un détail de commande"""
        if not self.selected_commande_id:
            messagebox.showwarning("Attention", "Veuillez d'abord sélectionner une commande")
            return
        
        selected = self.details_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un produit dans la commande")
            return
        
        detail_id = self.details_tree.item(selected[0], "values")[0]
        produit_nom = self.details_tree.item(selected[0], "values")[1]
        current_quantite = int(self.details_tree.item(selected[0], "values")[2])
        
        # Demander la nouvelle quantité
        new_quantite_str = simpledialog.askstring(
            "Modifier la quantité",
            f"Nouvelle quantité pour {produit_nom}:",
            initialvalue=str(current_quantite)
        )
        
        if not new_quantite_str:
            return
        
        try:
            new_quantite = int(new_quantite_str)
            if new_quantite <= 0:
                messagebox.showwarning("Attention", "La quantité doit être positive")
                return
            
            if new_quantite == current_quantite:
                return  # Pas de changement
            
            # Récupérer l'ID du produit et le stock disponible
            try:
                if self.connection.is_connected():
                    cursor = self.connection.cursor()
                    
                    # Récupérer les infos du détail et du produit
                    cursor.execute(
                        """
                        SELECT d.produit_id, p.stock + d.quantite
                        FROM details_commande d
                        JOIN produits p ON d.produit_id = p.id
                        WHERE d.id = %s
                        """,
                        (detail_id,)
                    )
                    result = cursor.fetchone()
                    
                    if not result:
                        messagebox.showerror("Erreur", "Détail de commande non trouvé")
                        cursor.close()
                        return
                    
                    produit_id, stock_total = result
                    
                    if new_quantite > stock_total:
                        messagebox.showwarning("Attention", f"Stock insuffisant. Disponible: {stock_total}")
                        cursor.close()
                        return
                    
                    # Calculer la différence de quantité
                    delta = new_quantite - current_quantite
                    
                    # Mettre à jour le détail
                    cursor.execute(
                        "UPDATE details_commande SET quantite = %s WHERE id = %s",
                        (new_quantite, detail_id)
                    )
                    
                    # Mettre à jour le stock du produit
                    cursor.execute(
                        "UPDATE produits SET stock = stock - %s WHERE id = %s",
                        (delta, produit_id)
                    )
                    
                    self.connection.commit()
                    cursor.close()
                    
                    messagebox.showinfo("Succès", "Quantité modifiée avec succès")
                    
                    # Rafraîchir les listes
                    self.load_details_commande(self.selected_commande_id)
                    self.load_commandes()  # Pour mettre à jour le total
                    self.load_produits()   # Pour mettre à jour le stock
            except Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de la modification de la quantité: {e}")
                
        except ValueError:
            messagebox.showwarning("Attention", "Quantité invalide")

    def delete_detail(self):
        """Supprime un produit de la commande"""
        if not self.selected_commande_id:
            messagebox.showwarning("Attention", "Veuillez d'abord sélectionner une commande")
            return
        
        selected = self.details_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un produit dans la commande")
            return
        
        detail_id = self.details_tree.item(selected[0], "values")[0]
        produit_nom = self.details_tree.item(selected[0], "values")[1]
        
        # Demander confirmation
        if not messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer {produit_nom} de la commande ?"):
            return
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                
                # Récupérer les infos du détail pour restaurer le stock
                cursor.execute(
                    "SELECT produit_id, quantite FROM details_commande WHERE id = %s",
                    (detail_id,)
                )
                result = cursor.fetchone()
                
                if result:
                    produit_id, quantite = result
                    
                    # Supprimer le détail
                    cursor.execute("DELETE FROM details_commande WHERE id = %s", (detail_id,))
                    
                    # Restaurer le stock
                    cursor.execute(
                        "UPDATE produits SET stock = stock + %s WHERE id = %s",
                        (quantite, produit_id)
                    )
                    
                    self.connection.commit()
                    messagebox.showinfo("Succès", "Produit supprimé de la commande")
                    
                    # Rafraîchir les listes
                    self.load_details_commande(self.selected_commande_id)
                    self.load_commandes()  # Pour mettre à jour le total
                    self.load_produits()   # Pour mettre à jour le stock
                else:
                    messagebox.showerror("Erreur", "Détail de commande non trouvé")
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression du produit: {e}")

    # ====================== FONCTIONS D'EXPORT PDF ======================

    def export_clients_pdf(self):
        """Exporte la liste des clients en PDF"""
        # Demander le chemin du fichier
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Enregistrer la liste des clients"
        )
        
        if not file_path:
            return
        
        try:
            # Récupérer les données des clients
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT id, nom, prenom, email, telephone, adresse FROM clients")
                clients = cursor.fetchall()
                cursor.close()
                
                if not clients:
                    messagebox.showinfo("Information", "Aucun client à exporter")
                    return
                
                # Créer le document PDF
                doc = SimpleDocTemplate(file_path, pagesize=A4)
                
                # Définir les styles
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']
                subtitle_style = styles['Heading2']
                normal_style = styles['Normal']
                
                # Contenu du document
                content = []
                
                # Titre
                content.append(Paragraph("Liste des Clients", title_style))
                content.append(Spacer(1, 12))
                
                # Date
                content.append(Paragraph(f"Généré le {datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')}", normal_style))
                content.append(Spacer(1, 12))
                
                # Tableau des clients
                headers = ["ID", "Nom", "Prénom", "Email", "Téléphone", "Adresse"]
                data = [headers]
                
                for client in clients:
                    data.append([
                        str(client[0]),
                        client[1],
                        client[2],
                        client[3] if client[3] else "",
                        client[4] if client[4] else "",
                        client[5] if client[5] else ""
                    ])
                
                # Créer le tableau
                table = Table(data)
                
                # Style du tableau
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ]))
                
                content.append(table)
                
                # Construire le document
                doc.build(content)
                
                messagebox.showinfo("Succès", f"La liste des clients a été exportée dans {file_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export PDF: {e}")

    def export_produits_pdf(self):
        """Exporte la liste des produits en PDF"""
        # Demander le chemin du fichier
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Enregistrer la liste des produits"
        )
        
        if not file_path:
            return
        
        try:
            # Récupérer les données des produits
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT id, nom, description, prix, stock FROM produits")
                produits = cursor.fetchall()
                cursor.close()
                
                if not produits:
                    messagebox.showinfo("Information", "Aucun produit à exporter")
                    return
                
                # Créer le document PDF
                doc = SimpleDocTemplate(file_path, pagesize=A4)
                
                # Définir les styles
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']
                subtitle_style = styles['Heading2']
                normal_style = styles['Normal']
                
                # Contenu du document
                content = []
                
                # Titre
                content.append(Paragraph("Liste des Produits", title_style))
                content.append(Spacer(1, 12))
                
                # Date
                content.append(Paragraph(f"Généré le {datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')}", normal_style))
                content.append(Spacer(1, 12))
                
                # Tableau des produits
                headers = ["ID", "Nom", "Description", "Prix (CHF)", "Stock"]
                data = [headers]
                
                for produit in produits:
                    data.append([
                        str(produit[0]),
                        produit[1],
                        produit[2] if produit[2] else "",
                        f"{produit[3]:.2f}",
                        str(produit[4])
                    ])
                
                # Créer le tableau
                table = Table(data)
                
                # Style du tableau
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                    ('ALIGN', (3, 1), (4, -1), 'RIGHT'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ]))
                
                content.append(table)
                
                # Construire le document
                doc.build(content)
                
                messagebox.showinfo("Succès", f"La liste des produits a été exportée dans {file_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export PDF: {e}")
            

    def update_client(self):
        """Modifie un client existant"""
        selected = self.clients_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un client à modifier")
            return
        
        client_id = self.clients_tree.item(selected[0], "values")[0]
        nom = self.client_nom.get().strip()
        prenom = self.client_prenom.get().strip()
        email = self.client_email.get().strip()
        telephone = self.client_telephone.get().strip()
        adresse = self.client_adresse.get().strip()
        
        if not nom or not prenom:
            messagebox.showwarning("Attention", "Les champs Nom et Prénom sont obligatoires")
            return
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    UPDATE clients
                    SET nom = %s, prenom = %s, email = %s, telephone = %s, adresse = %s
                    WHERE id = %s
                """
                values = (nom, prenom, email, telephone, adresse, client_id)
                cursor.execute(query, values)
                self.connection.commit()
                
                cursor.close()
                messagebox.showinfo("Succès", "Client modifié avec succès")
                
                # Réinitialiser les champs
                self.client_nom.delete(0, tk.END)
                self.client_prenom.delete(0, tk.END)
                self.client_email.delete(0, tk.END)
                self.client_telephone.delete(0, tk.END)
                self.client_adresse.delete(0, tk.END)
                
                # Rafraîchir la liste
                self.load_clients()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la modification du client: {e}")

    def delete_client(self):
        """Supprime un client"""
        selected = self.clients_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner un client à supprimer")
            return
        
        client_id = self.clients_tree.item(selected[0], "values")[0]
        
        # Vérifier si le client a des commandes
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT COUNT(*) FROM commandes WHERE client_id = %s", (client_id,))
                count = cursor.fetchone()[0]
                
                if count > 0:
                    messagebox.showwarning("Attention", "Ce client a des commandes et ne peut pas être supprimé")
                    cursor.close()
                    return
                
                # Demander confirmation
                if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce client ?"):
                    cursor.execute("DELETE FROM clients WHERE id = %s", (client_id,))
                    self.connection.commit()
                    messagebox.showinfo("Succès", "Client supprimé avec succès")
                    
                    # Réinitialiser les champs
                    self.client_nom.delete(0, tk.END)
                    self.client_prenom.delete(0, tk.END)
                    self.client_email.delete(0, tk.END)
                    self.client_telephone.delete(0, tk.END)
                    self.client_adresse.delete(0, tk.END)
                    
                    # Rafraîchir la liste
                    self.load_clients()
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de la suppression du client: {e}")

    def on_client_select(self, event):
        """Gère l'événement de sélection d'un client"""
        selected = self.clients_tree.selection()
        if selected:
            # Récupérer les valeurs du client sélectionné
            values = self.clients_tree.item(selected[0], "values")
            
            # Effacer les champs
            self.client_nom.delete(0, tk.END)
            self.client_prenom.delete(0, tk.END)
            self.client_email.delete(0, tk.END)
            self.client_telephone.delete(0, tk.END)
            self.client_adresse.delete(0, tk.END)
            
            # Remplir les champs avec les valeurs du client
            self.client_nom.insert(0, values[1])
            self.client_prenom.insert(0, values[2])
            self.client_email.insert(0, values[3] if values[3] else "")
            self.client_telephone.insert(0, values[4] if values[4] else "")
            self.client_adresse.insert(0, values[5] if values[5] else "")

    # ====================== FONCTIONS POUR LES PRODUITS ======================

    def load_produits(self):
        """Charge les produits depuis la base de données"""
        # Effacer les données actuelles
        for item in self.produits_tree.get_children():
            self.produits_tree.delete(item)
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                cursor.execute("SELECT * FROM produits")
                rows = cursor.fetchall()
                
                for row in rows:
                    self.produits_tree.insert("", "end", values=row)
                
                cursor.close()
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors du chargement des produits: {e}")

    def add_produit(self):
        """Ajoute un nouveau produit"""
        nom = self.produit_nom.get().strip()
        description = self.produit_description.get().strip()
        prix_str = self.produit_prix.get().strip()
        stock_str = self.produit_stock.get().strip()
        
        if not nom:
            messagebox.showwarning("Attention", "Le champ Nom est obligatoire")
            return
        
        try:
            prix = float(prix_str)
            stock = int(stock_str)
            
            if prix < 0:
                messagebox.showwarning("Attention", "Le prix doit être positif")
                return
                
            if stock < 0:
                messagebox.showwarning("Attention", "Le stock doit être positif")
                return
                
        except ValueError:
            messagebox.showwarning("Attention", "Prix et Stock doivent être des nombres valides")
            return
        
        try:
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    INSERT INTO produits (nom, description, prix, stock)
                    VALUES (%s, %s, %s, %s)
                """
                values = (nom, description, prix, stock)
                cursor.execute(query, values)

                self.connection.commit()
            
                cursor.close()
                messagebox.showinfo("Succès", "Produit ajouté avec succès")

                # Réinitialiser les champs
                self.produit_nom.delete(0, tk.END)
                self.produit_description.delete(0, tk.END)
                self.produit_prix.delete(0, tk.END)
                self.produit_stock.delete(0, tk.END)
                
                # Rafraîchir la liste
                self.load_produits()
                
                
        except Error as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'ajout du client: {e}")
        except ValueError:
            messagebox.showwarning("Attention", "Impossible d’ajouter le produit :-(")
            return
        self.rafraîchir

    def export_commandes_pdf(self):
        """Exporte la liste des commandes en PDF"""
        # Demander le chemin du fichier
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            title="Enregistrer la liste des commandes"
        )
        
        if not file_path:
            return
        
        try:
            # Récupérer les données des commandes
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                query = """
                    SELECT c.id, CONCAT(cl.nom, ' ', cl.prenom) as client, 
                           c.date_commande, c.statut,
                           COALESCE(SUM(d.quantite * d.prix_unitaire), 0) as total
                    FROM commandes c
                    JOIN clients cl ON c.client_id = cl.id
                    LEFT JOIN details_commande d ON c.id = d.commande_id
                    GROUP BY c.id
                    ORDER BY c.date_commande DESC
                """
                cursor.execute(query)
                commandes = cursor.fetchall()
                cursor.close()
                
                if not commandes:
                    messagebox.showinfo("Information", "Aucune commande à exporter")
                    return
                
                # Créer le document PDF
                doc = SimpleDocTemplate(file_path, pagesize=A4)
                
                # Définir les styles
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']
                subtitle_style = styles['Heading2']
                normal_style = styles['Normal']
                
                # Contenu du document
                content = []
                
                # Titre
                content.append(Paragraph("Liste des Commandes", title_style))
                content.append(Spacer(1, 12))
                
                # Date
                content.append(Paragraph(f"Généré le {datetime.datetime.now().strftime('%d/%m/%Y à %H:%M')}", normal_style))
                content.append(Spacer(1, 12))
                
                # Tableau des commandes
                headers = ["ID", "Client", "Date", "Statut", "Total (CHF)"]
                data = [headers]
                
                for commande in commandes:
                    data.append([
                        str(commande[0]),
                        commande[1],
                        commande[2].strftime("%d/%m/%Y %H:%M"),
                        commande[3],
                        f"{commande[4]:.2f}"
                    ])
                
                # Créer le tableau
                table = Table(data)
                
                # Style du tableau
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('ALIGN', (0, 0), (0, -1), 'CENTER'),
                    ('ALIGN', (4, 1), (4, -1), 'RIGHT'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ]))
                
                content.append(table)
                
                # Construire le document
                doc.build(content)
                
                messagebox.showinfo("Succès", f"La liste des commandes a été exportée dans {file_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export PDF: {e}")
    
    def export_commande_pdf(self):
        """Exporte la commande sélectionnée en PDF (facture)"""
        selected = self.commandes_tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner une commande à exporter")
            return
        
        commande_id = self.commandes_tree.item(selected[0], "values")[0]
        client_nom = self.commandes_tree.item(selected[0], "values")[1]
        date_commande = self.commandes_tree.item(selected[0], "values")[2]
        statut = self.commandes_tree.item(selected[0], "values")[3]
        total = self.commandes_tree.item(selected[0], "values")[4]
        
        # Demander le chemin du fichier
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
            initialfile=f"Facture_{commande_id}_{client_nom.replace(' ', '_')}",
            title="Enregistrer la facture"
        )
        
        if not file_path:
            return
        
        try:
            # Récupérer les détails de la commande
            if self.connection.is_connected():
                cursor = self.connection.cursor()
                
                # Récupérer les infos du client
                cursor.execute("""
                    SELECT cl.nom, cl.prenom, cl.email, cl.telephone, cl.adresse
                    FROM commandes c
                    JOIN clients cl ON c.client_id = cl.id
                    WHERE c.id = %s
                """, (commande_id,))
                client_info = cursor.fetchone()
                
                if not client_info:
                    messagebox.showerror("Erreur", "Client non trouvé")
                    cursor.close()
                    return
                
                # Récupérer les détails de la commande
                cursor.execute("""
                    SELECT p.nom, d.quantite, d.prix_unitaire, (d.quantite * d.prix_unitaire) as total
                    FROM details_commande d
                    JOIN produits p ON d.produit_id = p.id
                    WHERE d.commande_id = %s
                """, (commande_id,))
                details = cursor.fetchall()
                
                cursor.close()
                
                if not details:
                    messagebox.showinfo("Information", "Aucun détail à exporter pour cette commande")
                    return
                
                # Créer le document PDF
                doc = SimpleDocTemplate(file_path, pagesize=A4)
                
                # Définir les styles
                styles = getSampleStyleSheet()
                title_style = styles['Heading1']
                subtitle_style = styles['Heading2']
                normal_style = styles['Normal']
                
                # Contenu du document
                content = []
                
                # Titre
                content.append(Paragraph(f"Facture N° {commande_id}", title_style))
                content.append(Spacer(1, 12))
                
                # Informations sur la commande
                content.append(Paragraph(f"Date: {date_commande}", normal_style))
                content.append(Paragraph(f"Statut: {statut}", normal_style))
                content.append(Spacer(1, 12))
                
                # Informations sur le client
                content.append(Paragraph("Informations client:", subtitle_style))
                content.append(Paragraph(f"Nom: {client_info[0]} {client_info[1]}", normal_style))
                if client_info[2]:  # Email
                    content.append(Paragraph(f"Email: {client_info[2]}", normal_style))
                if client_info[3]:  # Téléphone
                    content.append(Paragraph(f"Téléphone: {client_info[3]}", normal_style))
                if client_info[4]:  # Adresse
                    content.append(Paragraph(f"Adresse: {client_info[4]}", normal_style))
                content.append(Spacer(1, 12))
                
                # Détails de la commande
                content.append(Paragraph("Détails de la commande:", subtitle_style))
                
                # Tableau des détails
                headers = ["Produit", "Quantité", "Prix unitaire (CHF)", "Total (CHF)"]
                data = [headers]
                
                for detail in details:
                    data.append([
                        detail[0],
                        str(detail[1]),
                        f"{detail[2]:.2f}",
                        f"{detail[3]:.2f}"
                    ])
                
                # Ajouter une ligne pour le total
                data.append(["", "", "Total:", total])
                
                # Créer le tableau
                table = Table(data)
                
                # Style du tableau
                table.setStyle(TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, 0), 12),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                    ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black),
                    ('ALIGN', (1, 1), (1, -2), 'CENTER'),
                    ('ALIGN', (2, 1), (3, -1), 'RIGHT'),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('SPAN', (0, -1), (1, -1)),
                    ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
                    ('FONTNAME', (2, -1), (3, -1), 'Helvetica-Bold'),
                ]))
                
                content.append(table)
                
                # Ajouter un pied de page
                content.append(Spacer(1, 24))
                content.append(Paragraph("Merci pour votre achat !", normal_style))
                
                # Construire le document
                doc.build(content)
                
                messagebox.showinfo("Succès", f"La facture a été exportée dans {file_path}")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de l'export PDF: {e}")
    
    def show_about(self):
        """Affiche la boîte de dialogue À propos"""
        messagebox.showinfo(
            "À propos",
            "ERP Client - Gestion des Commandes et Produits\n\n"
            "Version 1.0\n\n"
            "Développé avec Python, Tkinter et MariaDB"
        )


# Point d'entrée de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = ERP(root)
    root.mainloop()
                #!/usr/bin/env python3
    # -*- coding: utf-8 -*-