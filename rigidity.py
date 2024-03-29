def calculateRigidity(charge, mass, speedOfLight):
    
    magneticRigidity =(mass*speedOfLight * 1.0)/charge
    return magneticRigidity
    
if __name__ == "__main__":  
    charge_value = 77*1.602e-19  # Coulombs
    mass_value = 197*1.66e-27   # kg
    speedOfLight = 3e8   # m/s

    # Create an instance of RigidityCalculator
    print(f"Rigidty value is  {calculateRigidity(charge_value, mass_value, speedOfLight)} T*m")
