
"""Derive your custom exception class from Python built in exception class or from more specific exception classes like ValueError or KeyError
You can use inheritance to define logically grouped exceptions 5 hierarchies"""

# Self documenting NameTooShortError exception type that extends the built-in ValueError class

class NameShortError(ValueError):
    pass

def validate(name):
    if len(name)<10:
        raise NameShortError(name)

#validate('arjun')

#--------------------------------------------------
class BaseValidationError(ValueError):
    pass

class NameTooShortError(BaseValidationError):
    pass

class NameTooLongError(BaseValidationError):
    pass

class NameTooCuteError(BaseValidationError):
    pass

def validate_new(name):
    try:
        validate(name)
    except BaseValidationError as err:
        handle_validation_error(err)

validate_new('Meena')


