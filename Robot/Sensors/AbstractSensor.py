class AbstractSensor(object):
    ###
     # This represents the Abstract Sensor class.
     # Classes that inherit this have to implement the _before and setState methods
     #
     ##
    def __init__(self):
        self.isActive = False
        self.state = False
        
    ###
     # You can use this to do something before the actual called method.
     #
     # Needs to be implemented on inherited classes
     #
     ##
        
    def _before(self):
        raise NotImplementedError

     ###
     # Checks if this current Sensor has been set as active.
     #
     # @return bool isActive - if it's active or not
     #
     ##
     
    def isActive(self):
        return self.isActive
    
    ###
     # Sets the current sensor as active.
     #
     #
     ##
        
    def setActive(self):
        self.isActive = True
        
    ###
     # Shows the state of the sensor.
     #
     # @return state
     #
     ##
        
    def showState(self):
        return self.state
    
    ###
     # Sets the state of the sensor.
     #
     # Needs to be implemented on inherited classes
     #
     ##
        
    def setState(self,state):
        raise NotImplementedError