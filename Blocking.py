import math
import random
import csv

positions = []
genned = 0
blocks = []

#Load position data
with open('blocking_stats.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        positions.append(row)

#Now lets generate and sim

while genned < 1000:

    #let's roll the block type
    blockstyle = random.randint(1,3)

    #offense generation
    if blockstyle == 3:
        roll_off = random.randint(5,21)
    else:
        roll_off = random.randint(1,21)
    pos_off = positions[roll_off][0]
    star_off = random.randint(0,4)
    trait_off = positions[roll_off][1]
    if star_off == 4:
        a = int(positions[roll_off][10])
        b = int(positions[roll_off][11])
        c = int(positions[roll_off][20])
        d = int(positions[roll_off][21])
        e = int(positions[roll_off][30])
        f = int(positions[roll_off][31])
        g = int(positions[roll_off][40])
        h = int(positions[roll_off][41])
        i = int(positions[roll_off][50])
        j = int(positions[roll_off][51])
        k = int(positions[roll_off][60])
        l = int(positions[roll_off][61])

    elif star_off == 3:
        a = int(positions[roll_off][8])
        b = int(positions[roll_off][9])
        c = int(positions[roll_off][18])
        d = int(positions[roll_off][19])
        e = int(positions[roll_off][28])
        f = int(positions[roll_off][29])
        g = int(positions[roll_off][38])
        h = int(positions[roll_off][39])
        i = int(positions[roll_off][48])
        j = int(positions[roll_off][49])
        k = int(positions[roll_off][58])
        l = int(positions[roll_off][59])

    elif star_off == 2:
        a = int(positions[roll_off][6])
        b = int(positions[roll_off][7])
        c = int(positions[roll_off][16])
        d = int(positions[roll_off][17])
        e = int(positions[roll_off][26])
        f = int(positions[roll_off][27])
        g = int(positions[roll_off][36])
        h = int(positions[roll_off][37])
        i = int(positions[roll_off][46])
        j = int(positions[roll_off][47])
        k = int(positions[roll_off][56])
        l = int(positions[roll_off][57])

    elif star_off == 1:
        a = int(positions[roll_off][4])
        b = int(positions[roll_off][5])
        c = int(positions[roll_off][14])
        d = int(positions[roll_off][15])
        e = int(positions[roll_off][24])
        f = int(positions[roll_off][25])
        g = int(positions[roll_off][34])
        h = int(positions[roll_off][35])
        i = int(positions[roll_off][44])
        j = int(positions[roll_off][45])
        k = int(positions[roll_off][54])
        l = int(positions[roll_off][55])

    else:
        a = int(positions[roll_off][2])
        b = int(positions[roll_off][3])
        c = int(positions[roll_off][12])
        d = int(positions[roll_off][13])
        e = int(positions[roll_off][22])
        f = int(positions[roll_off][23])
        g = int(positions[roll_off][32])
        h = int(positions[roll_off][33])
        i = int(positions[roll_off][42])
        j = int(positions[roll_off][43])
        k = int(positions[roll_off][52])
        l = int(positions[roll_off][53])
    
    off_run = random.randint(a,b)
    off_pass = random.randint(c,d)
    off_spe = random.randint(e,f)
    off_stre = random.randint(g,h)
    off_agi = random.randint(i,j)
    off_iq = random.randint(k,l)

    #defense generation
    roll_def = random.randint(23,35)
    pos_def = positions[roll_def][0]
    star_def = random.randint(0,4)
    trait_def = positions[roll_def][1]

    if star_def == 4:
        m = int(positions[roll_def][70])
        n = int(positions[roll_def][71])
        o = int(positions[roll_def][80])
        p = int(positions[roll_def][81])
        q = int(positions[roll_def][30])
        r = int(positions[roll_def][31])
        s = int(positions[roll_def][40])
        t = int(positions[roll_def][41])
        u = int(positions[roll_def][50])
        v = int(positions[roll_def][51])
        w = int(positions[roll_def][60])
        x = int(positions[roll_def][61])

    elif star_def == 3:
        m = int(positions[roll_def][68])
        n = int(positions[roll_def][69])
        o = int(positions[roll_def][78])
        p = int(positions[roll_def][79])
        q = int(positions[roll_def][28])
        r = int(positions[roll_def][29])
        s = int(positions[roll_def][38])
        t = int(positions[roll_def][39])
        u = int(positions[roll_def][48])
        v = int(positions[roll_def][49])
        w = int(positions[roll_def][58])
        x = int(positions[roll_def][59])

    elif star_def == 2:
        m = int(positions[roll_def][66])
        n = int(positions[roll_def][67])
        o = int(positions[roll_def][76])
        p = int(positions[roll_def][77])
        q = int(positions[roll_def][26])
        r = int(positions[roll_def][27])
        s = int(positions[roll_def][36])
        t = int(positions[roll_def][37])
        u = int(positions[roll_def][46])
        v = int(positions[roll_def][47])
        w = int(positions[roll_def][56])
        x = int(positions[roll_def][57])

    elif star_def == 1:
        m = int(positions[roll_def][64])
        n = int(positions[roll_def][65])
        o = int(positions[roll_def][74])
        p = int(positions[roll_def][75])
        q = int(positions[roll_def][24])
        r = int(positions[roll_def][25])
        s = int(positions[roll_def][34])
        t = int(positions[roll_def][35])
        u = int(positions[roll_def][44])
        v = int(positions[roll_def][45])
        w = int(positions[roll_def][54])
        x = int(positions[roll_def][55])

    else:
        m = int(positions[roll_def][62])
        n = int(positions[roll_def][63])
        o = int(positions[roll_def][72])
        p = int(positions[roll_def][73])
        q = int(positions[roll_def][22])
        r = int(positions[roll_def][23])
        s = int(positions[roll_def][32])
        t = int(positions[roll_def][33])
        u = int(positions[roll_def][42])
        v = int(positions[roll_def][43])
        w = int(positions[roll_def][52])
        x = int(positions[roll_def][53])

    
    def_run = random.randint(m,n)
    def_pass = random.randint(o,p)
    def_spe = random.randint(q,r)
    def_stre = random.randint(s,t)
    def_agi = random.randint(u,v)
    def_iq = random.randint(w,x)

    if blockstyle == 1:
        test = "Man"
        value_off = (off_run * .4 + off_spe * .1 + off_stre * .25 + off_agi * .1 + off_iq * .15)
        value_def = (def_run * .4 + def_spe * .1 + def_stre * .25 + def_agi * .1 + def_iq * .15)
        
    elif blockstyle == 2:
        test = "Zone"
        value_off = (off_run * .4 + off_spe * .1 + off_stre * .1 + off_agi * .25 + off_iq * .15)
        value_def = (def_run * .4 + def_spe * .1 + def_stre * .1 + def_agi * .25 + def_iq * .15)

    else:
        test = "Pass"
        value_off = (off_pass * .4 + off_spe * .05 + off_stre * .2 + off_agi * .2 + off_iq * .15)
        value_def = (def_pass * .4 + def_spe * .15 + def_stre * .15 + def_agi * .15 + def_iq * .15)

    if value_off > value_def:
        winner = "OFF"
    elif value_def > value_off:
        winner = "DEF"
    else:
        winner = "TIE"
    result = value_off - value_def

    #Lets Put it all together
    blocks.append([test,pos_off,star_off,trait_off,value_off,pos_def,star_def,trait_def,value_def,winner,result,off_run,off_pass,off_spe,off_stre,off_agi,off_iq,def_run,def_pass,def_spe,def_stre,def_agi,def_iq])
    genned += 1

    #let's make sure we're working
    print("Genned block #" + str(genned))

#Now Lets output
with open('blocking_trials.csv', "w") as output:
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["Trial"]+["OffP"]+["OffS"]+["OffT"]+["Off Score"]+["DefP"]+["DefS"]+["DefT"]+["Off Score"]+["Winner"]+["Diff"]+["off_run"]+["off_pass"]+["off_spe"]+["off_stre"]+["off_agi"]+["off_iq"]+["def_run"]+["def_pass"]+["def_spe"]+["def_stre"]+["def_agi"]+["def_iq"])
    writer.writerows(blocks)
