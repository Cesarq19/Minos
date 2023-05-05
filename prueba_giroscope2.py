import machine
import math
import time
from mpu6050 import MPU6050
# MPU6050 register addresses
MPU_ADDR = const(0x68)
MPU_PWR_MGMT1_REG = const(0x6B)
MPU_ACCEL_XOUTH_REG = const(0x3B)
MPU_GYRO_XOUTH_REG = const(0x43)

# MPU6050 configuration
MPU_SAMPLE_RATE = const(100) # Hz
MPU_ACCEL_SENSITIVITY = const(16384) # LSB/g
MPU_GYRO_SENSITIVITY = const(131) # LSB/(deg/s)
COMPLEMENTARY_FILTER_ALPHA = const(0.98) # filter coefficient

# Initialize I2C bus and MPU6050

mpu = MPU6050(13,14)

# Initialize filter state
angle = 0.0
gyro_bias = 0.0
last_time = time.ticks_ms()

# Main loop
while True:
    # Read gyroscope and accelerometer data
    gyro_data = mpu.read_gyro_data() / MPU_GYRO_SENSITIVITY
    accel_data = mpu.read_accel_data() / MPU_ACCEL_SENSITIVITY

    # Calculate time elapsed since last loop iteration
    now = time.ticks_ms()
    delta_time = (now - last_time) / 1000.0
    last_time = now

    # Apply gyroscope bias correction
    gyro_data -= gyro_bias

    # Integrate gyroscope data to get angle change
    angle_change = gyro_data * delta_time

    # Update angle estimate with complementary filter
    accel_angle = math.atan2(accel_data[1], accel_data[2]) * 180.0 / math.pi
    angle = COMPLEMENTARY_FILTER_ALPHA * (angle + angle_change) + (1 - COMPLEMENTARY_FILTER_ALPHA) * accel_angle

    # Print angle
    print("Angle: {:.2f} deg".format(angle))

    # Update gyroscope bias estimate (optional)
    gyro_bias = COMPLEMENTARY_FILTER_ALPHA * gyro_bias + (1 - COMPLEMENTARY_FILTER_ALPHA) * gyro_data[0]
    time.sleep_ms(1000)
