import csv
import urllib.parse

size = 160
rowscols = 6

splits = ["NASHOR","DRAGON1","DRAGON2","Amateur"]

with open("results/urls.html","w") as f:
    pass
for s in splits:
    with open("../data/teams.txt",'r',encoding='utf8') as f:
        r = csv.DictReader(f,fieldnames=['id','division','name','logo','inv1','inv2','inv3','inv4','inv5','sup1','sup2','trainer'])
        for team in r:
            if team["division"] == s:
                with open("results/urls.html","a") as f:
                    if (team["logo"] == "1"):
                        x = (int)(team['id']) - 1
                        y = x % rowscols * 160
                        x = x // rowscols * 160
                    else:
                        x = 800
                        y = 800
                    f.write("<a target='_blank' href='http://euw.op.gg/multi/query={}' style='margin:5px;text-decoration:none;display:inline-block;position:relative;width:160px;height:160px;background:url(\"http://juegoluegoexisto.com/wp-content/uploads/2018/12/lnl_logos.png\") -{}px -{}px no-repeat'><span style='position:absolute;text-shadow:0 0 5px #000,0 0 5px #000,0 0 5px #000,0 0 5px #000;bottom:-16px;display:block;text-align:center;width:100%;font-family:Staatliches;font-size:22px;'>{}</a>".format(urllib.parse.quote_plus(",".join([team["inv1"],team["inv2"],team["inv3"],team["inv4"],team["inv5"],team["sup1"] if team["sup1"] else '',team["sup2"] if team["sup2"] else ''])), y, x, team["name"]))
        with open("results/urls.html","a") as f:
            f.write("\n\n")
