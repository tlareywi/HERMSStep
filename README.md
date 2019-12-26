# HERMSStep
Plugin for CraftBeerPi3 to support temperature monitoring of two kettles simultaneously for HERMS process where the HLT is 
maintained at temperature x while the mash is recirculated through it until it reaches temperature y. This also gives one 
indirect control over the rate of temprature change in the mash tun; depending upon the delta between x and y. 

PROPERTIES
--------------------------------------------------------------------
__HLT__: The kettle serving as the hot liquor tank

__HLT Offset__: Number of degrees above mash tun target to maintain the HLT during step

__Mash Tun__: The kettle serving as the mash tun

__Recirculation Pump__: The pump responsible for moving wort through the HLT and back into the mash tun

__Target Temp__: Desired temperature of mash tun at start of rest

__Rest__: Rest in minutes after hitting Target Temp

CONTROL FLOW
--------------------------------------------------------------------
```
Init -> Recirculation Pump On, HLT On

Begin Loop
   Mash target not reached -> Maintain HLT temp offset
   Mash target reached -> Pump off, HLT Off, goto Rest
End Loop

Rest -> wait for z minutes
Rest Time Remaining < Ramp Next -> Begin to re-heat HLT 
Rest expired -> proceed to next step
```
