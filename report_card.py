def main():
	# dictionary
	report_card = {
		"name": "Carlos Vera",
		"subject": "Math",
		"grades": (90, 85, 88),
	}

	# name and subject
	print(f"Student: {report_card['name']}")
	print(f"Subject: {report_card['subject']}")

	# average
	grades = report_card.get("grades", [])
	if not grades:
		print("No grades available to calculate an average.")
		return

	average = sum(grades) / len(grades)

	report_card["average"] = average

	# evaluation based on the average
	print(f"Average: {average:.2f}")
	if average >= 90:
		print("excellent")
	elif 70 <= average <= 89:
		print("good job")
	else:
		print("needs improvement!")

	# 6) Remove the "subject" key and print the updated dictionary
	report_card.pop("subject", None)
	print("Updated report card:", report_card)


if __name__ == "__main__":
	main()

