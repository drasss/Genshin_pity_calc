import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
#recupération des valeurs

fichier=open("result.txt","r")
k=fichier.read()
fichier.close()

result=eval(k)

fichier=open("result5.txt","r")
k=fichier.read()
fichier.close()

result5=eval(k)
#transformation des valeurs


result=np.array([float(result[i]) for i in range(len(result))])
result5=np.array([float(result5[i]) for i in range(len(result5))])
result=result/np.sum(result)
result5=result5/np.sum(result5)

rep=[np.sum(result[:i])for i in range(len(result))]
rep5=[np.sum(result5[:i])for i in range(len(result5))]




# streamlit

st.title("Calculateur de probabilités Genshin Impact")
st.markdown("# A savoir !")
st.text("ce site a pour but de permettre de calculer les probabilités d'avoir un 5* sur genshin impact et d'avoir celui que l'on souhaite (bannière)")
st.html("""les règles : <br>
        <ul><li>tout les 90 voeux un 5* est promis</li><li>les voeux de bannières se réinitialisent a chaque changement de bannières (la pity se réinitialise a chaque bannière sauf pour les voeux bleus) </li>
        <li>bien respecter les catégories dans les nombres a rentrer ci dessous</li></ul>""")
fig2 = plt.figure() 

plt.plot(result)
plt.plot(result5)
st.pyplot(fig2)

V=st.number_input("combien de voeux as-tu a dépenser?", 0)

Vf=st.number_input("combien de voeux as-tu dépensé depuis le dernier 50/50 ?", 0)

F=st.selectbox("A cette bannière, as-tu déja perdu un 50/50 ? ", ["Pas encore","Oui"])



B=st.button(label="test")

calc=V+Vf+90*int(F=="Oui")
val=""
val5=""
if B:
    if calc>180:
        val="Tu es certain a 100 % d'avoir ton personnage"
    else:
        val=str(round(rep[calc]*100,4))+" %"
        if calc>90:
            val5="Tu es certain a 100 % d'avoir un 5*"
        else:
            val5=str(round(rep5[calc]*100,4))+" %"
st.title("Voila la probabilité que tu aies le 5* de ton choix : ")
st.title(val)
st.title("Voila la probabilité que tu aies un 5* : ")
st.title(val5)
    
