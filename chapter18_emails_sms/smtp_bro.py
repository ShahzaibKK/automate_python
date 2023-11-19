import smtplib

try:
    smtp_obj = smtplib.SMTP("smtp.gmail.com", 587, timeout=5)
    print(type(smtp_obj))
    print(smtp_obj.ehlo())
    # print(smtp_obj.starttls())

except Exception as e:
    print(f"An error occurred: {e}")
