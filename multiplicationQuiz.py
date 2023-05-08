import pyinputplus as pyip
import random, time 

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):

     #Pick two random numbers:
     num1 = random.randint(0, 9)
     num2 = random.randint(0, 9)

     prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

     try:
          # Right answers are handled by allowRegexes.
          # Wrong answers are handled by blockRegexs, with a custom message.
          pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                        blockRegexes=[('.*', 'Incorrect!')],
                        timeout=8, limit=3)
    except pyip.TimeoutException:
