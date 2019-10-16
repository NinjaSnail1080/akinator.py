"""
MIT License

Copyright (c) 2019 NinjaSnail1080

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from .exceptions import InvalidAnswerError, InvalidLanguageError, AkiConnectionFailure, AkiTimedOut, AkiNoQuestions, AkiServerDown, AkiTechnicalError


def ans_to_id(ans):
    """Convert an input answer string into an Answer ID for Akinator"""

    ans = ans.lower()
    if ans == "yes" or ans == "y" or ans == "0":
        return "0"
    elif ans == "no" or ans == "n" or ans == "1":
        return "1"
    elif ans == "i" or ans == "idk" or ans == "i dont know" or ans == "i don't know" or ans == "2":
        return "2"
    elif ans == "probably" or ans == "p" or ans == "3":
        return "3"
    elif ans == "probably not" or ans == "pn" or ans == "4":
        return "4"
    else:
        raise InvalidAnswerError("""
        You put "{}", which is an invalid answer.
        The answer must be one of these:
            - "yes" OR "y" OR "0" for YES
            - "no" OR "n" OR "1" for NO
            - "i" OR "idk" OR "i dont know" OR "i don't know" OR "2" for I DON'T KNOW
            - "probably" OR "p" OR "3" for PROBABLY
            - "probably not" OR "pn" OR "4" for PROBABLY NOT
        """.format(ans))


def get_region(lang=None):
    """Returns an Aki server based on what language is input"""

    if isinstance(lang, str):
        lang = lang.lower()
    if lang is None or lang == "en" or lang == "english":
        return "srv13.akinator.com:9196"
    elif lang == "en2":
        return "srv6.akinator.com:9126"
    elif lang == "en3":
        return "srv11.akinator.com:9152"
    elif lang == "ar" or lang == "arabic":
        return "srv2.akinator.com:9155"
    elif lang == "cn" or lang == "chinese":
        return "srv11.akinator.com:9150"
    elif lang == "de" or lang == "german":
        return "srv14.akinator.com:9283"
    elif lang == "es" or lang == "spanish":
        return "srv11.akinator.com:9151"
    elif lang == "fr" or lang == "french":
        return "srv12.akinator.com:9185"
    elif lang == "fr2":
        return "srv3.akinator.com:9217"
    elif lang == "il" or lang == "hebrew":
        return "srv12.akinator.com:9189"
    elif lang == "it" or lang == "italian":
        return "srv9.akinator.com:9214"
    elif lang == "jp" or lang == "japanese":
        return "srv11.akinator.com:9172"
    elif lang == "kr" or lang == "korean":
        return "srv2.akinator.com:9156"
    elif lang == "nl" or lang == "dutch":
        return "srv9.akinator.com:9215"
    elif lang == "pl" or lang == "polish":
        return "srv14.akinator.com:9282"
    elif lang == "pt" or lang == "portuguese":
        return "srv2.akinator.com:9161"
    elif lang == "ru" or lang == "russian":
        raise AkiConnectionFailure("This server is currently not available. The library will be updated when it's working again.")
    elif lang == "tr" or lang == "turkish":
        return "srv3.akinator.com:9211"
    else:
        raise InvalidLanguageError(
            "You put \"{}\", which is an invalid language.".format(lang))


def raise_connection_error(response):
    """Raise the proper error if the API failed to connect"""

    if response == "KO - SERVER DOWN":
        raise AkiServerDown("Akinator's servers are down in this region. Try again later or use a different language")
    elif response == "KO - TECHNICAL ERROR":
        raise AkiTechnicalError("Akinator's servers have had a technical error. Try again later or use a different language")
    elif response == "KO - TIMEOUT":
        raise AkiTimedOut("Your Akinator session has timed out")
    elif response == "WARN - NO QUESTION":
        raise AkiNoQuestions("\"Akinator.step\" reached 80. No more questions")
    else:
        raise AkiConnectionFailure("An unknown error has occured. Server response: {}".format(response))
