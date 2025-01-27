"""
Scenario class with global parameters for the pathway model.
"""


class Scenario(object):

    """
    Global variables for model.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor class for Scenario.
        """

        # General
        self.name = 'No_name'

        # Geography
        self.limit_to_england = True

        # Stroke types
        # Proportions for 6 hour arrivals:
        # https://samuel-book.github.io/samuel-1/descriptive_stats/10_using_nihss_10_for_lvo.html
        self.stroke_type_proportions = {
            'h': 13.6,
            'nlvo': 60.9,
            'lvo': 25.5
        }

        # Mimics = proportion of all calls that are mimics
        self.stroke_mimics = 0.3

        # Treatment proportions; Gives 20% IVT and 15% MT with above proportions
        self.prop_nlvo_treated_with_ivt = 0.16
        self.prop_nlvo_treated_with_mt = 0.0
        self.prop_lvo_treated_with_ivt = 0.40
        self.prop_lvo_treated_with_mt = 0.60

        # Process times
        self.process_time_call_ambulance = 60
        self.process_time_ambulance_response = 20
        self.process_ambulance_on_scene_duration = 30
        self.process_msu_dispatch = 15
        self.process_msu_thrombolysis = 30
        self.process_msu_on_scene_post_thrombolysis = 5
        self.process_msu_on_scene_no_thrombolysis = 30
        self.process_time_arrival_to_needle = 45
        self.transfer_time_delay = 60
        self.process_time_arrival_to_puncture = 90
        self.process_time_msu_arrival_to_puncture = 60

        # Save options
        self.save_lsoa_results = False

        # Overwrite default values (can take named arguments or a dictionary)
        for dictionary in args:
            for key in dictionary:
                setattr(self, key, dictionary[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])
