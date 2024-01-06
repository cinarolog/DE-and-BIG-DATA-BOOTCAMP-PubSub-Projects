import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

# Google Cloud hesap kimlik bilgilerini belirtme
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'analog-pilot.json'

# Apache Beam PipelineOptions ayarlarını belirleme
pipeline_options = {
    "runner": 'DirectRunner',  # Lokalde çalıştırılacağı için DirectRunner kullanıyoruz.
    "project": 'analog-pilot-402809',
    "job_name": 'read-csv-to-console'
}

# Apache Beam PipelineOptions'ı oluşturma
options = PipelineOptions.from_dictionary(pipeline_options)

# Apache Beam Pipeline oluşturma
p = beam.Pipeline(options=options)

# CSV dosyasını okuma
csv_lines = (
    p | 'Read CSV' >> beam.io.ReadFromText('gs://graduation-de/churn.csv')
)

# Her bir satırı işlemek için bir fonksiyon
def process_element(element):
    # Unicode BOM karakterini kaldır
    element = element.lstrip('\ufeff')
    
    columns = element.split(',')
    
    # Eğer satır boşsa veya sütun sayısı beklenenden azsa, satırı atla
    if not columns or len(columns) < 16:
        return None
    
    try:
        # Her bir satırı bir sözlük formatına çevirme
        return {
            'year': int(columns[0]),
            'customer_id': int(columns[1]),
            'phone_no': columns[2],
            'gender': columns[3],
            'age': int(columns[4]),
            'no_of_days_subscribed': int(columns[5]),
            'multi_screen': columns[6],
            'mail_subscribed': columns[7],
            'weekly_mins_watched': float(columns[8]),
            'minimum_daily_mins': float(columns[9]),
            'maximum_daily_mins': float(columns[10]),
            'weekly_max_night_mins': int(columns[11]),
            'videos_watched': int(columns[12]),
            'maximum_days_inactive': float(columns[13]) if columns[13] else None,
            'customer_support_calls': int(columns[14]),
            'churn': float(columns[15]),
        }
    except ValueError as e:
        # Değer dönüştürme hatası durumunda None döndür
        return None


# Okunan veriyi işlemek için Map transform'u uygulama
formatted_data = csv_lines | 'Process Data' >> beam.Map(process_element)

# İşlenen veriyi konsola yazdırma
formatted_data | 'Write to Console' >> beam.Map(print)

# Pipeline'ı çalıştırma
p.run()
