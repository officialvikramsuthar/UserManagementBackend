from celery import shared_task
from .models import User


@shared_task
def send_email(user_id):
    try:
        user = User.objects.get(id=user_id)
        subject = 'Welcome to User Management'
        message = f'Hi {user.username},\n\nWelcome to User Management. Thank you for registering!'
        from_email = 'your_email@example.com'  # Update with your email
        recipient_list = [user.email]

        # send_mail(subject, message, from_email, recipient_list)
        print(f"Email sent successfully to {user.email}")

    except User.DoesNotExist:
        print(f"User with id {user_id} does not exist.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")
