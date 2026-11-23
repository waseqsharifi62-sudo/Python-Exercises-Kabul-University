import csv

def create_csv(filename):
    data = [
        ["student_id", "name", "midterm", "final"],
        ["1", "Ali Reza", 18, 17],
        ["2", "Sara", 15, 19],
        ["3", "John Doe", 12, 10]
    ]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(data)

def process_csv(input_file, output_file, threshold):
    results = []
    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total = int(row["midterm"]) + int(row["final"])
            average = total / 2
            if average >= threshold:
                results.append({
                    "student_id": row["student_id"],
                    "name": row["name"],
                    "total": total,
                    "average": average
                })
    
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["student_id", "name", "total", "average"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

create_csv("grades.csv")
process_csv("grades.csv", "results.csv", 15)