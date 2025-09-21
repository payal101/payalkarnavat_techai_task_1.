{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cd042f9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " *********WORDLE*********\n",
      "\n"
     ]
    }
   ],
   "source": [
    "import  random\n",
    "from termcolor import colored\n",
    "chances=0\n",
    "max_chances=6\n",
    "true_check=False\n",
    "words=[\n",
    "    \"input\",\n",
    "    \"words\",\n",
    "    \"payal\",\n",
    "    \"green\"\n",
    "]\n",
    "random_words=random.choice(words)\n",
    "splitted_random_words=([*random_words])\n",
    "print(\"\\n *********WORDLE*********\\n\")\n",
    "while chances<max_chances and not true_check:\n",
    "    user_input=input(\"Guess:\")\n",
    "    splitted_input=([*user_input]) # this is how the user input will be converted into an array.\n",
    "    true_check_counter=0\n",
    "    if len(splitted_input)>5 or len(splitted_input)<5:\n",
    "        print(\"Enter a word with only  5 letters\")\n",
    "    for i in range(len(splitted_input)):\n",
    "        if  i != len(splitted_input)-1:\n",
    "            if splitted_input[i] == splitted_random_words[i]:\n",
    "               print(colored(splitted_input[i],'green'))\n",
    "            elif i in splitted_input[i] in splitted_random_words[i]:\n",
    "                  print(colored(splitted_input[i],'yellow'))\n",
    "            else:\n",
    "                 print(colored(splitted_input[i],'red'))\n",
    "        else:\n",
    "            if i in splitted_input[i] == splitted_random_words[i]:\n",
    "               print(colored(splitted_input[i],'green'))\n",
    "               true_check_counter+=1\n",
    "\n",
    "            elif i in splitted_input[i] in splitted_random_words[i]:\n",
    "                  print(colored(splitted_input[i],'yellow'))\n",
    "            else:\n",
    "                 print(colored(splitted_input[i],'red'))\n",
    "    if true_check_counter<5:\n",
    "        pass\n",
    "    else:\n",
    "        true_check=True\n",
    "    chances+=1\n",
    "if true_check:\n",
    "    print(\" You guess it correct!\")\n",
    "else:\n",
    "    print(\"You guessed it wrong!It was \",random_words)\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
