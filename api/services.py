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
    pokemon.pokedex_number = pokemon.pokedex_number
    pokemon.name = pokemon.name
    pokemon.german_name = pokemon.german_name
    pokemon.japanese_name = pokemon.japanese_name
    pokemon.generation = pokemon.generation
    pokemon.status = pokemon.status
    pokemon.species = pokemon.species
    pokemon.type_number = pokemon.type_number
    pokemon.type_1 = pokemon.type_1
    pokemon.type_2 = pokemon.type_2
    pokemon.height_m = pokemon.height_m
    pokemon.weight_kg = pokemon.weight_kg
    pokemon.abilities_number = pokemon.abilities_number
    pokemon.ability_1 = pokemon.ability_1
    pokemon.ability_2 = pokemon.ability_2
    pokemon.ability_hidden = pokemon.ability_hidden
    pokemon.pokemon.total_points = pokemon.pokemon.total_points
    pokemon.hp = pokemon.hp
    pokemon.attack = pokemon.attack
    pokemon.defense = pokemon.defense
    pokemon.sp_attack = pokemon.sp_attack
    pokemon.sp_defense = pokemon.sp_defense
    pokemon.speed = pokemon.speed
    pokemon.catch_rate = pokemon.catch_rate
    pokemon.base_friendship = pokemon.base_friendship
    pokemon.base_experience = pokemon.base_experience
    pokemon.growth_rate = pokemon.growth_rate
    pokemon.egg_type_number = pokemon.egg_type_number
    pokemon.egg_type_1 = pokemon.egg_type_1
    pokemon.egg_type_2 = pokemon.egg_type_2
    pokemon.percentage_male = pokemon.percentage_male
    pokemon.egg_cycles = pokemon.egg_cycles
    pokemon.against_normal = pokemon.against_normal
    pokemon.against_fire = pokemon.against_fire
    pokemon.against_water = pokemon.against_water
    pokemon.against_electric = pokemon.against_electric
    pokemon.against_grass = pokemon.against_grass
    pokemon.against_ice = pokemon.against_ice
    pokemon.against_fight = pokemon.against_fight
    pokemon.against_poison = pokemon.against_poison
    pokemon.against_ground = pokemon.against_ground
    pokemon.against_flying = pokemon.against_flying
    pokemon.against_psychic = pokemon.against_psychic
    pokemon.against_bug = pokemon.against_bug
    pokemon.against_rock = pokemon.against_rock
    pokemon.against_ghost = pokemon.against_ghost
    pokemon.against_dragon = pokemon.against_dragon
    pokemon.against_dark = pokemon.against_dark
    pokemon.against_steel = pokemon.against_steel
    pokemon.against_fairy = pokemon.against_fairy

    db.commit()
    db.refresh(pokemon)

    return _schemas.Pokemon.from_orm(pokemon)
