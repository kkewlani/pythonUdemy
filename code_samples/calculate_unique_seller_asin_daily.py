import subprocess

output_string = "{}\t{}"
output_entries = []
for month in range(5, 6):
    month_date = "2019/{:02d}".format(month)
    month_date = month_date + "/{:02d}"
    for day in range (0, 1):
        day_date = month_date.format(day)
        cmd_with_arguments = "hive -hiveconf month={:02d} -hiveconf day={:02d} -f unique_seller_asin_daily_calculation.hql".format(month, day)
        all_args = cmd_with_arguments.split(" ")
        cmd_output = subprocess.check_output(all_args)
        output_entries.append(output_string.format(day_date, cmd_output))

output_file = open("unique_seller_asin_daily_output", "w")
for entry in output_entries:
    print(entry)
    output_file.write(entry)
output_file.close()