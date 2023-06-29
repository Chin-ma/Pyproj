from plyer import notification

title = 'Hello amazing people'
message = 'Thank you for reading! Take care.'

# Set the path to your custom icon file
# icon_path = '/path/to/your/icon.png'

notification.notify(title=title,message=message,timeout=5,toast=True)