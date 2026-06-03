import re


def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)


def validate_name(name):

    return len(name.strip()) > 0


def validate_glucose(glucose):

    return 50 <= glucose <= 300


def validate_haemoglobin(haemoglobin):

    return 5 <= haemoglobin <= 20


def validate_cholesterol(cholesterol):

    return 100 <= cholesterol <= 400