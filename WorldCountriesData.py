from datetime import date
import numpy as np

# Define one country data and operations
class countryData:
  def __init__(self, name, population, isostartdate):
    self.name = name
    self.population = population
    # The first day when more than 100 infected.
    self.startdate = date.fromisoformat(isostartdate)
    self.data = {}
  def AddDay(self, isodate, Ninfected, Ndead):
    self.data.update({isodate : {'date' : date.fromisoformat(isodate), 'Ninfected' : Ninfected, 'Ndead' : Ndead}})

# Create a list of countries to store Covid19 data about.
WorldCountries = {}
# Add country name, population, and first day with more than 100 infected.
WorldCountries.update({'China' : countryData('China', 1000e6, '2019-12-31')})
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
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 1689, 35)
WorldCountries['Spain'].AddDay(isodate, 45, 0)
WorldCountries['Czechia'].AddDay(isodate, 3, 0)
WorldCountries['France'].AddDay(isodate, 100, 2)
WorldCountries['Germany'].AddDay(isodate, 129, 0)
WorldCountries['UK'].AddDay(isodate, 36, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-03'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-04'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-05'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-06'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-07'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-08'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-09'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-10'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-11'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-12'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-13'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-14'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-15'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-16'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-17'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-18'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-19'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

isodate = '2020-03-20'
WorldCountries['China'].AddDay(isodate, 0, 0)
WorldCountries['USA'].AddDay(isodate, 0, 0)
WorldCountries['Italy'].AddDay(isodate, 0, 0)
WorldCountries['Spain'].AddDay(isodate, 0, 0)
WorldCountries['Czechia'].AddDay(isodate, 0, 0)
WorldCountries['France'].AddDay(isodate, 0, 0)
WorldCountries['Germany'].AddDay(isodate, 0, 0)
WorldCountries['UK'].AddDay(isodate, 0, 0)
WorldCountries['Russia'].AddDay(isodate, 0, 0)

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

countries = ['China', 'USA', 'Spain', 'Czechia', 'California']
for country in countries:
  print("country, date, Ndead, Ninfected:", country, WorldCountries[country].data[isodate]['date'], WorldCountries[country].data[isodate]['Ndead'], WorldCountries[country].data[isodate]['Ninfected'])
