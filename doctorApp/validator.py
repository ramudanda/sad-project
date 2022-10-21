def dated(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    return value