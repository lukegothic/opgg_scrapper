import csv
import urllib.parse
import os
print(os.getcwd())
size = 160
rowscols = 6

splits = ["NASHOR","DRAGON1","DRAGON2","Amateur"]
data_division = {
    "NASHOR": {
        "logo": "liga_nashor",
        "battlefy": "5c27609214e24103a57d29a1",
        "label": "Nashor",
        "color1": "b54bfc",
        "color2": "9c18f9"
    },
    "DRAGON1": {
        "logo": "liga_dragon",
        "battlefy": "5c313aa5c3126e03b0595543",
        "label": "&nbsp;Drag&oacute;n</span><span style='font-family: Lobster;'> (grupo A)",
        "color1": "ad4556",
        "color2": "b20022"
    },
    "DRAGON2": {
        "logo": "liga_dragon",
        "battlefy": "5c313aa5c3126e03b0595543",
        "label": "&nbsp;Drag&oacute;n</span><span style='font-family: Lobster;'> (grupo B)",
        "color1": "ad4556",
        "color2": "b20022"
    },
    "Amateur": {
        "logo": "liga_poro",
        "battlefy": "5c2752dea5deb4039f7d1b88",
        "label": "Poro",
        "color1": "a08081",
        "color2": "a2696b",
    }
}
with open("lnl/opgg/results/urls.html","w") as f_html:
    pass
for s in splits:
    with open("lnl/opgg/results/urls.html","a") as f_html:
        f_html.write('<div style="background: linear-gradient(to bottom, #{} 0%,#{} 50%,#{} 51%,#{} 100%); height: 60px; line-height: 60px; font-size: 40px; margin-left: 20px; padding-left: 80px; position: relative; margin: 30px 0;"><img class="logo-division alignnone size-full wp-image-201" style="position: absolute; top: -30px; left: -30px;" src="http://juegoluegoexisto.com/wp-content/uploads/2018/12/{}.png" alt="" width="120" height="120"><a target="_blank" href="https://battlefy.com/juegoluegoexisto/liga-navarra-de-league-of-legends/5c2752964993b903a55f6afe/stage/{}/results"><span style="font-family: Lobster;">divisi&oacute;n</span><span style="text-shadow: 0 0 5px #000; font-family: Staatliches; font-size: 50px;">&nbsp;{}</span></a></div>\n'.format(data_division[s]["color1"],data_division[s]["color1"],data_division[s]["color2"],data_division[s]["color2"],data_division[s]["logo"],data_division[s]["battlefy"],data_division[s]["label"]))
    with open("lnl/data/teams.txt",'r',encoding='utf8') as f_teams:
        r = csv.DictReader(f_teams,fieldnames=['id','division','name','logo','inv1','inv2','inv3','inv4','inv5','sup1','sup2','trainer'])
        for team in r:
            if team["division"] == s:
                with open("lnl/opgg/results/urls.html","a") as f_html:
                    if (team["logo"] == "1"):
                        x = (int)(team['id']) - 1
                        y = x % rowscols * 160
                        x = x // rowscols * 160
                    else:
                        x = 800
                        y = 800
                    f_html.write("<a target='_blank' href='http://euw.op.gg/multi/query={}' style='margin:5px;text-decoration:none;display:inline-block;position:relative;width:160px;height:160px;background:url(\"http://juegoluegoexisto.com/wp-content/uploads/2018/12/lnl_logos.png\") -{}px -{}px no-repeat'><span style='position:absolute;text-shadow:0 0 5px #000,0 0 5px #000,0 0 5px #000,0 0 5px #000;bottom:-16px;display:block;text-align:center;width:100%;font-family:Staatliches;font-size:22px;'>{}</a>".format(urllib.parse.quote_plus(",".join([team["inv1"],team["inv2"],team["inv3"],team["inv4"],team["inv5"],team["sup1"] if team["sup1"] else '',team["sup2"] if team["sup2"] else ''])), y, x, team["name"]))
        with open("lnl/opgg/results/urls.html","a") as f_html:
            f_html.write("\n\n")
