import numpy as np

class Controller:
    def __init__(self):
        self.dt = 0.01 # s
        self.p_x_eq = 0. # m
        self.p_y_eq = 0. # m
        self.p_z_eq = 0. # m
        self.psi_eq = 0. # rad
        self.theta_eq = 0. # rad
        self.phi_eq = 0. # rad
        self.v_x_eq = 0. # rad
        self.v_y_eq = 0. # rad
        self.v_z_eq = 0. # rad
        self.w_x_eq = 0. # rad
        self.w_y_eq = 0. # rad
        self.w_z_eq = 0. # rad
        self.tau_x_eq = 0. # rad
        self.tau_y_eq = 0. # rad
        self.tau_z_eq = 0. # rad
        self.f_z_eq = 4.905 # rad
        self.A = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0, 0.0, 0.0, 0.0, 1.0, -0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 9.81, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, -9.81, -0.0, 0.0, 0.0, 0.0, 0.0, -0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0, 0.0, -0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.0, -0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])
        
        self.B = np.array([[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 2.0], [434.7826086956522, 0.0, 0.0, 0.0], [0.0, 434.7826086956522, 0.0, 0.0], [0.0, 0.0, 250.0, 0.0]])
        
        self.C = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]])
        
        self.K = np.array([[9.134600829732552e-17, -0.22360679774997938, -4.452796316104523e-16, 1.3920481793250233e-16, 5.5813999853515e-16, 1.1181764037606552, -4.499047600463742e-17, -0.2903587871463353, -2.0533401518022015e-16, 0.21247026017139198, 1.0278624768152847e-17, -8.285136927854704e-17], [0.17320508075689012, 2.324122402859083e-16, 4.042720292158712e-16, 2.4593382744413345e-16, 0.9340663571855737, 2.4628426655278927e-16, 0.2509655315541599, 5.95810978259692e-17, 3.421330125117151e-16, 7.708968576114635e-18, 0.17116280332786574, -3.0821364380136253e-18], [3.909246978351563e-17, -4.3682993002453535e-16, 2.254671197083333e-15, 0.23804761428476248, -5.024791112498625e-16, 1.3234128260208554e-16, -1.799039560696237e-16, -2.7465030662850136e-16, 2.735016169949901e-15, -4.7639537335164555e-17, -2.3629712691437793e-18, 0.18771711229296997], [-9.945175028116074e-17, -5.0694939287226376e-17, 0.25819888974716004, 5.899035235893694e-16, -7.049423014278584e-17, 9.286038552460162e-17, -5.559132726470364e-17, -9.824418214853735e-17, 0.5399372399459886, -9.445364698290126e-19, 2.0984158100718526e-18, 2.1880129359599206e-17]])
        
        self.L = np.array([[10.115988385654246, 0.0, 0.0, 0.0], [0.0, 10.453917407831748, 0.0, 0.0], [0.0, 0.0, 5.094551123514538, 0.0], [0.0, 0.0, 0.0, 5.348037955515341], [7.948428934351373, 0.0, 0.0, 0.0], [0.0, -8.676973659805924, 0.0, 0.0], [38.666610509345986, 0.0, 0.0, 0.0], [0.0, 41.3088612515502, 0.0, 0.0], [0.0, 0.0, 5.477225575051655, 0.0], [0.0, -5.773502691896306, 0.0, 0.0], [5.477225575051634, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 5.477225575051659]])
        
        self.reset(0., 0., 0., 0.)
#         self.variables_to_log = ['x_des', 'xhat']
        self.r = 2.45
        self.u_des = np.array([0., 0., 0., 0.])
        self.x_des = np.array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]) 

    def get_color(self):
        return [0., 0., 0.]

    def reset(
            self,
            p_x_meas, p_y_meas, p_z_meas, # <-- measured position of drone (meters)
            yaw_meas,                     # <-- measured yaw angle of drone (radians)
        ):
        
        # define initial state estimate
        self.xhat = np.array([p_x_meas, p_y_meas, p_z_meas, yaw_meas, 0., 0., 0., 0., 0., 0., 0., 0.])

    def run(
            self,
            p_x_meas, p_y_meas, p_z_meas, # <-- measured position of drone (meters)
            yaw_meas,                     # <-- measured yaw angle of drone (radians)
            p_x_ring, p_y_ring, p_z_ring, # <-- center position of next ring (meters)
            is_last_ring,                 # <-- True if next ring is the last ring, False otherwise
            pos_others,                   # <-- 2d array of size n x 3, where n is the number
                                          #     of all *other* drones - the ith row in this array
                                          #     has the coordinates [x_i, y_i, z_i], in meters, of
                                          #     the ith other drone
        ):
        
        # Initialize and update the desired state
        if p_z_meas < 0.5: # We want the vertical height of the drone to clear the initial ring, so we make the drone achieve a height of 0.8 m before it moves to the next ring
            self.x_des[0:3] = np.array([p_x_meas, p_y_meas, 0.6])
            
        else: # Once the desired vertical height is reached, the drone will start moving through the rings
            self.phat = np.array([p_x_meas, p_y_meas,  p_z_meas])
            self.p_ring = np.array([p_x_ring, p_y_ring, p_z_ring])
            
            # compute vector between ring and estimated position
            d = self.p_ring - self.phat
            
            # implement tracking as defined in equation (14)
            self.p_des = self.phat + self.r*d / np.linalg.norm(d)
            self.x_des[0:3] = self.p_des
        
        # find input
        u = self.u_des - self.K @ (self.xhat - self.x_des)
        
        # implement system output
        y = np.array([p_x_meas - self.p_x_eq, p_y_meas - self.p_y_eq, p_z_meas - self.p_z_eq, yaw_meas - self.psi_eq])
        
        # find state estimate
        self.xhat += self.dt * (self.A @ self.xhat + self.B @ u - self.L@(self.C@self.xhat - y))
        
        # relay actuator commands and f_z
        tau_x = u[0] + self.tau_x_eq
        tau_y = u[1] + self.tau_y_eq
        tau_z = u[2] + self.tau_z_eq
        f_z = u[3] + self.f_z_eq

        return tau_x, tau_y, tau_z, f_z