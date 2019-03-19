import csv
import urllib.parse
import os
print(os.getcwd())
rowscols = 6

urls = {
    "logo": "http://juegoluegoexisto.com/wp-content/uploads/2018/12/{}.png",
    "calendar": "http://docs.juegoluegoexisto.com/lnl/LNL2019_Calendario_{}.pdf",
    "battlefy": "https://battlefy.com/juegoluegoexisto/liga-navarra-de-league-of-legends/5c2752964993b903a55f6afe/stage/{}/result"
}
splits = ["NASHOR","DRAGON1","DRAGON2","PORO"]
data_division = {
    "NASHOR": {
        "class": "nashor",
        "logo": "liga_nashor",
        "calendar": "Nashor",
        "battlefy": "5c27609214e24103a57d29a1",
        "label": "Nashor"
    },
    "DRAGON1": {
        "class": "dragon",
        "logo": "liga_dragon",
        "calendar": "DragonGrupo1",
        "battlefy": "5c313aa5c3126e03b0595543",
        "label": "Drag&oacute;n A"
    },
    "DRAGON2": {
        "class": "dragon",
        "logo": "liga_dragon",
        "calendar": "DragonGrupo2",
        "battlefy": "5c313aa5c3126e03b0595543",
        "label": "Drag&oacute;n B"
    },
    "PORO": {
        "class": "poro",
        "logo": "liga_poro",
        "calendar": "Poro",
        "battlefy": "5c2752dea5deb4039f7d1b88",
        "label": "Poro"
    }
}
with open("lnl/opgg/results/urls.html","w") as f_html:
    pass
for s in splits:
    with open("lnl/opgg/results/urls.html","a") as f_html:
        f_html.write('<div class="lnl-division-header {}"><img class="lnl-division-icon alignnone size-full wp-image-201" src="http://juegoluegoexisto.com/wp-content/uploads/2018/12/{}.png" alt="{}"><a target="_blank" href="https://battlefy.com/juegoluegoexisto/liga-navarra-de-league-of-legends/5c2752964993b903a55f6afe/stage/{}/results"><span class="lnl-division-text">divisi&oacute;n</span><span class="lnl-division-name">&nbsp;{}</span></a></div>\n'
            .format(data_division[s]["class"], data_division[s]["logo"], data_division[s]["label"], data_division[s]["battlefy"], data_division[s]["label"]))

    with open("lnl/data/teams.txt",'r',encoding='utf8') as f_teams:
        r = csv.DictReader(f_teams,fieldnames=['id','division','name','logo','inv1','inv2','inv3','inv4','inv5','sup1','sup2','trainer'])
        with open("lnl/opgg/results/urls.html","a") as f_html:
            f_html.write("<div class='lnl-division-teams'>")
            for team in r:
                if team["division"] == s:
                    if (team["logo"] == "1"):
                        x = (int)(team['id']) - 1
                        y = x % rowscols
                        x = x // rowscols
                    else:
                        x = 100
                        y = 100
                    #f_html.write("<a class='lnl-team-logo' target='_blank' href='http://euw.op.gg/multi/query={}' style='background-position:-{}px -{}px;'><span class='lnl-team-name'>{}</a>"
                    f_html.write("<a class='lnl-team-logo' target='_blank' href='http://euw.op.gg/multi/query={}' style='background-position:{}% {}%;'><span class='lnl-team-name'>{}</a>"
                    .format(urllib.parse.quote_plus(",".join([team["inv1"],team["inv2"],team["inv3"],team["inv4"],team["inv5"],team["sup1"] if team["sup1"] else '',team["sup2"] if team["sup2"] else ''])), y*20, x*20, team["name"]))
            f_html.write("</div>\n\n")
