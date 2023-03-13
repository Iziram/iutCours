import requests
BASE_URL = "https://fakestoreapi.com"
new_product = {
	"title": "test",
	"description": "desc",
	"image":"https://exammple.com/img",
	"price": 12.58,
	"category":'electronic'
}
response = requests.put(f"{BASE_URL}/products/5", json=new_product)
print(response.status_code)
print(response.json())

