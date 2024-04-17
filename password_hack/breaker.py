#! python3
# breaker.py - Brute-Force PDF Password Breaker
# Usage  - # searches for the correct password for a pdf file from a dictionary of words

import PyPDF2


def crack_password(file_path: str, passwords: list):
    pdf_reader = PyPDF2.PdfReader(file_path)
    hacked_password = None
    for password in passwords:
        result_lower = pdf_reader.decrypt(password.lower())
        result_upper = pdf_reader.decrypt(password.upper())
        if result_lower:
            hacked_password = password.lower()
            break
        elif result_upper:
            hacked_password = password.upper()
            break

    return hacked_password


def get_password_list(dictionary_path):
    word_list = []
    with open(dictionary_path, 'r') as f:
        for line in f.readlines():
            word_list.append(line.strip())
    return word_list


if __name__ == "__main__":
    file_p = 'encrypted.pdf'
    dictionary_p = 'dictionary.txt'
    password_list = get_password_list(dictionary_p)
    correct_password = crack_password(file_p, password_list)
    if correct_password:
        print(f'The hacked password is: {correct_password}.')
    else:
        print('Password not found')
