from datetime import timedelta, date
import numpy as np

def daterange(start_date, end_date):
  for n in range(int ((end_date - start_date).days)):
    yield start_date + timedelta(n)

# Read from csv file from John Hopkins repo.
def GetCSVData(csvfile_name, countryname, iname, iinfect, idead):
  ifile = open(csvfile_name, "r")
  #print("Name of the file: ", ifile.name)
  lines = ifile.readlines()
  Ninfected = 0
  Ndead = 0
  for line in lines: 
    words = line.split(',')
    if countryname==words[iname]:
      Ninfected += int(words[iinfect])
      Ndead += int(words[idead])
  ifile.close()
  return Ninfected, Ndead

# Define one country data and operations
class countryData:
  def __init__(self, countrynames, population):
    self.countrynames = countrynames
    self.population = population
    self.data = {}
  def AddDay(self, isodate, Ninfected, Ndead):
    datum = date.fromisoformat(isodate)
    self.data.update({datum : {'date' : datum, 'Ninfected' : Ninfected, 'Ndead' : Ndead}})
  def AddDayFromCSV(self, isodate):
    datum = date.fromisoformat(isodate)
    # Covid data are placed in directory:
    csvfile_name = 'COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'+datum.strftime("%m-%d-%Y")+'.csv' 
    csv_position = 1
    Ninfected = 0
    Ndead = 0
    for countryname in self.countrynames:
      # Special case of region of the US.
      if countryname=='California':
        Ninf, Ndea = GetCSVData(csvfile_name, countryname, 0, 3, 4)
        Ninfected += Ninf
        Ndead += Ndea
      # Exception in country name, "Korea, South" is used, braking the ',' split.
      if countryname=='"Korea':
        Ninf, Ndea = GetCSVData(csvfile_name, countryname, 1, 4, 5)
        Ninfected += Ninf
        Ndead += Ndea
      # Standard read: region, country, date, infected(confirmed), dead, recovered, latitude, longitude
      else:
        Ninf, Ndea = GetCSVData(csvfile_name, countryname, 1, 3, 4)
        Ninfected += Ninf
        Ndead += Ndea
    self.AddDay(isodate, Ninfected, Ndead)
  def GetDatesInfectedDead(self):
    dates = self.data.keys()
    infected = [self.data[datum]['Ninfected'] for datum in dates]
    dead = [self.data[datum]['Ndead'] for datum in dates]
    return dates, infected, dead 

# Create a list of countries to store Covid19 data about.
WorldCountries = {}
# Add country name/s and population.
WorldCountries.update({'Czechia' : countryData(['Czech Republic', 'Czechia'], 10.65e6)})
# The population corresonds to Hubei province containing 95% of dead in China.
WorldCountries.update({'China-Hubei' : countryData(['China', 'Mainland China'], 58.5e6)}) 
WorldCountries.update({'South Korea' : countryData(['South Korea','"Korea'], 51.47e6)})
WorldCountries.update({'US' : countryData(['US'], 327.2e6)})
WorldCountries.update({'Italy' : countryData(['Italy'], 60.48e6)})
WorldCountries.update({'Spain' : countryData(['Spain'], 46.66e6)})
WorldCountries.update({'California' : countryData(['California'], 39.56e6)})
WorldCountries.update({'France' : countryData(['France'], 66.99e6)})
WorldCountries.update({'Germany' : countryData(['Germany'], 82.79e6)})
WorldCountries.update({'UK' : countryData(['UK', 'United Kingdom'], 66.44e6)})
WorldCountries.update({'Russia' : countryData(['Russia'], 144.5e6)})

countries = ['Czechia', 'China-Hubei', 'Italy', 'Spain', 'France', 'US']
#countries = ['Czechia', 'Spain', 'California']
# Fill the data on one-day-basis
#start_date = date(2020, 3, 12)
#end_date = date(2020, 3, 23)
start_date = date(2020, 2, 1)
end_date = date.today()#date(2020, 3, 22)
for country in countries:
  for single_date in daterange(start_date, end_date):
    #print(single_date.isoformat()) 
    WorldCountries[country].AddDayFromCSV(single_date.isoformat())

# PLOT DATA
import matplotlib.pyplot as plt
from matplotlib.dates import (WEEKLY, DateFormatter,
                              rrulewrapper, RRuleLocator)

fig, ax = plt.subplots()
plt.title('Dead patients (per 1 million people)')
rule = rrulewrapper(WEEKLY)#, interval=5)
loc = RRuleLocator(rule)
ax.xaxis.set_major_locator(loc)
formatter = DateFormatter('%m/%d/%y')
ax.xaxis.set_major_formatter(formatter)
# Loop over the list of countries.
for country in countries:
  dates, infected, dead = WorldCountries[country].GetDatesInfectedDead()
  plt.plot_date(dates, np.array(dead) / float(WorldCountries[country].population) * 1e6, label=country)
plt.legend()

fig, ax = plt.subplots()
plt.title('Infected patients (per 1 million people)')
rule = rrulewrapper(WEEKLY)#, interval=5)
loc = RRuleLocator(rule)
ax.xaxis.set_major_locator(loc)
formatter = DateFormatter('%m/%d/%y')
ax.xaxis.set_major_formatter(formatter)
# Loop over the list of countries.
for country in countries:
  dates, infected, dead = WorldCountries[country].GetDatesInfectedDead()
  plt.plot_date(dates, np.array(infected) / float(WorldCountries[country].population) * 1e6, label=country)
plt.legend()

plt.show()
