
# CS61002: Algorithms and Programming 1 
# SHIVA JALIGAMA
# 9/25/2016
# LAB02.PY
#We use import math  library function which obtains math functions in the program
import math
#Side length of the given garden is represented as length_lt, we use float to give the value in decimals
length_lt = float(input("Enter side length of the garden in feets:"))
#space_sc will cover the area in between plants
space_sc= float(input("Enter the reqired spacing in feets in between plants:"))
#The depth_dp will show how much deep the flowerbed will be
depth_dp=float(input("Enter the flowerbed depth in feets:"))
#fill_dep_th will show the complete depth of filled areas
fill_dep_th=float(input("Enter the filled areas depth in feets:"))

# radius_rs represents the length of the side of square which is 4 times raidus of circle
radius_rs=length_lt/4
#This represents _area_cir and area_semicir which is half of _area_cir 
_area_cir=math.pi*(radius_rs*radius_rs)
area_semicir=_area_cir/2
tot_area_semicir=math.trunc(area_semicir/(space_sc*space_sc))
 
#trucating represents
_tot_cir=math.trunc(_area_cir/(space_sc*space_sc))
# number of plants in the area
tot_plants_tp=_tot_cir+(tot_area_semicir*4)
# volume of soil used for semicircle
v_cir_c=(math.pi*(radius_rs*radius_rs)*depth_dp)
v_cir=v_cir_c/2
_cubic_vol=v_cir/27
# round function will round up decimal point to the number given

cv_semi_cir=round(_cubic_vol,1)
#this represents volume of the soil for circle
vol_vs=(math.pi*(radius_rs*radius_rs)*depth_dp)
_cubic_vol=vol_vs/27

# Here is the cubic volume in yards for the cirlce
c_cir=round(_cubic_vol,1) 
tot_c1=(cv_semi_cir * 4)
tot_c=tot_c1+c_cir
r_tot= round(tot_c,1)
#The volume needed for complete filling
tot_v=(length_lt*length_lt)*fill_dep_th
#The total area of flowerbeds
tot_fbs=(math.pi*(radius_rs*radius_rs)*depth_dp+(math.pi*(radius_rs*radius_rs)*depth_dp/2)*4)
#For the soil to be filled, take out area of flowebeds from volume of the flowebeds
s_fill=tot_v-tot_fbs
c_fill_cf=s_fill/27
t_sf=round(c_fill_cf,1)

#Here it prints all results 
print "\n"
print "plants in the semicircle area :",tot_area_semicir
print "plants in the circle area :",_tot_cir
print "Total number of plants in garden :",tot_plants_tp
print "Soil in semicircle area :",cv_semi_cir, 'cubic yards'
print "Soil in circle area :",c_cir, 'cubic yards'
print "Total soil in garden :",r_tot, 'cubic yards'
print "Total fill for the garden :",t_sf ,'cubic yards'


 
