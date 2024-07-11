import csv
import math
import matplotlib.pyplot as plt

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
for i in alphae:
    i /= 25
    HE.append(-i * (math.log(i, 2)) - (1 - i) * (math.log((1 - i), 2)))
    # HE.append(-i * (math.log(i/(1-i), 2)))

HM = []
for i in alpham:
    i /= 25
    HM.append(-i * (math.log(i, 2)) - (1 - i) * (math.log((1 - i), 2)))
    # HM.append(-i * (math.log(i/(1-i), 2)))

HH = []
for i in alphah:
    i /= 25
    HH.append(-i * (math.log(i, 2)) - (1 - i) * (math.log((1 - i), 2)))
    # HH.append(-i * (math.log(i/(1-i), 2)))

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
