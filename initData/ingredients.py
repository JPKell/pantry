from constants import *
from initData.ingredientsData.baking import baking
from initData.ingredientsData.cannedGoods import cannedGoods
from initData.ingredientsData.dairy import dairy
from initData.ingredientsData.dryGoods import dryGoods
from initData.ingredientsData.fresh import fresh
from initData.ingredientsData.fruitAndVeg import fruitAndVeg
from initData.ingredientsData.spice import spice
from initData.ingredientsData.wetGoods import wetGoods
from initData.ingredientsData.greens import greens
from initData.ingredientsData.frozen import frozen

initIngredients = baking.copy()
initIngredients.update(cannedGoods)
initIngredients.update(dairy)
initIngredients.update(dryGoods)
initIngredients.update(fresh)
initIngredients.update(fruitAndVeg)
initIngredients.update(spice)
initIngredients.update(wetGoods)
initIngredients.update(greens)
initIngredients.update(frozen)
