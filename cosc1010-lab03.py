# Bradley Ekstrom
# UWYO COSC 1010
# 09/26/24
# Lab 03
# Lab Section: 13
# Sources, Nolan Hottel, and Rylie Green
print('Part One-----------------------------')

states = ['Wyoming', 'Colorado', 'Montana']
print(states)
print(states[0])
print(states[-1])

#Using an F-string to access the first and second element print the string
print(f"{states[0:2]}")

# "COLORADO is south of WYOMING", matching the casing provided
print(f"{states[1].upper()} is south of {states[0].upper()}")

print("Part Two-----------------------------")

#Append the following states to your list: Washington, Oregon, California and printyour list
states.append('Washington')
states.append('Oregon')
states.append('California')
print(states)

#Again using the specific syntax mentioned in class overwrite the second to lastelement to be Maine, printing the list
states[-2] = 'Maine'
print(states)

#Insert the state Texas to be the third element in the list, again printing yourlist
states.insert(4, 'Texas')
print(states)

#Using the `del` statement remove the fourth item from the list, print your list
del states[5]
print(states)

#Remove Texas using its value, print the list
states.remove('Texas')
print(states)

print("Part Three-----------------------------")

#Temporarily sort your list, print it both sorted and unsorted
print(states)
states.sort()
print(states)

#Permanently sort your list in reverse order, printing it out
print(sorted(states))
print(sorted(states,reverse=True))

#Using the reverse method reverse the list and print it
states.reverse()
print(states)