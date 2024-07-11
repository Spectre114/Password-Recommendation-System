import re
import math
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import string
import csv
from dateutil.parser import parse

score = 0


# Password Generation
def generatePassword(row):
    chars = ""
    for value in row:
        if isinstance(value, str):
            chars += "".join(list(value.replace(" ", "").strip()))

    easyPass = []
    moderatePass = []
    hardPass = []

    if "/" in row[3]:
        separator = "/"
    else:
        separator = "-"
    parts = row[3].split(separator)
    day = parts[0]
    month = parts[1]
    year = parts[2]
    age = str(row[2])

    if len(day) == 1:
        day = "0" + day
    if len(month) == 1:
        month = "0" + month
    if len(year) == 2:
        if int(year) > 23:
            year = "19" + year
        else:
            year = "20" + year
    if len(age) == 1:
        age = "0" + age
    num = [
        age,  # age
        day,  # DD of dob
        month,  # MM of dob
        year[0:1],  # first half of YY of dob
        year[2:3],
    ]  # second half of YY of dob

    spl_chr = [
        "!",
        '"',
        "#",
        "$",
        "%",
        "&",
        "'",
        "(",
        ")",
        "*",
        "+",
        ",",
        "-",
        ".",
        ":",
        ";",
        "<",
        "=",
        ">",
        "?",
        "@",
        "[",
        "]",
        "^",
        "_",
        "`",
        "{",
        "|",
        "}",
        "~",
        "/",
    ]

    # Generate easy password
    for i in range(random.randint(1, 4)):
        f_char = row[0][0].lower() + row[0][1].upper() + row[0][2].lower()
        # first three characters of name
        password = random.sample([f_char, random.choice(num), random.choice(num)], 3)
        # join randomly f_char and two numbers from num list
        password = "".join(password)
        easyPass.append(password)

    # Generate moderate password
    for i in range(random.randint(1, 3)):
        f_char = random.sample(
            [row[0][0].lower(), row[1][0].upper(), row[4][0].lower()], 3
        )
        # first characters of name(lower), surname(upper), father_name(lower) in random order
        f_char = f_char[0] + f_char[1] + f_char[2]
        password = random.sample(
            [f_char, random.choice(num), random.choice(num), random.choice(spl_chr)], 4
        )
        # join randomly f_char and two numbers from num list and a speacial char
        password = "".join(password)
        moderatePass.append(password)

    # Generate hard password
    upr_chars = row[0][0] + row[1][0] + row[4][0]
    lwr_chars = row[0][1:] + row[1][1:] + row[4][1:]
    digs = "".join([char for char in chars if char.isdigit()])
    for i in range(random.randint(1, 2)):
        pwd_list = []
        pwd_list = random.sample(upr_chars, 2) + random.sample(lwr_chars, 2)
        pwd_list += random.sample(digs, 2) + random.sample(spl_chr, 2)
        random.shuffle(pwd_list)
        hardPass.append("".join(pwd_list))

    passwords_gen = []
    for i in easyPass:
        passwords_gen.append(i)
    for j in moderatePass:
        passwords_gen.append(j)
    for k in hardPass:
        passwords_gen.append(k)
    return passwords_gen


# Strength Estimation
def check_commanpass(password):
    with open("comman_passwords.txt", "r") as f:
        rd = f.read().splitlines()
        for i in range(len(rd)):
            if rd[i] in password:
                return -4
            else:
                continue
        return 4


def substitute(password):
    substitutions = {
        "0": ["o"],
        "1": ["i", "l"],
        "3": ["e"],
        "4": ["a"],
        "5": ["s"],
        "7": ["t"],
        "8": ["b"],
        "9": ["g", "q"],
    }
    for sub, chars in substitutions.items():
        for char in chars:
            password = password.replace(char, sub)
    return password


def check_cred(password, name, last, father):
    str1 = substitute(password)  # Apply password transformation function
    aux_score = 0

    # Pattern matching for username, name, last name, and father's name
    patterns = [(name.lower(), -2), (last.lower(), -2), (father.lower(), -2)]
    for pattern, weight in patterns:
        if re.search(r"\b{}\b".format(re.escape(pattern)), str1):
            aux_score += weight

    # Pattern matching for different date formats
    date_patterns = [
        r"\b(0?[1-9]|[12][0-9]|3[01])[./-](0?[1-9]|1[012])[./-]\d{4}\b",
        r"\b\d{4}[./-](0?[1-9]|1[012])[./-](0?[1-9]|[12][0-9]|3[01])\b",
        r"\b(0?[1-9]|1[012])[./-](0?[1-9]|[12][0-9]|3[01])[./-]\d{4}\b",
        r"\b(0?[1-9]|[12][0-9]|3[01])(0?[1-9]|1[012])\d{2}\b",
        r"\b\d{2}(0?[1-9]|1[012])(0?[1-9]|[12][0-9]|3[01])\b",
    ]
    date_regex = "|".join(date_patterns)
    if re.search(date_regex, str1):
        aux_score -= 4

    # Pattern matching for repeated characters
    if re.search(r"(.)\1{2,}", str1):
        aux_score -= 2

    # Pattern matching for sequential digits
    if re.search(r"0123456789", str1):
        aux_score -= 1

    # Pattern matching for keyboard patterns
    if re.search(r"qwertyuiopasdfghjklzxcvbnm", str1):
        aux_score -= 1

    return aux_score


def check_ent(password):
    entropy = 0
    N = len(password)
    char_frequency = {}

    # Calculate character frequency
    for char in password:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Calculate entropy using Shannon entropy formula
    for char in char_frequency:
        probability = char_frequency[char] / N
        entropy -= probability * math.log2(probability)

    # Assign scores based on entropy range
    if entropy > 4.0:
        return 5
    elif entropy > 3.5:
        return 3
    elif entropy > 3.0:
        return 1
    else:
        return -3


def check_relation(password):
    aux_score = 0
    charset_size = 94
    password_len = len(password)

    if password_len >= 8:
        aux_score += 6
    else:
        aux_score -= 4

    for i in range(password_len - 1):
        if not password[i].isalnum() and not password[i + 1].isalnum():
            aux_score -= 1
        else:
            aux_score += 2

    char_freq = {}
    for c in password:
        char_freq[c] = char_freq.get(c, 0) + 1

    entropy = 0
    for c in char_freq:
        p = char_freq[c] / password_len
        entropy += -p * math.log(p, 2)

    possible_combinations = charset_size**password_len
    aux_score += entropy * math.log(possible_combinations, 2)

    if aux_score >= 3:
        return 5
    elif aux_score >= 1:
        return 2
    else:
        return -1


def check_attempts(password):
    # character set size based on contents of password
    if password.isalnum():
        L = 62
        aux_score = -2
    elif not password.isalnum():
        L = 94
        aux_score = 2
    N = len(password)  # password length
    aux_score += check_relation(password)
    attempts = L**N
    if attempts < 10**6:
        aux_score += 1
    elif attempts < 10**12:
        aux_score += 2
    elif attempts < 10**18:
        aux_score += 3
    else:
        aux_score += 4
    return aux_score


def password_est(name, last, age, dob, father, password):
    score = 0
    if len(password) >= 8:
        score += 4
    else:
        score -= 2
    if password.isalnum():
        score -= 2
    else:
        score += 4
    score += check_commanpass(password)
    aux_score = check_cred(password, name, last, father)
    if aux_score == 0:
        aux_score -= 5
    else:
        aux_score += 4
    score += aux_score
    score += check_ent(password)
    score += check_attempts(password)
    score += check_relation(password)

    if score < 0:
        return f"{score}  'Easy'"
    elif score >= 0 and score <= 7:
        return f"{score}  Easy"
    elif score > 7 and score <= 11:
        return f"{score}  'Moderate'"
    else:
        return f"{score}  'Hard'"


def submit():
    # Get the input values from the entry fields
    name = name_entry.get()
    last = last_entry.get()
    age = int(age_entry.get())
    date_str = dob_entry.get()
    dob = parse(date_str).date()
    father = father_entry.get()
    choice = password_choice.get()
    # Generate or estimate the password based on the user's choice
    if choice == "Y":

        def check_strength():
            password_list = Listbox(window, width=100, height=100)
            password_list.pack()
            password_list.delete(0, END)
            password = password_entry.get()
            score = password_est(name, last, age, dob, father, password)
            password_list.insert(END, f"Password: {password}    Score: {score}")

        password_label = Label(window, text="Password:")
        password_label.pack()
        password_entry = Entry(window, show="*", width=35)
        password_entry.pack()

        Estimation = Button(window, text="Check Strength", command=check_strength)
        Estimation.pack()
    else:
        name = name.capitalize()
        last = last.capitalize()
        father = father.capitalize()
        passwords = generatePassword([name, last, age, date_str, father])
        password_list_label = Label(
            window,
            text="Generated Passwords:",
            padx=5,
            pady=5,
            font=("TimeNewRoman", 12),
        )
        password_list_label.pack()

        password_list = Listbox(
            window, font=("TimeNewRoman", 12), width=100, height=100
        )
        password_list.pack()

        password_list.delete(0, END)
        for password in passwords:
            score = password_est(name, last, age, dob, father, password)
            password_list.insert(END, f"Password:- {password}    Score:- {score}")


# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry("400x400")
# Create the input fields
name_label = Label(
    window, text="First Name:", padx=5, pady=5, font=("TimeNewRoman", 12)
)
name_label.pack()

name_entry = Entry(window, width=35)
name_entry.pack()

last_label = Label(window, text="Last Name:", padx=5, pady=5, font=("TimeNewRoman", 12))
last_label.pack()
last_entry = Entry(window, width=35)
last_entry.pack()

age_label = Label(window, text="Age:", padx=5, pady=5, font=("TimeNewRoman", 12))
age_label.pack()
age_entry = Entry(window, width=35)
age_entry.pack()

dob_label = Label(
    window, text="Date of Birth:", padx=5, pady=5, font=("TimeNewRoman", 12)
)
dob_label.pack()
dob_entry = Entry(window, width=35)
dob_entry.pack()

father_label = Label(
    window, text="Father's Name:", padx=5, pady=5, font=("TimeNewRoman", 12)
)
father_label.pack()
father_entry = Entry(window, width=35)
father_entry.pack()

password_choice = StringVar()
password_choice.set("N")

choice_label = Label(
    window,
    text="Do you want to enter your own password?",
    padx=5,
    pady=5,
    font=("TimeNewRoman", 12),
)
choice_label.pack()

yes_button = Radiobutton(
    window, text="Yes", variable=password_choice, value="Y", font=("TimeNewRoman", 12)
)
yes_button.pack()

no_button = Radiobutton(
    window,
    text="No",
    variable=password_choice,
    value="N",
    padx=3,
    pady=3,
    font=("TimeNewRoman", 12),
)
no_button.pack()

submit_button = Button(
    window, text="Submit", command=submit, padx=5, pady=5, font=("TimeNewRoman", 12)
)
submit_button.pack()

window.mainloop()
