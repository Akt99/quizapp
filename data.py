
import requests as req
parameters={
    "amount":10,
    "type":"boolean"
}
response=req.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data=response.json()
question_data=data["results"]
#print(data["results"])