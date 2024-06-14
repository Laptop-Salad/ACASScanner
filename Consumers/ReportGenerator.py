# Consumers/ReportGenerator
from Consumers.Consumer import Consumer
from Producers.GenerateReport import GenerateReport
from datetime import datetime, timedelta

class ReportGenerator(Consumer):
    """
    This is subscribed to the GenerateReport producer
    """
    subscribers = []

    def __init__(self, api_service, card_numbers):
        self.api_service = api_service
        self.card_numbers = card_numbers

    def update(self, producer, *args):
        students = []
        report_data = []
        start_date = producer.start_date
        
        begin_date = datetime.strptime(start_date, "%d%m%Y")
        
        for card_number in self.card_numbers:
            entry = self.api_service.get_student_entry_by_date(card_number, start_date)
            
            try:
                time = entry['items']['time'].split(":")
                students.append([int(time[0]), int(time[1])])
            except Exception as e:
                print(f"Error getting students entry for this date: {e}")
                return
        
        for _ in range(7):
            begin_date += timedelta(days=1)
            formatted_date = begin_date.strftime('%d%m%Y')

            new_students = []
            for card_number in self.card_numbers:
                entry = self.api_service.get_student_entry_by_date(card_number, formatted_date)
            
                try:
                    time = entry['items']['time'].split(":")
                    new_students.append([int(time[0]), int(time[1])])
                except Exception as e:
                    print(f"Error getting students entry. Exception: {e}")
                    return

            for i in range(len(students)):
                students[i][0] += new_students[i][0]
                students[i][1] += new_students[i][1]
                
        for i in range(len(students)):
            points = self.api_service.get_student_points(self.card_numbers[i])
            avg_hour = int(students[i][0] / 8)
            avg_minute = int(students[i][1] / 8)
            report_data.append([[avg_hour, avg_minute], points])

        if isinstance(producer, GenerateReport):
            data_for_graph = report_data
            report = {
                      "data": [
                        {
                          "scatter-chart": {
                            "data": data_for_graph,
                            "name": "Correlation between student punctuality and performance",
                            "x-axis": {
                            "name": "Punctuality",
                            "type": "entrytime"
                          },
                          "y-axis": {
                            "name": "Performance",
                            "type": "points"
                          }
                        }
                      }
                    ],
                    "name" : "report to look at"
                  }

            print(self.api_service.post_report(report))
