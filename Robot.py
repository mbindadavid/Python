class Robot:
      #Reperesent a robot with a name

    # Class variable, counting the number of robot
    population = 0

    def __init__(self, name):
      # Initailize the data
      self.name = name
      print("(Initialize {})".format(self.name))

      # When this person is created,the robot adds to the population
      Robot.population += 1

    def die(self):
        """I am dying"""
        print("{} is been destroyed".format(self.name))

        Robot.population -= 1
        if Robot.population == 0:
            print('{} was last one'.format(self.name))
        else:
            print("There are still {:d} robots working".format(Robot.population))

    def say_hi(self):
        # Greeting by the robot
        print("Greetings,my master call me {}".format(self.name))

    @classmethod
    def how_many(cls):
    # Print the current population
        print("We have {:d} population".format(cls.population))

droid1 = Robot("R1-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobot can do some work here\n")

print("Robot have finished their work,so lets destory them")
droid1.die()
droid2.die()

Robot.how_many()

