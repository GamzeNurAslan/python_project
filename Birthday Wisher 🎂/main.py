#SMTP => Simple Mail Transfer Protoc
from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "your_mail"
MY_PASSWORD = "your_password"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    try:
        with open(file_path) as letter_file:
             contents = letter_file.read()
             contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
             connection.starttls()
             connection.login(user=MY_EMAIL, password=MY_PASSWORD)
             connection.sendmail(from_addr=MY_EMAIL,
                                 to_addrs=birthday_person["email"],
                                 msg=f"Subject:Mutlu Yıllar 🎉\n\n{contents}"
                            )
             print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")
else:
    print("Bugün doğum günü olan kimse yok.")


