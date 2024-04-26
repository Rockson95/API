from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

# Defining the Pydantic Model
class Race(BaseModel):
    year: int
    winner: str
    country: str

app = FastAPI()
#  Read Data from Excel
def read_race_data(file_path: str):
    data = pd.read_excel(file_path, header=None, names=["year", "winner", "country"])
    return data

# Create Endpoints
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Tour de France API"}

@app.get("/races/")
async def read_races():
    # Implement CRUD Operations (Read)
    races_data = read_race_data('data/tour_de_france.xlsx')
    races = races_data.to_dict(orient='records')
    return races

@app.get("/races/{year}")
async def read_race(year: int):
    # Step 4: Implement CRUD Operations (Read)
    races_data = read_race_data('data/tour_de_france.xlsx')
    race = races_data.to_dict(orient='records')
    if not race:
        raise HTTPException(status_code=404, detail="Race not found")
    return race[0]


@app.post("/races/")
async def create_race(race: Race):
    # Step 4: Implement CRUD Operations (Create)
    races_data = read_race_data('data/tour_de_france.xlsx')
    new_race = pd.DataFrame([race.dict()])
    races_data = races_data.append(new_race, ignore_index=True)
    races_data.to_excel('data/tour_de_france.xlsx', index=False)
    return race.dict()

@app.put("/races/{year}")
async def update_race(year: int, race: Race):
    # Step 4: Implement CRUD Operations (Update)
    races_data = read_race_data('data/tour_de_france.xlsx')
    race_index = races_data[races_data['year'] == year].index
    if race_index.empty:
        raise HTTPException(status_code=404, detail="Race not found")
    races_data.loc[race_index, ['winner', 'country']] = race.winner, race.country
    races_data.to_excel('data/tour_de_france.xlsx', index=False)
    return {"message": "Race updated successfully"}


@app.delete("/races/{year}")
async def delete_race(year: int):
    # Step 4: Implement CRUD Operations (Delete)
    races_data = read_race_data('data/tour_de_france.xlsx')
    race_index = races_data.index
    if race_index.empty:
        raise HTTPException(status_code=404, detail="Race not found")
    races_data.drop(race_index, inplace=True)
    races_data.to_excel('data/tour_de_france.xlsx', index=False)
    return {"message": "Race deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
