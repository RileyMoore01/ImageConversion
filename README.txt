------------------------------
--         NOTES            --
------------------------------
There is only 2 3.3 VDC GPIO pins, which will have to be used by the laser and laser receiver. Then we will need an external fan as it is the easiest replacement.



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
