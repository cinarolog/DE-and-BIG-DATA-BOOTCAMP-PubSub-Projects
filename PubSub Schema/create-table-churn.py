CREATE TABLE kafka.churn (
  year INT64,
  customer_id INT64,
  phone_no STRING,
  gender STRING,
  age INT64,
  no_of_days_subscribed INT64,
  multi_screen STRING,
  mail_subscribed STRING,
  weekly_mins_watched FLOAT64,
  minimum_daily_mins FLOAT64,
  maximum_daily_mins FLOAT64,
  weekly_max_night_mins INT64,
  videos_watched INT64,
  maximum_days_inactive FLOAT64,
  customer_support_calls INT64,
  churn FLOAT64
);



"""
  # Servis hesabına izinleri eklemek için
bq update-iam-policy \
  --role roles/bigquery.dataEditor \
  --member serviceAccount:service-859364423364@gcp-sa-pubsub.iam.gserviceaccount.com \
  analog-pilot-402809:kafka.churn_schema
"""


"""

  {
  "type": "record",
  "name": "CustomerData",
  "fields": [
    {
      "name": "year",
      "type": "int"
    },
    {
      "name": "customer_id",
      "type": "int"
    },
    {
      "name": "phone_no",
      "type": "string"
    },
    {
      "name": "gender",
      "type": "string"
    },
    {
      "name": "age",
      "type": "int"
    },
    {
      "name": "no_of_days_subscribed",
      "type": "int"
    },
    {
      "name": "multi_screen",
      "type": "string"
    },
    {
      "name": "mail_subscribed",
      "type": "string"
    },
    {
      "name": "weekly_mins_watched",
      "type": "float"
    },
    {
      "name": "minimum_daily_mins",
      "type": "float"
    },
    {
      "name": "maximum_daily_mins",
      "type": "float"
    },
    {
      "name": "weekly_max_night_mins",
      "type": "int"
    },
    {
      "name": "videos_watched",
      "type": "int"
    },
    {
      "name": "maximum_days_inactive",
      "type": "float"
    },
    {
      "name": "customer_support_calls",
      "type": "int"
    },
    {
      "name": "churn",
      "type": "float"
    }
  ]
}


"""