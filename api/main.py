from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import schemas as _schemas
import sqlalchemy.orm as _orm
import services as _services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = _fastapi.FastAPI()


@app.post("/api/pokemon/", response_model=_schemas.Pokemon)
async def create_pokemon(pokemon: _schemas.CreatePokemon, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.create_pokemon(pokemon=pokemon, db=db)


@app.get("/api/pokemon/", response_model=List[_schemas.Pokemon])
async def get_pokemons(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_pokemons(db=db)


@app.get("/api/pokemon/{pokemon_id}", response_model=_schemas.Pokemon)
async def get_pokemon(pokemon_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    pokemon = await _services.get_pokemon(db=db, pokemon_id=pokemon_id)
    if pokemon is None:
        raise _fastapi.HTTPException(status_code=404, detail="Pokemon does not exist")

    return pokemon


@app.delete("/api/pokemon/{pokemon_id}/")
async def delete_pokemon(pokemon_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    pokemon = await _services.get_pokemon(db=db, pokemon_id=pokemon_id)
    if pokemon is None:
        raise _fastapi.HTTPException(status_code=404, detail="pokemon does not exist")
    await _services.delete_pokemon(pokemon, db=db)
    return "Successfuly deleted " + pokemon.name


@app.put("/api/pokemon/{pokemon_id}/", response_model=_schemas.Pokemon)
async def update_pokemon(
        pokemon_id: int,
        pokemon_data: _schemas.CreatePokemon,
        db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    pokemon = await _services.get_contact(db=db, pokemon_id=pokemon_id)
    if pokemon is None:
        raise _fastapi.HTTPException(status_code=404, detail="Pokemon does not exist")

    return await _services.update_pokemon(
        pokemon_data=pokemon_data, pokemon=pokemon, db=db
    )
