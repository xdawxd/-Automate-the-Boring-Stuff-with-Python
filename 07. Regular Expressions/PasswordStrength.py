# PasswordStrength.py - Program that checks your password strength.


def strongPass(password):
    """
    This is a function that tests your password strength.
    0-1 conditions met --> weak
    2-3 conditions met --> strong

    Conditions:
    - At least 8 characters long
    - It contains both lower and upper case letters
    - Contains at least one number
    """
    import re

    def password_len():
        psw_len_re = re.search(r'.{8}', password)
        if psw_len_re:
            return True  # more or equal to 8 chars (strong).
        else:
            return False  # less than 8 chars (weak).

    def letter_case():
        letter_upp, letter_low = re.search(r'[A-Z]+', password), \
                                 re.search(r'[a-z]+', password)
        if letter_upp and letter_low:
            return True  # at least one upper or lower case letter (strong).
        else:
            return False  # no upper or lower case letters (weak).

    def number_appearance():
        # option for end/start with a number
        """
        num_st, num_end = re.compile(r'^\d+.*'), re.compile(r'.*\d+$')
        mo1, mo2 = num_st.search(password), num_end.search(password)

        if mo1:
            return 'Your password begins with a number.'
        if mo2:
            return 'Your password ends with a number.'
        else:
            return 'Your password does not start nor end with a number.'
        """

        num_re = re.search(r'\d+', password)
        if num_re:
            return True  # contains a number (strong).
        else:
            return False  # no number (weak).

    conditions = [password_len(),
                  letter_case(),
                  number_appearance()]
    pass_strength = 0

    for condition in conditions:
        if condition:
            pass_strength += 1

    weak, strong = [0, 1], [2, 3]

    if pass_strength in weak:
        return 'Your password is too weak.'
    else:
        return 'Your password is strong.'


print(strongPass('zaqwedc123'))
