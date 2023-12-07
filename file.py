def save_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8")
    # w for writing
    # csv : comma separated values
    file.write("Company,Position,Location,URL\n")

    for job in jobs:
        file.write(
            f"{job['company']},{job['position']},{job['location'],{job['link']}}\n"
        )

    file.close()
