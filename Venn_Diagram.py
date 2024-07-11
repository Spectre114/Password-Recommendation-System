from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt

# Define the sets
MCE = {'32sId19', '3gAu1805', '96sUm96', 'aAr2697',
      '1999hRi','20kUn05','1997dEv','nIk3333',
      '99aMi24','aKa1902','aRj0919','1920aDi',
      '05aMi05','06aRj19','0306aBh','vIk2220',
      '1919rOh','28aRj95','20aNk01','0799aVi'}

userE = {'1999hRi', 'aAr2697', "'01naN01", '20kUn05',
      '1997dEv','nIk3333','99aMi24','aKa1902',
      '02aTa-03','0799aVi','20aNk01','28aRj95',
      '28:19Mah','1919rOh','vIk2220','20-20Kdv',
      '0306aBh','!akC1111','06aRj19','05aMi05',
      'Pga0117','1920aDi','1920*aaT','aRj0919','Ska~2626'}

MCM = {'9109ksD~', '03+03gJk', '27saR]96', '[0909Chh',
      "'01naN01",'23@00nCk','S$}S61vt','VN0@:5ih',
      '03Si{k@N','02aTa-03','17+Kl@yA','04&12aaT',
      'Pga0117:','04aDa06@','11#Cka20','20-20Kdv',
      'aNr04.26','28:19Mah','01)21Psa','19,vaB19'}

userM = {'32sId19', '9109ksD~', "gAu1805", '03+03gJk',
      'RhS@+26a','96sUm96','27saR]96','[0909Chh',
      '0899;hhC','23@00nCk',"sdS'0326",'VN0@:5ih',
      '3390"Svn','19,vaB19','01)21Psa','.h9V9vA>',
      'aNr04.26',',KoD8(2a','11#Cka20','04aDa06@',
      'aTa%1919','04&12aaT'}

MCH = {'{9ir1~NN', 'RhS@+26a', '9}NA9hk(', '0899;hhC',
      ']Cnk2523',"sdS'0326",'3390"Svn','3)lN/3iS',
      'k~]An3T9','aG~1>K1u','Ska~2626','1920*aaT',
      'aTa%1919','!akC1111',',KoD8(2a','2-D2]Vak',
      '>RNn]6d9','[2M7*aHr','.h9V9vA>','@BVhj9{4'}

userH = {'aG~1>K1u', '9}NA9hk(', "{9ir1~NN", ']Cnk2523',
      'S$}S61vt','3)lN/3iS','03Si{k@N','k~]An3T9',
      '@BVhj9{4','[2M7*aHr','>RNn]6d9','2-D2]Vak',
      '17+Kl@yA'}


# Create a Venn diagram with two sets
venn = venn2([userE, MCE], set_labels=('User', 'Machine'))

# Customize the colors
venn.get_patch_by_id('10').set_color('white')
venn.get_patch_by_id('01').set_color('white')
venn.get_patch_by_id('11').set_color('white')

# Set hatch pattern for the common part
p = venn.get_patch_by_id('11')
p.set_hatch('\\\\')
p.set_edgecolor('black')

# Add labels to the subsets
venn.get_label_by_id('10').set_text(len(userE))
venn.get_label_by_id('01').set_text(len(MCE))
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
venn = venn2([userM, MCM], set_labels=('User', 'Machine'))

# Customize the colors
venn.get_patch_by_id('10').set_color('white')
venn.get_patch_by_id('01').set_color('white')
venn.get_patch_by_id('11').set_color('white')

# Set hatch pattern for the common part
p = venn.get_patch_by_id('11')
p.set_hatch('\\\\')
p.set_edgecolor('black')

# Add labels to the subsets
venn.get_label_by_id('10').set_text(len(userM))
venn.get_label_by_id('01').set_text(len(MCM))
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
venn = venn2([userH, MCH], set_labels=('User', 'Machine'))

# Customize the colors
venn.get_patch_by_id('10').set_color('white')
venn.get_patch_by_id('01').set_color('white')
venn.get_patch_by_id('11').set_color('white')

# Set hatch pattern for the common part
p = venn.get_patch_by_id('11')
p.set_hatch('\\\\')
p.set_edgecolor('black')

# Add labels to the subsets
venn.get_label_by_id('10').set_text(len(userH))
venn.get_label_by_id('01').set_text(len(MCH))
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
