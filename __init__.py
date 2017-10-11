# -*- coding: utf-8 -*-
import time


from modules.core.props import Property, StepProperty
from modules.core.step import StepBase
from modules import cbpi

@cbpi.step
class HERMSStep(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method
    '''
    # Properties
    target_temp = Property.Number("Target Temp", configurable=True, description="Target Temperature of Mash Step")
    mash_tun = StepProperty.Kettle("Mash Tun", description="Kettle in which the mashing takes place")
    hlt = StepProperty.Kettle("HLT", description="Kettle used for heat transfer, hot liquor tank")
    timer = Property.Number("Rest (m)", configurable=True, description="Minutes of rest at target temp")
    hlt_offset = StepProperty.Number("HLT Offset", configurable=True, description="Temp relative to mash target to maintain in HLT while rising")
    pump = StepProperty.Actor("Recirculation Pump")

    def init(self):
        '''
        Initialize Step. This method is called once at the beginning of the step
        :return:
        '''
        # set target tep
        self.set_target_temp(self.target_temp, self.mash_tun)
	self.set_target_temp(self.target_temp + self.hlt_offset, self.hlt)
        self.actor_on(int(self.pump))

    @cbpi.action("Start Timer Now")
    def start(self):
        '''
        Custom Action which can be execute form the brewing dashboard.
        All method with decorator @cbpi.action("YOUR CUSTOM NAME") will be available in the user interface
        :return:
        '''
        if self.is_timer_finished() is None:
            self.start_timer(int(self.timer) * 60)

    def reset(self):
        self.stop_timer()
        self.set_target_temp(self.target_temp, self.mash_tun)
	self.set_target_temp(self.target_temp + self.hlt_offset, self.hlt)

    def finish(self):
        self.set_target_temp(0, self.mash_tun)
	self.set_target_temp(0, self.hlt)
        self.actor_off(int(self.pump))

    def execute(self):
        '''
        This method is execute in an interval
        :return:
        '''

        # Check if Target Temp is reached
        if self.get_kettle_temp(self.mash_tun) >= int(self.target_temp):
            if self.is_timer_finished() is None:
                self.start_timer(int(self.timer) * 60)

        # Check if timer finished and go to next step
        if self.is_timer_finished() == True:
            self.notify("Mash Step Completed!", "Starting the next step", timeout=None)
            self.next()
