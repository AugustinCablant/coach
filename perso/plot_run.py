import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import chart_studio.plotly as py
import chart_studio
from plotly.subplots import make_subplots

start_date = '2018-06-24'
link_start_date = 'https://www.leparisien.fr/yvelines-78/conflans-sainte-honorine-la-culture-dans-la-course-24-06-2018-7790922.php'
description = 'Mon père ne peut participer à une course pour raison médicale, il me confie donc son dossard et je gagne la course à la surprise générale avec des baskets trouées'

utmb_2018_date = '2018-08-28'
utmb_2018_date_link = 'https://utmb.world/fr/utmb-index/races/4365.utmb--ycc.2018'
description_utmb = "Après avoir remporté la course de Conflans, je décide de m'inscrire à la course jeune de l'UTMB, c'est dur ..."

triel_date = '2021-08-29'
triel_link = 'https://www.sartrouville-athle.fr/wp-content/uploads/2021/08/resultats-triel-13-km.pdf'
description_triel = "Entre mes deux années de prépa, je m'inscis à la course locale, que je remporte ..."

ekiden_2022 = '2022-04'
ekiden_link = 'https://www.ekiden-platal.fr/'
description_ekiden = "Fin des concours (écrit), je participe à un ekiden avec Ginette (ma prépa). Nous arrivons à la troisième place et j'ai le meilleur temps des participants sur 10km (environ 34 minutes)."

ecotrail = '2023-03'
ecotrail_link = "https://www.ecotrailparis.com/fr/course-ecotrail-paris/trail-45-km"
description_ecotrail = "Première course que je prépare vraiment : vélo et côtes ! Je pars avec la tête de course mais une erreur de parcours au km 9 ... Je termine dans le top30, avec 8km de plus que les autres participants, et une remontada folle ! Beaucoup de déception ce jour-là, j'aurais pu faire top3 selon moi. " 

utmb_2023 = '2023-08'
utmb_2023_link = "https://www.betrail.run/race/utmb/2023/15km-7811565/results#d"
utmb_2023_description = "Je décide de participer à la course jeune de l'UTMB. Encore une fois, beaucoup de travail en côtes. Cette année le niveau est relevé, je termine à la 23e position, 2 places derrière Baptiste Cartieaux, un AS chez les jeunes !"

marathon_date = '2023-10-22'
marathon_link = 'https://www.breizhchrono.com/detail-de-la-course/marathonvertrennesschoolofbusiness-lemarathonvertrennes-2023-16622'
marathon_description = "Pour mon anniversaire (22 ans) je décide de faire un marathon sans préparation. Il y a Lyon ou Rennes le 22 octobre, j'opte pour Rennes et m'en tire avec un 2h33 tout plaisir !"

semi_boulbi_date = '2023-11'
semi_boulbi_description = "Après avoir participé à une séance collective du TRC, je décide de partir sur le semi de Boulogne sans véritable préparation mais avec la barre des 1h10 en tête. Malheureusement (sans grande surprise), j'explose : 1h11. Je suis déçu et frustré. Ca y est, la machine est en route, à partir de maintenant je vais me donner le moyen d'atteindre les objectifs que je me suis fixé."

issy = '2023-12'
issy_des = "Je participe au 10km de Issy, j'ai commencé à m'entraîner sérieusement et passe de belles séances. Je viens pour le sub 32 et repars avec un 32:10. Fin de course mitigée, j'en ai encore dans le sac donc un peu de frustration ... Ce n'est que partie remise !"

prom = '2024-01'
prom_des = "Je participe à la prom'classic. Ambiance de fou furieux, entraînement de fou furieux. J'ai tout pour reussir ! J'en ai peut-être trop fait à l'entraînement car veille de la course je tombe dans les pommes lors de mes accels'. J'ai pas fait le déplacement pour rien, je m'aligne donc sur la ligne de départ. Résultat : 31'06. Je suis content, mais j'ai encore les crocs !"

cross_semi = '2024-03'
cross_semi_des = "Après avoir écouté le podcast de Runnix sur Etienne Daguinos, je décide de tenter l'enchaînement France de cross -> Semi de Lille, qui marche plutôt bien ! 108e position aux France de cross sur un parcours pas facile et un joli 1h05'42 sur semi ... La progression continue !"

valenciennes = '2024-04'
valenciennes_des = "Après Lille, je n'ai plus qu'un objectif en tête : validé le fameux sub 30. Je passe de très belles séances, m'entraîne bien, récupère bien. Je décide donc de m'aligner sur les 10km de Valenciennes. Je fais 30:15 (passage au 5km en 14:36), joli popcorn ! Je ne perds jamais, j'apprends."

piste = '2024-05'
piste_des = "Début de la saison de piste (que je n'ai pas envie de faire). J'essaye de me motiver car on me dit que ça va me faire progresser sur la route. J'execute donc. Premier tour des interclubs, pop corn total sur 3000m avec un 8:39. Beaucoup de déception ... Je commence à avoir du mal à m'entraîner, je perds la motivation. Fin du mois, 5000m de St Maur que je remporte en 14:40. Je suis toujours frustré."

piste_acte_2 = '2024-06'
piste_acte_2_des = "Je m'entraîne tant bien que mal, je passe quelques séances. Mais je sens que je commence à être fatigué. Je vise 14:10 sur 5000m et je pense que j'en ai les capacités. Malheureusement, je ne parviens pas à efffectuer ce chrono et réalise deux fois 14:30 (Cergy puis FAST5000)."

bilan_date = '2024-08'
bilan_des = "Je décide de faire une coupure sur une partie de juillet et août afin de me régénérer. J'ai beaucoup d'objectifs en tête mais si je retiens une chose de ma saison d'athlé, c'est que j'ai aussi besoin des études pour être stimulé. J'ai très hâte de débuter mon master 2 au MVA à la rentrée de septembre et souhaite concilier mon cursus académique avec mes aventures sportives."

end_date = '2024-09-01'


# Liste des événements
events = [
    {'Date': '2018-06-24', 'Title': "Course à Conflans-Sainte-Honorine", 'Description': "Mon père ne peut participer à une course pour raison médicale,<br> il me confie donc son dossard et je gagne la course à la surprise générale avec des baskets trouées", 'Link': 'https://www.leparisien.fr/yvelines-78/conflans-sainte-honorine-la-culture-dans-la-course-24-06-2018-7790922.php'},
    {'Date': '2018-08-28', 'Title': "UTMB Jeune", 'Description': "Après avoir remporté la course de Conflans,<br> je décide de m'inscrire à la course jeune de l'UTMB, c'est dur ...", 'Link': 'https://utmb.world/fr/utmb-index/races/4365.utmb--ycc.2018'},
    {'Date': '2021-08-29', 'Title': "Course à Triel", 'Description': "Entre mes deux années de prépa,<br> je m'inscris à la course locale, que je remporte ...", 'Link': 'https://www.sartrouville-athle.fr/wp-content/uploads/2021/08/resultats-triel-13-km.pdf'},
    {'Date': '2022-04', 'Title': "Ekiden 2022", 'Description': "Fin des concours (écrit), je participe à un ekiden avec Ginette (ma prépa).<br> Nous arrivons à la troisième place et j'ai le meilleur temps des participants sur 10km (environ 34 minutes).", 'Link': 'https://www.ekiden-platal.fr/'},
    {'Date': '2023-03', 'Title': "Ecotrail Paris", 'Description': "Première course que je prépare vraiment : vélo et côtes !<br> Je pars avec la tête de course mais une erreur de parcours au km 9 ... Je termine dans le top30, avec 8km de plus que les autres participants, et une remontada folle !<br> Beaucoup de déception ce jour-là, j'aurais pu faire top3 selon moi.", 'Link': 'https://www.ecotrailparis.com/fr/course-ecotrail-paris/trail-45-km'},
    {'Date': '2023-08', 'Title': "UTMB 2023", 'Description': "Je décide de participer à la course jeune de l'UTMB.<br> Encore une fois, beaucoup de travail en côtes. Cette année le niveau est relevé,<br> je termine à la 23e position, 2 places derrière Baptiste Cartieaux, un AS chez les jeunes !", 'Link': 'https://www.betrail.run/race/utmb/2023/15km-7811565/results#d'},
    {'Date': '2023-10-22', 'Title': "Marathon de Rennes", 'Description': "Pour mon anniversaire (22 ans) je décide de faire un marathon sans préparation.<br> Il y a Lyon ou Rennes le 22 octobre, j'opte pour Rennes et m'en tire avec un 2h33 tout plaisir !", 'Link': 'https://www.breizhchrono.com/detail-de-la-course/marathonvertrennesschoolofbusiness-lemarathonvertrennes-2023-16622'},
    {'Date': '2023-11', 'Title': "Semi de Boulogne", 'Description': "Après avoir participé à une séance collective du TRC, je décide de partir sur le semi de Boulogne sans véritable préparation mais avec la barre des 1h10 en tête.<br> Malheureusement (sans grande surprise), j'explose : 1h11. Je suis déçu et frustré.<br> Ca y est, la machine est en route, à partir de maintenant je vais me donner le moyen d'atteindre les objectifs que je me suis fixé.", 'Link': ''},
    {'Date': '2023-12', 'Title': "10km de Issy", 'Description': "Je participe au 10km de Issy, j'ai commencé à m'entraîner sérieusement et passe de belles séances.<br> Je viens pour le sub 32 et repars avec un 32:10. Fin de course mitigée, j'en ai encore dans le sac donc un peu de frustration ...<br> Ce n'est que partie remise !", 'Link': ''},
    {'Date': '2024-01', 'Title': "Prom'Classic", 'Description': "Je participe à la prom'classic. Ambiance de fou furieux, entraînement de fou furieux.<br> J'ai tout pour reussir ! J'en ai peut-être trop fait à l'entraînement car veille de la course je tombe dans les pommes lors de mes accels'.<br> J'ai pas fait le déplacement pour rien, je m'aligne donc sur la ligne de départ. Résultat : 31'06. Je suis content, mais j'ai encore les crocs !", 'Link': ''},
    {'Date': '2024-03', 'Title': "France de Cross et Semi de Lille", 'Description': "Après avoir écouté le podcast de Runnix sur Etienne Daguinos, je décide de tenter l'enchaînement France de cross -> Semi de Lille,<br> qui marche plutôt bien ! 108e position aux France de cross sur un parcours pas facile et un joli 1h05'42 sur semi ...<br> La progression continue !", 'Link': ''},
    {'Date': '2024-04', 'Title': "10km de Valenciennes", 'Description': "Après Lille, je n'ai plus qu'un objectif en tête : validé le fameux sub 30.<br> Je passe de très belles séances, m'entraîne bien, récupère bien.<br> Je décide donc de m'aligner sur les 10km de Valenciennes. Je fais 30:15 (passage au 5km en 14:36), joli popcorn ! Je ne perds jamais, j'apprends.", 'Link': ''},
    {'Date': '2024-05', 'Title': "Début de la saison de piste", 'Description': "Début de la saison de piste (que je n'ai pas envie de faire). J'essaye de me motiver car on me dit que ça va me faire progresser sur la route.<br> J'execute donc. Premier tour des interclubs, pop corn total sur 3000m avec un 8:39. Beaucoup de déception ...<br> Je commence à avoir du mal à m'entraîner, je perds la motivation. Fin du mois, 5000m de St Maur que je remporte en 14:40. Je suis toujours frustré.", 'Link': ''},
    {'Date': '2024-06', 'Title': "Piste acte 2", 'Description': "Je m'entraîne tant bien que mal, je passe quelques séances.<br> Mais je sens que je commence à être fatigué. Je vise 14:10 sur 5000m et je pense que j'en ai les capacités.<br> Malheureusement, je ne parviens pas à efffectuer ce chrono et réalise deux fois 14:30 (Cergy puis FAST5000).", 'Link': ''},
    {'Date': '2024-08', 'Title': "Bilan de la saison", 'Description': "Je décide de faire une coupure sur une partie de juillet et août afin de me régénérer.<br> J'ai beaucoup d'objectifs en tête mais si je retiens une chose de ma saison d'athlé, c'est que j'ai aussi besoin des études pour être stimulé.<br> J'ai très hâte de débuter mon master 2 au MVA à la rentrée de septembre et souhaite concilier mon cursus académique avec mes aventures sportives.", 'Link': ''},
]

# Créer le DataFrame des événements
events_df = pd.DataFrame(events)

training_volume = [
    {'Start Date': '2018-06-24', 'End Date': '2019-06-23', 'Volume (km/week)': 15},
    {'Start Date': '2019-06-24', 'End Date': '2020-06-23', 'Volume (km/week)': 25},
    {'Start Date': '2020-06-24', 'End Date': '2022-06-23', 'Volume (km/week)': 50},
    {'Start Date': '2022-09-01', 'End Date': '2022-12-31', 'Volume (km/week)': 70},
    {'Start Date': '2023-01-01', 'End Date': '2023-06-30', 'Volume (km/week)': 70},
    {'Start Date': '2023-06-01', 'End Date': '2023-11-30', 'Volume (km/week)': 100},
    {'Start Date': '2023-12-01', 'End Date': '2023-12-31', 'Volume (km/week)': 130},
    {'Start Date': '2024-01-01', 'End Date': '2024-03-31', 'Volume (km/week)': 150},
    {'Start Date': '2024-04-01', 'End Date': '2024-04-15', 'Volume (km/week)': 180},
    {'Start Date': '2024-04-16', 'End Date': '2024-04-30', 'Volume (km/week)': 160},
    {'Start Date': '2024-05-01', 'End Date': '2024-06-15', 'Volume (km/week)': 150},
    {'Start Date': '2024-06-16', 'End Date': '2024-06-30', 'Volume (km/week)': 130},
    {'Start Date': '2024-07-01', 'End Date': '2024-08-31', 'Volume (km/week)': 50},
]

# Créer le DataFrame du volume d'entraînement
training_df = pd.DataFrame(training_volume)

# Convertir les dates en datetime
training_df['Start Date'] = pd.to_datetime(training_df['Start Date'])
training_df['End Date'] = pd.to_datetime(training_df['End Date'])
events_df['Date'] = pd.to_datetime(events_df['Date'])

# Créer le graphique de volume d'entraînement
fig1 = go.Figure()

# Ajout du volume d'entraînement
fig1.add_trace(go.Scatter(
    x=training_df['Start Date'],
    y=training_df['Volume (km/week)'],
    mode='lines+markers',
    name='Volume d\'entraînement',
    line=dict(color='blue')
))

# Ajout des événements
for _, event in events_df.iterrows():
    fig1.add_trace(go.Scatter(
        x=[event['Date']],
        y=[training_df[training_df['Start Date'] <= event['Date']]['Volume (km/week)'].values[-1]],
        text=f"<b>{event['Title']}</b><br>{event['Description']}",
        hoverinfo='text',
        mode='markers',
        marker=dict(size=10),
        name=event['Title']
    ))

fig1.update_layout(
    title='Évolution de mon volume d\'entraînement',
    xaxis_title='Date',
    yaxis_title='Volume (km/semaine)',
    title_x=0.5,
    height=500
)

"""# Créer le tableau pour les descriptions des événements
fig2 = go.Figure(data=[go.Table(
    header=dict(values=['Description']),
    cells=dict(values=[
        events_df['Title'] + "<br>" + 
        events_df['Description']
    ]),
    columnwidth=[20]
)])

fig2.update_layout(
    title='Descriptions des Événements',
    height=1200,
)"""

# Sauvegarder les graphiques en PNG
fig1.write_image("/Users/augustincablant/Documents/GitHub/coach/training_volume.png")
#fig2.write_image("/Users/augustincablant/Documents/GitHub/coach/events_table.png")

#pio.write_image(fig, '/Users/augustincablant/Documents/GitHub/coach/evolution.png', format='png')
