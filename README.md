I-Card Reader

This project can be used to take attendance of I-Card holders. It can also serve another purpose using I-Cards with simple modification. 

Step 1) Install Python 2.7 on your computer

Step 2) Download this repository onto your computer

Step 3) Create a file 'card.json' and have the UINs of users as a key with their names as a value.

  Example)
  card.json
  {
    "123456789":"Bob",
    "987654321":"Sarah"
  }
  
It is important to note that a student's UIN is private information and should not be put on internet or shared.

Step 4) Get a USB Card reader and plug it in to your computer

Step 5) Run read.py and have your users swipe their I-Cards

If the above steps are followed, a [date].txt file should appear with the names of those who swiped in.
