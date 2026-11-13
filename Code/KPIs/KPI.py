from abc import ABC, abstractmethod

class KPI(ABC):


    @property
    @abstractmethod
    def name(self):
        """
        Name of the KPI
        """    
        pass

    
    @property
    @abstractmethod
    def dependencies(self):
        """
        List of other KPIs that this KPI depends on
        """
        pass

    @property
    @abstractmethod
    def description(self):
        """
        Description of what this KPI calculates
        """
        pass

    # @property
    # @abstractmethod
    # def inputs(self): # List of raw signals that are used to calculate this KPI
    #     pass

    
    @property
    @abstractmethod
    def rollup_columns(self):
        """
        What calculate must return so that rollup can have the necessary underlying data to calculate the rolled up values of the KPI
        """
        pass

 
    @abstractmethod
    def rollup(self, df, grouping_keys):
        """
        Has the instructions for how to rollup the KPI from the underlying data
        
        input: dataframe with the calculated KPI and any additional columns that are needed for rollup
        output: dataframe with the rolled up KPI and any additional columns that are needed for rollup
        """
        pass

    # """
    # Has the instructions for how to finalize the KPI calculation

    # input: dataframe with the calculated KPI and any additional columns that are needed for rollup
    # output: dataframe with the finalized KPI and any additional columns that are needed for rollup
    # """
    # @abstractmethod
    # def finalize(self, df):  # ya tbh idk what this is for maybe ill use it
    #     pass

    
    @abstractmethod
    def calculate(self, df):
        """
        Has the instructions for how to calculate the KPI from the raw signals

        input: dataframe with the raw signals that are used to calculate this KPI
        output: dataframe with the calculated KPI and any additional columns that are needed for rollup
        """ 
        pass