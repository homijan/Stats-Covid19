from datetime import timedelta, date
import numpy as np

def daterange(start_date, end_date):
  for n in range(int ((end_date - start_date).days)):
    yield start_date + timedelta(n)

def GetCSVData(csvfile_name, country):
  ifile = open(csvfile_name, "r")
  #print("Name of the file: ", ifile.name)
  lines = ifile.readlines()
  Ninfected = 0
  Ndead = 0
  for line in lines:
    words = line.split(',')
    if country in words[1]:
      Ninfected += int(words[3])
      Ndead += int(words[4])
  ifile.close()
  return Ninfected, Ndead

# Define one country data and operations
class countryData:
  def __init__(self, name, population, isostartdate):
    self.name = name
    self.population = population
    # The first day when more than 100 infected.
    self.startdate = date.fromisoformat(isostartdate)
    self.data = {}
  def AddDay(self, isodate, Ninfected, Ndead):
    datum = date.fromisoformat(isodate)
    self.data.update({datum : {'date' : datum, 'Ninfected' : Ninfected, 'Ndead' : Ndead}})
  def AddDayFromCSV(self, isodate):
    datum = date.fromisoformat(isodate)
    # Covid data are placed in directory:
    csvfile_name = 'COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'+datum.strftime("%m-%d-%Y")+'.csv' 
    Ninfected, Ndead = GetCSVData(csvfile_name, self.name)
    self.AddDay(isodate, Ninfected, Ndead)
  def GetDatesInfectedDead(self):
    dates = self.data.keys()
    infected = [self.data[datum]['Ninfected'] for datum in dates]
    dead = [self.data[datum]['Ndead'] for datum in dates]
    return dates, infected, dead 

# Create a list of countries to store Covid19 data about.
WorldCountries = {}
# Add country name, population, and first day with more than 100 infected.
WorldCountries.update({'China' : countryData('China', 60e6, '2019-12-31')}) # The population corresonds to Hubei province containing 95% of dead in China.
WorldCountries.update({'USA' : countryData('USA', 300e6, '2020-03-07')})
WorldCountries.update({'Italy' : countryData('Italy', 60e6, '2020-02-25')})
WorldCountries.update({'Spain' : countryData('Spain', 40e6, '2020-03-04')})
WorldCountries.update({'Czechia' : countryData('Czechia', 10e6, '2020-03-13')})
WorldCountries.update({'California' : countryData('California', 30e6, '2020-03-14')})
WorldCountries.update({'France' : countryData('France', 80e6, '2020-03-02')})
WorldCountries.update({'Germany' : countryData('Germany', 80e6, '2020-03-01')})
WorldCountries.update({'UK' : countryData('UK', 50e6, '2020-03-06')})
WorldCountries.update({'Russia' : countryData('Russia', 200e6, '2020-03-07')})

# Fill the data on one-day-basis
isodate = '2020-03-02'
WorldCountries['China'].AddDay(isodate, 80174, 2915)
WorldCountries['Italy'].AddDay(isodate, 1689, 35)
WorldCountries['Spain'].AddDay(isodate, 45, 0)
WorldCountries['Czechia'].AddDay(isodate, 3, 0)
WorldCountries['France'].AddDay(isodate, 100, 2)
WorldCountries['Germany'].AddDay(isodate, 129, 0)
WorldCountries['UK'].AddDay(isodate, 36, 0)

isodate = '2020-03-03'
WorldCountries['China'].AddDay(isodate, 80304, 2946)
WorldCountries['Italy'].AddDay(isodate, 2036, 52)
WorldCountries['Spain'].AddDay(isodate, 114, 0)
WorldCountries['Czechia'].AddDay(isodate, 3, 0)
WorldCountries['France'].AddDay(isodate, 191, 3)
WorldCountries['Germany'].AddDay(isodate, 157, 0)
WorldCountries['UK'].AddDay(isodate, 39, 0)

isodate = '2020-03-04'
WorldCountries['China'].AddDay(isodate, 80422, 2984)
WorldCountries['Italy'].AddDay(isodate, 2502, 80)
WorldCountries['Spain'].AddDay(isodate, 159, 0)
WorldCountries['Czechia'].AddDay(isodate, 5, 0)
WorldCountries['France'].AddDay(isodate, 212, 4)
WorldCountries['Germany'].AddDay(isodate, 196, 0)
WorldCountries['UK'].AddDay(isodate, 51, 0)

isodate = '2020-03-05'
WorldCountries['China'].AddDay(isodate, 80565, 3015)
WorldCountries['Italy'].AddDay(isodate, 3089, 107)
WorldCountries['Spain'].AddDay(isodate, 198, 1)
WorldCountries['Czechia'].AddDay(isodate, 5, 0)
WorldCountries['France'].AddDay(isodate, 282, 4)
WorldCountries['Germany'].AddDay(isodate, 262, 0)
WorldCountries['UK'].AddDay(isodate, 89, 0)

isodate = '2020-03-06'
WorldCountries['China'].AddDay(isodate, 80711, 3045)
WorldCountries['Italy'].AddDay(isodate, 3858, 148)
WorldCountries['Spain'].AddDay(isodate, 257, 3)
WorldCountries['Czechia'].AddDay(isodate, 12, 0)
WorldCountries['France'].AddDay(isodate, 420, 0)
WorldCountries['Germany'].AddDay(isodate, 534, 0)
WorldCountries['UK'].AddDay(isodate, 118, 0)

isodate = '2020-03-07'
WorldCountries['China'].AddDay(isodate, 80813, 3073)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 4636, 197)
WorldCountries['Spain'].AddDay(isodate, 374, 5)
WorldCountries['Czechia'].AddDay(isodate, 26, 0)
WorldCountries['France'].AddDay(isodate, 613, 0)
WorldCountries['Germany'].AddDay(isodate, 639, 0)
WorldCountries['UK'].AddDay(isodate, 167, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-08'
WorldCountries['China'].AddDay(isodate, 80859, 3100)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 5883, 234)
WorldCountries['Spain'].AddDay(isodate, 430, 5)
WorldCountries['Czechia'].AddDay(isodate, 32, 0)
WorldCountries['France'].AddDay(isodate, 706, 10)
WorldCountries['Germany'].AddDay(isodate, 795, 0)
WorldCountries['UK'].AddDay(isodate, 210, 2)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-09'
WorldCountries['China'].AddDay(isodate, 80904, 3123)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 7375, 366)
WorldCountries['Spain'].AddDay(isodate, 589, 10)
WorldCountries['Czechia'].AddDay(isodate, 32, 0)
WorldCountries['France'].AddDay(isodate, 1116, 19)
WorldCountries['Germany'].AddDay(isodate, 1112, 0)
WorldCountries['UK'].AddDay(isodate, 277, 2)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-10'
WorldCountries['China'].AddDay(isodate, 80924, 3140)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 9172, 463)
WorldCountries['Spain'].AddDay(isodate, 1024, 28)
WorldCountries['Czechia'].AddDay(isodate, 38, 0)
WorldCountries['France'].AddDay(isodate, 1402, 30)
WorldCountries['Germany'].AddDay(isodate, 1139, 2)
WorldCountries['UK'].AddDay(isodate, 323, 3)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-11'
WorldCountries['China'].AddDay(isodate, 80935, 3162)
WorldCountries['USA'].AddDay(isodate, 696, 25)
WorldCountries['Italy'].AddDay(isodate, 10149, 631)
WorldCountries['Spain'].AddDay(isodate, 1636, 36)
WorldCountries['Czechia'].AddDay(isodate, 61, 0)
WorldCountries['France'].AddDay(isodate, 1774, 33)
WorldCountries['Germany'].AddDay(isodate, 1296, 2)
WorldCountries['UK'].AddDay(isodate, 373, 6)
WorldCountries['Russia'].AddDay(isodate, 7, 0)

isodate = '2020-03-12'
WorldCountries['China'].AddDay(isodate, 80981, 3173)
WorldCountries['USA'].AddDay(isodate, 987, 29)
WorldCountries['Italy'].AddDay(isodate, 12462, 827)
WorldCountries['Spain'].AddDay(isodate, 2140, 48)
WorldCountries['Czechia'].AddDay(isodate, 94, 0)
WorldCountries['France'].AddDay(isodate, 2269, 48)
WorldCountries['Germany'].AddDay(isodate, 1567, 3)
WorldCountries['UK'].AddDay(isodate, 460, 7)
WorldCountries['Russia'].AddDay(isodate, 20, 0)

isodate = '2020-03-13'
WorldCountries['China'].AddDay(isodate, 80991, 3180)
WorldCountries['USA'].AddDay(isodate, 1264, 36)
WorldCountries['Italy'].AddDay(isodate, 15113, 1016)
WorldCountries['Spain'].AddDay(isodate, 2965, 84)
WorldCountries['Czechia'].AddDay(isodate, 116, 0)
WorldCountries['France'].AddDay(isodate, 2860, 61)
WorldCountries['Germany'].AddDay(isodate, 2369, 6)
WorldCountries['UK'].AddDay(isodate, 594, 8)
WorldCountries['Russia'].AddDay(isodate, 34, 0)

isodate = '2020-03-14'
WorldCountries['China'].AddDay(isodate, 81021, 3194)
WorldCountries['USA'].AddDay(isodate, 1678, 41)
WorldCountries['Italy'].AddDay(isodate, 17660, 1268)
WorldCountries['Spain'].AddDay(isodate, 4231, 120)
WorldCountries['Czechia'].AddDay(isodate, 150, 0)
WorldCountries['France'].AddDay(isodate, 3640, 79)
WorldCountries['Germany'].AddDay(isodate, 3062, 6)
WorldCountries['UK'].AddDay(isodate, 802, 10)
WorldCountries['Russia'].AddDay(isodate, 34, 0)

isodate = '2020-03-15'
WorldCountries['China'].AddDay(isodate, 81048, 3204)
WorldCountries['USA'].AddDay(isodate, 1678, 41)
WorldCountries['Italy'].AddDay(isodate, 21157, 1441)
WorldCountries['Spain'].AddDay(isodate, 5753, 136)
WorldCountries['Czechia'].AddDay(isodate, 214, 0)
WorldCountries['France'].AddDay(isodate, 4469, 91)
WorldCountries['Germany'].AddDay(isodate, 3795, 8)
WorldCountries['UK'].AddDay(isodate, 1144, 21)
WorldCountries['Russia'].AddDay(isodate, 34, 0)

isodate = '2020-03-16'
WorldCountries['China'].AddDay(isodate, 81077, 3218)
WorldCountries['USA'].AddDay(isodate, 4168, 74)
WorldCountries['Italy'].AddDay(isodate, 24747, 1809)
WorldCountries['Spain'].AddDay(isodate, 7753, 288)
WorldCountries['Czechia'].AddDay(isodate, 298, 0)
WorldCountries['France'].AddDay(isodate, 5380, 127)
WorldCountries['Germany'].AddDay(isodate, 4818, 12)
WorldCountries['UK'].AddDay(isodate, 1395, 35)
WorldCountries['Russia'].AddDay(isodate, 63, 0)

isodate = '2020-03-17'
WorldCountries['China'].AddDay(isodate, 81049, np.nan)
WorldCountries['USA'].AddDay(isodate, 4661, 93)
WorldCountries['Italy'].AddDay(isodate, 27980, 2158)
WorldCountries['Spain'].AddDay(isodate, 9942, 342)
WorldCountries['Czechia'].AddDay(isodate, 344, 0)
WorldCountries['France'].AddDay(isodate, 6650, 148)
WorldCountries['Germany'].AddDay(isodate, 7272, 17)
WorldCountries['UK'].AddDay(isodate, 1553, 55)
WorldCountries['Russia'].AddDay(isodate, 114, np.nan)

isodate = '2020-03-18'
WorldCountries['China'].AddDay(isodate, 81058, np.nan)
WorldCountries['USA'].AddDay(isodate, 6233, np.nan)
WorldCountries['Italy'].AddDay(isodate, 31506, 2503)
WorldCountries['Spain'].AddDay(isodate, 11748, 533)
WorldCountries['Czechia'].AddDay(isodate, 396, 0)
WorldCountries['France'].AddDay(isodate, 7658, 148)
WorldCountries['Germany'].AddDay(isodate, 9257, 24)
WorldCountries['UK'].AddDay(isodate, 1906, 55)
WorldCountries['Russia'].AddDay(isodate, 114, np.nan)

isodate = '2020-03-19'
WorldCountries['China'].AddDay(isodate, 81102, np.nan)
WorldCountries['USA'].AddDay(isodate, 7769, np.nan)
WorldCountries['Italy'].AddDay(isodate, 35713, 2978)
WorldCountries['Spain'].AddDay(isodate, 13910, 623)
WorldCountries['Czechia'].AddDay(isodate, 464, 0)
WorldCountries['France'].AddDay(isodate, 9052, 148)
WorldCountries['Germany'].AddDay(isodate, 12327, 28)
WorldCountries['UK'].AddDay(isodate, 2642, 71)
WorldCountries['Russia'].AddDay(isodate, 147, np.nan)

isodate = '2020-03-20'
WorldCountries['China'].AddDay(isodate, 81199, np.nan)
WorldCountries['USA'].AddDay(isodate, 14250, np.nan)
WorldCountries['Italy'].AddDay(isodate, 41035, 3405)
WorldCountries['Spain'].AddDay(isodate, 18897, 833)
WorldCountries['Czechia'].AddDay(isodate, 694, 0)
WorldCountries['France'].AddDay(isodate, 11010, 372)
WorldCountries['Germany'].AddDay(isodate, 15320, 44)
WorldCountries['UK'].AddDay(isodate, np.nan, 137)
WorldCountries['Russia'].AddDay(isodate, 199, np.nan)

isodate = '2020-03-21'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-22'
WorldCountries['China'].AddDay(isodate, 81397, 3265)
WorldCountries['USA'].AddDay(isodate, 33276, 417)
WorldCountries['Italy'].AddDay(isodate, 59138, 5476)
WorldCountries['Spain'].AddDay(isodate, 28768, 1772)
WorldCountries['Czechia'].AddDay(isodate, 1047, 1)
WorldCountries['California'].AddDay(isodate, 1642, 30)
WorldCountries['France'].AddDay(isodate, 14485, 674)
WorldCountries['Germany'].AddDay(isodate, 24873, 94)
WorldCountries['UK'].AddDay(isodate, 5741, 282)
WorldCountries['Russia'].AddDay(isodate, 367, 0)

#country = 'US'
#csvfile_name = 'COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/03-22-2020.csv'
#Ninfected, Ndead = GetCSVData(csvfile_name, country)
#print(Ninfected, Ndead)


countries = ['China', 'Italy', 'Spain', 'France', 'Czechia']

start_date = date(2020, 3, 1)
end_date = date(2020, 3, 22)
for country in countries:
  for single_date in daterange(start_date, end_date):
    #print(single_date.isoformat()) 
    WorldCountries[country].AddDayFromCSV(single_date.isoformat())

# PLOT DATA
import matplotlib.pyplot as plt
from matplotlib.dates import (WEEKLY, DateFormatter,
                              rrulewrapper, RRuleLocator)

fig, ax = plt.subplots()
plt.title('Dead per 10 millions of poplation')
rule = rrulewrapper(WEEKLY)#, interval=5)
loc = RRuleLocator(rule)
ax.xaxis.set_major_locator(loc)
formatter = DateFormatter('%m/%d/%y')
ax.xaxis.set_major_formatter(formatter)
# Loop over the list of countries.
for country in countries:
  dates, infected, dead = WorldCountries[country].GetDatesInfectedDead()
  plt.plot_date(dates, np.array(dead) / WorldCountries[country].population * 10e6, label=country)

plt.legend()

plt.show()

#datum = date.fromisoformat(isodate)
#for country in countries:
#  print("country, date, Ndead, Ninfected:", country, WorldCountries[country].data[datum]['date'], WorldCountries[country].data[datum]['Ndead'], WorldCountries[country].data[datum]['Ninfected'])
