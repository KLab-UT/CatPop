#!/bin/bash
#!/bin/bash

input_prefix=""
output_pdf=""
p_value="0.05"
batch_size="50"
data_dir="."

# Function to run the Python script
run_python_script() {
    python3 main.py -i "$input_prefix"
}

# Function to run the R script with default output PDF name
run_r_script() {
    output_pdf="${input_prefix}_plots.pdf"
    Rscript create_plots.R -i "${input_prefix}_all_output.csv" -o "$output_pdf" -p "$p_value" -b "$batch_size" -d "$data_dir"
}

# Function to display usage information
usage() {
    echo "Usage: $0 -i <input_prefix>"
    exit 1
}

# Parse command-line options
while getopts "i:" opt; do
    case "$opt" in
        i)
            input_prefix="$OPTARG"
            ;;
        \?)
            usage
            ;;
    esac
done

# Check if the input_prefix is provided
if [ -z "$input_prefix" ]; then
    usage
fi

# Call the Python script function
run_python_script

# Call the R script function
run_r_script

