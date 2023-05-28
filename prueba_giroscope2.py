from mpu6050 import MPU6050
import time
 
mpu=MPU6050(14,13) #attach the IIC pin(sclpin,sdapin)
mpu.MPU_Init()     #initialize the MPU6050
G = 9.8
time.sleep_ms(1000)#waiting for MPU6050 to work steadily

try:
    while True:
        accel=mpu.MPU_Get_Accelerometer()#gain the values of Acceleration
        gyro=mpu.MPU_Get_Gyroscope()     #gain the values of Gyroscope
        print("\na/g:\t")
        print(accel[0],"\t",accel[1],"\t",accel[2],"\t",
              gyro[0],"\t",gyro[1],"\t",gyro[2])
        print("a/g:\t")
        print(accel[0]/16384,"g",accel[1]/16384,"g",accel[2]/16384,"g",
              gyro[0]/131,"d/s",gyro[1]/131,"d/s",gyro[2]/131,"d/s")
    

        # Define the time step.
        dt = 0.01

        # Integrate the gyroscope data to get the object's angular position.
        angular_position = 0
        for i in range(3):
            angular_position += (gyro[0]/131) * dt
        print(angular_position)
        # Use the accelerometer data to filter the object's angular position.
        accel_data_g = [accel[0]/16384,accel[1]/16384,accel[2]/16384]
        filtered_angular_position = accel_data_g.copy()
        for i in range(len(accel)):
            filtered_angular_position[i] = filtered_angular_position[i - 1] + (accel_data_g[i] - filtered_angular_position[i - 1]) * dt
        print(filtered_angular_position)
        time.sleep_ms(1000)
        
except:
    pass
