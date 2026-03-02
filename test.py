from main import dish_fetch

# Test 1: Verifica que dish_fetch devuelve un diccionario
def test_trivia_fetch_returns_dict():
    result = dish_fetch(1)
    assert isinstance(result, dict)

# Test 2: Verifica que el diccionario tiene los campos requeridos
def test_trivia_fetch_has_required_fields():
    result = dish_fetch(1)
    assert "id" in result
    assert "name" in result

# Test 3: Verifica que el id devuelto coincide con el número ingresado
def test_trivia_fetch_correct_id():
    result = dish_fetch(5)
    assert result["id"] == 5

# Test 4: Verifica que el nombre no esté vacío y sea una cadena
def test_trivia_fetch_name_not_empty():
    result = dish_fetch(1)
    assert result["name"]
    assert isinstance(result["name"], str)

# Test 5: Verifica que dish_fetch acepta números más grandes
def test_trivia_fetch_accepts_numbers():
    result = dish_fetch(15)
    assert result is not None