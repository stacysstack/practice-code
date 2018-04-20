

#import requests
from bs4 import BeautifulSoup as Soup 
import urllib, requests, re, pandas as pd 
from collections import Counter

# inputdate = raw_input('Date (mo_day format): ')
jobfield = raw_input('Which career are you searching? (add "+" between words): ')
fromage = raw_input('How many days back should I check? ')

beginurl = 'http://api.indeed.com/ads/apisearch?publisher=3025890005972088&q=%22'+jobfield+'%22&sort=&radius=&st=&jt=fulltime&start='
endurl = '&limit=3000&fromage='+fromage+'&filter=1&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2'

pd.set_option('max_colwidth',500)	#remove column limit
df = pd.DataFrame()		# create a new data frame

for page in range(0,12): #12 pages per day
    print page
    indeedurl = "%s%s%s" % (beginurl, page*25, endurl) # get full url 
    # print indeedurl
    rawdata = Soup(urllib.urlopen(indeedurl), "lxml") 

    for i in range(0,25): #25 job postings per page

        try:
            result = rawdata.results.contents[i]
            category = jobfield
            jobtitle = result.find({'jobtitle'}).getText()
            print jobtitle
            # print jobtitle
            company = result.find({'company'}).getText()
            # print company
            location = result.find({'formattedlocation'}).getText()
            # print location
            city = result.find({'city'}).getText()
            state = result.find({'state'}).getText()
            date = result.find({'date'}).getText()
            jobkey = result.find({'jobkey'}).getText()
            # print date
            snippet = result.find({'snippet'}).getText()
            # print snippet
            joburl = result.find({'url'}).getText()
            # print joburl
            # access url and grab full job description
            wordsoup = Soup(urllib.urlopen(joburl), "lxml")

            descript = wordsoup.find('span', attrs = {'id':'job_summary'}).getText().strip()

#            try: 
#                country = result.find({'country'}).getText()
#            except:
#                country = ''
#            try: 
#                latitude = result.find({'latitude'}).getText()
#            except: 
#                latitude = ''
#
#            try:                 
#                longitude = result.find({'longitude'}).getText()
#            except: 
#                longitude = ''

            for k in range(0,len(descript)):
                active = descript.count(" activ")
                adven = descript.count(" adventurous")
                aggr = descript.count(" aggress")
                amb = descript.count(" ambitio")
                anal = descript.count(" analy")
                asser = descript.count(" assert")
                athl = descript.count(" athlet")
                auto = descript.count(" autonom")
                boast = descript.count(" boast")
                chall = descript.count(" challeng")
                compet = descript.count(" compet")
                conf = descript.count(" confident")
                cour = descript.count(" courag")
                decide = descript.count(" decide")
                decisive = descript.count(" decisive")
                decision = descript.count(" decision")
                determin = descript.count(" determin")
                domin = descript.count(" dominant")
                force = descript.count(" force")
                greedy = descript.count(" greedy")
                headstrong = descript.count(" headstrong")
                hierarchy = descript.count(" hierarch")
                hostil = descript.count(" hostil")
                impulsive = descript.count(" impulsive")
                independen = descript.count(" independen")
                individual = descript.count(" individual")
                intellect = descript.count(" intellect")
                lead = descript.count(" lead")
                logic = descript.count(" logic")
                masculine = descript.count(" masculine")
                objective = descript.count(" objective")
                opinion = descript.count(" opinion")
                outspoken = descript.count(" outspoken")
                persist = descript.count(" persist")
                principle = descript.count(" principle")
                reckless = descript.count(" reckless")
                stubborn = descript.count(" stubborn")
                superior = descript.count(" superior")
                selfconfid = descript.count(" self-confid")
                selfsufficien = descript.count(" self-sufficien")
                selfrelian = descript.count(" self-relian")
                
                ninja = descript.count("ninja")
                he = descript.count(" he ")
                his = descript.count(" his ")
                
                #TEXTIO words male
                # proven = descript.count(" proven")
                # manage = descript.count(" manage")
                # managethe = descript.count(" manage the ")
                # managing = descript.count(" managing")
                # thrive = descript.count(" thrive")
                # rockstar = descript.count(" rock star")
                # exceptional = descript.count(" exceptional")
                # overseeing = descript.count("overseeing")
                # expert = descript.count(" expert")
                # adrive = descript.count(" a drive to")
                # fastpaced = descript.count(" fast-paced")
                # oversees = descript.count(" oversee")
                # worldclass = descript.count(" world class")
                # caliber = descript.count(" caliber")
                # underpress = descript.count(" under pressure")
                # extremely = descript.count(" extremely")
                # enforce = descript.count(" enforce")
                # outstanding = descript.count("outstanding")
                # comejoin = descript.count(" come join")
                # partnering = descript.count(" partnering")
                # drivenby = descript.count(" driven by")
                # justify = descript.count(" justify")
                # dictating = descript.count(" dictating")
                # ownthe = descript.count(" own the")
                # perfection = descript.count(" perfect")
                # manageproc = descript.count(" manage process")
                # gogetter = descript.count(" go-get")
                # manpower = descript.count(" manpower ")
                # tackle = descript.count(" tackle")
                # extrem = descript.count(" extrem")
                # capture = descript.count(" capture")
                # ahugeplus = descript.count(" a huge plus")
                #TEXTIO end




                #  FEMININE
                affectionate = descript.count(" affectionate")
                child = descript.count(" child")
                cheer = descript.count(" cheer")
                commit = descript.count(" commit")
                communal = descript.count(" communal")
                compassion = descript.count(" compassion")
                connect = descript.count(" connect")
                considerate = descript.count(" considerate")
                cooperate = descript.count(" cooperat")
                depend = descript.count(" depend")
                emotiona = descript.count(" emotiona")
                empath = descript.count(" empath")
                feminine = descript.count(" feminine")
                flatterable = descript.count(" flatterable")
                gentle = descript.count(" gentle")
                honest = descript.count(" honest")
                interpersonal = descript.count(" interpersonal")
                interdependen = descript.count(" interdependen")
                interpersona = descript.count(" interpersona")
                kind = descript.count(" kind")
                kinship = descript.count(" kinship")
                loyal = descript.count(" loyal")
                modesty = descript.count(" modesty")
                nag = descript.count(" nag")
                nurtur = descript.count(" nurtur")
                pleasant = descript.count(" pleasant")
                polite = descript.count(" polite")
                quiet = descript.count(" quiet")
                respon = descript.count(" respon")
                sensitiv = descript.count(" sensitiv")
                submissive = descript.count(" submissive")
                support = descript.count(" support")
                sympath = descript.count(" sympath")
                tender = descript.count(" tender")
                together = descript.count(" together")
                trust = descript.count(" trust")
                understand = descript.count(" understand")
                warm = descript.count(" warm")
                whin = descript.count(" whin")
                yiel = descript.count(" yield")

                her = descript.count(" her ")
                hers = descript.count(" hers ")
                she = descript.count( " she ")


                #TEXTIO feminine
            
                # inclusive = descript.count(" inclusive")
                # collaborat = descript.count(" collaborat")
                # contribute = descript.count(" contribut")
                # diplomacy = descript.count(" diplomacy")
                # passion = descript.count(" passion")
                # creat = descript.count(" creat")
                # wedlike = descript.count(" we'd like")
                # successstart = descript.count(" success starting")
                # tellastory = descript.count(" tell a story")
                # foster = descript.count(" foster")
                # progressive = descript.count(" progressive")
                # balancing = descript.count(" balanc")
                # family = descript.count(" family")
                # transparent = descript.count(" transparent")
                # strongrel = descript.count(" strong relation")
                # comfortable = descript.count(" comfort")
                # team = descript.count(" team")
                # encourage = descript.count(" encourag")
                # embrace = descript.count(" embrac")
                # beautiful = descript.count(" beaut")
                # care = descript.count(" care")
                # partner = descript.count(" partner")
                # withothers = descript.count(" with other")
                # partof = descript.count(" part of")
                # imagine = descript.count(" imagin")
                # teach = descript.count(" teach")
                # striv = descript.count(" striv")
                # nourish = descript.count(" nourish")
                # comejoin = descript.count(" come join")
                # openness = descript.count(" openness")
                # welcome = descript.count(" welcom")
                # meaning = descript.count(" meaning")
                

            femtotal = affectionate+child+cheer+commit+communal+compassion+connect+considerate+cooperate+depend+emotiona+empath+feminine+flatterable+gentle+honest+interpersonal+interdependen+interpersona+kind+kinship+loyal+modesty+nag+nurtur+pleasant+polite+quiet+respon+sensitiv+submissive+support+sympath+tender+together+trust+understand+warm+whin+yiel
            
            femextras = her+hers+she
            
            masctotal = active+adven+aggr+amb+anal+asser+athl+auto+boast+chall+compet+conf+cour+decide+decisive+decision+determin+domin+force+greedy+headstrong+hierarchy+hostil+impulsive+independen+individual+intellect+lead+logic+masculine+objective+opinion+outspoken+persist+principle+reckless+stubborn+superior+selfconfid+selfsufficien+selfrelian

            mascextras = ninja+he+his
            #textio fem total 
            #femtotal = affectionate+child+cheer+commit+communal+compassion+connect+considerate+cooperate+depend+emotiona+empath+feminine+flatterable+gentle+honest+interpersonal+interdependen+interpersona+kind+kinship+loyal+modesty+nag+nurtur+pleasant+polite+quiet+respon+sensitiv+submissive+support+sympath+tender+together+trust+understand+warm+whin+yiel+inclusive+collaborat+contribute+diplomacy+passion+creat+wedlike+successstart+tellastory+foster+progressive+balancing+family+transparent+strongrel+comfortable+team+encourage+embrace+beautiful+care+partner+withothers+partof+imagine+teach+striv+nourish+comejoin+openness+welcome+meaning



            #textio masc total
            #masctotal = active+advent+aggr+amb+anal+asser+athl+auto+boast+chall+compet+conf+cour+decide+decisive+decision+determin+domin+force+greedy+headstrong+hierarchy+hostil+impulsive+independen+individual+intellect+lead+logic+masculine+objective+opinion+outspoken+persist+principle+reckless+stubborn+superior+selfconfid+selfsufficien+selfrelian+proven+manage+managethe+managing+thrive+rockstar+exceptional+overseeing+expert+adrive+fastpaced+oversees+worldclass+caliber+underpress+extremely+enforce+outstanding+comejoin+partnering+drivenby+justify+dictating+ownthe+perfection+manageproc+gogetter+manpower+tackle+extrem+capture+ahugeplus



            characternumber = len(descript)

            wordnumber = len(descript.split())
            # print descript
            sponsored = result.find({'sponsored'}).getText()
            # print sponsored
            expired = result.find({'expired'}).getText()
            # print expired
            uniqueID = company[0:1]+location[0:1]+date[5:7]+joburl[37:40]
            # print uniqueID     
            
            mascratio = masctotal/float(wordnumber)
            femratio = femtotal/float(wordnumber)

            df = df.append({
                
                #GEN INFO
                'A10-Unique ID': uniqueID, 
                'A11-Job Key': jobkey,
                'A12-Category': category,
                'A2-Job Title': jobtitle,
                'A30-Company': company, 
#                'A31-Country': country,
                'A32-State': state,
                'A33-City': city, 
#                'A34-Latitude': latitude,
#                'A35-Longitude': longitude,
                'A4-Location': location,
                'A7-Snippet': snippet, 
                'A8-Date': date, 
                'A9-Url': joburl, 
                'A91-Sponsored': sponsored, 
                'A92-Expired': expired, 
                'A921-Word Number': wordnumber,
                'A922-Characters':characternumber,
                'A93-Full description': descript,
                'A94-Masc Total': masctotal,
                'A96-Masc Ratio': mascratio,
                'A95-Fem Total': femtotal,
                'A97-Fem Ratio': femratio,
                #extras
                'A98-Male Extras': mascextras,
                'A99-Fem Extras': femextras,
                           
                # MASCULINE LIST - for spreadsheet columns
                'B1-Active': active, 
                'B2-Adventurous': adven, 
                'B3-Aggress': aggr,
                'B4-Ambitio': amb,
                'B5-Analy': anal,
                'B6-Assert': asser,
                'B7-Athlet': athl,
                'B8-Autonom': auto,
                'B9-Boast': boast,
                'C1-Challeng': chall,
                'C2-Compet': compet,
                'C3-Confi': conf,
                'C4-Cour': cour,
                'C5-Decide': decide,
                'C6-Decisive': decisive,
                'C7-Decision': decision,
                'C8-Determin': determin,
                'C9-Dominant': domin,
                'D1-Force': force,
                'D2-Greedy': greedy,
                'D3-Headstrong': headstrong,
                'D4-Hierarch': hierarchy,
                'D5-Hostil': hostil,
                'D6-Impulsive': impulsive,
                'D7-Independ': independen,
                'D8-Individual': individual,
                'D9-Intellect': intellect,
                'E1-Lead': lead,
                'E2-Logic': logic,
                'E3-Masculine': masculine,
                'E4-Objective': objective,
                'E5-Opinions': opinion,
                'E6-Outspoken': outspoken,
                'E7-Persist': persist,
                'E8-Principle': principle,
                'E9-Reckless': reckless, 
                'F1-Stubborn': stubborn,
                'F2-Superior': superior,
                'F3-Self-Confiden': selfconfid,
                'F4-Self-Suff': selfsufficien,
                'F5-Self-Relian': selfrelian,

                #mas extras - for spreadsheet
                'F6-Ninja': ninja,
                'F7-He': he ,
                'F8-His': his ,

                #FEMININE LIST - for spreadsheet columns
                'G1-Affect': affectionate,
                'G1-Child': child,
                'G2-Cheer': cheer,
                'G3-Commit': commit,
                'G4-Communal': communal,
                'G5-Compassion': compassion,
                'G6-Connect': connect,
                'G7-Considerate': considerate,
                'G8-Cooperat': cooperate,
                'G9-Depend': depend,
                'H1-Emotiona': emotiona,
                'H2-Empath': empath,
                'H3-Feminine': feminine,
                'H4-Flatterable': flatterable,
                'H5-Gentle': gentle,
                'H6-Honest': honest,
                'H7-Interpersonal': interpersonal,
                'H8-Interdependen': interdependen,
                'H9-Interpersona': interpersona,
                'I1-Kind': kind,
                'I2-Kinship': kinship,
                'I3-Loyal': loyal,
                'I4-Modesty': modesty,
                'I5-Nag': nag,
                'I6-Nurtur': nurtur,
                'I7-Pleasant': pleasant,
                'I8-Polite': polite,
                'I9-Quiet': quiet,
                'J1-Respon': respon,
                'J2-Sensitiv': sensitiv,
                'J3-Submissive': submissive,
                'J4-Support': support,
                'J5-Sympath': sympath,
                'J6-Tender': tender,
                'J7-Together': together,
                'J8-Trust': trust,
                'J9-Understand': understand,
                'K1-Warm': warm,
                'K2-Whin': whin,
                'K3-Yield': yiel,

                #femextras - for spreadsheet
                'K4-She': she, 
                'K5-Her': her,
                'K7-Hers': hers,

                #TEXTIO WORDS
                # 'K5-Inclusive': inclusive,
                # 'K6-Collaborat': collaborat,
                # 'K7-Contribut': contribute,
                # 'K8-Diplomacy': diplomacy,
                # 'K9-Passion': passion,
                # 'L0-Creat': creat,
                # 'L1-Wed Like': wedlike,
                # 'L2-Success Start': successstart,
                # 'L3-TellaStory': tellastory,
                # 'L4-Foster': foster,
                # 'L5-Progressive': progressive,
                # 'L6-Balancing': balancing,
                # 'L7-Family': family,
                # 'L8-Transparent': transparent,
                # 'L9-Strong Relation': strongrel,
                # 'M0-Comfortable': comfort,
                # 'M1-Team': team,
                # 'M2-Encourag': encourage,
                # 'M3-Embrace': embrace,
                # 'M4-Beautiful': beautiful,
                # 'M5-Care': care,
                # 'M6-Partner': partner,
                # 'M7-WithOthers': withothers,
                # 'M8-PartOf': partof,
                # 'M9-Imagine': imagine,
                # 'N0-Teach': teach,
                # 'N1-Strive': strive,
                # 'N2-Nourish': nourish,
                # 'N3-Come Join': comejoin,
                # 'N4-Openness': openness,
                # 'N5-Welcome': welcome,
                # 'N6-Meaning': meaning,

                }, 
                ignore_index=True)
    
        except IndexError:
 #            output_string = "/Users/stacy/Desktop/scraper/Data/"+inputdate+jobfield+".csv"
 #            df.to_csv(output_string, encoding="utf-8")

            # write new file
            #  output_string = "/Users/stacy/Desktop/scraper/Summer2017Data/summerdata"+jobfield+"2.csv"
            #  df.to_csv(output_string, encoding="utf-8")

            # append existing file 
             output_string = "/Users/stacy/Desktop/scraper/Spring2018/spring2018"+jobfield+".csv"
             df.to_csv(output_string, mode = 'a', header = False, encoding="utf-8")
             print "end of job advertisements"
             
             raise

df

# output_string = "/Users/stacy/Desktop/scraper/Summer2017Data/summerdata"+jobfield+"2.csv"
# output_string = "/Users/stacy/Desktop/scraper/Data/fulldata.csv"

#append existing file
output_string = "/Users/stacy/Desktop/scraper/Spring2018/spring2018"+jobfield+".csv"
df.to_csv(output_string, mode = 'a', header = False, encoding="utf-8")

#write new file
# output_string = "/Users/stacy/Desktop/scraper/Summer2017Data/summerdata"+jobfield+"2.csv"
# df.to_csv(output_string, encoding="utf-8")
