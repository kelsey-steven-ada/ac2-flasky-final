
def test_get_cats_optional_query_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/cats")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []

def test_get_cats_optional_query_returns_seeded_cat(client, one_cat):
    response = client.get("/cats")

    assert response.status_code == 200
    cat_list = response.get_json()
    assert len(cat_list) == 1
    assert cat_list[0]["id"] == 1
    assert cat_list[0]["name"] == "Zoro"
    assert cat_list[0]["breed"] == "Orange Tabby"
    assert cat_list[0]["color"] ==  "Orange and White"
    assert cat_list[0]["size"] == "Medium"
    assert cat_list[0]["likes_catnip"] == False

def test_get_cat_by_id_returns_seeded_cat(client, one_cat):
    response = client.get(f"/cats/{one_cat.id}")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body["id"] == one_cat.id
    assert response_body["name"] == "Zoro"
    assert response_body["breed"] == "Orange Tabby"
    assert response_body["color"] ==  "Orange and White"
    assert response_body["size"] == "Medium"
    assert response_body["likes_catnip"] == False