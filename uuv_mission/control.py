class Controller: #Implements PD controller for submarine
    def __init__(self, Kp: float, Kd: float):
        self.Kp = Kp
        self.Kd = Kd
        self.previous_error = 0 #Initialise previous error variable

    def control(self, reference: float, current_depth: float) -> float:
        #e[t] = r[t] - y[t]
        error = reference - current_depth

        #u[t] = Kp x e[t] + Kd x (e[t] - e[t-1])
        action = (self.Kp * error) + (self.Kd * (error - self.previous_error))

        self.previous_error = error
        return action