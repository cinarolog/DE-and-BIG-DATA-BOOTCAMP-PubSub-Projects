from google.cloud import pubsub_v1
import os

# Google Cloud kimlik bilgilerini belirleme
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "analog-pilot.json"

# Google Cloud proje ID'si ve topic adı
proje_id = "analog-pilot-402809"
topic_name = "demayis"

# Gönderilecek mesaj
msg = "Pubsub Çalışması test"

# Pub/Sub PublisherClient oluşturma
publisher = pubsub_v1.PublisherClient()

# Pub/Sub topic adresini oluşturma
topic_adres = publisher.topic_path(proje_id, topic_name)

# Mesajı Pub/Sub topic'e gönderme
send = publisher.publish(topic_adres, data=msg.encode("utf-8"))

# Mesajın ID'sini yazdırma
print(f"Mesaj ID'si: {send.result()}")