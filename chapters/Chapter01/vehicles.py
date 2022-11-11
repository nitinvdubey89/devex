import click
import requests

@click.group()
def cars():
    pass

@cars.command()
@click.argument("makes")
def searchmakes(makes):
    r = requests.get("https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json")
    all_makes = [i['Make_Name'] for i in r.json()['Results'] if makes.upper() in i['Make_Name']]
    for c in all_makes:
        print(c)

@cars.command()
@click.argument("make")
@click.option("--year", type=click.IntRange(1986, 2022))
def listmodels(make, year):
    if year:
        r = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeYear/make/{make}/modelyear/{year}?format=json")
        all_models = [i['Model_Name'] for i in r.json()['Results']]
    else:
        r = requests.get(f"https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json")
        all_models = [i['Model_Name'] for i in r.json()['Results']]
    for c in all_models:
        print(c)

if __name__ == "__main__":
    cars()