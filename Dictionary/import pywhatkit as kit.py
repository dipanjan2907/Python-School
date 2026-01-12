import pywhatkit as kit
import time


def send_whatsapp_message_continuously(phone_number, message, interval_seconds, max_messages):
    """
    Sends a WhatsApp message continuously using pywhatkit.
    """
    try:
        for i in range(max_messages):
            print(f"Sending message {i + 1} to {phone_number}")
            # Send the message immediately
            kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
            print(f"Message {i + 1} sent successfully to {phone_number}")
            
            # Wait before sending the next message
            time.sleep(interval_seconds)
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
if __name__ == "__main__":
    phone = "+918420253634"  # Replace with the recipient's phone number
    msg = "❌"
    interval = 1  # 1 second between messages
    max_msgs = 5  # Send 5 messages

    send_whatsapp_message_continuously(phone, msg, interval, max_msgs)
