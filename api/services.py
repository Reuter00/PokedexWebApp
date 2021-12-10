from typing import TYPE_CHECKING, List
import database as _database
import models as _models
import schemas as _schemas

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_pokemon(pokemon: _schemas.CreatePokemon, db: "Session") -> _schemas.Pokemon:
    pokemon = _models.Pkmnlist(**pokemon.dict())
    db.add(pokemon)
    db.commit()
    db.refresh(pokemon)
    return _schemas.Pokemon.from_orm(pokemon)


async def get_all_pokemons(db: "Session") -> List[_schemas.Pokemon]:
    pokemons = db.query(_models.Pkmnlist).all()
    return list(map(_schemas.Pokemon.from_orm, pokemons))


async def get_pokemon(pokemon_id: int, db: "Session"):
    pokemon = db.query(_models.Pkmnlist).filter(_models.Pkmnlist.pokedex_number == pokemon_id).first()
    return pokemon


async def delete_pokemon(pokemon: _models.Pkmnlist, db: "Session"):
    db.delete(pokemon)
    db.commit()


async def update_pokemon(
        pokemon_data: _schemas.CreatePokemon, pokemon: _models.Pkmnlist, db: "Session"
) -> _schemas.Pokemon:
    pokemon.pokedex_number = pokemon_data.pokedex_number
    pokemon.name = pokemon_data.name
    pokemon.german_name = pokemon_data.german_name
    pokemon.japanese_name = pokemon_data.japanese_name
    pokemon.generation = pokemon_data.generation
    pokemon.status = pokemon_data.status
    pokemon.species = pokemon_data.species
    pokemon.type_number = pokemon_data.type_number
    pokemon.type_1 = pokemon_data.type_1
    pokemon.type_2 = pokemon_data.type_2
    pokemon.height_m = pokemon_data.height_m
    pokemon.weight_kg = pokemon_data.weight_kg
    pokemon.abilities_number = pokemon_data.abilities_number
    pokemon.ability_1 = pokemon_data.ability_1
    pokemon.ability_2 = pokemon_data.ability_2
    pokemon.ability_hidden = pokemon_data.ability_hidden
    pokemon.total_points = pokemon_data.total_points
    pokemon.hp = pokemon_data.hp
    pokemon.attack = pokemon_data.attack
    pokemon.defense = pokemon_data.defense
    pokemon.sp_attack = pokemon_data.sp_attack
    pokemon.sp_defense = pokemon_data.sp_defense
    pokemon.speed = pokemon_data.speed
    pokemon.catch_rate = pokemon_data.catch_rate
    pokemon.base_friendship = pokemon_data.base_friendship
    pokemon.base_experience = pokemon_data.base_experience
    pokemon.growth_rate = pokemon_data.growth_rate
    pokemon.egg_type_number = pokemon_data.egg_type_number
    pokemon.egg_type_1 = pokemon_data.egg_type_1
    pokemon.egg_type_2 = pokemon_data.egg_type_2
    pokemon.percentage_male = pokemon_data.percentage_male
    pokemon.egg_cycles = pokemon_data.egg_cycles
    pokemon.against_normal = pokemon_data.against_normal
    pokemon.against_fire = pokemon_data.against_fire
    pokemon.against_water = pokemon_data.against_water
    pokemon.against_electric = pokemon_data.against_electric
    pokemon.against_grass = pokemon_data.against_grass
    pokemon.against_ice = pokemon_data.against_ice
    pokemon.against_fight = pokemon_data.against_fight
    pokemon.against_poison = pokemon_data.against_poison
    pokemon.against_ground = pokemon_data.against_ground
    pokemon.against_flying = pokemon_data.against_flying
    pokemon.against_psychic = pokemon_data.against_psychic
    pokemon.against_bug = pokemon_data.against_bug
    pokemon.against_rock = pokemon_data.against_rock
    pokemon.against_ghost = pokemon_data.against_ghost
    pokemon.against_dragon = pokemon_data.against_dragon
    pokemon.against_dark = pokemon_data.against_dark
    pokemon.against_steel = pokemon_data.against_steel
    pokemon.against_fairy = pokemon_data.against_fairy

    db.commit()
    db.refresh(pokemon)

    return _schemas.Pokemon.from_orm(pokemon)
