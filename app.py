import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')






# -----------------------------
# 2. Ventes par produit
# -----------------------------
#Calcul de la quantité totale vendue par produit
ventes_produit = données.groupby('produit', as_index=False)['qte'].sum()

#Graphe des ventes par produit 
fig_produit = px.bar(
    ventes_produit,
    #x et y sont les noms des colonnes du DataFrame ventes_produit
    x='produit',
    y='qte',
    title='Ventes par produit'
)

#envoie du fichier html
fig_produit.write_html('ventes-par-produit.html')

# -----------------------------
# 3. Chiffre d’affaires par produit
# -----------------------------

#Calcul du chiffre d’affaires par produit
données['ca'] = données['qte'] * données['prix']

ca_produit = données.groupby('produit', as_index=False)['ca'].sum()

#Graphe du chiffre d’affaires par produit
fig_ca = px.bar(
    ca_produit,
    #x et y sont les noms des colonnes du DataFrame ca_produit
    x='produit',
    y='ca',
    title='Chiffre d’affaires par produit'
)

fig_ca.write_html('ca-par-produit.html')

print("3 graphiques générés avec succès !")