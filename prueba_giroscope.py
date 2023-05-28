from mpu6050 import MPU6050
import time

mpu = MPU6050(14, 13)  # attach the IIC pin(sclpin, sdapin)
mpu.MPU_Init()  # initialize the MPU6050
G = 9.8
time.sleep_ms(1000)  # waiting for MPU6050 to work steadily

try:
    previous_yaw_angle = 0
    right_rotation_degrees=0
    left_rotation_degrees=0
    while True:
        accel = mpu.MPU_Get_Accelerometer()  # gain the values of Acceleration
        gyro = mpu.MPU_Get_Gyroscope()  # gain the values of Gyroscope
        print("\na/g:\t")
        print(accel[0], "\t", accel[1], "\t", accel[2], "\t",gyro[0], "\t", gyro[1], "\t", gyro[2])
        print("a/g:\t")
        print(accel[0] / 16384, "g", accel[1] / 16384, "g", accel[2] / 16384, "g",gyro[0] / 131, "d/s", gyro[1] / 131, "d/s", gyro[2] / 131, "d/s")

        # Calculate the yaw angle
        yaw_angle = (gyro[0] / 131) * 0.017453292519943295
        print(yaw_angle)
        # Calculate the change in yaw angle
        change_in_yaw_angle = yaw_angle - previous_yaw_angle
        print(change_in_yaw_angle)
        # Record the number of degrees the robot has rotated
        if change_in_yaw_angle > 0:
            right_rotation_degrees += change_in_yaw_angle
        elif change_in_yaw_angle < 0:
            left_rotation_degrees += abs(change_in_yaw_angle)

        # Print the number of degrees the robot has rotated
        print("Right rotation degrees:", right_rotation_degrees)
        print("Left rotation degrees:", left_rotation_degrees)

        previous_yaw_angle = yaw_angle
        time.sleep_ms(1000)

except:
    pass
