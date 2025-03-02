from utils import Station,Line

bybus2 = Line(0,"BB2")
bybus2.lineName="Bybus 2"

vdb = Station(0,"VDB")
vdb.upcode='A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@'
vdb.downcode='A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@'

vfw = Station(0,"VFW")
vfw.downcode="A=1@O=Vestre Fjordvej (Kastetvej / Aalborg)@X=9893411@Y=57055622@U=86@L=851102202@B=1@p=1740743877@"
vfw.upcode = "A=1@O=Vestre Fjordvej (Kastetvej / Aalborg)@X=9893330@Y=57055775@U=86@L=851102201@B=1@p=1740743877@"

hld = Station(0,"HLD")
hld.downcode = "A=1@O=Haraldslund (Kastetvej / Aalborg)@X=9899416@Y=57054472@U=86@L=851203302@B=1@p=1740743877@"
hld.upcode = "A=1@O=Haraldslund (Kastetvej / Aalborg)@X=9899146@Y=57054660@U=86@L=851203301@B=1@p=1740743877@"

avs = Station(0,"AVS")
avs.downcode = "A=1@O=Aalborg Vestby St. (Kastetvej / Aalborg Vestby St)@X=9908603@Y=57052665@U=86@L=851121902@B=1@p=1740743877@"
avs.upcode = "A=1@O=Aalborg Vestby St. (Kastetvej / Aalborg Vestby St)@X=9907461@Y=57052934@U=86@L=851121901@B=1@p=1740743877@"

jag = Station(0,"JAG")
jag.downcode = "A=1@O=Jomfru Ane Gade (Borgergade / Aalborg)@X=9918212@Y=57050957@U=86@L=851002402@B=1@p=1740743877@"
jag.upcode = "A=1@O=Jomfru Ane Gade (Borgergade / Aalborg)@X=9918967@Y=57050957@U=86@L=851002401@B=1@p=1740743877@"

nyt = Station(0,"NYT")
nyt.downcode = "A=1@O=Nytorv (Østeraagade / Aalborg)@X=9921412@Y=57048638@U=86@L=851801201@B=1@p=1740743877@"
nyt.upcode = "A=1@O=Nytorv (Østeraagade / Aalborg)@X=9921592@Y=57048593@U=86@L=851801204@B=1@p=1740743877@"

aas = Station(0,"AAS")

ett = Station(0,"ETT")
ett.upcode="A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935795@Y=57038228@U=86@L=851008902@"
ett.downcode="A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935624@Y=57038174@U=86@L=851008901@"
ett.name="Eternitten (Bornholmsgade / Aalborg)"
ett.upname = "AAU Bus"
ett.upname2 = "Aalborg Universitets"
ett.downname = "Vædd"
