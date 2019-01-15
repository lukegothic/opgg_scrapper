import requests
import os
from lxml import html
import csv

datasets = ["amateur","competitivo"]
for ds in datasets:
    teams = []
    with open("../data/teams_{}.txt".format(ds), "r", encoding="utf-8") as f:
        teams = f.read().splitlines()
    for team in teams:
        mmrs = []
        totalmmr = 0
        team = team.split(",")
        print('====' + team[0] + '====')
        teamdir = "cache/{}".format(team[0])
        if not os.path.exists(teamdir):
            os.makedirs(teamdir)
        for m in team:
            if m != team[0]:
                filete = "{}/{}.html".format(teamdir, m)
                try:
                    with open(filete) as f:
                        data = f.read()
                except:
                    req = requests.get("http://euw.op.gg/summoner/ajax/mmr/summonerName={}".format(m))
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
        with open("results/opgg_{}.csv".format(ds), "a", newline='\n') as f:
            writer = csv.DictWriter(f, fieldnames=["team", "mmr"], delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow({ "team": team[0], "mmr": "{}".format(totalmmr / 5).replace(".", ",") })
