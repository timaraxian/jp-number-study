# JP Number Study

### Purpose

In Japanese language class I struggling with quickly answering the Japanese translation of numbers,


This program asks you for: 
* A maximum number you wish to study up to
* The amount of numbers you wish to study in a session
* How many seconds break you desire between the Arabic numerals and the Hiragana number

The program will then display a random number between 1 and the maximum number you input. <br>
The program will then sleep for the desired time you input. <br>
The program will then display the hiragana reading of that number. <br>
The program will then sleep again for the same amount of time. <br>
If you input more than 1 for the amount of numbers you wanted to study then the program will loop.


### Usage

```bash
python3 main.py
```

### Known bugs (aka todo)

- user can input something that isn't an int
- user can input 0 as the number of cycles
- doesn't go past 99,999,999
- number splitter and switch cases are ugly
