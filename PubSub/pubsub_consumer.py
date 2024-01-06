from google.cloud import pubsub_v1
import os

# Google Cloud kimlik bilgilerini belirleme
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "analog-pilot.json"

# Google Cloud proje ID'si ve topic adı
proje_id = "analog-pilot-402809"
topic_name = "demayis"

# Pub/Sub SubscriberClient oluşturma
subscriber = pubsub_v1.SubscriberClient()

# Pub/Sub topic adresini oluşturma
topic_adres = subscriber.topic_path(proje_id, topic_name)

# Mesajları işlemek için callback fonksiyonu
def callback(message):
    print(f"Received message: {message.data}")
    # Mesajı işleme tamamlandı olarak işaretleme
    message.ack()

# Abone olma işlemi
subscription_path = subscriber.subscription_path(proje_id, "my-subscription")
subscriber.create_subscription(name=subscription_path, topic=topic_adres)
print(f"Subscription created: {subscription_path}")

# Mesajları dinleme işlemi
subscriber.subscribe(subscription_path, callback=callback)

# Programın çalışmasını beklemek için giriş yapılmasını bekleyin
print("Listening for messages...")
input("Press any key to exit.")
