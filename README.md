# parse-ingredients
Parse strings of ingredients to their name, unit, quantity and optional comments.

## To install
```
pip install parse-ingredients
```

## To use
```python
from recipe_searchers import search_recipe

result = search_recipe("12 ounces lean ground beef, preferably 85 percent lean")
print(f"Found results: \n {result}")
```
```search_recipe()``` returns an object in the form of:


```json
{
    "name": "lean ground beef",
    "quantity": 12,
    "unit": "oz",
    "comment": "preferably 85 percent lean",
    "original_string": "12 ounces lean ground beef, preferably 85 percent lean"
}
```