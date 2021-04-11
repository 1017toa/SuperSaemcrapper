import csv

def save_to_file(jobs):
  file = open("jobs.csv",mode="w")
  writer = csv.writer(file)
  writer.writerow(['Title','Company','Location','Link'])

  for job in jobs:
    job = list(job.values())
    writer.writerow(job)
    
  return
