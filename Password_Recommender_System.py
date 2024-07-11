import math
from tkinter import *
import random
import csv
from dateutil.parser import parse
import matplotlib.pyplot as plt
from matplotlib_venn import venn2, venn2_circles
from datetime import datetime
# Password Generation


def read_csv_file(filename):
    data = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            data.append(row)
    return data


# Reading the CSV files to take data
userE_data = read_csv_file("Form-1-report.csv")
userM_data = read_csv_file("Form-2-report.csv")
userM_data.append(userE_data)


# Calculating the probabilty of a password being rated as same by the user as the program
def calculate_password_prob(data):
    password_strengths = [row[1] for row in userM_data]
    total_count = len(password_strengths)
    password_count = {
        'Easy': password_strengths.count('Easy'),
        'Moderate': password_strengths.count('Moderate'),
        'Hard': password_strengths.count('Hard')
    }

    password_prob = {}
    for strength, count in password_count.items():
        password_prob[strength] = count / total_count

    return password_prob


userM_password_prob = calculate_password_prob(userM_data)
print(userM_password_prob)


# Checking which strength to recommend by generating a random probability
def recommend_password(probabilities):
    random_prob = random.random()
    cumulative_prob = 0

    for strength, prob in probabilities.items():
        cumulative_prob += prob
        if random_prob <= cumulative_prob:
            return strength


# Password generation algorithm to generate a password based on recommended strength
def generatePassword(row, var):
    chars = ''
    for value in row:
        if isinstance(value, str):
            chars += ''.join(list(value.replace(' ', '').strip()))

    easyPass = []
    moderatePass = []
    hardPass = []

    if '/' in row[3]:
        separator = '/'
    elif '.' in row[3]:
        separator = '.'
    else:
        separator = '-'
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
    num = [age,  # age
           day,  # DD of dob
           month,  # MM of dob
           year[0:1],  # first half of YY of dob
           year[2:3]]  # second half of YY of dob

    spl_chr = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
               '-', '.', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^',
               '_', '`', '{', '|', '}', '~', '/']
    passwords_gen = []
    # Generate easy password
    '''if (var == 0):
        for i in range(random.randint(1, 4)):
            f_char = row[0][0].lower() + row[0][1].upper() + row[0][2].lower()
            # first three characters of name
            password = random.sample(
                [f_char, random.choice(num), random.choice(num)], 3)
            # join randomly f_char and two numbers from num list
            password = ''.join(password)
            easyPass.append(f'{password} Strength - Easy ')
            for i in easyPass:
                passwords_gen.append(i)'''

    # Generate moderate password
    if (var == 1):
        for i in range(random.randint(1, 3)):
            f_char = random.sample(
                [row[0][0].lower(), row[1][0].upper(), row[4][0].lower()], 3)
            # first characters of name(lower), surname(upper) in random order
            f_char = f_char[0] + f_char[1] + f_char[2]
            password = random.sample([f_char, random.choice(
                num), random.choice(num), random.choice(spl_chr)], 4)
            # join randomly f_char and two numbers from num list and a speacial char
            password = ''.join(password)
            moderatePass.append(f'{password} Strength - Moderate ')
        for j in moderatePass:
            passwords_gen.append(j)

    # Generate hard password
    else:
        upr_chars = row[0][0] + row[1][0] + row[4][0]
        lwr_chars = row[0][1:] + row[1][1:] + row[4][1:]
        digs = ''.join([char for char in chars if char.isdigit()])
        for i in range(random.randint(1, 2)):
            pwd_list = []
            pwd_list = random.sample(upr_chars, 2) + \
                random.sample(lwr_chars, 2)
            pwd_list += random.sample(digs, 2) + random.sample(spl_chr, 2)
            random.shuffle(pwd_list)
            hardPass.append(f"{''.join(pwd_list)} Strength - Hard")
        for k in hardPass:
            passwords_gen.append(k)

    return passwords_gen


# Recommending passwords based on how probable a user is to rate it as same as the program
def recommend_passwords():
    strength = recommend_password(userM_password_prob)
    if strength == 'Easy':
        # Generate easy password using the existing generatePassword function
        generated_passwords = generatePassword(
            [name_entry.get(), last_entry.get(), age, dob_entry.get(), father_entry.get()], 0)
    if strength == 'Moderate':
        # Generate moderate password using the existing generatePassword function
        generated_passwords = generatePassword(
            [name_entry.get(), last_entry.get(), age, dob_entry.get(), father_entry.get()], 1)
    else:
        # Generate hard password using the existing generatePassword function
        generated_passwords = generatePassword(
            [name_entry.get(), last_entry.get(), age, dob_entry.get(), father_entry.get()], 2)

    return generated_passwords


def entropyCalc():
    # Entropy Calculation
    agree = 0
    disagree = 0
    MCE = ['32sId19', '3gAu1805', '96sUm96', 'aAr2697',
           '1999hRi', '20kUn05', '1997dEv', 'nIk3333',
           '99aMi24', 'aKa1902', 'aRj0919', '1920aDi',
           '05aMi05', '06aRj19', '0306aBh', 'vIk2220',
           '1919rOh', '28aRj95', '20aNk01', '0799aVi']

    MCM = ['9109ksD~', '03+03gJk', '27saR]96', '[0909Chh',
           "'01naN01", '23@00nCk', 'S$}S61vt', 'VN0@:5ih',
           '03Si{k@N', '02aTa-03', '17+Kl@yA', '04&12aaT',
           'Pga0117:', '04aDa06@', '11#Cka20', '20-20Kdv',
           'aNr04.26', '28:19Mah', '01)21Psa', '19,vaB19']

    MCH = ['{9ir1~NN', 'RhS@+26a', '9}NA9hk(', '0899;hhC',
           ']Cnk2523', "sdS'0326", '3390"Svn', '3)lN/3iS',
           'k~]An3T9', 'aG~1>K1u', 'Ska~2626', '1920*aaT',
           'aTa%1919', '!akC1111', ',KoD8(2a', '2-D2]Vak',
           '>RNn]6d9', '[2M7*aHr', '.h9V9vA>', '@BVhj9{4']
    userE = []
    alphae = []
    alpham = []
    alphah = []
    # Counting how many users agree with the program and how many disagree
    with open("Form-1-report.csv") as file:
        rd = csv.reader(file, delimiter=',')

        for i in rd:
            userE = i
            break
        rdtemp = list(rd)  # Create a copy of rd as list
        for i in range(len(userE)):
            if userE[i] in MCE:  # Check if the password is in MCE list
                agree_easy = 0
                for cont in rdtemp:
                    if cont[i] == "Easy":
                        agree_easy += 1
                alphae.append(agree_easy)

            elif userE[i] in MCM:
                agree_mod = 0
                for cont in rdtemp:
                    if cont[i] == "Moderate":
                        agree_mod += 1
                alpham.append(agree_mod)

            elif userE[i] in MCH:
                agree_hard = 0
                for cont in rdtemp:
                    if cont[i] == "Hard":
                        agree_hard += 1
                alphah.append(agree_hard)

    with open("Form-2-report.csv") as file:
        rd = csv.reader(file, delimiter=',')

        for i in rd:
            userE = i
            break
        rdtemp = list(rd)  # Create a copy of rd as list
        for i in range(len(userE)):
            if userE[i] in MCE:  # Check if the password is in MCE list
                agree_easy = 0
                for cont in rdtemp:
                    if cont[i] == "Easy":
                        agree_easy += 1
                alphae.append(agree_easy)

            elif userE[i] in MCM:
                agree_mod = 0
                for cont in rdtemp:
                    if cont[i] == "Moderate":
                        agree_mod += 1
                alpham.append(agree_mod)

            elif userE[i] in MCH:
                agree_hard = 0
                for cont in rdtemp:
                    if cont[i] == "Hard":
                        agree_hard += 1
                alphah.append(agree_hard)

    HE = []
    '''Entropy calculation using the formula
    H = (-alpha*log(alpha)) - ((1-alpha)*log(1-alpha))'''
    for i in alphae:
        i /= 25
        HE.append(-i * (math.log(i, 2)) - (1 - i) * (math.log((1 - i), 2)))

    HM = []
    for i in alpham:
        i /= 25
        HM.append(-i * (math.log(i, 2)) - (1 - i) * (math.log((1 - i), 2)))

    HH = []
    for i in alphah:
        i /= 25
        HH.append(-i * (math.log(i, 2)) - (1 - i) * (math.log((1 - i), 2)))

    for i in range(len(alphae)):
        alphae[i] /= 25
    for i in range(len(alpham)):
        alpham[i] /= 25
    for i in range(len(alphah)):
        alphah[i] /= 25
    print((alphae))
    print((alpham))
    print((alphah))
    alpha_easy = []
    alpha_mod = []
    alpha_hard = []
    alpha_easy.extend(alphae)
    alpha_mod.extend(alpham)
    alpha_hard.extend(alphah)

    alpha_ent_easy = []
    alpha_ent_mod = []
    alpha_ent_hard = []
    alpha_ent_easy.extend(HE)
    alpha_ent_mod.extend(HM)
    alpha_ent_hard.extend(HH)

    # Sort the data in ascending order of alpha
    sorted_data = sorted(zip(alpha_easy, alpha_ent_easy))
    x_sorted, y_sorted = zip(*sorted_data)
    # Plot the curve
    plt.plot(x_sorted, y_sorted, "o", color='black',
             markersize=6)

    # Set the labels and title
    plt.xlabel('Agreement (α)')
    plt.ylabel('Entropy of agreement [H(α)]')
    plt.title('Normal Distribution Curve')

    # Display the plot
    plt.show()
    sorted_data = sorted(zip(alpha_mod, alpha_ent_mod))
    x_sorted, y_sorted = zip(*sorted_data)
    # Plot the curve as scatter plots
    plt.scatter(x_sorted, y_sorted, color='black', marker='o')

    # Set the labels and title
    plt.xlabel('Agreement (α)')
    plt.ylabel('Entropy of agreement [H(α)]')
    plt.title('Normal Distribution Curve')

    # Display the plot
    plt.show()
    sorted_data = sorted(zip(alpha_hard, alpha_ent_hard))
    x_sorted, y_sorted = zip(*sorted_data)

    # Plot the curve
    plt.plot(x_sorted, y_sorted, "o", color='black',
             markersize=6)

    # Set the labels and title
    plt.xlabel('Agreement (α)')
    plt.ylabel('Entropy of agreement [H(α)]')
    plt.title('Normal Distribution Curve')

    # Display the plot
    plt.show()


def vennDiag():
    MCE = {'32sId19', '3gAu1805', '96sUm96', 'aAr2697',
           '1999hRi', '20kUn05', '1997dEv', 'nIk3333',
           '99aMi24', 'aKa1902', 'aRj0919', '1920aDi',
           '05aMi05', '06aRj19', '0306aBh', 'vIk2220',
           '1919rOh', '28aRj95', '20aNk01', '0799aVi'}

    userE = {'1999hRi', 'aAr2697', "'01naN01", '20kUn05',
             '1997dEv', 'nIk3333', '99aMi24', 'aKa1902',
             '02aTa-03', '0799aVi', '20aNk01', '28aRj95',
             '28:19Mah', '1919rOh', 'vIk2220', '20-20Kdv',
             '0306aBh', '!akC1111', '06aRj19', '05aMi05',
             'Pga0117', '1920aDi', '1920*aaT', 'aRj0919', 'Ska~2626'}

    MCM = {'9109ksD~', '03+03gJk', '27saR]96', '[0909Chh',
           "'01naN01", '23@00nCk', 'S$}S61vt', 'VN0@:5ih',
           '03Si{k@N', '02aTa-03', '17+Kl@yA', '04&12aaT',
           'Pga0117:', '04aDa06@', '11#Cka20', '20-20Kdv',
           'aNr04.26', '28:19Mah', '01)21Psa', '19,vaB19'}

    userM = {'32sId19', '9109ksD~', "gAu1805", '03+03gJk',
             'RhS@+26a', '96sUm96', '27saR]96', '[0909Chh',
             '0899;hhC', '23@00nCk', "sdS'0326", 'VN0@:5ih',
             '3390"Svn', '19,vaB19', '01)21Psa', '.h9V9vA>',
             'aNr04.26', ',KoD8(2a', '11#Cka20', '04aDa06@',
             'aTa%1919', '04&12aaT'}

    MCH = {'{9ir1~NN', 'RhS@+26a', '9}NA9hk(', '0899;hhC',
           ']Cnk2523', "sdS'0326", '3390"Svn', '3)lN/3iS',
           'k~]An3T9', 'aG~1>K1u', 'Ska~2626', '1920*aaT',
           'aTa%1919', '!akC1111', ',KoD8(2a', '2-D2]Vak',
           '>RNn]6d9', '[2M7*aHr', '.h9V9vA>', '@BVhj9{4'}

    userH = {'aG~1>K1u', '9}NA9hk(', "{9ir1~NN", ']Cnk2523',
             'S$}S61vt', '3)lN/3iS', '03Si{k@N', 'k~]An3T9',
             '@BVhj9{4', '[2M7*aHr', '>RNn]6d9', '2-D2]Vak',
             '17+Kl@yA'}
    # Create a Venn diagram with two sets
    venn = venn2([userE, MCE], set_labels=('User(25)', 'Program(20)'))

    # Customize the colors
    venn.get_patch_by_id('10').set_color('white')
    venn.get_patch_by_id('01').set_color('white')
    venn.get_patch_by_id('11').set_color('white')

    # Set hatch pattern for the common part
    p = venn.get_patch_by_id('11')
    p.set_hatch('\\\\')
    p.set_edgecolor('black')

    # Add labels to the subsets
    venn.get_label_by_id('10').set_text('8')
    venn.get_label_by_id('01').set_text('3')
    venn.get_label_by_id('11').set_text(len(userE & MCE))

    # Add circles around the sets
    venn_circles = venn2_circles([userE, MCE])
    venn_circles[0].set_ls('solid')
    venn_circles[1].set_ls('solid')

    # Set line width for the circles
    venn_circles[0].set_lw(2)
    venn_circles[1].set_lw(2)

    # Display the diagram
    plt.title('Easy Passwords Venn Diagram')
    plt.show()

    print('\n\n\n\n\n\n\n')
    # Create a Venn diagram with two sets
    venn = venn2([userM, MCM], set_labels=('User(22)', 'Program(20)'))

    # Customize the colors
    venn.get_patch_by_id('10').set_color('white')
    venn.get_patch_by_id('01').set_color('white')
    venn.get_patch_by_id('11').set_color('white')

    # Set hatch pattern for the common part
    p = venn.get_patch_by_id('11')
    p.set_hatch('\\\\')
    p.set_edgecolor('black')

    # Add labels to the subsets
    venn.get_label_by_id('10').set_text('10')
    venn.get_label_by_id('01').set_text('8')
    venn.get_label_by_id('11').set_text(len(userM & MCM))

    # Add circles around the sets
    venn_circles = venn2_circles([userM, MCM])
    venn_circles[0].set_ls('solid')
    venn_circles[1].set_ls('solid')

    # Set line width for the circles
    venn_circles[0].set_lw(2)
    venn_circles[1].set_lw(2)

    # Display the diagram
    plt.title('Moderate Passwords Venn Diagram')
    plt.show()

    print('\n\n\n\n\n\n\n')
    # Create a Venn diagram with two sets
    venn = venn2([userH, MCH], set_labels=('User(13)', 'Program(20)'))

    # Customize the colors
    venn.get_patch_by_id('10').set_color('white')
    venn.get_patch_by_id('01').set_color('white')
    venn.get_patch_by_id('11').set_color('white')

    # Set hatch pattern for the common part
    p = venn.get_patch_by_id('11')
    p.set_hatch('\\\\')
    p.set_edgecolor('black')

    # Add labels to the subsets
    venn.get_label_by_id('10').set_text('3')
    venn.get_label_by_id('01').set_text('10')
    venn.get_label_by_id('11').set_text(len(userH & MCH))

    # Add circles around the sets
    venn_circles = venn2_circles([userH, MCH])
    venn_circles[0].set_ls('solid')
    venn_circles[1].set_ls('solid')

    # Set line width for the circles
    venn_circles[0].set_lw(2)
    venn_circles[1].set_lw(2)

    # Display the diagram
    plt.title('Hard Passwords Venn Diagram')
    plt.show()


def submit(age_user):
    # Input values provided by the user
    name = name_entry.get()
    last = last_entry.get()
    date_str = dob_entry.get()
    age = age_user
    dob = parse(date_str).date()
    father = father_entry.get()
    name = name.capitalize()
    last = last.capitalize()
    father = father.capitalize()

    # To recommend passwords based on the dataset
    passwords = recommend_passwords()
    update_password_list(passwords)

    password_list.delete(0, END)
    for password in passwords:
        password_list.insert(
            END, f"Password: {password}")


# Updating password list for multiple generations
def update_password_list(passwords):
    password_list.delete(0, END)
    for password in passwords:
        password_list.insert(END, f"Password: {password}")


# Create the main window
window = Tk()
window.title("Password Generator")
window.geometry("400x400")
# Taking inputs from the user
name_label = Label(window, text="First Name:",
                   fg="black", padx=5, pady=5, font=("TimeNewRoman", 12))
name_label.pack()

name_entry = Entry(window, width=35)
name_entry.pack()

last_label = Label(window, text="Last Name:", fg="black",
                   padx=5, pady=5, font=("TimeNewRoman", 12))
last_label.pack()
last_entry = Entry(window, width=35)
last_entry.pack()


dob_label = Label(window, text="Date of Birth:", fg="black",
                  padx=5, pady=5, font=("TimeNewRoman", 12))
dob_label.pack()
dob_entry = Entry(window, width=35)

dob = dob_entry.get()
age = 0
if dob:
    dob_date = datetime.strptime(dob, "%d-%m-%Y")
    current_date = datetime.now()
    age = current_date.year - dob_date.year
    if (current_date.month, current_date.day) < (dob_date.month, dob_date.day):
        age -= 1
dob_entry.pack()
father_label = Label(window, text="Father's Name:", fg="black",
                     padx=5, pady=5, font=("TimeNewRoman", 12))
father_label.pack()
father_entry = Entry(window, width=35)
father_entry.pack()

# Submit button
submit_button = Button(window, text="Submit", command=lambda: submit(age),
                       fg="black", padx=5, pady=5, font=("TimeNewRoman", 12))
submit_button.pack()
password_list_label = Label(window, text="Recommended Passwords:",
                            fg="black", bg="white", padx=5, pady=5, font=("TimeNewRoman", 12))
password_list_label.pack()

password_list = Listbox(window, fg="black", font=(
    "TimeNewRoman", 12), width=100, height=100)
password_list.pack()

# Create and add an initial value to the password list
password_list.insert(END, "Press 'Submit' to generate passwords.")
vennDiag()  # Generates Venn Diagrams
entropyCalc()  # Entropy calculation and Scatterplots
password_choice = StringVar()
password_choice.set("N")


window.mainloop()
