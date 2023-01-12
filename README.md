------------------------------
--         NOTES            --
------------------------------
There is only 2 3.3 VDC GPIO pins, which will have to be used by the laser and laser receiver. Then we will need an external fan as it is the easiest replacement.

Needed ToDo:
  Photoelectric sensor
  Draw on image

-------------------------------

raspistill -o ~/Pictures/name
  -vf to flip the camera

Laser:
     Pin 17 (9 down from the first row)
     Ground - Pin 20 (One up and one over)
     
Fan:
  Pin 1 (Red)
  Ground - Pin 14 (white)
  
  
  https://stackoverflow.com/questions/44496249/mark-the-difference-between-2-pictures-in-python
  
  sensor: https://www.youtube.com/watch?v=LLzRWzszbzQ

https://www.quora.com/How-do-you-connect-a-photoelectric-sensor-to-a-Raspberry-pi

https://community.element14.com/learn/learning-center/stem-academy/b/blog/posts/reading-a-photo-sensor-with-the-raspberry-pi-b

__Touch Drivers__
sudo apt-get install build-essential git cmake pkg-config libjpeg8-dev libtiff4-dev libjasper-dev libpng12-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libgtk2.0-dev libatlas-base-dev gfortran

git clone https://github.com/Itseez/opencv.git && cd opencv &&git checkout 3.0.0

sudo apt-get install build-essential cmake pkg-config libjpeg-dev libtiff5-dev libjasper-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 python3-pyqt5 python3-dev -y


sudo apt install -y build-essential cmake pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libfontconfig1-dev libcairo2-dev libgdk-pixbuf2.0-dev libpango1.0-dev libgtk2.0-dev libgtk-3-dev libatlas-base-dev gfortran libhdf5-dev libhdf5-serial-dev libhdf5-103 libqt5gui5 libqt5webkit5 libqt5test5 python3-pyqt5 python3-dev

<hr />
__Required pip install's__
- pip install opencv-python
