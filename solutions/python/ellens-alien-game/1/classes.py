"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    # Class variable to display the health of the alien
    health = 3
    total_aliens_created = 0    # number of objects created

    #class constructor to get the coordinate of the alien
    def __init__(self,x, y):
        self.x_coordinate = x
        self.y_coordinate = y
        Alien.total_aliens_created += 1    

    # hit() to reduce the health by 1
    def hit(self):
        self.health -= 1

    '''
    Note: 
    1. We are calling the 'health' variable using the 'self' keyword, because the health will be             initialized for each alien. That means, for each alien created, the health = 3.
    2. But, we are calling the 'total_aliens_created' variable using the 'Class_name', because for         each alien created, the value of the variable should increase by 1.
    '''

    # is_alive() to check whether the health is > 0
    def is_alive(self):
        return self.health > 0

    # teleport() to move to a new location
    def teleport(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def collision_detection(self, *params):
        pass

#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.

def new_aliens_collection(alien_positions):
    new = []
    for position in alien_positions:
        new.append(Alien(position[0], position[1]))
    return new
    