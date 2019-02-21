import subprocess

output_string = "{}\t{}"
output_entries = []
for month in range(2, 3):
    month_date = "2019/{:02d}".format(month)
    month_date = month_date + "/{:02d}"
    for day in range (5, 7):
        day_date = month_date.format(day)
        day_date = day_date + "/{:02d}"
        for hour in range(0, 24):
            hour_date = day_date.format(hour)
            cmd_with_arguments = "hive -hiveconf month={:02d} -hiveconf day={:02d} -hiveconf hour={:02d} -f unique_seller_asin_tps_calculation.hql".format(month, day, hour)
            all_args = cmd_with_arguments.split(" ")
            cmd_output = subprocess.check_output(all_args)
            output_entries.append(output_string.format(hour_date, cmd_output))

output_file = open("unique_seller_asin_hourly_output", "w")
for entry in output_entries:
    print(entry)
    output_file.write(entry)
output_file.close()
