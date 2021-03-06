{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "append: 0.09872150200000007\n",
      "concat: 0.10876064500000027\n",
      "unpack: 0.14667600099999945\n"
     ]
    }
   ],
   "source": [
    "from timeit import timeit\n",
    "\n",
    "append = \"\"\"\n",
    "array1 = [0, 1, 2]\n",
    "array1.append(3)\n",
    "\"\"\"\n",
    "concat = \"\"\"\n",
    "array2 = [0, 1, 2]\n",
    "array2 += [3]\n",
    "\"\"\"\n",
    "unpack = \"\"\"\n",
    "array3 = [0, 1, 2]\n",
    "array3 = [*array3, 3]\n",
    "\"\"\"\n",
    "\n",
    "print(f\"append: {timeit(append)}\")\n",
    "print(f\"concat: {timeit(concat)}\")\n",
    "print(f\"unpack: {timeit(unpack)}\")"
   ]
  }
 ],
 "metadata": {
  "interpreter": {
   "hash": "31f2aee4e71d21fbe5cf8b01ff0e069b9275f58929596ceb00d14d90e3e16cd6"
  },
  "kernelspec": {
   "display_name": "Python 3.8.2 64-bit",
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
   "version": "3.8.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
