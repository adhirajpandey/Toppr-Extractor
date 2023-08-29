import os
import json

def merge_json_files(input_dir, output_file):
    merged_data = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            with open(os.path.join(input_dir, filename), "r") as file:
                data = json.load(file)

                if "page_info" in data and "current_page" in data["page_info"]:
                    data["page_info"]["current_page"] = int(data["page_info"]["current_page"])

                merged_data.append(data)

    merged_data.sort(key=lambda x: x["page_info"]["current_page"])

    with open(output_file, "w") as outfile:
        json.dump(merged_data, outfile, indent=4)

    print(f"Successfully merged all JSON files into '{output_file}'")


if __name__ == "__main__":
    input_dir = "Final/results"
    output_file = "Final/merged_results.json"
    merge_json_files(input_dir, output_file)
