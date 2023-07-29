# STATUS CODE VERIFICATION
def verify_http_code(response_data, expected_data):
    assert response_data.status_code == int(expected_data), "Expected HTTP Status:" + expected_data


# ANY KEY SHOULD NOT BE NULL OR EMPTY
def verify_key(response_data, key):
    assert key != 0, "Key is non empty" + key
    assert key > 0, "key should be greater than zero" + key
