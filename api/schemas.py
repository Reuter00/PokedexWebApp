import datetime as _dt
import pydantic as _pydantic
from typing import  Optional


class _BasePokemon(_pydantic.BaseModel):
    pokedex_number: int
    name: str
    german_name: Optional[str] = None
    japanese_name: Optional[str] = None
    generation: int
    status: str
    species: str
    type_number: int
    type_1: str
    type_2: Optional[str] = None
    height_m: Optional[float] = None
    weight_kg: Optional[float] = None
    abilities_number: int
    ability_1: Optional[str] = None
    ability_2: Optional[str] = None
    ability_hidden: Optional[str] = None
    total_points: int
    hp: int
    attack: int
    defense: int
    sp_attack: int
    sp_defense: int
    speed: int
    catch_rate: Optional[int] = None
    base_friendship: Optional[int] = None
    base_experience: Optional[int] = None
    growth_rate: Optional[str] = None
    egg_type_number: Optional[int] = None
    egg_type_1: Optional[str] = None
    egg_type_2: Optional[str] = None
    percentage_male: Optional[float] = None
    egg_cycles: Optional[int] = None
    against_normal: float
    against_fire: float
    against_water: float
    against_electric: float
    against_grass: float
    against_ice: float
    against_fight: float
    against_poison: float
    against_ground: float
    against_flying: float
    against_psychic: float
    against_bug: float
    against_rock: float
    against_ghost: float
    against_dragon: float
    against_dark: float
    against_steel: float
    against_fairy: float


class Pokemon(_BasePokemon):
    id: int


    class Config:
        orm_mode = True



class CreatePokemon(_BasePokemon):
    pass
