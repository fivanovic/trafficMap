from utils import Station,Line

bybus2 = Line(0,"BB2")
bybus2.lineName="Bybus 2"

vdb = Station(0,"VDB")
vdb.upcode='A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@'
vdb.downcode='A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@'
vdb.name="Væddeløbsbanen (Skydebanevej / Aalborg)"
vdb.upname = "AAU Bus"
vdb.upname2 = "Aalborg Universitets"
vdb.downname = "Vædd"
vdb.topEndFlag = 1


vfw = Station(1,"VFW")
vfw.downcode="A=1@O=Vestre Fjordvej (Kastetvej / Aalborg)@X=9893411@Y=57055622@U=86@L=851102202@B=1@p=1740743877@"
vfw.upcode = "A=1@O=Vestre Fjordvej (Kastetvej / Aalborg)@X=9893330@Y=57055775@U=86@L=851102201@B=1@p=1740743877@"
vfw.name="Vestre Fjordvej (Kastetvej / Aalborg)"
vfw.upname = "AAU Bus"
vfw.upname2 = "Aalborg Universitets"
vfw.downname = "Vædd"


hld = Station(2,"HLD")
hld.downcode = "A=1@O=Haraldslund (Kastetvej / Aalborg)@X=9899416@Y=57054472@U=86@L=851203302@B=1@p=1740743877@"
hld.upcode = "A=1@O=Haraldslund (Kastetvej / Aalborg)@X=9899146@Y=57054660@U=86@L=851203301@B=1@p=1740743877@"
hld.name="Haraldslund (Kastetvej / Aalborg)"
hld.upname = "AAU Bus"
hld.upname2 = "Aalborg Universitets"
hld.downname = "Vædd"


avs = Station(3,"AVS")
avs.downcode = "A=1@O=Aalborg Vestby St. (Kastetvej / Aalborg Vestby St)@X=9908603@Y=57052665@U=86@L=851121902@B=1@p=1740743877@"
avs.upcode = "A=1@O=Aalborg Vestby St. (Kastetvej / Aalborg Vestby St)@X=9907461@Y=57052934@U=86@L=851121901@B=1@p=1740743877@"
avs.name="Aalborg Vestby St. (Kastetvej / Aalborg Vestby St)"
avs.upname = "AAU Bus"
avs.upname2 = "Aalborg Universitets"
avs.downname = "Vædd"


jag = Station(4,"JAG")
jag.downcode = "A=1@O=Jomfru Ane Gade (Borgergade / Aalborg)@X=9918212@Y=57050957@U=86@L=851002402@B=1@p=1740743877@"
jag.upcode = "A=1@O=Jomfru Ane Gade (Borgergade / Aalborg)@X=9918967@Y=57050957@U=86@L=851002401@B=1@p=1740743877@"
jag.name="Jomfru Ane Gade (Borgergade / Aalborg)"
jag.upname = "AAU Bus"
jag.upname2 = "Aalborg Universitets"
jag.downname = "Vædd"


nyt = Station(5,"NYT")
nyt.downcode = "A=1@O=Nytorv (Østeraagade / Aalborg)@X=9921412@Y=57048638@U=86@L=851801201@B=1@p=1740743877@"
nyt.upcode = "A=1@O=Nytorv (Østeraagade / Aalborg)@X=9921592@Y=57048593@U=86@L=851801204@B=1@p=1740743877@"
nyt.name="Nytorv (Østeraagade / Aalborg)"
nyt.upname = "AAU Bus"
nyt.upname2 = "Aalborg Universitets"
nyt.downname = "Vædd"


aas = Station(6,"AAS")
aas.downcode = "A=1@O=Aalborg St. (Område A / John F. Kennedys Plads)@X=9918329@Y=57043172@U=86@L=851002705@B=1@p=1741264077@"
aas.upcode = "A=1@O=Aalborg St. (Område A / John F. Kennedys Plads)@X=9918428@Y=57043163@U=86@L=851002706@B=1@p=1741264077@"
aas.name="Aalborg St. (Område A / John F. Kennedys Plads)"
aas.upname = "AAU Bus"
aas.upname2 = "Aalborg Universitets"
aas.downname = "Vædd"


jlg = Station(7,"JLG")
jlg.downcode = "A=1@O=Jyllandsgade (Aalborg Kommune)@X=9926293@Y=57042471@U=86@L=851012201@B=1@p=1741264077@"
jlg.upcode = "A=1@O=Jyllandsgade (Aalborg Kommune)@X=9926087@Y=57042480@U=86@L=851012202@B=1@p=1741264077@"
jlg.name="Jyllandsgade (Aalborg Kommune)"
jlg.upname = "AAU Bus"
jlg.upname2 = "Aalborg Universitets"
jlg.downname = "Vædd"


kld = Station(8,"KLD")
kld.downcode = "A=1@O=Karolinelund (Bornholmsgade / Aalborg)@X=9934006@Y=57041905@U=86@L=851210401@B=1@p=1741264077@"
kld.upcode = "A=1@O=Karolinelund (Bornholmsgade / Aalborg)@X=9934195@Y=57042282@U=86@L=851210402@B=1@p=1741264077@"
kld.name="Karolinelund (Bornholmsgade / Aalborg)"
kld.upname = "AAU Bus"
kld.upname2 = "Aalborg Universitets"
kld.downname = "Vædd"


ett = Station(9,"ETT")
ett.upcode="A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935795@Y=57038228@U=86@L=851008902@"
ett.downcode="A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935624@Y=57038174@U=86@L=851008901@"
ett.name="Eternitten (Bornholmsgade / Aalborg)"
ett.upname = "AAU Bus"
ett.upname2 = "Aalborg Universitets"
ett.downname = "Vædd"

sgp = Station(10,"SGP")
sgp.downcode = "A=1@O=Sohngårdsholmsparken (Sohngårdsholmsvej / Aalborg)@X=9943139@Y=57032322@U=86@L=851108201@B=1@p=1741264077@"
sgp.upcode = "A=1@O=Sohngårdsholmsparken (Sohngårdsholmsvej / Aalborg)@X=9942699@Y=57033104@U=86@L=851108204@B=1@p=1741264077@"
sgp.name="Sohngårdsholmsparken (Sohngårdsholmsvej / Aalborg)"
sgp.upname = "AAU Bus"
sgp.upname2 = "Aalborg Universitets"
sgp.downname = "Vædd"


dal = Station(11,"DAL")
dal.downcode = "A=1@O=Danalien (Sohngårdsholmsvej / Aalborg)@X=9944344@Y=57029050@U=86@L=851009201@B=1@p=1741264077@"
dal.upcode = "A=1@O=Danalien (Sohngårdsholmsvej / Aalborg)@X=9944443@Y=57029742@U=86@L=851009202@B=1@p=1741264077@"
dal.name="Danalien (Sohngårdsholmsvej / Aalborg)"
dal.upname = "AAU Bus"
dal.upname2 = "Aalborg Universitets"
dal.downname = "Vædd"


glt = Station(12,"GLT")
glt.downcode = "A=1@O=Grønlands Torv (Universitetsboulevarden / Aalborg)@X=9943103@Y=57023845@U=86@L=851017601@B=1@p=1741264077@"
glt.upcode = "A=1@O=Grønlands Torv (Universitetsboulevarden / Aalborg)@X=9943256@Y=57023935@U=86@L=851017602@B=1@p=1741264077@"
glt.name="Grønlands Torv (Universitetsboulevarden / Aalborg)"
glt.upname = "AAU Bus"
glt.upname2 = "Aalborg Universitets"
glt.downname = "Vædd"


sbs = Station(13,"SBS")
sbs.downcode = "A=1@O=Scoresbysundvej (Universitetsboulevarden/Aalborg)@X=9952749@Y=57020852@U=86@L=851009301@B=1@p=1741264077@"
sbs.upcode = "A=1@O=Scoresbysundvej (Universitetsboulevarden/Aalborg)@X=9951409@Y=57021400@U=86@L=851009302@B=1@p=1741264077@"
sbs.name="Scoresbysundvej (Universitetsboulevarden/Aalborg)"
sbs.upname = "AAU Bus"
sbs.upname2 = "Aalborg Universitets"
sbs.downname = "Vædd"


plp = Station(14,"PLP")
plp.downcode = "A=1@O=Pendlerpladsen (Bertil Ohlins Vej / Aalborg)@X=9956785@Y=57018461@U=86@L=851991401@B=1@p=1741264077"
plp.upcode = "A=1@O=Pendlerpladsen (Bertil Ohlins Vej / Aalborg)@X=9956839@Y=57018551@U=86@L=851991402@B=1@p=1741264077@"
plp.name="Pendlerpladsen (Bertil Ohlins Vej / Aalborg"
plp.upname = "AAU Bus"
plp.upname2 = "Aalborg Universitets"
plp.downname = "Vædd"


gnt = Station(15,"GNT")
gnt.downcode = "A=1@O=Gigantium (Bertil Ohlins Vej / Aalborg)@X=9962448@Y=57016969@U=86@L=851991301@B=1@p=1741264077@"
gnt.upcode = "A=1@O=Gigantium (Bertil Ohlins Vej / Aalborg)@X=9962187@Y=57017094@U=86@L=851991302@B=1@p=1741264077@"
gnt.name="Gigantium (Bertil Ohlins Vej / Aalborg)"
gnt.upname = "AAU Bus"
gnt.upname2 = "Aalborg Universitets"
gnt.downname = "Vædd"


ptp = Station(16,"PTP")
ptp.downcode = "A=1@O=Pontoppidanstræde (Bertil Ohlins Vej / Aalborg)@X=9971779@Y=57015476@U=86@L=851991202@B=1@p=1741264077@"
ptp.upcode = "A=1@O=Pontoppidanstræde (Bertil Ohlins Vej / Aalborg)@X=9971716@Y=57015387@U=86@L=851991201@B=1@p=1741264077@"
ptp.name="Pontoppidanstræde (Bertil Ohlins Vej / Aalborg)"
ptp.upname = "AAU Bus"
ptp.upname2 = "Aalborg Universitets"
ptp.downname = "Vædd"


fib = Station(17,"FIB")
fib.downcode = "A=1@O=AAU Fibigerstræde (Bertil Ohlins Vej / Aalborg)@X=9976121@Y=57015324@U=86@L=851991501@B=1@p=1741264077@"
fib.upcode = "A=1@O=AAU Fibigerstræde (Bertil Ohlins Vej / Aalborg)@X=9975941@Y=57015351@U=86@L=851991502@B=1@p=1741264077@"
fib.name="AAU Fibigerstræde (Bertil Ohlins Vej / Aalborg)"
fib.upname = "AAU Bus"
fib.upname2 = "Aalborg Universitets"
fib.downname = "Vædd"


frb = Station(18,"FRB")
frb.downcode = "A=1@O=AAU Fr.Bajers Vej (Bertil Ohlins Vej / Aalborg)@X=9983986@Y=57014829@U=86@L=851991601@B=1@p=1741264077@"
frb.upcode = "A=1@O=AAU Fr.Bajers Vej (Bertil Ohlins Vej / Aalborg)@X=9983851@Y=57014919@U=86@L=851991602@B=1@p=1741264077@"
frb.name="AAU Fr. Bajers Vej (Bertil Ohlins Vej / Aalborg)"
frb.upname = "AAU Bus"
frb.upname2 = "Aalborg Universitets"
frb.downname = "Vædd"


aau = Station(19,"AAU")
aau.downcode = "A=1@O=AAU Busterminal (Sigrid Undsetsvej / Aalborg)@X=9990944@Y=57016375@U=86@L=851000305@B=1@p=1741264077@"
aau.upcode = "A=1@O=AAU Busterminal (Sigrid Undsetsvej / Aalborg)@X=9991330@Y=57016232@U=86@L=851000306@B=1@p=1741264077@"
aau.name="AAU Busterminal (Sigrid Undsetsvej / Aalborg)"
aau.upname = "AAU Bus"
aau.upname2 = "Aalborg Universitets"
aau.downname = "Vædd"
aau.bottomEndFlag = 1






