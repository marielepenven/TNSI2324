tableau_distance={"Nancy":{"Metz":55,"Paris":303,"Reims":188,"Troyes":183},"Metz":{"Nancy":55,"Paris":306,"Reims":176,"Troyes":203},
                  "Paris":{"Nancy":303,"Metz":306,"Reims":142,"Troyes":153},"Reims":{"Nancy":188,"Metz":176,"Paris":142,"Troyes":123},
                  "Troyes":{"Nancy":183,"Metz":203,"Paris":153,"Reims":123}}
A_visiter = ["Metz","Paris","Reims","Troyes"]
#Visitees=[]
Ville_depart="Nancy"

def ville_plus_proche(ville_courante,A_Visiter,tableau_distance,Ville_depart):
    if len(A_visiter) == 0:
        return None
    else:
        ville_proche = A_Visiter[0]
        distance_min = tableau_distance[ville_courante][ville_proche]
        for i in range(len(A_Visiter)):
            if distance_min>tableau_distance[ville_courante][A_Visiter[i]] and A_Visiter[i]!=Ville_depart:
                ville_proche = A_Visiter[i]
                distance_min = tableau_distance[ville_courante][A_Visiter[i]]
        return ville_proche
    
