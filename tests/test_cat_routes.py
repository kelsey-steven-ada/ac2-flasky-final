
def test_get_cats_optional_query_empty_db_returns_empty_list(client):
    # Act
    response = client.get("/cats")

    # Assert 
    assert response.status_code == 200
    assert response.get_json() == []