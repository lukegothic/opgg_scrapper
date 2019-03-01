import csv,os,requests
from lxml import html

teams = []
teammembers = ['inv1','inv2','inv3','inv4','inv5','sup1','sup2']
with open("lnl/opgg/results/opggall.csv", "w") as f:
    pass
with open("lnl/data/teams.txt",'r',encoding='utf8') as f:
    r = csv.DictReader(f,fieldnames=['id','division','name','logo','inv1','inv2','inv3','inv4','inv5','sup1','sup2','trainer'])
    for team in r:
        mmrs = []
        totalmmr = 0
        print('====' + team['name'] + '====')
        teamdir = "cache/{}".format(team['name'])
        if not os.path.exists(teamdir):
            os.makedirs(teamdir)
        for m in teammembers:
            jugador = team[m]
            if jugador != '':
                filete = "{}/{}.html".format(teamdir, jugador)
                try:
                    with open(filete) as f:
                        data = f.read()
                except:
                    req = requests.get("http://euw.op.gg/summoner/ajax/mmr/summonerName={}".format(jugador))
                    data = req.text
                    with open(filete, "w") as f:
                        f.write(data)
                if len(data) > 0:
                    tree = html.fromstring(data)
                    membermmr = tree.xpath("//td[@class='MMR']/text()")
                else:
                    membermmr = []
                # TODO: sólo coger los miembros con mas elo
                if len(membermmr) > 0:
                    mmr = membermmr[0]
                    mmr = membermmr[0].replace("\n", "").replace("\t", "").replace(",", "")
                    mmr = (int)(mmr)
                    mmrs.append(mmr)
                else:
                    mmrs.append(1200)
        mmrs = sorted(mmrs, reverse=True)
        print(mmrs)
        for i in range(0,5):
            totalmmr += mmrs[i]
        print(totalmmr)
        with open("lnl/opgg/results/opggall.csv", "a", newline='\n') as f:
            writer = csv.DictWriter(f, fieldnames=["division","team", "mmr"], delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow({ "division": team["division"], "team": team["name"], "mmr": "{}".format(totalmmr / 5).replace(".", ",") })
