import csv

rows=[]

with open("c131/new.csv","r") as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        rows.append(row)

headers=rows[0]
planet_data_rows=rows[1:]
print(headers)
print(planet_data_rows[0])

headers[0]="planet number"
solar_sytem_planet_count={}

for planet_data in planet_data_rows:
    if solar_sytem_planet_count.get(planet_data[11]):
        solar_sytem_planet_count[planet_data[11]]+=1
    else:solar_sytem_planet_count[planet_data[11]]=1

max_solar_sytem_planet_count=max(solar_sytem_planet_count,key=solar_sytem_planet_count.get)

print("Solar system {} has maximum planets {} out of all the planets we have discovered so far.".format(max_solar_sytem_planet_count,solar_sytem_planet_count[max_solar_sytem_planet_count]))

temp_planet_data_rows=list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    planet_mass=planet_data[3]
    if planet_mass.lower() == "unknown":
        planet_data_rows.remove(planet_data)
        continue
    else: 
        planet_mass_value=planet_mass.split(" ")[0]
        planet_mass_ref=planet_mass.split(" ")[1]
        if planet_mass_ref=="Jupiters":
            planet_mass_value=float(planet_mass_value)*317.8 
        planet_data[3]=planet_mass_value
    planet_radius=planet_data[7]
    if planet_radius.lower()=="unknown":
        planet_data_rows.remove(planet_data)
        continue
    else: 
        planet_radius_value=planet_radius.split(" ")[0]
        planet_radius_ref=planet_radius.split(" ")[2]
        if planet_radius_ref=="Jupiters":
            planet_radius_value=float(planet_radius_value)*11.2
        planet_data[7]=planet_radius_value

print(len(planet_data_rows))

hd_10180_planets=[]

for planet_data in planet_data_rows:
  if max_solar_sytem_planet_count==planet_data[11]:
    hd_10180_planets.append(planet_data)

print(len(hd_10180_planets))
print(hd_10180_planets)

import plotly.express as px
hd_10180_planet_masses = []
hd_10180_planet_names = []

for planet_data in hd_10180_planets: 
  hd_10180_planet_masses.append(planet_data[3]) 
  hd_10180_planet_names.append(planet_data[1]) 

hd_10180_planet_masses.append(1) 
hd_10180_planet_names.append("Earth") 

# fig = px.bar(x=hd_10180_planet_names, y=hd_10180_planet_masses) 
# fig.show()

temp_planet_data_rows=list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    if planet_data[1].lower=="hd 100526 b":
        planet_data_rows.remove(planet_data)

planet_masses=[]
planet_radiuses=[]
planet_names=[]

for planet_data in planet_data_rows:
    planet_masses.append(planet_data[3])
    planet_radiuses.append(planet_data[7])
    planet_names.append(planet_data[1])

planet_gravity=[]

for index,name in enumerate(planet_names):
    gravity=(float(planet_masses[index])*5.972e+24)/(float(planet_radiuses[index]))*(float(planet_radiuses[index])*6371000)*6.674e-1
    planet_gravity.append(gravity)

# print(planet_gravity)

# fig=px.scatter(x=planet_radiuses,y=planet_masses,size=planet_gravity)
# fig.show()

low_gravity_planet=[]

for index,gravity in enumerate(planet_gravity):
    if gravity<10000:
        # print("index:",planet_data_rows[index])
        low_gravity_planet.append(planet_data_rows[index])

print("gravity",len(low_gravity_planet))

for index,gravity in enumerate(planet_gravity):
    if gravity<100:
        low_gravity_planet.append(planet_data_rows[index])

print(len(low_gravity_planet))