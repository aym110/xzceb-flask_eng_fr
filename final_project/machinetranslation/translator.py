from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('iio9tY6vKhbMLOgkgUd_Q8Id0tyiF7nK-FUYX6pM5Pjz')
language_translator = LanguageTranslatorV3(
    version='2021-04-01',
    authenticator=authenticator
)
language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/1b8d2aa0-d628-4791-867b-d984675bd1be')

def english_to_french(english_text):
    """
    Translates English text to French.
    """
    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr'  # Translation from English to French
    ).get_result()
    french_text = translation['translations'][0]['translation']
    return french_text


def french_to_english(french_text):
    """
    Translates French text to English.
    """
    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en'  # Translation from French to English
    ).get_result()
    english_text = translation['translations'][0]['translation']
    return english_text


if __name__ == '__main__':
    pass