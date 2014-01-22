# catapult simulation
# for FRC 2014 Aerial Assist
# Uses Python, numpy, matplotlib

BALL_KG = 1.25 # kg the mass of a ball
NUM_MOTORS = 2 

dt = 0.001 # simulation time increment
n_m_per_foot_lb = 1.356
oz_in_per_foot_lb = 16 * 12

CIM_R = 0.09/NUM_MOTORS # volts per amp (ohms) (two motors just cuts this in half)

# we lose some torque to accelerating the motor.
# How much? well, FIRST does not publish the motor's moment of inertia.
# we can guess however. Mechanical time constant of the motor is about 20 milliseconds
CIM_J = 0.0001 # kg-m**2 of motor Gives 20 msec-ish halfway point with no load.

CIM_KT = (343.4 / 133) # oz-in per amp
CIM_KT /= oz_in_per_foot_lb # foot-lb per amp
CIM_KT *= n_m_per_foot_lb # newton meters per amp

# CIM_KT is ALSO CIM_KV in volts per (radian per second)

class CatSim :
    def __init__(self, reduction, arm_radius, drive) :
        self.drive = drive
        self.cur_t = 0 # time in seconds
        self.cur_v = 0 # motor speed in radians per second
        self.cur_ang = 0 # motor position in radians
        self.reduction = reduction # reduction gearing from motor to load.
        self.arm_radius = arm_radius
        self.load_moment = BALL_KG * self.arm_radius**2 # kg*m**2 point load model
        self.load_moment += 0.0775 # moment of inertia of ball itself. I = 2/3*m*R**2
        
        self.reflected_moment = self.load_moment / self.reduction**2
        self.v = []
        self.t = []
        self.s = []

    def step(self) :
        self.v.append(self.cur_v)
        self.t.append(self.cur_t)
        self.s.append(self.cur_ang)
        emf = self.cur_v * CIM_KT # current back_emf
        amps = (self.drive - emf) / CIM_R # how much current do we draw?
        torque = CIM_KT * amps # torque in newton-meters
        if False :
            load_torque = torque * self.reduction # torque is amplified thru gearbox
            load_accel = load_torque / self.load_moment # rad/sec*2
            motor_accel = load_accel * self.reduction # motor is faster than load.
        else :
            # motor accel = motor torque  * self.reduction**2 / self.load_moment 
            motor_accel = torque / (self.reflected_moment + (NUM_MOTORS*CIM_J))
        self.cur_v += motor_accel * dt # change our state (motor velocity radians per second)
        self.cur_ang += self.cur_v * dt # change our position (motor rotation in radians)
        self.cur_t += dt

from numpy import array
from pylab import plot, show, ylabel, xlabel
catsims = []

reductions = [14.8] # <<< prototyping this
reductions = [9, 12, 14.8, 16, 20, 27, 36, 48, 64] # a range of planetary gearbox reductions
arm_radii = [0.5, 0.6, 0.7] 
arm_radii = [0.53] # <<< design for this radius (21 inches)
drive_voltages = [9, 10, 11, 12]
drive_voltages = [10]

plotvel = True

for reduction in reductions :
  for arm_radius in arm_radii:
   for drive in drive_voltages :
    catsim = CatSim(reduction, arm_radius, drive) 
    while (catsim.cur_ang / reduction) < 1.57 : # end plot when catapult arm hits the end
        catsim.step()
    motorv = array(catsim.v) # motor speed, radians per second
    motors = array(catsim.s) # motor angle in radians
    motort = catsim.t
    loadv = motorv * arm_radius / reduction # ball speed, meters per second
    loads = motors * arm_radius / reduction # ball position, meters
    if plotvel :
        plot(motort, loadv)
    else :
        plot(motort, loads)
    catsims.append(catsim)
   
xlabel("time in seconds")
if plotvel : 
    ylabel("ball meters per second")   
else :
    ylabel("ball meters")   
show()

# load moment of 1.25 kg point load at 0.58 meters = 0.429 kg*m**2
# moment of a 1.22 kg thin spherical shell, radius of 12 inches = 0.0775 kg-m**2
# total load moment = 0.428 + 0.0775 = 0.506
# ball inertia = 15 percent of the total inertia. measurable but not huge.

