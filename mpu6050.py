import machine
from machine import I2C,Pin
import time
 
MPU_ADDR    = const(0X68)
MPU_DEVICE_ID_REG       = 0x75
MPU_PWR_MGMT1_REG       = 0x6B
MPU_PWR_MGMT2_REG       = 0x6C
MPU_SELF_TESTX_REG      = 0x0D
MPU_SELF_TESTY_REG      = 0x0E
MPU_SELF_TESTZ_REG      = 0x0F
MPU_SELF_TESTA_REG      = 0x10
MPU_SAMPLE_RATE_REG     = 0x19
MPU_CFG_REG             = 0x1A
MPU_GYRO_CFG_REG        = 0x1B
MPU_ACCEL_CFG_REG       = 0x1C
MPU_MOTION_DET_REG      = 0x1F
MPU_FIFO_EN_REG         = 0x23
MPU_I2CMST_CTRL_REG     = 0x24
MPU_I2CSLV0_ADDR_REG    = 0x25
MPU_I2CSLV0_REG         = 0x26
MPU_I2CSLV0_CTRL_REG    = 0x27
MPU_I2CSLV1_ADDR_REG    = 0x28
MPU_I2CSLV1_REG         = 0x29
MPU_I2CSLV1_CTRL_REG    = 0x2A
MPU_I2CSLV2_ADDR_REG    = 0x2B
MPU_I2CSLV2_REG         = 0x2C
MPU_I2CSLV2_CTRL_REG    = 0x2D
MPU_I2CSLV3_ADDR_REG    = 0x2E
MPU_I2CSLV3_REG         = 0x2F
MPU_I2CSLV3_CTRL_REG    = 0x30
MPU_I2CSLV4_ADDR_REG    = 0x31
MPU_I2CSLV4_REG         = 0x32
MPU_I2CSLV4_DO_REG      = 0x33
MPU_I2CSLV4_CTRL_REG    = 0x34
MPU_I2CSLV4_DI_REG      = 0x35
 
MPU_I2CMST_STA_REG      = 0x36
MPU_INTBP_CFG_REG       = 0x37
MPU_INT_EN_REG          = 0x38
MPU_INT_STA_REG         = 0x3A
 
MPU_ACCEL_XOUTH_REG     = 0x3B
MPU_ACCEL_XOUTL_REG     = 0x3C
MPU_ACCEL_YOUTH_REG     = 0x3D
MPU_ACCEL_YOUTL_REG     = 0x3E
MPU_ACCEL_ZOUTH_REG     = 0x3F
MPU_ACCEL_ZOUTL_REG     = 0x40
 
MPU_TEMP_OUTH_REG       = 0x41
MPU_TEMP_OUTL_REG       = 0x42
 
MPU_GYRO_XOUTH_REG      = 0x43
MPU_GYRO_XOUTL_REG      = 0x44
MPU_GYRO_YOUTH_REG      = 0x45
MPU_GYRO_YOUTL_REG      = 0x46
MPU_GYRO_ZOUTH_REG      = 0x47
MPU_GYRO_ZOUTL_REG      = 0x48
 
MPU_I2CSLV0_DO_REG      = 0x63
MPU_I2CSLV1_DO_REG      = 0x64
MPU_I2CSLV2_DO_REG      = 0x65
MPU_I2CSLV3_DO_REG      = 0x66
 
MPU_I2CMST_DELAY_REG    = 0x67
MPU_SIGPATH_RST_REG     = 0x68
MPU_MDETECT_CTRL_REG    = 0x69
MPU_USER_CTRL_REG       = 0x6A
MPU_PWR_MGMT1_REG       = 0x6B
MPU_PWR_MGMT2_REG       = 0x6C
MPU_FIFO_CNTH_REG       = 0x72
MPU_FIFO_CNTL_REG       = 0x73
MPU_FIFO_RW_REG         = 0x74
MPU_DEVICE_ID_REG       = 0x75
 
MPU_ADDR_ADDR           = 0x68
 
class MPU6050(object):
    def __init__(self,sclpin,sdapin):
        self.i2c=I2C(scl=Pin(sclpin),sda=Pin(sdapin),freq=100000)
    
    def Write_Mpu6050_REG(self,reg,dat):
        buf=bytearray(1)
        buf[0]=dat
        self.i2c.writeto_mem(MPU_ADDR,reg,buf)
    def Read_Mpu6050_REG(self,reg):
        t = self.i2c.readfrom_mem(MPU_ADDR,reg,1)[0]
        return  (t>>4)*10 + (t%16)
    def Read_Mpu6050_Len(self,reg,len,buffer):
        #buffer=bytearray(len)
        self.i2c.readfrom_mem_into(MPU_ADDR,reg,buffer)
    
    #fsr:0,±250dps;1,±500dps;2,±1000dps;3,±2000dps
    def MPU_Set_Gyro_Fsr(self,fsr):  
        return  self.Write_Mpu6050_REG(MPU_GYRO_CFG_REG,fsr<<3)
    #fsr:0,±2g;1,±4g;2,±8g;3,±16g
    def MPU_Set_Accel_Fsr(self,fsr): 
        return  self.Write_Mpu6050_REG(MPU_ACCEL_CFG_REG,fsr<<3)
    
    def MPU_Set_LPF(self,lpf):
        if(lpf>=188):
            data=1
        elif(lpf>=98):
            data=2
        elif(lpf>=42):
            data=3
        elif(lpf>=20):
            data=4
        elif(lpf>=10):
            data=5
        else: 
            data=6;
        self.Write_Mpu6050_REG(MPU_CFG_REG,data)
    #rate:4~1000(Hz)
    def MPU_Set_Rate(self,rate):
        if(rate>1000):
            rate=1000
        if(rate<4):
            rate=4;
        data=int(1000/rate-1)
        datas=self.Write_Mpu6050_REG(MPU_SAMPLE_RATE_REG,data)
        return  self.MPU_Set_LPF(rate/2)
    def MPU_Init(self):
        self.Write_Mpu6050_REG(MPU_PWR_MGMT1_REG,0x80)
        time.sleep_ms(100)
        self.Write_Mpu6050_REG(MPU_PWR_MGMT1_REG,0x00)
        self.MPU_Set_Gyro_Fsr(3)
        self.MPU_Set_Accel_Fsr(0)
        self.MPU_Set_Rate(50)
        self.Write_Mpu6050_REG(MPU_INT_EN_REG,0x00)
        self.Write_Mpu6050_REG(MPU_USER_CTRL_REG,0x00)
        self.Write_Mpu6050_REG(MPU_FIFO_EN_REG,0x00)
        self.Write_Mpu6050_REG(MPU_INTBP_CFG_REG,0x80)
        res = self.Read_Mpu6050_REG(MPU_DEVICE_ID_REG)
        if(res == 68):
            self.Write_Mpu6050_REG(MPU_PWR_MGMT1_REG,0x01)
            self.Write_Mpu6050_REG(MPU_PWR_MGMT2_REG,0x00)
            self.MPU_Set_Rate(50)
        else:
            return 1
        return 0
    #Get raw data
    def MPU_Get_Gyroscope(self):
        buf = bytearray(6)
        res = self.Read_Mpu6050_Len(MPU_GYRO_XOUTH_REG,6,buf)
        gx=(buf[0]<<8)|buf[1]
        gy=(buf[2]<<8)|buf[3]
        gz=(buf[4]<<8)|buf[5]
        #print('MPU_Get_Gyroscope: ',gx,gy,gz)
        return gx,gy,gz
    def MPU_Get_Accelerometer(self):
        buf = bytearray(6)
        res = self.Read_Mpu6050_Len(MPU_ACCEL_XOUTH_REG,6,buf)
        ax=(buf[0]<<8)|buf[1]
        ay=(buf[2]<<8)|buf[3]
        az=(buf[4]<<8)|buf[5]
        #print('MPU_Get_Accelerometer: ',ax,ay,az)
        return ax,ay,az
    def read_raw_data(self):
        # Read the raw sensor data
        buffer = bytearray(14)
        self.Read_Mpu6050_Len(MPU_ACCEL_XOUTH_REG, 14, buffer)
        ax = (buffer[0] << 8 | buffer[1])
        ay = (buffer[2] << 8 | buffer[3])
        az = (buffer[4] << 8 | buffer[5])
        temp = (buffer[6] << 8 | buffer[7])
        gx = (buffer[8] << 8 | buffer[9])
        gy = (buffer[10] << 8 | buffer[11])
        gz = (buffer[12] << 8 | buffer[13])
        
        # Convert the raw sensor data to real values
        ax = ax / 16384.0
        ay = ay / 16384.0
        az = az / 16384.0
        temp = (temp / 340.00) + 36.53
        gx = gx / 131.0
        gy = gy / 131.0
        gz = gz / 131.0
        
        return (ax, ay, az, temp, gx, gy, gz)
    
    def get_angle(self):
        # Read the raw sensor data
        (ax, ay, az, temp, gx, gy, gz) = self.read_raw_data()
        
        # Apply complementary filter
        pitch = math.atan2(ax, math.sqrt(ay**2 + az**2))
        roll = math.atan2(ay, math.sqrt(ax**2 + az**2))
        gyro_pitch = pitch + gy * 0.001
        gyro_roll = roll + gx * 0.001
        pitch = pitch * 0.98 + gyro_pitch * 0.02
        roll = roll * 0.98 + gyro_roll * 0.02
        
        return (pitch, roll)
