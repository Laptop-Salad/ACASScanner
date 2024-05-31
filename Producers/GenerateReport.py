# Producers/ReportGenerator
from Producers.Producer import Producer

class GenerateReport(Producer):
    """
    When the generate report button is clicked this dispatches the "generate-report" event
    """
    def click_generate(self, student_arr):
        self.students = student_arr
        self.notify_subscribers()
