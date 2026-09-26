Q-17 Convert seconds into hours, minutes and seconds

total_seconds = 10000

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} hours, {minutes} minutes, and {seconds} seconds")

