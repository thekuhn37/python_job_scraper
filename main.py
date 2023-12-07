from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

for job in jobs:
    print(job)
    print("/////\n/////\n")

save_to_file(keyword, jobs)