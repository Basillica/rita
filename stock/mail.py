from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient
from prettytable import PrettyTable

message = []
CHOICE = "sp500"  # "yahoo_fin", "sp500", "crypto

def send_mail(receiver: str, data=message) -> None:
    if len(data) <= 0:
        print('There are no stocks to watch at the moment!')
        return

    t = PrettyTable(
        ['Stock', f"Old Price for portfolio {CHOICE}", "New Price"])
    for i in range(len(data)):
        t.add_row([data[i][0], data[i][2], data[i][1]])
    print(t)

    message = Mail(
        from_email='ezeabasilianthony@gmail.com',
        to_emails=receiver,
        subject='Stock Update!',
        plain_text_content=str(t))
    try:
        sg = SendGridAPIClient(
            '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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print('Email sent succesfully!')
    except Exception as e:
        print(e)