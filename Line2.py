from utils import Station,Line

bybus2 = Line(0,"BB2")
bybus2.lineName="Bybus 2"

vdb = Station(0,"VDB")
vdb.upcode='A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@'
vdb.downcode='A=1@O=Væddeløbsbanen (Skydebanevej / Aalborg)@X=9881159@Y=57054184@U=86@L=851007301@B=1@p=1739892283@'

ett = Station(0,"ETT")
ett.upcode="A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935795@Y=57038228@U=86@L=851008902@"
ett.downcode="A=1@O=Eternitten (Bornholmsgade / Aalborg)@X=9935624@Y=57038174@U=86@L=851008901@"
ett.name="Eternitten (Bornholmsgade / Aalborg)"
ett.upname = "AAU Bus"
ett.upname2 = "Aalborg Universitets"
ett.downname = "Vædd"
