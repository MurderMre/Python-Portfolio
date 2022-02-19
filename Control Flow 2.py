#Our variables for our problem
weight_in_lb = 188.4
ground_flat_fee = 20.00
premium_price = 125.00

#Ground shipping calculation
if weight_in_lb <= 2:
   ground_price = 1.50*weight_in_lb+ground_flat_fee
elif weight_in_lb >= 2 and weight_in_lb <= 6:
   ground_price = 3.00*weight_in_lb+ground_flat_fee
elif weight_in_lb >= 6 and weight_in_lb <= 10:
  ground_price = 4.00*weight_in_lb+ground_flat_fee
else:
  ground_price = 4.75*weight_in_lb + ground_flat_fee

#Drone shipping calculation
if weight_in_lb <= 2:
   drone_price = 4.50*weight_in_lb
elif weight_in_lb >= 2 and weight_in_lb <= 6:
   drone_price = 9*weight_in_lb
elif weight_in_lb >= 6 and weight_in_lb <= 10:
  drone_price = 12*weight_in_lb
else:
  drone_price = 14.75*weight_in_lb 

#Determining which option is most affordable
if ground_price < drone_price   and ground_price < premium_price:
  print("Ground shipping is your most affordable option at " + str(ground_price))
elif drone_price < ground_price and drone_price < premium_price:
    print("Drone shipping is your most affordable option at " + str(drone_price))
elif premium_price < drone_price and premium_price < ground_price:
  print("Premium ground shipping is your most affordable option at " + str(premium_price))
else:
  print("Error")
