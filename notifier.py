from plyer import notification

title = 'Hello amazing people'
message = 'Thank you for reading Take care'

notification.notify(title=title,
                    message=message,
                    app_icon=None,
                    timeout=5,
                    toast=False)
                    