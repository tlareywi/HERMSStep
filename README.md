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

### Copyright © 2022 Trystan Larey-Williams
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
