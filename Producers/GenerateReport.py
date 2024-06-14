# Producers/ReportGenerator
from Producers.Producer import Producer

class GenerateReport(Producer):
    """
    When the generate report button is clicked this dispatches the "generate-report" event
    """
    def click_generate(self, start_date):
        self.start_date = start_date
        self.notify_subscribers()
