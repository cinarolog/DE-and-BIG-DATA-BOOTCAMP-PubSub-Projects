from google.cloud import pubsub_v1
import pandas as pd
import json
import os
import time

# CSV dosyasını pandas kullanarak okuma
df = pd.read_csv("churn.csv")

# Google Cloud kimlik bilgilerini belirleme

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "analog-pilot.json"

proje_id = "analog-pilot-402809"
topic_name = "demayis"

# Pub/Sub PublisherClient oluşturma
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(proje_id,topic_name)

# Her bir satırı işleyerek Pub/Sub topic'e gönderme

for _, row in df.iterrows():
    if row.isnull().any():
        # Skip the row if it contains any missing values
        continue

    time.sleep(1)
    message = row.to_dict()

    for key, value in message.items():
        if isinstance(value, float):
            if key != "Acres":
                message[key] = int(value)

    json_veri = str(message)
    print(type(json_veri))
    
    json_veri = json_veri.replace("'", '"')
    print(json_veri)
    publisher.publish(topic_path, json_veri.encode("utf-8"))


# avro yapısı
    

"""
{
  "type": "record",
  "name": "Home",
  "fields": [
    {
      "name": "Sell",
      "type": "int"
    },
    {
      "name": "List",
      "type": "int"
    },
    {
      "name": "Living",
      "type": "int"
    },
    {
      "name": "Rooms",
      "type": "int"
    },
    {
      "name": "Beds",
      "type": "int"
    },
    {
      "name": "Baths",
      "type": "int"
    },
    {
      "name": "Age",
      "type": "int"
    },
    {
      "name": "Acres",
      "type": "float"
    },
    {
      "name": "Taxes",
      "type": "int"
    }
  ]
}


"""

# BigQuery
"""
CREATE TABLE `db.my_table`
(
  Sell INT64,
  List INT64,
  Living INT64,
  Rooms INT64,
  Beds INT64,
  Baths INT64,
  Age INT64,
  Acres FLOAT64,
  Taxes INT64
)

"""