{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71163300-7a06-4670-a8f2-cef4a2ce4fae",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Nathan Romeo\n",
    "#U1060425\n",
    "#8 September 2023\n",
    "\n",
    "def letter_a(size: int, word_list: list):\n",
    "    \"\"\"\n",
    "    Generate and append the pattern for the letter 'A' to the word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - size (int): The size of the letter.\n",
    "    - word_list (list): The list to which the letter will be appended. This list will be modified in place.\n",
    "    \"\"\"\n",
    "    print_a = [[\" \" for i in range(size)] for j in range(size)] # Generate an empty grid of size x size\n",
    "    for row in range(size):\n",
    "        for column in range(size):\n",
    "            if (column==0 or column==size-1) and row>=size//2 or row==size//2 or row==column-size//2 or row==size//2-column:\n",
    "                print_a[row][column]=\"*\" # Print '*' in required rows and columns to spell letter A\n",
    "    word_list.append(print_a)\n",
    "\n",
    "def letter_b(size: int, word_list: list):\n",
    "    \"\"\"\n",
    "    Generate and append the pattern for the letter 'B' to the word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - size (int): The size of the letter.\n",
    "    - word_list (list): The list to which the letter will be appended. This list will be modified in place.\n",
    "    \"\"\"\n",
    "    print_b = [[\" \" for i in range(size)] for j in range(size)] # Generate an empty grid of size x size\n",
    "    for row in range(size):\n",
    "        for column in range(size):\n",
    "            if (row==0 or row==size-1 or row==size//2) and column!=size-1 or column==0 or column==size-1 and (row!=0 and row!=size-1 and row!=size//2 ):\n",
    "                print_b[row][column]=\"*\" # Print '*' in required rows and columns to spell letter B\n",
    "    word_list.append(print_b)\n",
    "    \n",
    "def letter_n(size: int, word_list: list):\n",
    "    \"\"\"\n",
    "    Generate and append the pattern for the letter 'N' to the word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - size (int): The size of the letter.\n",
    "    - word_list (list): The list to which the letter will be appended. This list will be modified in place.\n",
    "    \"\"\"\n",
    "    print_n = [[\" \" for i in range(size)] for j in range(size)] # Generate an empty grid of size x size\n",
    "    for row in range(size):\n",
    "        for column in range(size):\n",
    "            if column==0 or column==size-1 or row==column:\n",
    "                print_n[row][column]=\"*\" # Print '*' in required rows and columns to spell letter N\n",
    "    word_list.append(print_n)\n",
    "    \n",
    "def letter_o(size: int, word_list: list):\n",
    "    \"\"\"\n",
    "    Generate and append the pattern for the letter 'O' to the word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - size (int): The size of the letter.\n",
    "    - word_list (list): The list to which the letter will be appended. This list will be modified in place.\n",
    "    \"\"\"\n",
    "    print_o = [[\" \" for i in range(size)] for j in range(size)] # Generate an empty grid of size x size\n",
    "    for row in range(size):\n",
    "        for column in range(size):\n",
    "            if (row>1 and row<size-2) and (column==0 or column==size-1) or (row==0 or row==size-1) and (column>1 and column<size-2) or (row==1 or row==size-2) and (column==1 or column==size-2): \n",
    "                print_o[row][column] = \"*\" # Print '*' in required rows and columns to spell letter O\n",
    "    word_list.append(print_o)\n",
    "\n",
    "def letter_t(size: int, word_list: list):\n",
    "    \"\"\"\n",
    "    Generate and append the pattern for the letter 'T' to the word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - size (int): The size of the letter.\n",
    "    - word_list (list): The list to which the letter will be appended. This list will be modified in place.\n",
    "    \"\"\"\n",
    "    print_t = [[\" \" for i in range(size)] for j in range(size)] # Generate an empty grid of size x size\n",
    "    for row in range(size):\n",
    "        for column in range(size):\n",
    "            if row==0 or column==round(size//2):\n",
    "                print_t[row][column] =\"*\" # Print '*' in required rows and columns to spell letter T\n",
    "    word_list.append(print_t)\n",
    "\n",
    "def letter_y(size: int, word_list: list):\n",
    "    \"\"\"\n",
    "    Generate and append the pattern for the letter 'Y' to the word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - size (int): The size of the letter.\n",
    "    - word_list (list): The list to which the letter will be appended. This list will be modified in place.\n",
    "    \"\"\"\n",
    "    print_y = [[\" \" for i in range(size)] for j in range(size)] # Generate an empty grid of size x size\n",
    "    for row in range(size):\n",
    "        for column in range(size):\n",
    "            if row<=size//2 and row==column or (column==size//2 and row>size//2) or (row<size//2 and column==(size-1-row)):\n",
    "                print_y[row][column]=\"*\" # Print '*' in required rows and columns to spell letter Y\n",
    "    word_list.append(print_y)\n",
    "     \n",
    "def print_word(word: str, size: int, word_list: list)-> list:\n",
    "    \"\"\"\n",
    "    Identifies characters in user word, generates and stores the printed letters to word_list.\n",
    "\n",
    "    Parameters:\n",
    "    - word (str): The input word to spell.\n",
    "    - size (int): The size of each letter.\n",
    "    - word_list (list): The list to store the printed letters.\n",
    "    Returns:\n",
    "    - word_list (list): The list with all the printed letters from user word.\n",
    "    \"\"\"\n",
    "    for char in range(len(word)): \n",
    "        if word[char].upper() == \"A\":\n",
    "            letter_a(size, word_list)\n",
    "        elif word[char].upper() == \"B\":\n",
    "            letter_b(size, word_list)\n",
    "        elif word[char].upper() == \"N\":\n",
    "            letter_n(size, word_list)    \n",
    "        elif word[char].upper() == \"O\":          \n",
    "            letter_o(size, word_list)             \n",
    "        elif word[char].upper() == \"T\":\n",
    "            letter_t(size, word_list)\n",
    "        elif word[char].upper() == \"Y\":\n",
    "            letter_y(size, word_list)        \n",
    "    return word_list\n",
    "\n",
    "def main():\n",
    "    \"\"\"\n",
    "    Generate and display patterns for words and letters using '*'.\n",
    "\n",
    "    This function lets users input a word containing the characters 'A', 'B', 'N, 'O', 'T', and 'Y'.\n",
    "    Decorative patterns corresponding to each character are displayed using '*'.\n",
    "\n",
    "    Usage:\n",
    "    - Enter a word (case-insensitive) using only the allowed characters ('A', 'B', 'N', 'O', 'T', 'Y').\n",
    "    - Displayed patterns are of a predefined size denoted by 'size' variable.\n",
    "    - Type 'END' (case-insensitive) at any time to exit.\n",
    "    \"\"\" \n",
    "    print(\"Welcome! Spell any word using the characters A, B, N, O, T and Y. Type 'END' to exit.\")\n",
    "    \n",
    "    allowed_chars = [ \"A\", \"B\", \"N\", \"O\", \"T\", \"Y\"] # Define allowed characters\n",
    "    size = 7 # Size of letters\n",
    "    \n",
    "    while True:\n",
    "        word_list = [] # Create empty list to store user word\n",
    "        try:           \n",
    "            word = input(\"What word would you like to spell?\")  # Ask user for input word to spell                    \n",
    "            word = word.strip() # Strip spaces off start or end of user input\n",
    "            \n",
    "            # Check if user has entered valid word or if user wants to end\n",
    "            if word.upper() == \"END\":\n",
    "                print(\"See you next time! Program exiting...\") # End program\n",
    "                return  \n",
    "            if len(word)<1: # User cannot enter empty input\n",
    "                raise ValueError             \n",
    "            for char in range(len(word)):     \n",
    "                if word[char].upper() not in allowed_chars: # Convert input characters into upper case and check if in allowed_chars\n",
    "                    raise ValueError                              \n",
    "\n",
    "            # Pass values and call print_word() function to append the final output to word_list\n",
    "            word_list = print_word(word, size, word_list)\n",
    "            \n",
    "            # Print final output\n",
    "            for row in range(size):\n",
    "                for index in range(len(word_list)):\n",
    "                    for column in range(size):\n",
    "                        print(word_list[index][row][column],end=\"\")\n",
    "                    print(end=\" \") # Allow one space between characters\n",
    "                print()\n",
    "                \n",
    "        # If user has entered invalid word then show error message and prompt again\n",
    "        except ValueError:\n",
    "            print(\"Please enter a word with the letters A, B, N, O, T, Y. Spaces are not allowed.\")\n",
    "      \n",
    "if __name__ == \"__main__\":                \n",
    "    main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
