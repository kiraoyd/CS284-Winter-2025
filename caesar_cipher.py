def find_index (some_alphabet, some_letter):
    index = 0

    #Determine the total number of characters in some_alphabet
    size = len(some_alphabet)
    last_index = size - 1 #get the value of the last index

    #As long as there is still data in some_alphabet to process
    while index <= last_index:
        #does the letter at this index in some_alphabet, match some_letter?
        if some_alphabet[index] == some_letter:
            return index #if so, return with the current index value

        #increment the value of index by 1 to "move" one letter to the-
        #right in some_alphabet
        index = index + 1 #index += 1 is also valid syntax

    #this is the next line of code after the loop break
    return -1 #error flag

def shift_letter(alphabet, letter, key, length):
    #Step 2.1 - call the function to find the index value
    #of the letter, in the alphabet string
    letter_index = find_index(alphabet, letter)

    if letter_index < 0:
        print(f"Sorry, {letter} does no exist in this alphabet.")
        return -1
    else:
        shifted_index = (letter_index + key) % length
        #access the alphabet at the new index to get the encoded letter
        encoded_letter = alphabet[shifted_index]

        return encoded_letter

def encrypt(alphabet, key, length, message):
    #message now holds some word in all caps "CODE"
    index = 0
    message_length = len(message)

    encoded_message = [] #empty list

    while index < message_length:
        #do some work
        letter = message[index]
        encoded_letter = shift_letter(alphabet, letter, key, length)
        #add the encoded_letter to my encoded_message list
        encoded_message.append(encoded_letter)
        index += 1

    #transform it, from a List type, back into a string
    secret_message = "".join(encoded_message)
    #print(secret_message)

    return secret_message

def main():
    # Step 1: Make the alphabet string
    alphabet_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(alphabet_string)
    key = 6

    #Step 2: Lets figure out how to shift a single letter by some key
    #to the right on our alphabet
    #letter = '7'

    message = input("Please enter a word, in all capital letters.")

    encoded_message = encrypt(alphabet_string, key, length, message)
    print(encoded_message)

main()