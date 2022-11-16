"""Notify when it is someone's birthday.
"""

import pandas as pd
import yaml
import azure.functions as func

from datetime import date, datetime

from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailRecipients, EmailMessage


def read_config(config_path) -> dict:
    with open(config_path, "r") as stream:
        config = yaml.safe_load(stream)
    
    return config

def read_birthday_data(file_path: str) -> pd.DataFrame:
    """Read birthday data from file."""

    return pd.read_csv(file_path, sep=";")

def parse_date_col(
    df: pd.DataFrame, 
    date_col: str="birthday", 
    date_format: str="%d-%m-%Y"
) -> pd.DataFrame:
    """Parse date column into the right format. We cannot implement
    this is with the parse_date parameter in the pd.read_csv function as
    by this some formats will be inferred as %m-%d-%Y."""
    
    df[date_col] = df[date_col].apply(pd.to_datetime, format=date_format)
    
    return df

def get_email_body(df: pd.DataFrame) -> str:
    """Create the email body."""

    today = pd.Timestamp(date.today())

    body = "<p>Hi,</p><p>Todays birthdays are:</p><p><ul>"
    
    for _, row in df.iterrows():
        if row["birthday"] == today:
            body += "<li>" + row["name"] + "</li>"

    body = body + "</ul></p><p>Don't forget to send a birthday message!</p>"

    return body



def send_email(
    connection_string: str, 
    body: str,
    sender: str,
    recipient: str="lars.van.asseldonk@hotmail.com",
) -> None:
    """Send an email to get notified of today's birthdays."""

    # Create the EmailClient object that you use to send Email messages.
    email_client = EmailClient.from_connection_string(connection_string)

    content = EmailContent(
        subject="Todays birthdays",
        html=body,
    )

    address = EmailAddress(email=recipient)
    recipient = EmailRecipients(to=[address])

    message = EmailMessage(
        sender=sender,
        content=content,
        recipients=recipient
    )

    response = email_client.send(message)

def main(dayTrigger: func.TimerRequest) -> None:

    # Load config
    config = read_config("config/config.yaml")

    # Load and preprocess data
    df = (
        read_birthday_data(file_path=config["data_path"])
        .pipe(parse_date_col)
    )
    
    # Create body based on todays birthdays
    body = get_email_body(df)

    # Send email
    send_email(
        connection_string=config["azure"]["connection_string"], 
        body=body,
        sender=config["azure"]["email_from"],
    )

main()


