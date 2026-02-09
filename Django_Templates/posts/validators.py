from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# def bad_language_validator(value: str) -> None:
#     bad_words = {'suka', 'nahui', 'blyat'}
#
#     if bad_words.intersection(value.split()):
#         raise ValidationError(f'The word "{value}" is not allowed.')


@deconstructible
class BadLanguageValidator:
    def __init__(self, message: str) -> None:
        self.message = message

    def __call__(self, value: str) -> None:
        bad_words = {'suka', 'nahui', 'blyat'}

        if bad_words.intersection(value.split()):
            raise ValidationError(self.message)