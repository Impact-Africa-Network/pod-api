from typing import List, Tuple
from celery import shared_task
from ian_utilities.notifications import notification_util

@shared_task
def notify_mail(subject: str, body: str, sender_name: str, recipients: List, template_name: str) -> Tuple: 
   successful, data = notification_util.send_email(subject=subject, body=body, recipients=recipients, template_name=template_name, sender_name=sender_name)
   return (successful, data)