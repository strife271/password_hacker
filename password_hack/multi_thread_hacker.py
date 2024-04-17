#! python3
# breaker.py - Brute-Force PDF Password Breaker
# Usage  - # searches for the correct password for a pdf file from a dictionary of words with four threads

import time
import threading
import PyPDF2


def crack_password(file_path: str, passwords: list, start_index, end_index, case, result_container, t):
    """Result container is a workaround to multithreading not having a return value"""

    pdf_reader = PyPDF2.PdfReader(file_path)
    hacked_password = None
    for password in passwords[start_index:end_index]:

        if case:
            p = pdf_reader.decrypt(password.lower())
        else:
            p = pdf_reader.decrypt(password.upper())
        if p:
            if case:
                hacked_password = password.lower()
                break
            else:
                hacked_password = password.upper()
                break

    if hacked_password:
        print(f'The hacked password is: {hacked_password}.')
        end_time = time.time()
        print(f'Elapsed seconds: {end_time - t}')
        result_container.append(hacked_password)


def get_password_list(dictionary_path):
    word_list = []
    with open(dictionary_path, 'r') as f:
        for line in f.readlines():
            word_list.append(line.strip())
    return word_list


if __name__ == "__main__":

    start_time = time.time()

    file_p = 'encrypted.pdf'
    dictionary_p = 'dictionary.txt'
    password_list = get_password_list(dictionary_p)

    # Create and start the Thread objects.
    crack_threads = []  # a list of all the Thread objects
    result = []
    for i in range(1, 5):  # loops 4 times, creates 4 threads
        if i == 1 or i == 3:
            start = 0
            end = int(((len(password_list))/2)+1)
        else:
            start = int((len(password_list))/2)
            end = len(password_list)+1
        if i == 1 or i == 2:
            case_flag = True
        else:
            case_flag = False

        crack_thread = threading.Thread(target=crack_password, args=(file_p, password_list, start, end, case_flag, result, start_time))
        crack_threads.append(crack_thread)
        crack_thread.start()

    # Wait for all threads to end
    for crack_thread in crack_threads:
        crack_thread.join()

    # Use
    # stop_event = threading.Event()
    # When you want to stop all threads
    # stop_event.set()
    #
    #
    print(result)

# No noticeable improve in time to hack
