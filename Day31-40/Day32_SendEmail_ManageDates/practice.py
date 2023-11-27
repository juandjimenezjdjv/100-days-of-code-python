import smtplib
import datetime as dt
import random

MY_EMAIL = "examplejd@mail.com"
my_password = "i am not using any password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, my_password)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}"
                            )
        

#--------------------------------------------------------------------------------------------#
# import smtplib
# my_email = "examplejd@mail.com"
# password = "i am not using any password"
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="emailtosendhappybirthday@gmail.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")
#--------------------------------------------------------------------------------------------#
# import datetime as dt
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_week = now.weekday()
# date_of_birthday = dt.datetime(year=2001, month=4, day=5, hour=14)
# print(date_of_birthday)
#--------------------------------------------------------------------------------------------#
